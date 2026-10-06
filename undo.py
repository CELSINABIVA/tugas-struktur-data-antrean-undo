"""Fitur Undo menggunakan struktur data STACK (LIFO).

Implementasi memakai list Python: append() = push, pop() = pop,
keduanya O(1) (amortized untuk append) pada ujung belakang list.
"""


class RiwayatUndo:
    def __init__(self):
        self._data = []  # struktur data: Stack (list)

    def push(self, waktu, aktivitas):
        """Penambahan data: simpan aktivitas baru di PUNCAK stack."""
        if not isinstance(aktivitas, str) or not aktivitas.strip():
            raise ValueError("Aktivitas tidak boleh kosong")
        self._data.append((waktu, aktivitas.strip()))

    def pop(self):
        """Penghapusan data: batalkan (Undo) aktivitas TERAKHIR."""
        if self.is_empty():
            raise IndexError("Riwayat aktivitas kosong")
        return self._data.pop()

    def peek(self):
        """Melihat data teratas (aktivitas terakhir) tanpa menghapusnya."""
        if self.is_empty():
            raise IndexError("Riwayat aktivitas kosong")
        return self._data[-1]

    def is_empty(self):
        """Memeriksa apakah riwayat aktivitas kosong."""
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def tampil(self):
        if self.is_empty():
            return "Dasar -> [ ] <- Puncak (kosong)"
        isi = ", ".join(f"A{i}" for i in range(1, len(self._data) + 1))
        return f"Dasar -> [{isi}] <- Puncak"
