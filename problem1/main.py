# tulis solusi code disini
class BangunDatar:
    def __init__(self, sisi1, sisi2=None):
        self.sisi1 = sisi1
        self.sisi2 = sisi2

    def luas(self):
        pass

    def keliling(self):
        pass

class Persegi(BangunDatar):
    def luas(self):
        return self.sisi1 ** 2

    def keliling(self):
        return 4 * self.sisi1

class Segitiga(BangunDatar):
    def luas(self):
        return 0.5 * self.sisi1 * self.sisi2

    def keliling(self):
        return self.sisi1 + self.sisi2 + (self.sisi1 ** 2 + self.sisi2 ** 2) ** 0.5

class PersegiPanjang(BangunDatar):
    def luas(self):
        return self.sisi1 * self.sisi2

    def keliling(self):
        return 2 * (self.sisi1 + self.sisi2)

def main():
    persegi = Persegi(4)
    segitiga = Segitiga(3, 4)
    persegi_panjang = PersegiPanjang(7, 8)

    print("Luas")
    print(f"Persegi : {persegi.luas()}")
    print(f"Segitiga : {segitiga.luas()}")
    print(f"Persegi Panjang : {persegi_panjang.luas()}")

    print("Keliling")
    print(f"Persegi : {persegi.keliling()}")
    print(f"Segitiga : {segitiga.keliling()}")
    print(f"Persegi Panjang : {persegi_panjang.keliling()}")

if __name__ == "__main__":
    main()
