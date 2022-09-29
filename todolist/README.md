1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

    CSRF Token digunakan untuk mencegah serangan CSRF, agar penyerang tidak bisa melakukan permintaan HTTP yang valid untuk diumpankan ke pengguna karena penyerang tidak bisa menentukan nilai token CSRF dari pengguna. 

    Jika tidak ada, penyerang bisa melakukan request ke aplikasi website seperti mengganti password korban, melakukan transfer uang, dan lain-lain.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

    Bisa, dengan membuat file html nya, seperti login.html dan register.html


3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

    User meng-input data lalu disimpan di variabel form di views.py, lalu form menyimpan data inputan tadi. Kemudian, views.py akan meminta data dari database melalui models.py untuk dilanjutkan ke template agar bisa ditampilkan di web / browser.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

    Pertama, saya membuat app todolist dengan command "python manage.py startapp todolist", lalu menambahkan todolist ke dalam setting.py dan path todolist ke urls.py

    Setelah itu, saya membuat models.py. Saya membuat class Task, dengan variabel user, date, title, dan description.
    
    Lalu saya ke views.py untuk membuat fungsi2 yang dibutuhkan. Pertama, saya membuat show_todolist yang berisi username dan data todolistnya yang me-refer ke template todolist.html.
    Lanjut, saya membuat fungsi login, register, dan logout sesuai dengan lab 3 sebelumnya. Setelah itu, saya membuat fungsi create_task yg me-refer ke template createtask.html

    Disamping itu, saya membuat forms.py yang berisi class CreateTask yang dipakai untuk fungsi create_task di views.py

    Lalu, saya membuat templatenya. Dimulai dari login.html dan register.html, isinya saya sesuaikan dengan lab sebelumnya.

    Untuk todolist.html saya menambahkan tombol Tambah yang akan me-refer ke create_task dan tombol Logout yang akan me-refer ke logout.

    Untuk createtask.html saya menambahkan input title, input description, dan tombol tambah.

    Setelah itu saya git add, commit, push dan deploy.