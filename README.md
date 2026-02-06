Tugas Analisis 1: • Apa yang terjadi jika kamu mengubah hero1. hp menjadi 500 setelah baris hero1 = Hero...? Coba lakukan print(hero1.hp).

-Jawab: Nilai hp dari hero1 akan berubah menjadi 500, sehingga ketika diprint, outputnya akan 500.

Tugas Analisis 2: Perhatikan parameter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

-Jawaban: Karena dengan menerima objek utuh, kita bisa mengakses semua atribut dan method dari objek lawan,
#bukan hanya nama. Misalnya, kita bisa memeriksa hp lawan, atau memanggil method lain dari objek lawan.

Tugas Analisis 3: Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora 
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no attribute 'name', padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?
Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke class Induk!

- jawaban: Error yang muncul adalah Mage object has no attribute 'name' karena constructor Hero tidak dijalankan. Fungsi super() berfungsi memanggil constructor class Induk agar
  atribut seperti name dan hp dimiliki oleh class Anak.

Tugas Analisis 4:
1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling bawah (luar class): print(f"Mencoba akses paksa: {hero1._Hero__hp}")
   Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling)
   dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik. 
2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya hanya self.__hp = nilai_baru. Pertanyaan: Kemudian lakukan hero1.set_hp(-100).
   Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method Setter sangat penting untuk menjaga integritas data dalam game!

- Jawaban: Saat menjalankan hero1.set_hp(-100), HP hero menjadi -100. Penjelasan: Tanpa validasi di setter: Data HP bisa menjadi negatif Sistem game jadi rusak
  dan tidak realistis Kesimpulan: Method setter sangat penting untuk menjaga integritas data, memastikan nilai HP tetap valid, aman, dan sesuai aturan game.

Tugas Analisis 5:
1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh blok method def serang(self, target):. Jalankan programnya.
   Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti pesan error Can't instantiate abstract class Hero with abstract method...?
   Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?
2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit(). Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
   Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

- jawaban: Interface memastikan aturan dipatuhi. Class abstrak tidak dibuat untuk dipakai langsung, tetapi sebagai dasar bagi class lain.

Tugas analisis 6: Apakah program berjalan lancar? Ya, program tetap berjalan lancar tanpa mengubah kode looping. Kesimpulan / Keuntungan Polimorfisme: 
Polimorfisme memudahkan penambahan karakter baru tanpa mengubah kode lama, sehingga program lebih fleksibel dan mudah dikembangkan di masa depan.

- Jawaban: Apa yang terjadi jika serang diganti tembak_panah? Program error karena method serang() tidak ditemukan. Mengapa nama method harus sama?
  Karena polimorfisme bergantung pada method dengan nama yang sama, agar satu pemanggilan method bisa bekerja untuk semua objek dengan perilaku berbeda.
