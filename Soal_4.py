class Buah:
    def __init__(self, warna, nama, rasa):
        self.warna = warna
        self.nama = nama
        self.rasa = rasa
    
    def set_nama(self, nama):
        self.nama = nama
    
    def set_warna(self, warna):
        self.warna = warna
    
    def set_rasa(self, rasa):
        self.rasa = rasa
    
    def information(self):
        return f"Nama Buah: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"