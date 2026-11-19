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

#if !defined(DISABLE_DEFAULT_EVENTMANAGER)
#define BACKEND_EVENTS_SWITCH_H

#include "backends/events/sdl/sdl-events.h"

#if defined(__SWITCH2__)
#include <switch.h>
#endif

/**
 * SDL Events manager for the SWITCH.
 */
class SwitchEventSource : public SdlEventSource {
public:
	SwitchEventSource() {}
	~SwitchEventSource() override;

protected:
	bool pollEvent(Common::Event &event) override;

#if defined(__SWITCH2__)
private:
	// The helper reports a queue failure once while ordinary SDL input continues.
	void pushJoyConMouseEvent(SDL_Event &mouseEvent);
	void queueJoyConMouseButton(SDL_Window *window, Uint32 type, Uint8 button, int x, int y);
	void queueJoyConMouseEvents(SDL_Window *window, int width, int height);

	// The Nmouse session is opened only after SDL has created its window.
	PadState _joyConPad{};
	PadPointer _joyConPointer{};
	// Avoid repeated service requests after a definite initialization failure.
	bool _joyConPointerAttempted = false;
	bool _joyConPointerReady = false;
	bool _joyConMouseQueueWarned = false;
#endif
};

#endif /* BACKEND_EVENTS_SWITCH_H */
