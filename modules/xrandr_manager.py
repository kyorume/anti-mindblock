# modules/xrandr_manager.py
import subprocess

class XrandrManager:
    def __init__(self):
        self.primary_monitor = self._get_primary_monitor()
        self.original_state = self._save_current_state()

    def _get_primary_monitor(self):
        output = subprocess.check_output(['xrandr', '--query']).decode('utf-8')
        for line in output.splitlines():
            if ' connected primary' in line:
                return line.split()[0]
        return None

    def _save_current_state(self):
        if self.primary_monitor:
            output = subprocess.check_output(['xrandr', '--query']).decode('utf-8')
            for line in output.splitlines():
                if self.primary_monitor in line:
                    if 'normal' in line:
                        return 'normal'
                    elif 'inverted' in line:
                        return 'inverted'
                    elif 'left' in line:
                        return 'left'
                    elif 'right' in line:
                        return 'right'
        return None

    def rotate_screen(self, rotation='inverted'):
        if self.primary_monitor:
            subprocess.run(['xrandr', '--output', self.primary_monitor, '--rotate', rotation])
            print(f"{self.primary_monitor} was rotated.")
        else:
            print("Primary monitor not found.")

    def restore_state(self):
        if self.primary_monitor and self.original_state:
            subprocess.run(['xrandr', '--output', self.primary_monitor, '--rotate', self.original_state])
            print(f"{self.primary_monitor} was restored.")
        else:
            print("Restore failed.")
