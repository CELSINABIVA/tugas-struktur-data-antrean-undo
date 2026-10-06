import unittest
from antrean import AntreanLayanan


class TestAntrean(unittest.TestCase):
    def setUp(self):
        self.q = AntreanLayanan()

    # --- Penambahan data (enqueue)
    def test_enqueue_satu_data(self):
        self.assertEqual(self.q.enqueue("Ahmad Fauzi"), (1, "Ahmad Fauzi"))
        self.assertEqual(self.q.size(), 1)

    def test_enqueue_banyak_data_urut_kedatangan(self):
        for nama in ["Ahmad", "Siti", "Budi"]:
            self.q.enqueue(nama)
        self.assertEqual(self.q.front(), (1, "Ahmad"))
        self.assertEqual(self.q.size(), 3)

    def test_enqueue_nama_kosong_ditolak(self):
        with self.assertRaises(ValueError):
            self.q.enqueue("   ")

    # --- Penghapusan data (dequeue)
    def test_dequeue_fifo(self):
        self.q.enqueue("Ahmad")
        self.q.enqueue("Siti")
        self.assertEqual(self.q.dequeue(), (1, "Ahmad"))
        self.assertEqual(self.q.dequeue(), (2, "Siti"))

    def test_dequeue_antrean_kosong(self):
        with self.assertRaises(IndexError):
            self.q.dequeue()

    # --- Melihat data terdepan (front)
    def test_front_tidak_menghapus(self):
        self.q.enqueue("Ahmad")
        self.q.enqueue("Siti")
        self.assertEqual(self.q.front(), (1, "Ahmad"))
        self.assertEqual(self.q.size(), 2)

    def test_front_antrean_kosong(self):
        with self.assertRaises(IndexError):
            self.q.front()

    # --- Memeriksa kondisi kosong (is_empty)
    def test_is_empty_awal(self):
        self.assertTrue(self.q.is_empty())

    def test_is_empty_setelah_enqueue_dan_dequeue(self):
        self.q.enqueue("Ahmad")
        self.assertFalse(self.q.is_empty())
        self.q.dequeue()
        self.assertTrue(self.q.is_empty())


if __name__ == "__main__":
    unittest.main()
