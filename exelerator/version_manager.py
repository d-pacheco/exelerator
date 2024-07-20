import logging
import os
import shutil
import subprocess
import sys
from typing import Optional
import requests as req
import socket
import zipfile
import tarfile

logger = logging.getLogger("exelerator")
LATEST_RELEASE_URL = "https://api.github.com/repos/d-pacheco/exelerator/releases/latest"


class VersionManager:
    @staticmethod
    def is_latest_version(current_version):
        latest_version_tag = get_field_from_latest_release_api("tag_name")
        if latest_version_tag is not None:
            latest_version = float(latest_version_tag[1:])
        else:
            latest_version = 0.0
        return current_version >= latest_version

    @staticmethod
    def has_internet(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            return False

    @staticmethod
    def download_latest_release():
        latest_version_tag = get_field_from_latest_release_api("tag_name")
        download_url = get_field_from_latest_release_api("zipball_url") or get_field_from_latest_release_api("tarball_url")
        file_extension = "zip" if "zipball" in download_url else "tar.gz"
        download_filename = f"latest_release.{file_extension}"
        download_release_file(download_url, download_filename)
        new_executable_path = extract_file(filename=download_filename, version=latest_version_tag)
        if new_executable_path is not None:
            launch_new_executable(new_executable_path)

    @staticmethod
    def delete_old_executable_versions():
        current_executable_path = sys.argv[0]
        current_executable_name = os.path.basename(current_executable_path)
        delete_old_executables(current_executable_name)


def get_field_from_latest_release_api(field_name: str) -> Optional[str]:
    latest_release_response = req.get(LATEST_RELEASE_URL)
    if 'application/json' in latest_release_response.headers.get('Content-Type', ''):
        latest_release_json = latest_release_response.json()
        if field_name in latest_release_json:
            return latest_release_json.get(field_name)
    return None


def download_release_file(url: str, local_filename: str):
    with req.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def extract_file(filename, version: str = "", extract_to=".") -> Optional[str]:
    if filename.endswith(".zip"):
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            extracted_dir = zip_ref.namelist()[0].split('/')[0]
            zip_ref.extractall(extract_to)
    elif filename.endswith((".tar.gz", ".tar")):
        with tarfile.open(filename, 'r:gz') as tar_ref:
            extracted_dir = tar_ref.getnames()[0].split('/')[0]
            tar_ref.extractall(extract_to)
    os.remove(filename)

    if extracted_dir:
        version.replace('.', '_')
        extracted_path = os.path.join(extract_to, extracted_dir)
        original_executable = 'Exelerator.exe'
        new_executable_name = f'Exelerator_{version}.exe'
        files_to_move = ['README.md']

        # Rename and move the executable file
        new_executable_path = None
        exe_src = os.path.join(extracted_path, original_executable)
        if os.path.exists(exe_src):
            new_executable_path = os.path.join(extract_to, new_executable_name)
            shutil.move(exe_src, new_executable_path)

        # Move the README.md file
        for file_name in files_to_move:
            src = os.path.join(extracted_path, file_name)
            if os.path.exists(src):
                shutil.move(src, os.path.join(extract_to, file_name))

        # Optionally remove the now-empty extracted directory
        shutil.rmtree(extracted_path)

        return new_executable_path
    else:
        logger.error("Couldn't get directory to extract files to")
        return None


def launch_new_executable(executable_path):
    subprocess.Popen([executable_path, '--upgraded'])
    sys.exit()


def delete_old_executables(current_executable_name: str, directory="."):
    for file_name in os.listdir(directory):
        if file_name.startswith("Exelerator") and file_name.endswith(".exe") and file_name != current_executable_name:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
