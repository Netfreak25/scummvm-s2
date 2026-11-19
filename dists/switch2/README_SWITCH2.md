# ScummVM-S2 for Nintendo Switch 2

This is an unofficial, unverified build of ScummVM v2026.4.0 for Switch 2
homebrew. The NRO has not been started on Switch 2 hardware. Graphics, input,
audio, SD access, engine compatibility, and clean exit remain untested.

## Install

Copy this `scummvm` directory to `sd:/switch/`. The program should then be at
`sd:/switch/scummvm/scummvm.nro`. Start it through a compatible Switch 2
homebrew menu. Supply your own legally obtained game data separately.

The large ZIP has the configured default engines; the smaller ZIP has only the
SCUMM engine. Their names describe build configuration, not tested support.

## Joy-Con 2 mouse input

This s2.4 build maps Joy-Con 2 optical movement, left and right buttons, and
vertical scrolling to ScummVM mouse events through libounce. Nintendo describes
the controller feature in its
[Joy-Con 2 FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/68217/~/joy-con%C2%A02-faq),
and the implementation uses the pinned libounce
[`PadPointer` API](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/nx/include/switch/runtime/pad.h).
Mouse behavior in this ScummVM build still requires a Switch 2 hardware test.

## Source and notices

The matching ScummVM-S2 source is tag `v2026.4.0-s2.4`. The release also
provides two dependency-source bundles for ouncebrew and the devkitPro
portlibs. Build and relink instructions are in the source repository's
`README.md`. Library notices and their SHA-256 list are in `doc/LICENSES_S2/`;
the dependency audit is in `doc/THIRD_PARTY_S2.md`.

No game data, keys, saves, or device data are included.

This software is based in part on the work of the Independent JPEG Group.
