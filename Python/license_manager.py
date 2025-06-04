import requests
from datetime import datetime
import time

class LicenseManager:
    def __init__(self, config, log_callback=None, on_save_config=None):
        self.config = config
        self.license_key = None
        self.license_valid = False
        self.license_email = None
        self.license_origin = None
        self.license_created_at = None
        self.log_callback = log_callback
        self.on_save_config = on_save_config

        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "iR2mqtt-CheckerLite/1.0"
        }

    def _log(self, message, level="INFO"):
        if self.log_callback:
            self.log_callback(message, level)

    def load_license(self):
        self.license_key = self.config.get("license", {}).get("key", "")

    def save_license(self, key):
        self.license_key = key
        self.config.setdefault("license", {})["key"] = key

    def validate_license(self):
        if not self.license_key:
            self._log("Chave de licença não encontrada.", "WARNING")
            self.license_valid = False
            return False

        try:
            response = requests.post(
                "https://sys1823.pt/ir2mqtt/api/check_license.php",
                json={"license_key": self.license_key},
                headers=self.headers,
                timeout=5
            )

            if response.status_code != 200:
                self._log(f"Erro HTTP: {response.status_code}", "ERROR")
                return False

            data = response.json()
            if data.get("success") is True:
                license_data = data.get("license", {})
                self.license_valid = True
                self.license_email = license_data.get("email")
                self.license_origin = license_data.get("origin")
                self.license_created_at = license_data.get("created_at")

                self.config["license"].update({
                    "validated_at": datetime.now().isoformat(),
                    "email": self.license_email,
                    "origin": self.license_origin,
                })

                if self.on_save_config:
                    self.on_save_config(self.config)
                return True

            else:
                self._log("Licença inválida: " + data.get("error", "Erro desconhecido"), "ERROR")
                return False

        except Exception as e:
            self._log(f"Erro ao validar licença: {e}", "ERROR")
            return False

    def get_license_info(self):
        if self.license_valid and self.license_email:
            return {
                "email": self.license_email,
                "origin": self.license_origin,
                "created_at": self.license_created_at
            }
        return None
