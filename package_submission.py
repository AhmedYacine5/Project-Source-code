"""
Packaging script to generate a clean submission ZIP file for Dr. Brahim Ferik.
Excludes bytecode caches, pytest caches, and logs.
"""
import os
import zipfile

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_ZIP = os.path.join(SOURCE_DIR, "..", "auth_security_service_submission.zip")

EXCLUDE_DIRS = {"__pycache__", ".pytest_cache", ".git", ".idea", "venv", ".venv"}
EXCLUDE_EXTS = {".pyc", ".pyo", ".log"}


def build_submission_zip():
    print(f"Creating submission package from: {SOURCE_DIR}")
    zip_path = os.path.abspath(OUTPUT_ZIP)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in EXCLUDE_EXTS:
                    continue

                abs_file_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_file_path, SOURCE_DIR)
                arcname = os.path.join("auth_security_service", rel_path)

                zf.write(abs_file_path, arcname=arcname)
                print(f"  + Added: {arcname}")

    print("=" * 60)
    print(f"Submission archive created successfully:")
    print(f"  -> {zip_path} ({os.path.getsize(zip_path) / 1024:.1f} KB)")
    print("=" * 60)


if __name__ == "__main__":
    build_submission_zip()
