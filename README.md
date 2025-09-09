# football-shop

Link : https://alvin-christian-fulltimegear.pbp.cs.ui.ac.id/

## Memenuhi checklist
1. Membuat sebuah proyek Django baru

Jalankan `django-admin startproject football_store .` untuk membuat django project bernama `football_store` di current directory </br >. Lalu saya membuat 2 file env, `.env` dan `.env.prod` yang akan digunakan untuk menyimpan data-data yang sensitif. Sebagai best practice, saya juga masukkan secret key django ke dalam kedua file tersebut. Lalu mengganti baris `SECRET_KEY` menjadi ```SECRET_KEY = os.getenv('SECRET_KEY')```

Setelah itu, saya membuat gitignore menggunakan template dari tutorial 0

2. Membuat aplikasi dengan nama main pada proyek tersebut.

Jalankan `python manage.py startapp main` untuk membuat direktori baru bernama main.</br >

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Tambahkan aplikasi `main` ke list Installed_Apps di file `settings.py`, ini akan membuat aplikasi main kita dikenali oleh proyek football_store</br>

4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
price sebagai harga item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
thumbnail sebagai gambar item dengan tipe URLField.
category sebagai kategori item dengan tipe CharField.
is_featured sebagai status unggulan item dengan tipe BooleanField.</br>

Untuk proyek kali ini saya menambahkan atribut `brand` yang bertipe `CharField`

Untuk mengimplementasikannya, cukup menambahkan kode ini ke `models.py` di aplikasi `main`.

```python
class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=15)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=10)
```

Kode ini akan membuat sebuah model bernama Products lewat kata kunci models.Model, lalu akan membuat atribut `name` dengan tipe `CharField` dan panjang maksimal 30 karakter, `price` dengan tipe `IntegerField`, `description` dengan tipe `Textfield`, `thumbnail` dengan tipe `URLField`, `category` dengan tipe `CharField` dan panjang maksimal 15 karakter, `is_featured` dengan tipe data `boolean` dimana nilai defaultnya adalah False, dan `brand` dengan tipe data `CharField` dan panjang maksimal 10

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Untuk ini saya menambahkan kode ini ke `views.py`
```python
def show_template(request):
    context = {
        'shop': 'Full Time Gear',
        'name': 'Alvin Christian Halim',
        'class': 'PBP F'
    }

    return render(request, "template.html", context)
```

kode ini mendefinisikan sebuah fungsi `show_template` dimana didalamnya ada 4 context yaitu `shop`, `name`, dan `class`. Lalu fungsi ini akan meretrun hasil render tersebut menurut `template.html`. Argumen request disini merupakan HTTP request yang diberikan ketika fungsi show_template dipanggil</br>

Karena untuk tugas individu kali ini hanya perlu menampilkan nama toko, nama, dan kelas, maka saya pakai template sederhana yang digunakan untuk tutorial 1</br>

```html
<p>{{ shop }}<p></p> 

<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}</p>

```
`{{}}` digunakan untuk mendisplay variabel yang ada didalamnya ketika html tersebut dirender. Dalam kasus ini, yang akan ditampilkan adalah nilai variabel `shop`, `name`, dan `class` menurut context di `show_template` diatas

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Untuk ini cukup tambahkan ini ke `urls.py`

```python
urlpatterns = [
    path('', show_template, name='show_template'),
]
```

Untuk penjelasan lebi lengkap ada di bagian berikutnya


7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Untuk melakukan deployment ke PWS, pertama saya membuat proyek baru bernama fulltimegear di pws, lalu saya tambahkan env variabel saya ke PWS agar dapat digunakan oleh website saya. Setelah itu saya tambahkan url `alvin-christian-fulltimegear.pbp.cs.ui.ac.id` ke AllOWED_HOST di `settings.py` agar aplikasi webnya mengenali url deployment PWS. Setelah itu tinggal jalankan perintah deployment yang ditunjukkan di PWS.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![flow](/images/basic-django.png)

ref:https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Introduction

Ketika seorang user membuka aplikasi django, maka browser akan mengirim sebuah `get` request. Sebuah get request dapat dianggap sebagai permintaan dari browser untuk mengambil sesuatu dari server. 

