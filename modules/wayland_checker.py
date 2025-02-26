# modules/wayland_checker.py
import os

class SessionChecker:
    def __init__(self):
        self.session_type = os.environ.get('XDG_SESSION_TYPE', '').lower()
        self.session_valid = self._check_session()

    def _check_session(self):
        if self.session_type == 'wayland':
            print("I don't know how to run this on Wayland. Sorry.")
            return False
        elif self.session_type == 'x11':
            print("We're running on X11. Good.")
            return True
        else:
            print(f"What the fuck is this session type? ({self.session_type})")
            return False

    def is_valid(self):
        return self.session_valid
