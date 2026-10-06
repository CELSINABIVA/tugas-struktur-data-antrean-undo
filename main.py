from antrean import AntreanLayanan
from undo import RiwayatUndo


def cetak(langkah, operasi, hasil, struktur):
    print(f"Langkah {langkah}: {operasi}")
    print(f"   Hasil   : {hasil}")
    print(f"   Struktur: {struktur}")


def simulasi_antrean():
    print("=== SIMULASI ANTREAN (QUEUE / FIFO) ===")
    antrean = AntreanLayanan()

    # Langkah 1
    m = antrean.enqueue("Ahmad Fauzi")
    cetak(1, "enqueue('Ahmad Fauzi')", f"masuk dengan nomor {m[0]}", antrean.tampil())

    # Langkah 2
    m = antrean.enqueue("Siti Rahma")
    cetak(2, "enqueue('Siti Rahma')", f"masuk dengan nomor {m[0]}", antrean.tampil())

    # Langkah 3
    m = antrean.enqueue("Budi Santoso")
    cetak(3, "enqueue('Budi Santoso')", f"masuk dengan nomor {m[0]}", antrean.tampil())

    # Langkah 4
    m = antrean.enqueue("Dewi Lestari")
    cetak(4, "enqueue('Dewi Lestari')", f"masuk dengan nomor {m[0]}", antrean.tampil())

    # Langkah 5
    m = antrean.enqueue("Rizki Pratama")
    cetak(5, "enqueue('Rizki Pratama')", f"masuk dengan nomor {m[0]}", antrean.tampil())

    # Langkah 6
    m = antrean.front()
    cetak(6, "front()", f"terdepan: {m[0]}.{m[1]} (tidak dihapus)", antrean.tampil())

    # Langkah 7
    m = antrean.dequeue()
    cetak(7, "dequeue()", f"dilayani: {m[0]}.{m[1]}", antrean.tampil())

    # Langkah 8
    m = antrean.dequeue()
    cetak(8, "dequeue()", f"dilayani: {m[0]}.{m[1]}", antrean.tampil())

    # Langkah 9
    kosong = antrean.is_empty()
    cetak(9, "is_empty()", f"{kosong} (sisa {antrean.size()} mahasiswa)", antrean.tampil())


def simulasi_undo():
    print("=== SIMULASI UNDO (STACK / LIFO) ===")
    undo = RiwayatUndo()
    A1 = ("05-10-2026 08:00", "Tambah mahasiswa Ahmad Fauzi ke antrean")
    A2 = ("05-10-2026 08:05", "Tambah mahasiswa Siti Rahma ke antrean")
    A3 = ("05-10-2026 08:10", "Layani mahasiswa Ahmad Fauzi")
    A4 = ("05-10-2026 08:15", "Tambah mahasiswa Budi Santoso ke antrean")
    A5 = ("05-10-2026 08:20", "Layani mahasiswa Siti Rahma")

    # Langkah 1
    undo.push(*A1)
    cetak(1, "push(A1)", f"disimpan: {A1[1]}", undo.tampil())

    # Langkah 2
    undo.push(*A2)
    cetak(2, "push(A2)", f"disimpan: {A2[1]}", undo.tampil())

    # Langkah 3
    undo.push(*A3)
    cetak(3, "push(A3)", f"disimpan: {A3[1]}", undo.tampil())

    # Langkah 4
    undo.push(*A4)
    cetak(4, "push(A4)", f"disimpan: {A4[1]}", undo.tampil())

    # Langkah 5
    undo.push(*A5)
    cetak(5, "push(A5)", f"disimpan: {A5[1]}", undo.tampil())

    # Langkah 6
    a = undo.peek()
    cetak(6, "peek()", f"teratas: {a[1]} (tidak dihapus)", undo.tampil())

    # Langkah 7
    a = undo.pop()
    cetak(7, "pop()  # Undo", f"dibatalkan: {a[1]}", undo.tampil())

    # Langkah 8
    a = undo.pop()
    cetak(8, "pop()  # Undo", f"dibatalkan: {a[1]}", undo.tampil())

    # Langkah 9
    kosong = undo.is_empty()
    cetak(9, "is_empty()", f"{kosong} (sisa {undo.size()} aktivitas)", undo.tampil())


if __name__ == "__main__":
    simulasi_antrean()
    print()
    simulasi_undo()
