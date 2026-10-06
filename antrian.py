"""Antrean layanan mahasiswa menggunakan struktur data QUEUE (FIFO).

Implementasi memakai collections.deque supaya enqueue (append) dan
dequeue (popleft) sama-sama O(1).
"""
from collections import deque


class AntreanLayanan:
    def __init__(self):
        self._data = deque()      # struktur data: Queue (deque)
        self._nomor_terakhir = 0  # penghitung nomor urut kedatangan

    def enqueue(self, nama):
        """Penambahan data: mahasiswa baru masuk di BELAKANG antrean."""
        if not isinstance(nama, str) or not nama.strip():
            raise ValueError("Nama mahasiswa tidak boleh kosong")
        self._nomor_terakhir += 1
        mahasiswa = (self._nomor_terakhir, nama.strip())
        self._data.append(mahasiswa)
        return mahasiswa

    def dequeue(self):
        """Penghapusan data: layani mahasiswa paling DEPAN."""
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data.popleft()

    def front(self):
        """Melihat data terdepan tanpa menghapusnya."""
        if self.is_empty():
            raise IndexError("Antrean kosong")
        return self._data[0]

    def is_empty(self):
        """Memeriksa apakah antrean kosong."""
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def tampil(self):
        if self.is_empty():
            return "Depan -> [ ] <- Belakang (kosong)"
        isi = ", ".join(f"{n}.{nama}" for n, nama in self._data)
        return f"Depan -> [{isi}] <- Belakang"
