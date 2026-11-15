# ScummVM-S2 2026.4.0-s2.3

This is an unofficial, unverified Nintendo Switch 2 homebrew pre-release of
ScummVM v2026.4.0. It includes two NRO packages: a default-engine build and a
smaller SCUMM-only build. Neither has been started on Switch 2 hardware.

The binary ZIPs include ScummVM's GPLv3 notices, the exact notices for linked
Switch 2 libraries, a SHA-256 notice manifest, and Switch 2 instructions.
The matching source is provided by this release tag and two dependency-source
bundles: `scummvm-s2-2026.4.0-s2.3-portlib-sources.zip` and
`scummvm-s2-2026.4.0-s2.3-ounce-sources.zip`. The former contains 16 verified
source archives and the relevant devkitPro recipes and patches; the latter
contains the pinned ounce-devkit, libounce, and OunceVK source trees.

The default-engine NRO SHA-256 is
`820d94a925fe5c7c5d240512c1f7481dc0026f3adb44652b5d21406543df42a2`.
The SCUMM-only NRO SHA-256 is
`df1f9f606bd72b735a55858c884d4c44435f9fd15bd356b9429db74a93dcaf6b`.
ZIP checksums are recorded alongside the release assets.

Install by extracting the `scummvm` directory to `sd:/switch/` and launch
`sd:/switch/scummvm/scummvm.nro` through a compatible homebrew menu. Supply
your own legally obtained game data. See `doc/README_SWITCH2.md` for installation,
`doc/THIRD_PARTY_S2.md` for library provenance, and the source repository's
`README.md` for build steps and limitations.

This software is based in part on the work of the Independent JPEG Group.
