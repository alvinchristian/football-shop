# football-shop

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
7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Untuk melakukan deployment ke PWS, pertama saya membuat proyek baru bernama fulltimegear di pws, lalu saya tambahkan env variabel saya ke PWS agar dapat digunakan oleh website saya. Setelah itu saya tambahkan url `alvin-christian-fulltimegear.pbp.cs.ui.ac.id` ke AllOWED_HOST di `settings.py` agar aplikasi webnya mengenali url deployment PWS. Setelah itu tinggal jalankan perintah deployment yang ditunjukkan di PWS.







