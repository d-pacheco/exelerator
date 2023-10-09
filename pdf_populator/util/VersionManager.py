import requests as req


CURRENT_VERSION = 1.2

class VersionManager:

    @staticmethod
    def getLatestTag():
        latest_tag_response = req.get("https://api.github.com/repos/d-pacheco/pdf-populator/releases/latest")
        if 'application/json' in latest_tag_response.headers.get('Content-Type', ''):
            latest_tag_json = latest_tag_response.json()
            if "tag_name" in latest_tag_json:
                return float(latest_tag_json["tag_name"][1:])
        return 0.0
    
    @staticmethod
    def isLatestVersion():
        latest_version = VersionManager.getLatestTag()
        is_latest_version = CURRENT_VERSION >= latest_version
        if not is_latest_version:
            print("New version is avialable for download at:")
            print("https://github.com/d-pacheco/pdf-populator/releases/latest")
            print(f"Current Version: {CURRENT_VERSION}")
            print(f"Available Version: {latest_version}")
            print("")
