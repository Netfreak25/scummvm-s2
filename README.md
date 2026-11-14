# ScummVM-S2

ScummVM-S2 is an independent build of [ScummVM](https://www.scummvm.org/)
for Nintendo Switch 2 homebrew using [libounce](https://github.com/ouncebrew/libounce).
It targets the NRO loader provided by kaiHEN. This is an unofficial project.

## Status

**Unverified build candidate.** The source compiles and produces AArch64 NRO
packages, but neither package has been started on a Switch 2 yet.

| Item | Pinned version or result |
| --- | --- |
| ScummVM base | v2026.4.0, commit `7d2709da5136866589f7602f5f5a7b17de03420e` |
| Switch 2 toolchain | ounce-devkit 20261114, repository commit `f3478152dc553a104dd991efca4bde0c6e7cfe3e` |
| Project source version | `2026.4.0-s2.2` in `VERSION_S2` |
| Target | Switch 2 NRO through kaiHEN and libounce |
| Hardware acceptance | Pending |

The port change is in `configure`. `SWITCH2_DEVKIT=1` selects libounce and the
Switch 2 portlibs while retaining ScummVM's existing Switch SDL2 backend.

## Local build packages

The packages below are local build artifacts in the ignored `dist/` directory.
They are **not release assets** and contain no game data. The first public
preview contains source code only while dependency notices for these statically
linked NROs are audited.

| Package | Contents | SHA-256 |
| --- | --- | --- |
| `scummvm-2026.4.0-switch2-default-engines-unverified.zip` | 108 enabled engine entries and support data; 22 entries skipped by configuration | `a97dce2c5ba91cb7de67a8bc07d9b7e813a9d86800212e7bbca317a1d3659863` |
| `scummvm-2026.4.0-switch2-scumm-only-unverified.zip` | SCUMM engine and support data | `dec5d62e4c155295c541d9de5f812f6f2a700d9bcfa8ea69eb6d0bb35ced5c1d` |

The larger package omits engines whose dependencies were unavailable, including
Macs2, QD Engine, and Thimbleweed Park. Package names describe their configured
scope; they do not claim that the engines run on Switch 2.

## Build

Use devkitPro's devkitA64 toolchain with ounce-devkit 20261114 and the Switch
portlibs used by ScummVM's SDL2 backend. The reference build used an isolated
Linux container based on `devkitpro/devkita64:20260219`; it did not modify the
host's network configuration.

From the repository root inside that environment:

```sh
export PATH="$DEVKITPRO/devkitA64/bin:$DEVKITPRO/tools/bin:$DEVKITPRO/portlibs/switch/bin:$PATH"
mkdir -p build-switch2
cd build-switch2
SWITCH2_DEVKIT=1 ../configure --host=switch --opengl-mode=none \
  --disable-sdlnet --disable-libcurl --disable-enet --disable-fluidsynth
make -j"$(nproc)" scummvm_switch.zip
```

For the smaller SCUMM build, use a separate build directory and append
`--disable-all-engines --enable-engine=scumm` to the configure command. The
output is `scummvm_switch.zip`, containing `scummvm/scummvm.nro`, data, and
documentation.

## Installation and first test

Extract the `scummvm` directory from one package to `sd:/switch/`. The NRO
should then be at `sd:/switch/scummvm/scummvm.nro`. Start it from a Switch 2
homebrew menu after kaiHEN is active. Supply game data separately.

The first hardware check should confirm menu startup, controller input, audio,
SD file access, a game launch, and clean exit. Record the console context and
which package hash was tested before making a compatibility claim.

## Verified results and limits

- Both ZIP archives passed an integrity test and matched their source-side
  SHA-256 values after transfer to the local workstation.
- Both generated NRO files contain the `NRO0` identifier. Their source ELFs
  are statically linked AArch64 programs.
- ScummVM's own OpenGL mode is disabled. SDL2 still links to the Switch 2 EGL
  overlay; video behavior requires a hardware test.
- SDL2's existing build flags retain Cortex-A57 tuning. This does not provide
  Switch 2 CPU optimization.
- Network features selected above are disabled. Runtime graphics, input,
  audio, filesystem behavior, and engine compatibility remain unverified.

## Development and releases

Project rules are in [AGENTS.md](AGENTS.md). Every change updates
`VERSION_S2` and `CHANGELOG_S2.md` and is committed locally. A push requires
explicit approval for its destination; a release requires separate approval.
Private research, logs, captures, keys, save data, and device data must never
be uploaded.

## Upstream and license

ScummVM and its original source are maintained by the
[ScummVM team](https://github.com/scummvm/scummvm). The Switch 2 toolchain is
maintained by [ouncebrew](https://github.com/ouncebrew/ounce-devkit).
ScummVM's GPL license and notices remain in this source tree; see
[COPYING](COPYING). This project is not affiliated with Nintendo or the
ScummVM team.
