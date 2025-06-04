import json
import os
from license_manager import LicenseManager
from updater import is_update_available, open_download_page

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def log(msg, level="INFO"):
    print(f"[{level}] {msg}")

def main():
    print("== iRacing2MQTT Lite ==")
    config = load_config()

    license_manager = LicenseManager(config, log_callback=log, on_save_config=save_config)
    license_manager.load_license()

    if not license_manager.license_key:
        license_input = input("Enter your donation key: ").strip()
        license_manager.save_license(license_input)

    if license_manager.validate_license():
        log("License is valid!")
        info = license_manager.get_license_info()
        if info:
            print(f"- Email: {info['email']}")
            print(f"- Origin: {info['origin']}")
            print(f"- Created at: {info['created_at']}")
    else:
        log("The donation key is not valid. Exiting program.", "ERROR")
        return

    update_available, latest = is_update_available()
    if update_available:
        log("A new version is available!", "INFO")
        print(f"Latest version: {latest['version']}")
        print("Changelog:\n", latest["changelog"])
        open_prompt = input("Open download page? (y/n): ").strip().lower()
        if open_prompt == "y":
            open_download_page(latest["download_url"])
    else:
        log("You are using the latest version.")

    print("\n-> This is just the Lite mode for donation key validation and update check.\n")

if __name__ == "__main__":
    main()
