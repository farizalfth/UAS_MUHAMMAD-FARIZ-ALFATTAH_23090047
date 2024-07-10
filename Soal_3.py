class RestaurantQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, order):
        """Menambahkan pesanan baru ke dalam antrian"""
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke dalam antrian.")
    
    def dequeue(self):
        """Menghapus pesanan dari depan antrian"""
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Pesanan '{order}' telah dihapus dari antrian.")
            return order
        else:
            print("Antrian kosong. Tidak ada pesanan yang dihapus.")
            return None
    
    def display_queue(self):
        """Menampilkan antrian saat ini"""
        if len(self.queue) > 0:
            print("Antrian pesanan saat ini:")
            for order in self.queue:
                print(order)
        else:
            print("Antrian kosong.")

if __name__ == "__main__":
    rq = RestaurantQueue()
    
    rq.enqueue("Pesanan 1: Nasi Goreng")
    rq.enqueue("Pesanan 2: Mie Ayam")
    rq.enqueue("Pesanan 3: Soto Ayam")
    
    rq.display_queue()
    
    rq.dequeue()
    rq.display_queue()
    
    rq.dequeue()
    rq.dequeue()
    rq.dequeue()  # Menghapus pesanan ketika antrian sudah kosong