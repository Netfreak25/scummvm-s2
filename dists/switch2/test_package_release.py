"""Focused checks for the Switch 2 release ZIP packager."""

import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

import package_release


class PackageReleaseTests(unittest.TestCase):
    """Check archive integrity and reject ambiguous release inputs."""

    def setUp(self) -> None:
        # Keep test packages isolated from the real ignored release directory.
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.directory = Path(self.temporary_directory.name)
        self.input_zip = self.directory / "build.zip"
        self.output_zip = self.directory / "release.zip"
        self.notice = self.directory / "NOTICE.txt"
        self.notice.write_text("An exact license notice.\n", encoding="utf-8")

    def create_build_zip(self, include_nro: bool = True) -> None:
        """Write a minimal valid build with optional executable content."""
        with zipfile.ZipFile(self.input_zip, "w") as build_archive:
            build_archive.writestr("scummvm/doc/COPYING", "GPLv3 text")
            build_archive.writestr(package_release.LEGACY_SWITCH_GUIDE, "Switch 1")
            if include_nro:
                build_archive.writestr(
                    package_release.NRO_ARCHIVE_PATH, b"NRO0 exact bytes"
                )

    def test_adds_notice_without_changing_executable(self) -> None:
        self.create_build_zip()
        added_name = "scummvm/doc/LICENSES_S2/NOTICE.txt"
        with patch.object(
            package_release, "document_entries", return_value={added_name: self.notice}
        ):
            nro_digest = package_release.package_release(
                self.input_zip, self.output_zip
            )

        # The new archive keeps the original NRO and carries the exact notice.
        with zipfile.ZipFile(self.output_zip) as release_archive:
            self.assertIsNone(release_archive.testzip())
            self.assertNotIn(
                package_release.LEGACY_SWITCH_GUIDE, release_archive.namelist()
            )
            self.assertEqual(
                release_archive.read(package_release.NRO_ARCHIVE_PATH),
                b"NRO0 exact bytes",
            )
            self.assertEqual(release_archive.read(added_name), self.notice.read_bytes())
        self.assertEqual(nro_digest, hashlib.sha256(b"NRO0 exact bytes").hexdigest())

    def test_rejects_missing_executable_without_output(self) -> None:
        # A documentation-only ZIP must never be presented as an NRO release.
        self.create_build_zip(include_nro=False)
        with (
            patch.object(package_release, "document_entries", return_value={}),
            self.assertRaisesRegex(ValueError, "no ScummVM NRO"),
        ):
            package_release.package_release(self.input_zip, self.output_zip)
        self.assertFalse(self.output_zip.exists())

    def test_rejects_notice_name_collision(self) -> None:
        # Existing entries cannot be silently replaced by the packager.
        self.create_build_zip()
        with (
            patch.object(
                package_release,
                "document_entries",
                return_value={"scummvm/doc/COPYING": self.notice},
            ),
            self.assertRaisesRegex(ValueError, "already contains"),
        ):
            package_release.package_release(self.input_zip, self.output_zip)
        self.assertFalse(self.output_zip.exists())

    def test_requires_component_notice_and_provenance(self) -> None:
        with (
            patch.object(package_release, "NOTICE_ROOT", self.directory / "missing"),
            self.assertRaisesRegex(ValueError, "missing notices for ounce"),
        ):
            package_release.document_entries()

    def test_rejects_tampered_notice(self) -> None:
        notice_root = self.directory / "notices"
        notice_root.mkdir()
        notice_path = notice_root / "LICENSE.txt"
        notice_path.write_text("modified", encoding="utf-8")
        manifest_path = notice_root / "SHA256SUMS"
        manifest_path.write_text("0" * 64 + "  LICENSE.txt\n", encoding="utf-8")
        with (
            patch.object(package_release, "NOTICE_ROOT", notice_root),
            patch.object(package_release, "NOTICE_MANIFEST", manifest_path),
            self.assertRaisesRegex(ValueError, "notice hash mismatch"),
        ):
            package_release.verify_notice_manifest({notice_path})


if __name__ == "__main__":
    unittest.main()
