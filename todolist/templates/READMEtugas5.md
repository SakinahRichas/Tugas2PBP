1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
    
    Internal CSS ditulis dalam tag <style> dan ditulis di bagian atas header file HTML.
    Kelebihan:
    1. Perubahan hanya terjadi pd 1 halaman saja
    2. class dan id bisa digunakan oleh interneal stylesheet
    Kekurangan:
    1. Meningkatkan waktu akses website
    2. Tidak efisien jika ingin menggunakan CSS untuk beberapa file

    External CSS ditulis terpisah dengan kode HTML.
    Kelebihan:
    1. Ukuran html menjadi lebih kecil dan rapi
    2. loading website lebih cepat
    Kekurangan:
    1. Halaman akan berantakan jika file CSS gagal dipanggil oleh html.

    Inline CSS ditulis langsung di atribut pada file html.
    Kelebihan:
    1. Berguna untuk memperbaiki kode dengan cepat
    2. proses permintaan http yg lebih kecil dan proses load website akan lebih cepat
    Kekurangan:
    1. Hanya bisa diterapkan pada satu elemen html.

2. Jelaskan tag HTML5 yang kamu ketahui.

    <div> = section halaman

    <p> = paragraf

    <hr> = garis horizontal untuk batas suatu section

    <a href=""> = link halaman

    <ul> = unordered list

    <li> = item dari list

    <form> = untuk form

    <input> = membuat kolom form

    <button> = tombol

    <table> = tabel

    <tr> = baris tabel

    <th> = cell header

    <td> = cell biasa

    <img> = untuk gambar



3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    1. Selector tag, akan memilih berdasarkan nama tag. contoh:

        p{
            color: pink;
        }
        maka semua elemen yang <p> akan menjadi teks pink.

    2. Selector class, akan memilih berdasarkan nama class. COntoh:
        .login{
            color:black;
        }
        maka class pink akan berubah warna.

    3. Selector id, mirip class tapi hanya untuk satu elemen saja. contoh
        #header{
            background: black;
        }
        yang berubah hanya satu elemen saja, yaitu header.

    4. selector universal, untuk menyeleksi semua elemen pada scope tertentu. contoh
        *{
            border: 1px;
        }
        seluruh border akan beukuran 1px


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    Pertama saya sudah mencoba metode external CSS, namun html dan css nya tidak bisa terhubung. 
    Jadi, saya menggunakan inline css untuk tugas 5 kali ini.
    Saya menggunakan css framework bookstrap.

    Pertama, saya masuk ke login.html. Saya membuat card, menambahkan warna, dan memodifikasi letak elemen agar ditengah.
    Lalu, saya lanjut ke regster.html, disini saya juga menggunakan card, menambahkan warna, dan modifikasi letak elemen-elemennya.
    Untuk todolist.html, saya menambahkan table dan warna tabel, menambahkan selamat datang {{username}}.
    Kemudian, di bagian createtask.html saya membuat card, menambahkan warna, dan memodifikasi letak elemen agar ditengah.
    Lalu, saya deploy 
