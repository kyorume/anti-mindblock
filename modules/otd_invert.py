# modules/otd_invert.py
import os
import json
import subprocess

class TabletRotator:
    CONFIG_PATH = os.path.expanduser("~/.config/OpenTabletDriver/settings.json")

    def __init__(self):
        """Загружает конфиг в self.config_data"""
        self.config_data = self._load_config()

    def _load_config(self):
        """Читает JSON-конфиг OpenTabletDriver."""
        if not os.path.exists(self.CONFIG_PATH):
            print("❌ Config file not found!")
            return None

        with open(self.CONFIG_PATH, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("❌ Error parsing settings.json!")
                return None

    def rotate(self, angle):
        """Меняет Rotation у всех профилей и сохраняет конфиг."""
        if self.config_data is None:
            print("❌ Failed to load config.")
            return False

        updated = False
        for profile in self.config_data.get("Profiles", []):
            tablet_settings = profile.get("AbsoluteModeSettings", {}).get("Tablet", None)
            if tablet_settings and "Rotation" in tablet_settings:
                old_rotation = tablet_settings["Rotation"]
                tablet_settings["Rotation"] = angle
                print(f"🔄 Rotation changed: {old_rotation}° → {angle}°")
                updated = True

        if updated:
            return self._save_config()
        else:
            print("⚠️ No rotation setting found in config.")
            return False

    def restore_rotation(self):
        """Сбрасывает Rotation обратно в 0°."""
        return self.rotate(0)

    def _save_config(self):
        """Сохраняет изменения в settings.json"""
        try:
            with open(self.CONFIG_PATH, "w", encoding="utf-8") as file:
                json.dump(self.config_data, file, indent=4)
            print("✅ Config updated successfully.")
            return True
        except Exception as e:
            print(f"❌ Error saving config: {e}")
            return False

    def restart_driver(self):
        """Перезапускает OpenTabletDriver через systemctl."""
        try:
            subprocess.run(["systemctl", "--user", "restart", "opentabletdriver"], check=True)
            print("✅ OpenTabletDriver restarted successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to restart OpenTabletDriver: {e}")
            return False
