"""Add audited Switch 2 notices to an existing ScummVM build ZIP."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

# Resolve project files from the script, independent of the caller's directory.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
NOTICE_ROOT = PROJECT_ROOT / "LICENSES" / "SWITCH2"
NOTICE_MANIFEST = NOTICE_ROOT / "SHA256SUMS"
ARCHIVE_DOCUMENT_ROOT = "scummvm/doc"
NRO_ARCHIVE_PATH = "scummvm/scummvm.nro"
LEGACY_SWITCH_GUIDE = f"{ARCHIVE_DOCUMENT_ROOT}/README.SWITCH"
RELEASE_DOCUMENTS = {
    "dists/switch2/README_SWITCH2.md": "README_SWITCH2.md",
    "RELEASE_NOTES_S2.md": "RELEASE_NOTES_S2.md",
    "THIRD_PARTY_S2.md": "THIRD_PARTY_S2.md",
}


def verify_notice_manifest(notice_files: set[Path]) -> None:
    """Require every bundled notice to match the reviewed SHA-256 list."""
    if not NOTICE_MANIFEST.is_file():
        raise FileNotFoundError(f"missing notice manifest: {NOTICE_MANIFEST}")
    manifest_files: set[Path] = set()

    # The two spaces between digest and relative path match sha256sum output.
    for line in NOTICE_MANIFEST.read_text(encoding="utf-8").splitlines():
        expected_digest, relative_name = line.split("  ", maxsplit=1)
        notice_path = NOTICE_ROOT / relative_name
        if not notice_path.is_file():
            raise FileNotFoundError(f"missing notice: {notice_path}")
        actual_digest = sha256_bytes(notice_path.read_bytes())
        if actual_digest != expected_digest:
            raise ValueError(f"notice hash mismatch: {notice_path}")
        manifest_files.add(notice_path)
    # A reviewed manifest must account for every file placed in the archive.
    if manifest_files != notice_files:
        raise ValueError("notice manifest does not cover every notice file")


def document_entries() -> dict[str, Path]:
    """Return the complete set of audited documents for a release ZIP."""
    entries = {
        f"{ARCHIVE_DOCUMENT_ROOT}/{target_name}": PROJECT_ROOT / source_name
        for source_name, target_name in RELEASE_DOCUMENTS.items()
    }

    # Keep every component notice with the binary that incorporates it.
    notice_files = {
        path
        for path in NOTICE_ROOT.rglob("*")
        if path.is_file() and path != NOTICE_MANIFEST
    }
    for notice_path in sorted(notice_files):
        archive_name = notice_path.relative_to(NOTICE_ROOT).as_posix()
        entries[f"{ARCHIVE_DOCUMENT_ROOT}/LICENSES_S2/{archive_name}"] = notice_path

    # A component needs both its notice and a provenance index.
    for component_directory in ("ounce", "portlibs", "toolchain"):
        notice_directory = NOTICE_ROOT / component_directory
        has_notice = any(
            path.is_file() and path.name != "SOURCES.md"
            for path in notice_directory.rglob("*")
        )
        if not (notice_directory / "SOURCES.md").is_file() or not has_notice:
            raise ValueError(f"missing notices for {component_directory}")
    missing = [str(path) for path in entries.values() if not path.is_file()]
    if missing:
        raise FileNotFoundError("missing release documents: " + ", ".join(missing))
    verify_notice_manifest(notice_files)
    entries[f"{ARCHIVE_DOCUMENT_ROOT}/LICENSES_S2/SHA256SUMS"] = NOTICE_MANIFEST
    return entries


def sha256_bytes(content: bytes) -> str:
    """Return the SHA-256 digest used to compare the embedded NRO."""
    return hashlib.sha256(content).hexdigest()


def package_release(input_zip: Path, output_zip: Path) -> str:
    """Copy an existing build and add notices without changing its NRO."""
    if input_zip.resolve() == output_zip.resolve():
        raise ValueError("input and output ZIP paths must differ")
    if output_zip.exists():
        raise FileExistsError(f"release ZIP already exists: {output_zip}")
    additions = document_entries()

    # Reject ambiguous input before creating any visible release artifact.
    with zipfile.ZipFile(input_zip) as source_archive:
        archive_names = source_archive.namelist()
        if len(archive_names) != len(set(archive_names)):
            raise ValueError("source ZIP contains duplicate paths")
        if NRO_ARCHIVE_PATH not in archive_names:
            raise ValueError("source ZIP contains no ScummVM NRO")
        if set(archive_names) & set(additions):
            raise ValueError("source ZIP already contains release documents")
        if bad_entry := source_archive.testzip():
            raise ValueError(f"source ZIP has a damaged entry: {bad_entry}")
        original_nro_digest = sha256_bytes(source_archive.read(NRO_ARCHIVE_PATH))

        # Build at a temporary path so a failed copy cannot look like a release.
        output_zip.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            suffix=".zip", dir=output_zip.parent, delete=False
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
        try:
            with zipfile.ZipFile(temporary_path, "w") as release_archive:
                # Replace the older Switch 1 guide with the current Switch 2 guide.
                for archive_entry in source_archive.infolist():
                    if archive_entry.filename == LEGACY_SWITCH_GUIDE:
                        continue
                    release_archive.writestr(
                        archive_entry, source_archive.read(archive_entry)
                    )
                for archive_name, document_path in sorted(additions.items()):
                    release_archive.write(document_path, archive_name)

            # Verify the whole package and prove the executable is unchanged.
            with zipfile.ZipFile(temporary_path) as release_archive:
                if bad_entry := release_archive.testzip():
                    raise ValueError(f"release ZIP has a damaged entry: {bad_entry}")
                packaged_nro_digest = sha256_bytes(
                    release_archive.read(NRO_ARCHIVE_PATH)
                )
                if packaged_nro_digest != original_nro_digest:
                    raise ValueError("packaged NRO differs from the build input")
            shutil.move(temporary_path, output_zip)
        finally:
            temporary_path.unlink(missing_ok=True)
    return original_nro_digest


def main() -> None:
    """Read paths from the CLI and print digests for human review."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_zip", type=Path)
    parser.add_argument("output_zip", type=Path)
    arguments = parser.parse_args()
    nro_digest = package_release(arguments.input_zip, arguments.output_zip)
    # Print both digests so reviewers can tie the ZIP to its unchanged NRO.
    package_digest = sha256_bytes(arguments.output_zip.read_bytes())
    print(f"NRO SHA-256: {nro_digest}")
    print(f"ZIP SHA-256: {package_digest}")
    print(f"Release candidate: {arguments.output_zip}")


if __name__ == "__main__":
    main()
