import subprocess

class tabletRotator:


    def __init__(self):
        """Проверка кол-ва планшетов"""
        self.tabletlist = subprocess.getoutput([]).split("\n")


    def rotate(self):
