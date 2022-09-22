1. Perbedaan JSON, XML, dan HTML

    XML bersifat self-descriptive, strukturnya seperti tree, dimulai dari root, branch, dan leaves. file XML harus memiliki sebuah root element yang merupakan parent dari element lainnya. 

    Kalau JSON, filenya bersifat self=describing dan sangat mudah dimengerti oleh manusia. Sehingga sering digunakan di aplikasi web dan mobile. Selain itu, format JSON berbentuk text, disimpan dalam bentuk key dan value.

    Kalau HTML, lebih menitikberatkan pada format tampilan data, berbeda dengan XML yang lebih menitikberatkan pada struktur dan konteksnya. 

2.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Karena data delivery digunakan untuk melakukan pertukaran data dari suatu stack ke stack lainnya. agar stack yang menerima data dari stack pengirim bisa mengirimkan data yang sama, diperlukan format yang bisa mengubah atau merepresentasikan nya ke stack penerima, agar data tidak salah.

3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    Pertama saya membuat aplikasi mywatchlist dengan menggunakan command 'python manage.py startapp mywatchlist', menambahkan 'mywatchlist' ke INSTALLED_APPS di setting.py di folder project_django.

    Setelah itu, saya menambahkan 'path('mywatchlist/', include('mywatchlist.urls'))' di urls.py pada project_django. Lanjut, saya buat code untuk model.py. di model.py saya menginisiasi watched sebagai BooleanField, title dengan CharField(max_length=200), rating dengan IntegerField, release_date dengan DateField, dan review dengan TextField

    Lalu saya buat file initial_watchlist_data.json di folder fixtures yang baru dan mengisi 10 data untuk object mywatchlist.

    Setelah itu saya makemigrations, migrate, dan loaddata.

    Selanjutnya, saya membuat template, dengan memasukkan object2 sesuai dengan object yang sudah saya buat di model.py.
    Tambahan, saya membuat 2 template, untuk show_html, agar yang ditampilkan data htmlnya saja. 

    Lalu, saya lanjut ke view untuk membuat fungsi show_html, show_json, dan show_xml. dan juga menambahkan urlspattern di urls.py dengan path untuk html,xml, dan json yang sudah dibuat sebelumnya di views.py

    Setelahnya saya deploy ke herokuapp. Lanjut, saya membuat test.py sesuai dengan kode yang ada dislide scele. Awalnya saat saya menjalankan 'pyhon manage.py test' test nya tidak muncul hanya 'Ran 0 test' setelah melihat discord, saya membuat folder css dan membuat file style.css sesuai dengan petunjuk asdos. lalu menjalankan command 'python manage.py collectstatic'. sehingga test saya berhasil.

4. Screenshot postman saya lampirkan pada link berikut:
    1. HTML : https://drive.google.com/file/d/1Y62KgZSldfLqTVskX08LVFzGnw6hFl76/view?usp=sharing

    2. XML : https://drive.google.com/file/d/1dJivEseSMwfTLUnJ0WHHiw58MzfTCHEj/view?usp=sharing

    3. JSON : https://drive.google.com/file/d/1hRBgFzW93y8ClvrOfRoFVRK8QpVkl_DK/view?usp=sharing
    
