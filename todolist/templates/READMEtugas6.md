1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    Asynchronous programming adalah program yang bisa tetap merespon saat program berjalan. tidak perlu menunggu program selesei berjalan.
    Synchronus programming program dijalan satu per satu, harus menunggu program pertama selesei di jalankan, baru bisa ke tahap selanjutnya.


2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    event-driven programming adalah event yang disebabkan oleh user yang mengklik button atau input data, dll.
    contohnya 


3. Jelaskan penerapan asynchronous programming pada AJAX.
    programming asynchonus pada AJAX dapat membuat program dapat merespon meskipun program sedang berjalan, selain itu, AJAX juga tidak bergantung pada web server.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    Pertama, saya membuat method show_json di views.py untuk mendapatkan data dalam bentuk json, kemudian menambahkan path "/json" kedalam urls.py
    Lalu, buat method add di views.py , kemudian menambahkan path "/add"  kedalam urls.py
    Membuat modal di file  todolist_ajax.html lalu menggunakan ajax get dan ajax post.
    
    