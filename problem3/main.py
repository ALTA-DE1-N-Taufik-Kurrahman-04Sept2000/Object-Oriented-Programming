# tulis solusi code disini
class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def penjumlahan(self):
        return self.angka1 + self.angka2

    def pengurangan(self):
        return self.angka1 - self.angka2

    def perkalian(self):
        return self.angka1 * self.angka2

    def pembagian(self):
        if self.angka2 == 0:
            return "Tidak dapat dibagi oleh nol"
        return self.angka1 / self.angka2

def main():
    penjumlahan = Kalkulator(3, 4)
    pengurangan = Kalkulator(15, 4)
    perkalian = Kalkulator(10, 10)
    pembagian = Kalkulator(12, 3)

    print("Penjumlahan :", penjumlahan.penjumlahan())
    print("Pengurangan :", pengurangan.pengurangan())
    print("Perkalian :", perkalian.perkalian())
    print("Pembagian :", pembagian.pembagian())

if __name__ == "__main__":
    main()