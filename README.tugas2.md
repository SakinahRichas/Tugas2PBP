Link aplikasi heroku : https://tugas2pbpsakinah.herokuapp.com/katalog/

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

    Berikut bagan yang saya buat:
    https://drive.google.com/file/d/10TJYpVl1mPBoRoRMMRWZ4RXqfGkBi9fU/view?usp=sharing

    Penjelasan bagan:
    User akan request laman melalui url, lalu url akan dilanjutkan requestnya ke views sesuai dengan request user. Views akan menerima request dan mengirim query sets ke dalam models. Dimana models ini yang akan melakukan transaksi data atau berinteraksi langsung dengan database. Lalu, jika transaksi data sukses, models akan mengirimkan result nya kepada views. Saat views menerima result, views akan men-generate respon ke template. Dari template, bisa menentukan tampilan laman web ke user



2. Virtual environment adalah sebuah wadah yang digunakan untuk menampung librari dan modul dalam suatu proyek/aplikasi agar terisolasi. 

    Kenapa kita perlu menggunakan virtual environment? 
    Karena ketika nantinya kita mengerjakan beberapa proyek / aplikasi dengan modul yang sama namun dengan versi yang berbeda, kita dapat mengisolasi proyek / aplikasi lainnya agar tidak tercampur. Dengan menggunakan virtual environment, masing- masing proyek / aplikasi akan memiliki modulnya sendiri.

    Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Tidak, karena untuk menjalankan command "python manage.py runserver" yang akan menjalankan dan melampilkan app, harus menggunakan atau mengaktifkan virtual environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas!

    Pertama tama, saya git clone repositori tugas 2, kemudian membuat virtual environment lalu mengaktifkannya.

    Lalu, karena app nya sudah ada di dalam repositori yaitu "katalog", saya lanjut melakukan perintah makemigrations untuk mempersiapkan migrasi kedalan database lokal django. dan lanjut menjalankan perintah migrate untuk menerapkan model yang telah dibuat ke dalam database lokal django.

    Selanjutnya, karena file json telah tersedia, saya lanjut melakukan perintah loaddata pada cmd untuk dapat memasukkan data didalamnya ke dalam database lokal django

    Selanjutnya saya membuat fungsi pada file views.py yang ada didalam folder katalog, yang nantinya akan mereturn file html yang sudah tersedia yaitu katalog.html

    Untuk dapat melakukan routing terhadap fungsi views.py sehingga nantinya halaman html dapat ditampilkan melalui browser, saya melanjutkan untuk membuat code di utls.py yg ada di folder katalog. saya membuat app_name menjadi 'katalog' dan urlpatterns yang berisi "path('', show_catalog, name= 'show_catalog')"

    Setelah membuat urls.py, saya mendaftarkan urls.py ke dalam project_django dengan menambahkan "path('katalog/', include('katalog.urls')), " kedalam variabel urlpatterns yang ada di file urls.py

    Selanjutnya, untuk menampilkan data pada tabel, saya melakukan code pada file views.py di dalam folder katalog yang nantinya akan menghubungkan views dengan template.Untuk mengambil data di database, saya mengimport models "from katalog.models import CatalogItem".  Selanjutnya, saya menambahkan code kedalam fungsi yang sudah dibuat sebelumnya dengan menginisiasi nama dan student id kedalam context. Lalu menambahkan context ke dalam return render.

    Selanjutnya, untuk dapat menampilkan daftar katalog, saya melakukan iterasi di dalam katalog.html.

    Setelah berhasil, saya melakukan add, commit, push ke github.

    Setelah itu, saya mendeploy aplikasi tersebut ke dalam heroku. Saya memasukkan kode ke dalam file dpl.yml yang ada di github/workflows sesuai dengan code yang ada di lab0. lalu memasukkan code juga ke dalam file gitignore. 

    Setelahnya, saya menambahkan beberapa konfigurasi kedalam settings.py, lalu menambahkan 'whitenoise.middleware.WhiteNoiseMiddleware', kedalam variabel middleware. Lalu saya git add, commit, dan push.

    Karena repositori saya belum menampilkan centang hijau, saya menambahkan variabel repository secret yang berisi nama aplikasi heroku saya dan API KEY heroku saya. Setelahnya, saya kembali menjalankan workflow yang gagal.

    Setelah menjalankan kembali workflows, muncul centang hijau di repositori yang menandakan deploy berhasil dilakukan.

