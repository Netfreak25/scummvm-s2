# Compiler runtime notice provenance

The local Switch 2 build image contains `devkita64-gcc 15.2.0-7` and
`devkita64-newlib 4.6.0.20260123-4`. The original ELF has symbol matches in
GCC `libstdc++` and `libgcc` and Newlib `libc` and `libm`. The link command
also names pthread support, but no symbol from Newlib's `libpthread.a` was
found in the ELF; its archive contribution is unconfirmed. These are standard
toolchain components, separate from the Switch 2 portlibs listed in
`../portlibs/SOURCES.md`.

| Local notice | Version and original source | SHA-256 |
| --- | --- | --- |
| `newlib-COPYING.NEWLIB` | [Newlib 4.6.0.20260123 source archive](https://sourceware.org/pub/newlib/newlib-4.6.0.20260123.tar.gz), file `COPYING.NEWLIB` | `f3afe48e4bc6ed8466a42e9dacb6be1d8f9cbf5aac15cb8e474a5ccde8b40ef6` |
| `gcc-COPYING.RUNTIME` | [GCC 15.2.0 release tag](https://gnu.googlesource.com/gcc/+/refs/tags/releases/gcc-15.2.0/COPYING.RUNTIME), file `COPYING.RUNTIME` | `9d6b43ce4d8de0c878bf16b54d8e7a10d9bd42b75178153e3af6a815bdc90f74` |

The Newlib archive was verified against SHA-256
`6ff27e3bf022666f43f7802255be680eeff722ac181b1725d21e2e8318604ee3`,
as recorded in devkitPro's
[pinned Newlib package recipe](https://github.com/devkitPro/pacman-packages/blob/5c46517a8a1a1f0939a90b8068655ea00fa125b9/devkita64/newlib/PKGBUILD).
That recipe applies the
[devkitA64 r29.2 Newlib patch](https://raw.githubusercontent.com/devkitPro/buildscripts/refs/tags/devkitA64_r29.2/patches/newlib-4.6.0.20260123-4.patch)
with SHA-256 `6d5aba4356553c727765c98e7553d3784f31d361c856e220ef27cc26353fb88f`.

The [GCC Runtime Library Exception](https://www.gnu.org/licenses/gcc-exception-3.1.html)
permits eligible GCC-built programs to combine covered GCC runtime code,
including static `libgcc` and `libstdc++` links. GPLv3 also excludes qualifying
System Libraries from the application's Corresponding Source. These exceptions
are specific to the toolchain; they do not remove the notice and source duties
for other linked libraries. Newlib's `COPYING.NEWLIB` contains its collected
source-license notices and is retained with the binary documentation.
