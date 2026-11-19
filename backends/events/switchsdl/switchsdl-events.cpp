/* ScummVM - Graphic Adventure Engine
 *
 * ScummVM is the legal property of its developers, whose names
 * are too numerous to list here. Please refer to the COPYRIGHT
 * file distributed with this source distribution.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include "common/scummsys.h"

#if defined(NINTENDO_SWITCH)

#include <math.h>

#include "backends/platform/sdl/switch/switch.h"
#include "backends/events/switchsdl/switchsdl-events.h"
#include "backends/timer/sdl/sdl-timer.h"
#include "backends/platform/sdl/sdl.h"
#include "engines/engine.h"

#include "common/util.h"
#include "common/events.h"
#include "common/config-manager.h"

#if defined(__SWITCH2__)
#include "backends/graphics/sdl/sdl-graphics.h"
#include "backends/platform/sdl/sdl-window.h"
#include "common/textconsole.h"
#endif

#if defined(__SWITCH2__)
// Bound movement to the SDL window before ScummVM converts it to game coordinates.
static int clampJoyConMouseCoordinate(s64 coordinate, int extent) {
	if (coordinate < 0)
		return 0;
	if (coordinate >= extent)
		return extent - 1;
	return static_cast<int>(coordinate);
}

void SwitchEventSource::pushJoyConMouseEvent(SDL_Event &mouseEvent) {
	// A full or filtered SDL queue must not break the other input sources.
	if (SDL_PushEvent(&mouseEvent) != 1 && !_joyConMouseQueueWarned) {
		warning("Joy-Con 2 mouse event could not be queued: %s", SDL_GetError());
		_joyConMouseQueueWarned = true;
	}
}

void SwitchEventSource::queueJoyConMouseButton(SDL_Window *window, Uint32 type, Uint8 button, int x, int y) {
	// Keep the pointer location on the button event even when motion is queued.
	SDL_Event mouseEvent = {};
	mouseEvent.type = type;
	mouseEvent.button.windowID = SDL_GetWindowID(window);
	mouseEvent.button.button = button;
	mouseEvent.button.state = type == SDL_MOUSEBUTTONDOWN ? SDL_PRESSED : SDL_RELEASED;
	mouseEvent.button.clicks = 1;
	mouseEvent.button.x = x;
	mouseEvent.button.y = y;
	pushJoyConMouseEvent(mouseEvent);
}
#endif

SwitchEventSource::~SwitchEventSource() {
#if defined(__SWITCH2__)
	// Release the transfer memory only after the event source stops reading it.
	if (_joyConPointerReady)
		padPointerExit(&_joyConPointer);
#endif
}

#if defined(__SWITCH2__)
void SwitchEventSource::queueJoyConMouseEvents(SDL_Window *window, int width, int height) {
	// PadPointer deduplicates samples and follows the last active Joy-Con.
	padUpdate(&_joyConPad);
	padPointerUpdate(&_joyConPointer, &_joyConPad);
	// Keep drag clipping active until the queued release event has been handled.
	const u32 mouseButtons = HidMouseButton_Left | HidMouseButton_Right;
	_graphicsManager->setSyntheticMouseButtonDown(
		((_joyConPointer.buttons_old | _joyConPointer.buttons_cur) & mouseButtons) != 0);

	// Relative movement keeps touch, stick and USB mouse positions in sync.
	const int x = clampJoyConMouseCoordinate(static_cast<s64>(_mouseX) + _joyConPointer.delta_x, width);
	const int y = clampJoyConMouseCoordinate(static_cast<s64>(_mouseY) + _joyConPointer.delta_y, height);
	if (_joyConPointer.delta_x || _joyConPointer.delta_y) {
		SDL_Event mouseEvent = {};
		mouseEvent.type = SDL_MOUSEMOTION;
		mouseEvent.motion.windowID = SDL_GetWindowID(window);
		mouseEvent.motion.x = x;
		mouseEvent.motion.y = y;
		mouseEvent.motion.xrel = x - _mouseX;
		mouseEvent.motion.yrel = y - _mouseY;
		pushJoyConMouseEvent(mouseEvent);
	}

	// Nmouse reports Joy-Con buttons using the ordinary mouse button bits.
	const u32 pressed = padPointerGetButtonsDown(&_joyConPointer);
	const u32 released = padPointerGetButtonsUp(&_joyConPointer);
	// Emit transitions once; an inactive pointer still releases held buttons.
	if (pressed & HidMouseButton_Left)
		queueJoyConMouseButton(window, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT, x, y);
	if (pressed & HidMouseButton_Right)
		queueJoyConMouseButton(window, SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT, x, y);
	if (released & HidMouseButton_Left)
		queueJoyConMouseButton(window, SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT, x, y);
	if (released & HidMouseButton_Right)
		queueJoyConMouseButton(window, SDL_MOUSEBUTTONUP, SDL_BUTTON_RIGHT, x, y);

	// ScummVM already translates SDL wheel events into its inventory/menu events.
	if (_joyConPointer.wheel_delta_y) {
		SDL_Event mouseEvent = {};
		mouseEvent.type = SDL_MOUSEWHEEL;
		mouseEvent.wheel.windowID = SDL_GetWindowID(window);
		mouseEvent.wheel.y = _joyConPointer.wheel_delta_y;
		mouseEvent.wheel.direction = SDL_MOUSEWHEEL_NORMAL;
#if SDL_VERSION_ATLEAST(2, 26, 0)
		mouseEvent.wheel.mouseX = x;
		mouseEvent.wheel.mouseY = y;
#endif
		pushJoyConMouseEvent(mouseEvent);
	}
}
#endif

bool SwitchEventSource::pollEvent(Common::Event &event) {
	((DefaultTimerManager *) g_system->getTimerManager())->handler();
	// Drain existing SDL input before sampling a new Joy-Con mouse frame.
	if (SdlEventSource::pollEvent(event))
		return true;

#if defined(__SWITCH2__)
	// The graphics manager may exist before SDL has opened a usable window.
	SDL_Window *window = _graphicsManager && _graphicsManager->getWindow()
		? _graphicsManager->getWindow()->getSDLWindow() : nullptr;
	if (!window)
		return false;

	int width = 0;
	int height = 0;
	SDL_GetWindowSize(window, &width, &height);
	if (width <= 0 || height <= 0)
		return false;

	// A failed Nmouse request leaves SDL controls usable and is logged once.
	if (!_joyConPointerAttempted) {
		_joyConPointerAttempted = true;
		// The active Joy-Con can be assigned to a different player than SDL's pad.
		padInitializeAny(&_joyConPad);
		const Result result = padPointerInitialize(&_joyConPointer, width, height);
		_joyConPointerReady = R_SUCCEEDED(result);
		if (!_joyConPointerReady)
			warning("Joy-Con 2 mouse unavailable (Nmouse result 0x%X)", result);
	}
	if (_joyConPointerReady) {
		queueJoyConMouseEvents(window, width, height);
		// Route generated events through the same coordinate and keymapper logic.
		return SdlEventSource::pollEvent(event);
	}
#endif
	return false;
}

#endif
