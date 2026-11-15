# Ounce stack license notice provenance

These files are byte-for-byte copies of notices for the pinned Switch 2
toolchain. They supplement the ScummVM notices in the repository. They do not
cover the other devkitPro portlibs linked into the NRO.

The build used ounce-devkit version `20261114` from source commit
[`f3478152dc553a104dd991efca4bde0c6e7cfe3e`](https://github.com/ouncebrew/ounce-devkit/tree/f3478152dc553a104dd991efca4bde0c6e7cfe3e).
Its [source manifest](https://github.com/ouncebrew/ounce-devkit/blob/f3478152dc553a104dd991efca4bde0c6e7cfe3e/build/sources)
pins libounce commit `9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f` and
OunceVK commit `f5afcd27a98d47a35b7091b097ffd7f46b0be3e4`. The published
devkit archive has SHA-256
`f24d5773b1ee1c2b19317f57e8ae54a60fcdcefe493a0e495297c241c4912f59`.

| Local notice | Original source | SHA-256 |
| --- | --- | --- |
| `ounce-devkit-MIT.txt` | [ounce-devkit `LICENSE`](https://github.com/ouncebrew/ounce-devkit/blob/f3478152dc553a104dd991efca4bde0c6e7cfe3e/LICENSE) | `a2b4d76a335c8cc7762b892df7ce0b5368fe5da91637983deb412c15fa756782` |
| `libnx-ISC.txt` | [libounce `LICENSE.md`](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/LICENSE.md) | `5b6675f85016009624d29c9222201d3c0fc6a2d5c59253367f27d3e15011cdb2` |
| `libounce-ISC.txt` | [libounce `LICENSES/libounce-ISC.txt`](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/LICENSES/libounce-ISC.txt) | `c125684a685ad177fb5c4650ab33981702b6eaf8aec6aba0a9dfe1b0f103ad16` |
| `mimalloc-MIT.txt` | [libounce `nx/external/mimalloc/LICENSE`](https://github.com/ouncebrew/libounce/blob/9382b1ec48ac5dabdaf52f1f99e0c0aacd02cd2f/nx/external/mimalloc/LICENSE) | `82ade5d7d9b029044b5fbbc326207fc47c2d44ee4dd71e8a559c36d728217de9` |
| `ouncevk-mesa-license.rst` | [OunceVK `docs/license.rst`](https://github.com/ouncebrew/ouncevk/blob/f5afcd27a98d47a35b7091b097ffd7f46b0be3e4/docs/license.rst) | `0d1a0472ecc81830e75c20d59b0ea02841e3db21255e0ebad97ab682c54d6615` |
| `ouncevk-zlib-license.txt` | Installed OunceVK archive, `portlibs/switch2/share/licenses/ouncevk/zlib-license.txt`; copied from devkitPro's `switch-zlib` by [OunceVK's packaging script](https://github.com/ouncebrew/ouncevk/blob/f5afcd27a98d47a35b7091b097ffd7f46b0be3e4/switch2/build/package-portlib.sh) | `807c3a7dd7f6203b3dae80e28c3064f231c333685488541825b040081087fc4d` |

The installed zlib package version was `switch-zlib 1.3.1-1`. Its upstream
source is [zlib v1.3.1](https://github.com/madler/zlib/tree/v1.3.1); the
notice above preserves the exact text supplied in the ounce-devkit archive.
