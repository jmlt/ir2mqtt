import requests
import webbrowser

GITHUB_USER = "jmlt"
GITHUB_REPO = "ir2mqtt"
CURRENT_VERSION = "3.0.0"

def get_latest_release():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}/releases/latest"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {
                "version": data["tag_name"],
                "changelog": data["body"],
                "download_url": data["html_url"]
            }
    except Exception as e:
        print(f"[UpdateLite] Falha ao verificar versão: {e}")
    return None

def is_update_available():
    latest = get_latest_release()
    if not latest:
        return False, None

    def normalize(v): return v.lstrip("v")

    if normalize(latest["version"]) != normalize(CURRENT_VERSION):
        return True, latest
    return False, latest

def open_download_page(url):
    webbrowser.open(url)
