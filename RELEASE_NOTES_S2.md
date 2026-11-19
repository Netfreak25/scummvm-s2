# ScummVM-S2 2026.4.0-s2.5

This is an unofficial Nintendo Switch 2 homebrew pre-release of ScummVM
v2026.4.0. It includes a default-engine NRO package and a smaller SCUMM-only
NRO package. Both contain the same NRO bytes as the s2.4 build. The user
reported starting ScummVM, running Day of the Tentacle, and confirming Joy-Con 2
mouse input on Switch 2. The exact package variant and NRO hash of that test
were not recorded; other engines and features need separate verification.

## New: Joy-Con 2 mouse support

The Switch 2 SDL event source uses libounce's `PadPointer` API to read Joy-Con 2
optical movement, left and right mouse-button transitions, and vertical
scrolling. These enter ScummVM through its existing SDL mouse-event path. Touch,
stick, and ordinary mouse input remain available. If the Nmouse request fails,
the application reports the error and continues with those other inputs.

Nintendo documents the Joy-Con 2 mouse capability in its
[Joy-Con 2 FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/68217/~/joy-con%C2%A02-faq).
The implementation uses the pinned libounce
[`PadPointer` declarations](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/nx/include/switch/runtime/pad.h)
and [implementation](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/nx/source/runtime/pad_pointer.c).
These sources explain the API and hardware feature. The user test confirms
mouse input for the tested package, within the context stated above.

The binary ZIPs include ScummVM's GPLv3 notices, the exact notices for linked
Switch 2 libraries, a SHA-256 notice manifest, and Switch 2 instructions.
Matching application source is at tag `v2026.4.0-s2.5`. The dependency-source
bundles `scummvm-s2-2026.4.0-s2.5-portlib-sources.zip` and
`scummvm-s2-2026.4.0-s2.5-ounce-sources.zip` carry the unchanged pinned
devkitPro portlib and ouncebrew sources used for both NRO variants.

Default-engine NRO SHA-256:
`6c3f489673a275da106134cf85f4548f8f4b0d80903becdc516ed71e3130c53d`

SCUMM-only NRO SHA-256:
`3481e2d667bf5f675992fa46a8e237b2bfe4d8a1dc6442a8bee6d6a7c370115a`

ZIP checksums are recorded alongside the release assets. Extract the `scummvm`
directory to `sd:/switch/` and launch `sd:/switch/scummvm/scummvm.nro` through a
compatible homebrew menu. Supply your own legally obtained game data. See
`doc/README_SWITCH2.md` for installation, `doc/THIRD_PARTY_S2.md` for library
provenance, and the source repository's `README.md` for build steps and limits.

This software is based in part on the work of the Independent JPEG Group.
