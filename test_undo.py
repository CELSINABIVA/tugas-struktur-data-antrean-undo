import unittest
from undo import RiwayatUndo


class TestUndo(unittest.TestCase):
    def setUp(self):
        self.s = RiwayatUndo()

    # --- Penambahan data (push)
    def test_push_satu_aktivitas(self):
        self.s.push("05-10-2026 08:00", "Tambah Ahmad")
        self.assertEqual(self.s.size(), 1)

    def test_push_banyak_aktivitas_puncak_terbaru(self):
        self.s.push("08:00", "Tambah Ahmad")
        self.s.push("08:05", "Tambah Siti")
        self.assertEqual(self.s.peek(), ("08:05", "Tambah Siti"))

    def test_push_aktivitas_kosong_ditolak(self):
        with self.assertRaises(ValueError):
            self.s.push("08:00", "")

    # --- Penghapusan data (pop / Undo)
    def test_pop_lifo(self):
        self.s.push("08:00", "Tambah Ahmad")
        self.s.push("08:05", "Layani Ahmad")
        self.assertEqual(self.s.pop(), ("08:05", "Layani Ahmad"))
        self.assertEqual(self.s.pop(), ("08:00", "Tambah Ahmad"))

    def test_pop_stack_kosong(self):
        with self.assertRaises(IndexError):
            self.s.pop()

    # --- Melihat data teratas (peek)
    def test_peek_tidak_menghapus(self):
        self.s.push("08:00", "Tambah Ahmad")
        self.assertEqual(self.s.peek(), ("08:00", "Tambah Ahmad"))
        self.assertEqual(self.s.size(), 1)

    def test_peek_stack_kosong(self):
        with self.assertRaises(IndexError):
            self.s.peek()

    # --- Memeriksa kondisi kosong (is_empty)
    def test_is_empty_awal(self):
        self.assertTrue(self.s.is_empty())

    def test_is_empty_setelah_push_dan_pop(self):
        self.s.push("08:00", "Tambah Ahmad")
        self.assertFalse(self.s.is_empty())
        self.s.pop()
        self.assertTrue(self.s.is_empty())


if __name__ == "__main__":
    unittest.main()
