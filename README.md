# ScummVM-S2

ScummVM-S2 is an independent build of [ScummVM](https://www.scummvm.org/)
for Nintendo Switch 2 homebrew using [libounce](https://github.com/ouncebrew/libounce).
It targets the NRO loader provided by kaiHEN. This is an unofficial project.

## Status

Version s2.5 packages the s2.4 Joy-Con 2 mouse-enabled NROs with corrected
documentation. The user reported starting ScummVM, running Day of the Tentacle,
and using Joy-Con 2 mouse input on Switch 2. The exact tested NRO hash was not
recorded, and other engines and features need separate checks. The earlier s2.3
NRO packages do not include this input path.

| Item | Pinned version or result |
| --- | --- |
| ScummVM base | v2026.4.0, commit `7d2709da5136866589f7602f5f5a7b17de03420e` |
| Switch 2 toolchain | ounce-devkit 20261114, repository commit `f3478152dc553a104dd991efca4bde0c6e7cfe3e` |
| Project source version | `2026.4.0-s2.5` in `VERSION_S2` |
| Target | Switch 2 NRO through kaiHEN and libounce |
| Hardware evidence | User-reported ScummVM start, Day of the Tentacle launch, and Joy-Con 2 mouse input; broader acceptance pending |

`SWITCH2_DEVKIT=1` selects libounce and the Switch 2 portlibs while retaining
ScummVM's existing Switch SDL2 backend.

On Switch 2, the SDL event source now reads Joy-Con 2 optical input through the
pinned libounce `PadPointer` API. It maps movement, buttons, and scrolling to
ScummVM mouse events while retaining touch, stick, and standard mouse input.
Any connected player can supply a Joy-Con pointer. If Nmouse initialization
fails, ScummVM logs the result and continues with its other input paths. A
small graphics-manager hook keeps a synthetic button hold active through its
release event so dragging at a letterboxed game-area edge is preserved. The
user reported that Joy-Con 2 mouse input worked on the console.
The controller feature is documented in Nintendo's
[Joy-Con 2 FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/68217/~/joy-con%C2%A02-faq);
the API and its behavior come from the pinned libounce
[`PadPointer` header](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/nx/include/switch/runtime/pad.h)
and [implementation](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/nx/source/runtime/pad_pointer.c).

The s2.4 NRO builds are in the ignored `build-switch2/scummvm_switch.zip` and
`build-switch2-scumm/scummvm_switch.zip` paths. They are local build outputs,
used to make the notice-complete release packages. Their ZIP integrity and NRO
headers were checked offline.

## Earlier local build packages

The s2.3 packages below are the original local build inputs in the ignored `dist/`
directory. They contain no game data. Public binary packages are made from
these inputs by adding the reviewed notices and Switch 2 documentation.

| Package | Contents | SHA-256 |
| --- | --- | --- |
| `scummvm-2026.4.0-switch2-default-engines-unverified.zip` | 108 enabled engine entries and support data; 22 entries skipped by configuration | `a97dce2c5ba91cb7de67a8bc07d9b7e813a9d86800212e7bbca317a1d3659863` |
| `scummvm-2026.4.0-switch2-scumm-only-unverified.zip` | SCUMM engine and support data | `dec5d62e4c155295c541d9de5f812f6f2a700d9bcfa8ea69eb6d0bb35ced5c1d` |

The larger package omits engines whose dependencies were unavailable, including
Macs2, QD Engine, and Thimbleweed Park. Package names describe their configured
scope; they do not claim that the engines run on Switch 2.

## Release packages and corresponding source

`dists/switch2/package_release.py` creates the notice-complete ZIPs from the
original build inputs. It rejects missing or changed notices and checks that
the packaged NRO is byte-identical to the input:

```sh
python dists/switch2/package_release.py INPUT.zip OUTPUT.zip
```

The `2026.4.0-s2.5` pre-release has a default-engine package, a SCUMM-only
package, and two dependency-source bundles. The binary ZIPs contain
`doc/README_SWITCH2.md`, `doc/THIRD_PARTY_S2.md`, and the exact library notices
under `doc/LICENSES_S2/`. The release page provides the final ZIP checksums.
The dependency bundles contain the pinned ouncebrew sources and all 16 directly
linked devkitPro portlib source archives with their relevant recipes and patches.
See [THIRD_PARTY_S2.md](THIRD_PARTY_S2.md) for provenance and license choices.

The source at the matching release tag, the dependency bundles, and the build
command below provide the application and library sources needed to rebuild or
relink. The s2.5 NROs are byte-identical to the s2.4 builds described above.

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

Further hardware checks should cover controller input beyond the reported
Joy-Con 2 mouse test, audio, SD file access, additional games, and clean exit.
Record the console context and package hash before making broader claims.

## Verified results and limits

- Both ZIP archives passed an integrity test and matched their source-side
  SHA-256 values after transfer to the local workstation.
- Both generated NRO files contain the `NRO0` identifier. Their source ELFs
  are statically linked AArch64 programs.
- ScummVM's own OpenGL mode is disabled. SDL2 still links to the Switch 2 EGL
  overlay; the user reported a successful Day of the Tentacle launch.
- SDL2's existing build flags retain Cortex-A57 tuning. This does not provide
  Switch 2 CPU optimization.
- Network features selected above are disabled. Audio, clean exit, other games,
  and the default-engine package have not been specifically verified.

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
