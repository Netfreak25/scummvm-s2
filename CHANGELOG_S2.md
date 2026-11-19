# ScummVM-S2 Changelog

## 2026.4.0-s2.4 (2026-11-19, unverified build candidate)

- Added Joy-Con 2 optical mouse input through the pinned libounce PadPointer API
  in the Switch 2 SDL event source. Motion, mouse buttons, and scrolling enter
  ScummVM through its existing mouse event handling.
- Preserved the existing Switch 1, touch, stick, and standard mouse input paths.
  A failed Nmouse initialization is reported and leaves those inputs available.
- Preserved dragging across the edge of a letterboxed game area for synthetic
  Joy-Con mouse-button events.

Both the default-engine and SCUMM-only NRO packages were built offline with the
pinned toolchain and passed ZIP integrity and NRO-header checks. The Joy-Con 2
input path has not been tested on Switch 2 hardware. The older s2.3 binary
packages do not contain it.

## 2026.4.0-s2.3 (2026-11-15)

- Audited the static library inputs in both NRO builds against their pinned
  original sources and retained their copyright and license notices.
- Prepared matching dependency source bundles with the devkitPro recipes and
  patches needed to rebuild the linked libraries.
- Added a checked release packager that preserves the NRO bytes and includes
  the audited notices and Switch 2 documentation in each ZIP.

The NROs remain unverified on Switch 2 hardware.

## 2026.4.0-s2.2 (2026-11-15, internal source preview)

- Prepared the first source-only preview under the ScummVM GPLv3 license.
- Added a dated modification notice and removed personal identity from the
  project-owned instructions and new commit metadata.
- Kept the untested NRO packages local while their third-party license notices
  and exact build dependencies are audited.

This source preview did not claim Switch 2 hardware compatibility.

## 2026.4.0-s2.1 (2026-11-14, internal build candidate)

- Established a standalone, remote-free project with project-owned privacy,
  versioning, and release rules.
- Preserved the ScummVM v2026.4.0 source and the initial libounce build change.
- Documented the verified host builds and the outstanding Switch 2 tests.

No public release or hardware compatibility claim was associated with this version.
