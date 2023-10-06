class HargaPengiriman:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi
        berat_pembulatan = round(self.berat)

        if volume >= 40 and berat_pembulatan >= 1:
            harga = 5000
        else:
            harga = 0

        return f"Harga : Rp {harga}"

def main():
    panjang = 5
    lebar = 2
    tinggi = 4
    berat = 1

    harga_pengiriman = HargaPengiriman(panjang, lebar, tinggi, berat)
    print(harga_pengiriman.hitung_harga())

if __name__ == "__main__":
    main()