![request](/images/request.png)


Server akan menerima request tersebut dan "check" file `urls.py` untuk menentukan views mana yang tepat

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

dalam kasus aplikasi saya, karena by default ketika membuka aplikasi akan berada di root URL, maka request akan diteruskan ke urls di aplikasi main, namun jika saya mengunjungi endpoin admin maka request akan diteruskan ke urls di admin.site. Untuk seterusnya saya akan gunakan main.urls sebagai contoh.

Di dalam urls di main ada potongan kode ini

```python
urlpatterns = [
    path('', show_template, name='show_template'),
]
```

Karena kita berada di root URL, maka fungsi yang akan dipanggil adalah `show_template` dari `views.py` di aplikasi main.show_template memiliki kode berikut

```python
def show_template(request):
    context = {
        'shop': 'Full Time Gear',
        'name': 'Alvin Christian Halim',
        'class': 'PBP F'
    }

    return render(request, "template.html", context)
```

kode ini mengambil file `template.html` lalu merendernya dan mereturnnya. Server kemudian mengembalikan hasil html yang dirender dan juga sebuah kode ke client untuk ditampilkan ke pengguna. Kode ini untuk memberi tahu ke client status dariaksi, apakah berhasil atau gagal, dan jika gagal, mengapa. 

![response](/images/response.png)


Tentu kita bisa menambahkan endpoint lain yang akan melakukanaksi lain tapi konsepnya tetap sama. Contoh jika kita ingin menulis atau membaca suatu data model, maka response akan diteruskan dari view ke `models.py` dimana kita dapat mengambil atau menulis data ke model yang ada di aplikasi. Setelah itu, tergantung bagaimana kita mensetup routing, kita dapat merender/mengupdate html baru dan mengembalikannya ke client.

## Jelaskan peran settings.py dalam proyek Django!

Sesuai namanya, `settings.py` merupakan kode yang menentukan konfigurasi dari aplikasi kita. Kode settings ini sebenarnya hanya merupakan sekumpulan variabel yang akan digunakan oleh aplikasi kita. Sebagai contoh, ada variabel `SECRET_KEY`, value yang kita assign ke variabel ini akan menjadi secret key yang digunakan oleh aplikasi kita untuk kegiatan kriptografi seperti signing. Variabel `ALLOWED_HOSTS` akan mendefinisikan host mana saja yang dimana aplikasi kita dapat ditampilkan (ref: https://docs.djangoproject.com/en/5.2/ref/settings/#allowed-hosts). Masih ada banyak lagi variabel yang kita bisa setting di file `settings.py`, untuk dokumentasi lengkapnya bisa lihat di https://docs.djangoproject.com/en/5.2/ref/settings/#

## Bagaimana cara kerja migrasi database di Django?

Pada saat kita melakukan perubahan pada model, maka kita perlu mengupdate database kita agar semua sinkron, proses ini bernama migration. Ketika ingin melakukan migration, kita dapat mulai dengan menjalankan perintah `python manage.py makemigrations`. Django akan scan model kita dan bandingkan dengan versi sebelumnya yang disimpan di file migrasi kita. Jika ada perbedaan, maka Django akan membuat file migrasi baru yang berisi perubahan yang ada. Ini bisa dibilang mirip dengansistem version control dari git. Kemudian kita dapat jalankan `python manage.py migrate` untuk mulai proses migrasi, tinggal tunggu sampai prosesnya kelar (ref: https://docs.djangoproject.com/en/5.2/topics/migrations/#migration-files)

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, alasan pertama adalah karena Django merupakan framework python, yang merupakan bahasa yang paling simpel dibanding bahasa-bahasa lain seperti php, javascript, dll. Kedua Django juga bagus untuk pengenalan design arkitektur, khususnya MVT, karena flownya jelas dan terstruktur. Terakhir, proses dari membuat proyek sampai mendeploy relatif mudah karena Django sudah memberikan cara untuk automasi seperti startapp, startproject, migrate, makemigrations, runserver, dll.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Mungkin dari saya belum ada karena dari materi tutorial sudah sangat membantu dan saya belum ketemu kendala apa-apa.






