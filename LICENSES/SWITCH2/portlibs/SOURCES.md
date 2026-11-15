# Switch 2 portlib notice provenance

These files preserve unmodified license and copyright notices for the portlibs
linked by the local ScummVM-S2 NRO build. One complete source header is included
to document libmad's version choice. This directory does not by itself provide
the complete corresponding source required for binary distribution.

Installed package versions were read from the build image
`scummvm-ounce-devkit:20261114`
(`sha256:407cea79e56e77555cdb9d97fc9ed903044e6bb5473c5adbed73a5942a532526`).
All package versions and five portlib patches match devkitPro's
[pinned package recipe tree](https://github.com/devkitPro/pacman-packages/tree/5c46517a8a1a1f0939a90b8068655ea00fa125b9/switch).
The libmad source archive was checked against the package recipe's SHA-256
`bbfac3ed6bfbc2823d3775ebb931087371e142bb0e9bb1bee51a76a6e0078690`
before extracting its `COPYING` file.
The unmodified `mad.h` from that same verified archive contains the explicit
GPL version 2 or later grant in its opening copyright notice.

| Package | Version | Notice file | Original source | SHA-256 |
| --- | --- | --- | --- | --- |
| `switch-bzip2` | `1.0.8-1` | `bzip2-LICENSE` | /opt/devkitpro/portlibs/switch/licenses/switch-bzip2/LICENSE | `c6dbbf828498be844a89eaa3b84adbab3199e342eb5cb2ed2f0d4ba7ec0f38a3` |
| `switch-flac` | `1.3.2-4` | `flac-COPYING.Xiph` | https://raw.githubusercontent.com/xiph/flac/1.3.2/COPYING.Xiph | `fa27cb11f13f97b0c5f3ff363b1e2610c6efe87ed175779cb2a78e44eb19d34c` |
| `switch-freetype` | `2.13.3-1` | `freetype-FTL.TXT` | /opt/devkitpro/portlibs/switch/licenses/switch-freetype/FTL.TXT | `08c135755dd589039470f1fdbb400daaabaaa50d0b366d19cebff4d22986baa1` |
| `switch-freetype` | `2.13.3-1` | `freetype-GPLv2.TXT` | /opt/devkitpro/portlibs/switch/licenses/switch-freetype/GPLv2.TXT | `c4120c6752c910c299e3bd9cb3a46ff262c268303ca2069b61f92f10a5656c18` |
| `switch-freetype` | `2.13.3-1` | `freetype-LICENSE.TXT` | /opt/devkitpro/portlibs/switch/licenses/switch-freetype/LICENSE.TXT | `2e3bbb7d7c5c396368dd0853a790ec29ce5b8647163dde42a0493fb0d6556b2b` |
| `switch-giflib` | `5.1.4-2` | `giflib-COPYING` | /opt/devkitpro/portlibs/switch/licenses/switch-giflib/COPYING | `0c9b7990ecdca88b676db232c226548ac408b279f550d424d996f0d83591dd8e` |
| `switch-harfbuzz` | `10.0.1-1` | `harfbuzz-COPYING` | https://raw.githubusercontent.com/harfbuzz/harfbuzz/10.0.1/COPYING | `ba8f810f2455c2f08e2d56bb49b72f37fcf68f1f4fade38977cfd7372050ad64` |
| `switch-libfribidi` | `1.0.12-1` | `fribidi-COPYING` | https://raw.githubusercontent.com/fribidi/fribidi/v1.0.12/COPYING | `32434afcc8666ba060e111d715bfdb6c2d5dd8a35fa4d3ab8ad67d8f850d2f2b` |
| `switch-libjpeg-turbo` | `2.1.2-2` | `libjpeg-turbo-LICENSE.md` | /opt/devkitpro/portlibs/switch/licenses/switch-libjpeg-turbo/LICENSE.md | `7d8683a7f048e715e08b4cada8b7f0d9a6ab8afad88ed09c1143ef764ecbc0f2` |
| `switch-libjpeg-turbo` | `2.1.2-2` | `libjpeg-turbo-README.ijg` | https://raw.githubusercontent.com/libjpeg-turbo/libjpeg-turbo/2.1.2/README.ijg | `4b7b9f8c03bb8d60270dfd12684e70ab21e4abfd27e73905cd1a7c4cae6f5cdb` |
| `switch-libmad` | `0.15.1b-3` | `libmad-COPYING` | https://downloads.sourceforge.net/project/mad/libmad/0.15.1b/libmad-0.15.1b.tar.gz (COPYING) | `32b1062f7da84967e7019d01ab805935caa7ab7321a7ced0e30ebe75e5df1670` |
| `switch-libmad` | `0.15.1b-3` | `libmad-mad.h` | https://downloads.sourceforge.net/project/mad/libmad/0.15.1b/libmad-0.15.1b.tar.gz (mad.h) | `d82d607988d1bab7d47b4db0381dca1feb0666e2a1183a68eb34bfeb40b1fe82` |
| `switch-libmikmod` | `3.3.11.1-2` | `libmikmod-COPYING.LESSER` | https://raw.githubusercontent.com/sezero/mikmod/libmikmod-3.3.11.1/libmikmod/COPYING.LESSER | `dc626520dcd53a22f727af3ee42c770e56c97a64fe3adb063799d8ab032fe551` |
| `switch-libmikmod` | `3.3.11.1-2` | `libmikmod-COPYING.LIB` | https://raw.githubusercontent.com/sezero/mikmod/libmikmod-3.3.11.1/libmikmod/COPYING.LIB | `b7993225104d90ddd8024fd838faf300bea5e83d91203eab98e29512acebd69c` |
| `switch-libmikmod` | `3.3.11.1-2` | `libmikmod-README` | https://raw.githubusercontent.com/sezero/mikmod/libmikmod-3.3.11.1/libmikmod/README | `287cb14e7bc0a70b4db81b1233a6bd4ab2f909940688c595b711a5c774fb38f7` |
| `switch-libogg` | `1.3.4-2` | `libogg-COPYING` | https://raw.githubusercontent.com/xiph/ogg/v1.3.4/COPYING | `d2ab5758336489da61c12cc5bb757da5339c4ae9001f9bb0562b4370249af814` |
| `switch-libpng` | `1.6.48-1` | `libpng-LICENSE` | /opt/devkitpro/portlibs/switch/licenses/switch-libpng/LICENSE | `16d9daaafbf63a31a5bdc91d4600972548fef5aaa1244202393288dbd079c49a` |
| `switch-libtheora` | `1.2.0alpha1-1` | `libtheora-COPYING` | /opt/devkitpro/portlibs/switch/licenses/switch-libtheora/COPYING | `8417fad7da775735564e209484a2e011e0fa201e94f01fdbee6e4977e478e6fc` |
| `switch-libvorbis` | `1.3.7-1` | `libvorbis-COPYING` | https://raw.githubusercontent.com/xiph/vorbis/v1.3.7/COPYING | `ec1815db59fcd302846df949d7424876cb2e2dc5ed1606c5fb0b36787b1cf43a` |
| `switch-libvpx` | `1.8.0-2` | `libvpx-LICENSE` | https://raw.githubusercontent.com/webmproject/libvpx/v1.8.0/LICENSE | `8267348d5af1262c11d1a08de2f5afc77457755f1ac658627dd9acf71011d615` |
| `switch-sdl2` | `2.28.5-4` | `sdl2-LICENSE.txt` | https://raw.githubusercontent.com/libsdl-org/SDL/release-2.28.5/LICENSE.txt | `9928507f684c1965d07f2b6ef4b4723d5efc2f6b4ab731f743a413c51c319927` |
| `switch-zlib` | `1.3.1-1` | `zlib-LICENSE` | /opt/devkitpro/portlibs/switch/licenses/switch-zlib/LICENSE | `807c3a7dd7f6203b3dae80e28c3064f231c333685488541825b040081087fc4d` |
