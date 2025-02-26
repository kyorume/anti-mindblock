from modules.wayland_checker import SessionChecker
from modules.xrandr_manager import XrandrManager
from modules.otd_invert import TabletRotator

if __name__ == "__main__":
    session = SessionChecker()
    
    if session.is_valid():
        # Инициализация менеджера для экрана
        xrandr_manager = XrandrManager()
        xrandr_manager.rotate_screen()

        print("✅ Session check passed. Rotating tablet...")
        
        # Инициализация менеджера для планшета
        tablet = TabletRotator()
        
        if tablet.rotate(180):  # Меняем ротацию
            tablet.restart_driver()

        print("✅ Australia mode activated.")

    else:
        print("❌ Session check failed. Exiting.")
