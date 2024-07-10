from Soal_4 import Buah

class Mangga(Buah):
    def __init__(self, warna, nama, rasa, vitamin):
        super().__init__(warna, nama, rasa)
        self.vitamin = vitamin
    
    def set_vitamin(self, vitamin):
        self.vitamin = vitamin
    
    def information(self):
        parent_info = super().information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

# Membuat instance objek dari kelas child Mangga
mangga = Mangga("Kuning", "Mangga Harum Manis", "Manis", "Vitamin C")

# Memanggil atribut dan metodenya
print(mangga.information())

# Mengubah nilai atribut menggunakan setter
mangga.set_nama("Mangga Manalagi")
mangga.set_warna("Hijau")
mangga.set_rasa("Asam Manis")
mangga.set_vitamin("Vitamin A")

# Menampilkan informasi setelah perubahan
print(mangga.information())