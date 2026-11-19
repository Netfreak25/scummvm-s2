# Switch 2 binary dependency and license audit

This document covers the two locally built ScummVM-S2 NRO packages described in
the source repository's `README.md`. It records their configured static link
inputs and the libraries whose symbols were found in the original build ELFs.
It does not certify that either NRO runs on Switch 2 hardware. The NROs are
unverified build candidates.

## Build provenance

- ScummVM base: v2026.4.0, commit `7d2709da5136866589f7602f5f5a7b17de03420e`.
- Switch 2 toolchain: [ounce-devkit `f3478152`](https://github.com/ouncebrew/ounce-devkit/tree/f3478152dc553a104dd991efca4bde0c6e7cfe3e), release `20261114`.
- The [toolchain source manifest](https://github.com/ouncebrew/ounce-devkit/blob/f3478152dc553a104dd991efca4bde0c6e7cfe3e/build/sources)
  pins [libounce `9382b1ec`](https://github.com/ouncebrew/libounce/tree/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f),
  [OunceVK `f5afcd27`](https://github.com/ouncebrew/ouncevk/tree/f5afcd27a98d47a35b7091b097ffd7f46b0be3e4),
  and [kaiHEN `eb81e191`](https://github.com/ouncebrew/kaihen/tree/eb81e1912586d32de96678153b7f806fca4a17e9).
  kaiHEN is installed with the toolchain; it is not a direct `-lkaihen` input
  in these ScummVM link configurations.
- The devkitPro package recipes come from
  [pacman-packages `5c46517a`](https://github.com/devkitPro/pacman-packages/tree/5c46517a8a1a1f0939a90b8068655ea00fa125b9),
  using `devkitA64 r29.2-1` and the base image
  `devkitpro/devkita64:20260219`. The local build image digest was
  `sha256:407cea79e56e77555cdb9d97fc9ed903044e6bb5473c5adbed73a5942a532526`.
- The [ounce-devkit build recipe](https://github.com/ouncebrew/ounce-devkit/blob/f3478152dc553a104dd991efca4bde0c6e7cfe3e/build/make-devkit.sh)
  and this repository's `README.md` describe the toolchain and ScummVM build.

The configured `-lnx` and `-lEGL` resolve through Switch 2 linker scripts to
`libounce.a` and `libouncevk-gl.a`. The original ELFs contain libounce-only
symbols such as `__ounce_platform` and an OunceVK-only symbol,
`eglPrintConfigDebug`. They contain no symbol unique to the older Switch 1
`libnx.a` or `libEGL.a`. This is stronger than a configured link flag, but the
original build did not record a complete linker map.

## Libraries used by the NROs

The package versions below were read from the pinned build image. A nonzero
symbol match in the original ELF supports inclusion; it is not a complete
archive-member or translation-unit inventory. `Both` means the large and the
SCUMM-only builds; `Full` means only the large build.

| Component | Build | Installed version or source pin | Recipe or source | License finding |
| --- | --- | --- | --- | --- |
| libounce, including mimalloc | Both | `9382b1ec` | [libounce source](https://github.com/ouncebrew/libounce/tree/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f) | ISC; bundled mimalloc is MIT |
| OunceVK OpenGL/EGL | Both | `f5afcd27` | [OunceVK source](https://github.com/ouncebrew/ouncevk/tree/f5afcd27a98d47a35b7091b097ffd7f46b0be3e4) | Mesa and zlib-style notices; see limitation below |
| SDL2 | Both | `2.28.5-4` | [switch/SDL2 recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/SDL2/PKGBUILD) | SDL2 upstream zlib license; package metadata still says LGPL |
| libvorbis and vorbisfile | Both | `1.3.7-1` | [libvorbis recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libvorbis/PKGBUILD) | Xiph.Org BSD-style terms |
| FLAC | Both | `1.3.2-4` | [FLAC recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/flac/PKGBUILD) | Xiph.Org BSD-style terms |
| libogg | Both | `1.3.4-2` | [libogg recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libogg/PKGBUILD) | Xiph.Org BSD-style terms |
| libmad | Both | `0.15.1b-3` | [libmad recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libmad/PKGBUILD) | GPL-2.0-or-later source header; GPLv3-compatible option |
| libjpeg-turbo | Both | `2.1.2-2` | [libjpeg-turbo recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libjpeg-turbo/PKGBUILD) | IJG and applicable BSD terms; required acknowledgment below |
| libpng | Both | `1.6.48-1` | [libpng recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libpng/PKGBUILD) | libpng license |
| zlib | Both | `1.3.1-1` | [zlib recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/zlib/PKGBUILD) | zlib license |
| FreeType | Both | `2.13.3-1` | [FreeType recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/freetype/PKGBUILD) | Use the FreeType License option and retain its notices |
| bzip2 | Both | `1.0.8-1` | [bzip2 recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/bzip2/PKGBUILD) | bzip2 license |
| HarfBuzz | Both | `10.0.1-1` | [HarfBuzz recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/harfbuzz/PKGBUILD) | Upstream Old MIT-style license; package metadata still says LGPL |
| FriBidi | Both | `1.0.12-1` | [FriBidi recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libfribidi/PKGBUILD) | LGPL-2.1-or-later |
| giflib | Full | `5.1.4-2` | [giflib recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/giflib/PKGBUILD) | MIT-style terms |
| libtheora | Full | `1.2.0alpha1-1` | [libtheora recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libtheora/PKGBUILD) | Xiph.Org BSD-style terms |
| libvpx | Full | `1.8.0-2` | [libvpx recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libvpx/PKGBUILD) | BSD-style terms |
| libmikmod | Full | `3.3.11.1-2` | [libmikmod recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch/libmikmod/PKGBUILD) | Library GPL-2.0-or-later / LGPL-2.1 option; retain chosen terms |

The link command also names the compiler's `libstdc++`, `libm`, and pthread
support. Symbols from the GCC runtime and Newlib `libc`/`libm` were found in
the ELF; no Newlib `libpthread.a` object contribution was confirmed. The
runtime notices and provenance are under `LICENSES/SWITCH2/toolchain/` in the
source tree and `doc/LICENSES_S2/toolchain/` in the binary ZIP.

## Distribution obligations and remaining limit

ScummVM is GPLv3. A binary release must give recipients the corresponding
source, notices, and build/install scripts for that exact binary. The
[GPLv3 text](https://www.gnu.org/licenses/gpl-3.0.html) and
[GNU guidance](https://www.gnu.org/licenses/gpl-faq.html)
explain these obligations. For statically linked LGPL components, the chosen
license terms may additionally require materials that let recipients relink
the program with a modified library. The
[LGPL-2.1 text](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
describes that route. Merely naming a library in this table is not enough.

The [libjpeg-turbo license guidance](https://github.com/libjpeg-turbo/libjpeg-turbo/blob/main/LICENSE.md)
requires this acknowledgment in documentation for an application statically
linked with its libjpeg API library:

> This software is based in part on the work of the Independent JPEG Group.

OunceVK's installed package includes Mesa and zlib license files, and no
GPL-2-only linked source was identified in the reviewed configuration. Its
prelinked `egl.o` prevents a complete translation-unit-level attribution from
the available build outputs. Retain the complete matching OunceVK source and
notices, and resolve this provenance limit before claiming a fully audited
binary package.

The original local build ZIPs contain ScummVM's `COPYING`, `COPYRIGHT`, and
bundled third-party texts. The release packager adds the 33 reviewed Switch 2
notice and provenance files under `doc/LICENSES_S2/`, plus their SHA-256 list.
It verifies the NRO bytes remain unchanged. The chosen FreeType terms are the
FreeType License; libmikmod is distributed under its LGPL-2.1 option.

The same release provides the ScummVM source at its tag and these source
bundles, each with checksums and origin records:

- `scummvm-s2-2026.4.0-s2.4-portlib-sources.zip`: all 16 source archives,
  the 16 relevant devkitPro recipes, and their patches and build inputs;
  SHA-256 `bd8817f47db8d27810d47f58b402542393efa5e5621f5484b76593498848dc83`.
- `scummvm-s2-2026.4.0-s2.4-ounce-sources.zip`: pinned ounce-devkit,
  libounce, and OunceVK sources and build scripts; SHA-256
  `5037a6006bca19fc22f65ca3ba02206055fd0e183f4943f2e4d6eb06dfb00ac3`.

The application source and documented build command allow recipients to build
against modified LGPL libraries. The two source bundles preserve the exact
library source versions and devkitPro patches used by the original build.
Compiler runtime sources are normal toolchain components; the GCC Runtime
Library Exception and Newlib copyright notice are included in the ZIP.

There is no original full linker map or hardware acceptance result. OunceVK
provides a prelinked `egl.o`, so its individual compiled source files could not
be exhaustively mapped. The pinned build enables Nouveau and Zink and no
GPL-2-only linked component was identified. This is the remaining provenance
limit; the matching complete OunceVK source and its notices accompany the
binary. No kernel or game compatibility claim follows from this license audit.
