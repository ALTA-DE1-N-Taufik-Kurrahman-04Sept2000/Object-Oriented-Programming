# tulis solusi code disini
from math import pi

class BangunRuang:
    def __init__(self, dimensi1, dimensi2=None, dimensi3=None):
        self.dimensi1 = dimensi1
        self.dimensi2 = dimensi2
        self.dimensi3 = dimensi3

    def volume(self):
        pass

class Kubus(BangunRuang):
    def volume(self):
        return self.dimensi1 ** 3

class Balok(BangunRuang):
    def volume(self):
        return self.dimensi1 * self.dimensi2 * self.dimensi3

class Tabung(BangunRuang):
    def volume(self):
        return pi * self.dimensi1 ** 2 * self.dimensi2

def main():
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)

    print("Volume")
    print(f"Kubus : {kubus.volume()}")
    print(f"Balok : {balok.volume()}")
    print(f"Tabung : {tabung.volume()}")

if __name__ == "__main__":
    main()