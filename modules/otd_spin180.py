import subprocess

def selectTablet(tabletList):

    return tabletList[0]

class tabletRotator:

    def __init__(self):
        """Проверка кол-ва планшетов"""
        self.tabletlist = subprocess.getoutput([]).split("\n")
        if len(self.tabletlist) > 1:
            self.selected = selectTablet(self.tabletlist)
        else:
            self.selected = self.tabletlist[0]


    def rotate(self):
