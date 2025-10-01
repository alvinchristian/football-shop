# football-shop

Link : https://alvin-christian-fulltimegear.pbp.cs.ui.ac.id/

<details>
<summary> Tugas 2 </summary>

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

Untuk proyek kali ini saya menambahkan atribut `brand` yang bertipe `CharField` dan juga atribut `sold` yang bertipe `IntegerField` untuk menunjukkan berapa banyak dari produk tertentu sudah terjual

Untuk mengimplementasikannya, cukup menambahkan kode ini ke `models.py` di aplikasi `main`.

```python
    Category_Choices = [
        ('topwear', 'Top Wear'),
        ('bottomwear', 'Bottom Wear'),
        ('shoes', 'Shoes'),
        ('gloves', 'Gloves'),
        ('accessories', 'Accessories'),
        ('socks', 'Socks'),
        ('trainingequipment', 'Training Equipment'),
        ('ball', 'Ball'),
        ('bag', 'Bag'),
    ]

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=Category_Choices)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=10)
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def add_sold(self, quantity):
        self.sold += quantity
        self.save()
```

Kode ini akan membuat sebuah model bernama Products lewat kata kunci models.Model, lalu akan membuat atribut `name` dengan tipe `CharField` dan panjang maksimal 30 karakter, `price` dengan tipe `IntegerField`, `description` dengan tipe `Textfield`, `thumbnail` dengan tipe `URLField`, `category` dengan tipe `CharField` dan panjang maksimal 20 karakter dan pilihan dari `Category_Choices`, `is_featured` dengan tipe data `boolean` dimana nilai defaultnya adalah False, `brand` dengan tipe data `CharField` dan panjang maksimal 10, dan `sold` dengan tipe data `IntegerField`

setelah itu ada fungsi `__str__` yang digunakan untuk mengembalikan nama dari model, dan fungsi `add_sold` yang berfungsi untuk menambah nilai atribut `sold`

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
</details>

<details>
<summary> Tugas 3 </summary>

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Sebuah platform tidak dapat berjalan tanpa adanya data, dan kita perlu sebuah cara untuk memindahkan data dari satu tempat ke tempat lain. Inilah gunanya data delivery, sebagai contoh misalkan sebuah platform menyimpan data dari produk yaitu nama, harga, dan stok. Data ini disimpan di database, ketika seorang user mengunjungi webstie tersebut untuk melihat produk, website harus dapat menampilkan data-data dari produk tersebut. Jadi harus ada perpindahan data dari database ke frontend untuk ditampilkan

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Saya pribadi lebih suka JSON karena lebih simpel untuk ditulis dan dibaca. JSON lebih populer karena lebih ringan dibanting XML sehingga dapat di-parse lebih cepat. (ref : https://www.geeksforgeeks.org/html/difference-between-json-and-xml/)

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

method is_valid() digunakan untuk ngecek apakah input form tersebut sesuai atau tidak dengan model yang ditentukan. Sebagai contoh, jika atribut nama memiliki maksimal panjang 10 char, dan ada yang input lebih dari 10 char maka method is_valid() akan mereturn false dan form tidak dapat disubmit. Sama juga jika pengguna tidak mengisi bagian yang wajib, seperti jika mencoba register tanpa memasukkan username atau password.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Cross-site request forgery (CSRF) merupakan sebuah serangan dimana seorang penyerang dapat mengirimkan request yang berbahaya atas nama pengguna. CSRF dapat terjadi ketika seorang user sedang logged in ke sebuah aplikasi. Untuk menjaga session, aplikasi web akan membuat cookie. Hal yang penting untuk dicatat adalah ketika kita mengirim sebuah request ke aplikasi tersebut, cookie akan secara otomatis dikirim juga ke server. 

Misalkan user sedang logged in ke aplikasi bank. Lalu dia pergi ke website lain yang ternyata dibuat oleh penyerang. Saat di website tersebut, ternyata website mengirim sebuah request ke aplikasi bank untuk mengganti password. Karena cookienya juga dikirim maka web bank menggangap bahwa user tersebut yang ingin mengganti password

![csrf](/images/csrf.svg)

CSRF token merupakan sebuah token random yang digunakan untuk mencegah CSRF. CSRF Ketika user mengirim form, maka CSRF token tersebut juga akan dikirm ke server, biasanya lewat hidden field di html dengan metode POST. Server akan cek apakah token tersebut sesuai, jika iya maka aksi tersebut akan dilakukan. Namun jika tidak maka aksi tersebut akan direject (ref: https://portswigger.net/web-security/csrf)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1.  Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

di `views.py` saya tambahkan 4 fungsi ini
```python
def show_xml(request):
    products = Products.objects.all()
    xml_data = serializers.serialize("xml", products)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Products.objects.all()
    json_data = serializers.serialize("json", products)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    products = Products.objects.get(id=id)
    xml_data = serializers.serialize("xml", [products])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    products = Products.objects.get(id=id)
    json_data = serializers.serialize("json", [products])
    return HttpResponse(json_data, content_type="application/json")
```

fungsi-fungsi tersebut berguna untuk menampilkan data products dalam bentuk xml (show_xml) dan json(show_json). Terdapat juga 2 fungsi untuk menampilkan data produk tertentu berdasarkan idnya dalam bentuk json (show_json_by_id) dan (show_xml_by_id)

2. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.

Dalam `urls.py` saya tambahkan 4 endpoint ini

```python
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
```

endpoint xml digunakan untuk menampilkan data dlm xml, endpoint json untuk menampilkan dlm json, xml/<uuid:id>/ untuk menampilkan data produk dengan uuid tertenu dlm xml, dan json/<uuid:id> dalam json

3.  Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.

Catatatan bahwa semua kode html digenerate oleh AI

`template.html` diubah menjadi 

```html
 {% extends 'base.html' %}
 {% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ shop }}</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .header { text-align: center; margin-bottom: 20px; }
        .add-button {
            display: inline-block;
            margin: 10px 0;
            padding: 10px 20px;
            background: dodgerblue;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 16px;
        }
        .add-button:hover { background: royalblue; }

        /* Product grid */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            max-width: 1000px;
            margin: auto;
        }
        .product-card {
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            text-align: center;
        }
        .product-card img {
            width: 250px;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 12px;
        }
        .product-card h2 {
            margin: 8px 0;
            font-size: 18px;
        }
        .price { font-weight: bold; color: green; margin: 5px 0; }
        .featured {
            color: #fff;
            background: crimson;
            padding: 3px 6px;
            border-radius: 5px;
            font-size: 11px;
            margin-left: 6px;
        }
        .details-button {
            display: inline-block;
            margin-top: 12px;
            padding: 8px 16px;
            background: #0b5ed7;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 14px;
        }
        .details-button:hover {
            background: #084298;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{ shop }}</h1>
        <h5>Name: {{ name }}</h5>
        <h5>Class: {{ class }}</h5>
        <a href="{% url 'main:add_product' %}" class="add-button">Add Product</a>
    </div>

    <div class="product-grid">
        {% for product in products %}
            <div class="product-card">
                <img src="{{ product.thumbnail }}" alt="{{ product.name }}">
                <h2>
                    {{ product.name }}
                    {% if product.is_featured %}
                        <span class="featured">Featured</span>
                    {% endif %}
                </h2>
                <p class="price">Rp {{ product.price }}</p>
                <p><strong>Brand:</strong> {{ product.brand }}</p>
                <p><strong>Stock:</strong> {{ product.stock }}</p>
                <a href="{% url 'main:show_product' product.id %}" class="details-button">View Details</a>
            </div>
        {% empty %}
            <p>No products available.</p>
        {% endfor %}
    </div>
</body>
</html>
{% endblock content %}

```

Disini ada button dengan label Add Product yang akan redirect ke url bernama add_product (path('add/', add_product, name='add_product')) diamana kita bisa menambahkan produk. 

Selain itu kita jalankan sebuah for loop untuk setiap produk dan menampilkan nama, harga, brand, dan jumblah stok

```html
        {% for product in products %}
            <div class="product-card">
                <img src="{{ product.thumbnail }}" alt="{{ product.name }}">
                <h2>
                    {{ product.name }}
                    {% if product.is_featured %}
                        <span class="featured">Featured</span>
                    {% endif %}
                </h2>
                <p class="price">Rp {{ product.price }}</p>
                <p><strong>Brand:</strong> {{ product.brand }}</p>
                <p><strong>Stock:</strong> {{ product.stock }}</p>
                <a href="{% url 'main:show_product' product.id %}" class="details-button">View Details</a>
```

ada juga button details yang akan redirect ke url bernama show_product (    path('product/<uuid:id>/', show_product, name='show_product'),)

Kode untuk show_product dalam views.py adalah

```python
def show_product(request, id):
    product = get_object_or_404(Products, id=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
```

Yaitu hanya sekedar merender `product_detail.html` untuk produk dengan id tertentu. 

4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya.

Kode dari `forms.py` adalah

```python
from django.forms import ModelForm
from main.models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "description", "price", "category", "thumbnail", "is_featured", "brand","stock"]



```

dimana forms ini akan digunakan di `add_product`

```python
def add_product(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_template')
    
    context = {'form': form}
    return render(request, 'add_product.html', context)

```

dengan kode html `add_product.html`

```html
 {% extends 'base.html' %}
 {% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Product</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .form-container {
            width: 400px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-container form p {
            margin-bottom: 15px;
        }
        .form-container button {
            width: 100%;
            padding: 10px;
            background: dodgerblue;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        .form-container button:hover {
            background: royalblue;
        }
        .back-link {
            display: block;
            margin-top: 15px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Add New Product</h2>
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Save Product</button>
        </form>
        <a href="{% url 'main:show_template' %}" class="back-link">⬅ Back to Products</a>
    </div>
</body>
</html>
{% endblock content %}

```

4. Membuat halaman yang menampilkan detail dari setiap data objek model.

Berikut adalah kode untuk `product_detail.html`. Kegunaan dari `product_detail.html` sudah dijelaskan di nomor 3


```html
 {% extends 'base.html' %}
 {% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ product.name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .product-card {
            width: 400px;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            margin: 20px auto;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .product-card img {
            width: 100%;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        .product-card h2 {
            margin: 10px 0;
        }
        .price {
            font-size: 20px;
            font-weight: bold;
            color: green;
        }
        .featured {
            color: #fff;
            background: crimson;
            padding: 4px 8px;
            border-radius: 5px;
            font-size: 12px;
            margin-left: 10px;
        }
        .add-button {
            display: inline-block;
            margin: 20px auto;
            padding: 10px 20px;
            background: dodgerblue;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 16px;
            transition: background 0.3s;
        }
        .add-button:hover {
            background: royalblue;
        }
    </style>
</head>
<body>

    <!-- Single Product -->
    <div class="product-card">
        <img src="{{ product.thumbnail }}" alt="{{ product.name }}">
        <h2>{{ product.name }}
            {% if product.is_featured %}
                <span class="featured">Featured</span>
            {% endif %}
        </h2>
        <p class="price">Rp {{ product.price }}</p>
        <p><strong>Stock:</strong> {{ product.stock }}</p>
        <p><strong>Category:</strong> {{ product.get_category_display }}</p>
        <p><strong>Brand:</strong> {{ product.brand }}</p>
        <p><strong>Sold:</strong> {{ product.sold }}</p>
        <p><strong>Description:</strong></p>
        <p>{{ product.description }}</p>

    </div>
</body>
</html>
{% endblock content %}

```

Yaitu mencetak name, price, stock, category, brand, desc, dan jumblah sold


## Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

`/xml`

![alt text](/images/xml.png)

`/json`
![alt text](/images/json.png)

`/xml/7dd4b197-d4ce-4c98-978b-48ef8d52af39`
![alt text](/images/xml-id.png)

`/json/7dd4b197-d4ce-4c98-978b-48ef8d52af39`
![alt text](/images/json-id.png)
</details>

<details>
<summary> Tugas 4 </summary>

## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan dari django yang digunakan untuk melakukan authentikasi pada saat login. Kelebihan dari AuthenticationForm adalah karena merupakan bawwan django, simpel untuk di set up dan sudah aman. Kekurangannya adalah fiturnya yang minim sehingga tidak ada pilihan seperti remember me (walaupun bisa ditambahkan) dan memaksa kita untuk menggunakan User bawaan dari django. Jika kita ingin menggunakan User custom, maka harus ada yang diganti.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses untuk memverifikasi identitas user (you're who you say you are) sedangkan otorisasi merupakan proses untuk memberifikasi apakah anda mempunyai akses untuk suatu hal. Untuk autentikasi kita bisa gunakan AuthenticationForm yang sudah dijelaskan di bagian sebelumnya sedangkan untuk otorisasi kita bisa menggunakan decorator seperti `@login_required`

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Session sendiri lebih lebih aman karena di store di server dan dapat menampung lebih banyak informasi. Sedangkan untuk cookies di store di client side sehingga kurang dan hanya dapat menyimpan sedikit informasi namun kelebihannya adalah cookies lebih ringan dan cepet sehingga tidak akan membenani server dibanding session yang bisa memakan memori yang lebih besar.  

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default penggunaan cookies belum tentu aman, pertama cookies dapat diubah oleh semua orang, sehingga perlu ada check untuk integriti dari cookie tersebut. Untuk django, cookies disecure menggunakan signing menggunakan secret key sehingga jika ada yang diubah, maka signaturenya tidak akan cocok. Selain itu, cookies juga ada kemungkinan untuk dicuri lewat serangan seperti Cross-Site Scripting (XSS), di django cookies mempunyai default keamanan yaitu `SESSION_COOKIE_HTTPONLY` = True sehingga cookie tidak bisa di akses lewat javascript. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.

Untuk ini kita cukup tambahkan 3 fungsi di `views.py`

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
          user = form.get_user()
          login(request, user)
          response = HttpResponseRedirect(reverse('main:show_template'))
          response.set_cookie('last_login', str(datetime.datetime.now()))
          return response
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

``` 
dan juga import 

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
```

Setelah itu tinggal tambahin `@login_required(login_url='/login')` di fungsi yang ingin kita restrik


2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.

Ini cukup register 2 akun terus masing-masing akun bikin 3 produk

3. Menghubungkan model Product dengan User.

Pertama-tama kita perlu mengimport User lalu menambahkan ```user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)``` ke products.

Setelah itu kita tinggal modifikasi `show_template` agar mengambil username dari requestnya dan last_login dari cookies dan menambahkan functionality untuk filter berdasarkan all products or my products

```python
@login_required(login_url='/login')
def show_template(request):
    filter_type = request.GET.get('filter','all')
    
    if filter_type == 'all':
        product_list = Products.objects.all()
    else:
        product_list = Products.objects.filter(user=request.user)
    context = {
        'shop': 'FullTime Gear',
        'name': request.user.username,
        'class': 'PBP F',
        'products': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    
    return render(request, "template.html", context)
```

dan `add_product` untuk membuat user product dari username yang membuatnya

```python
@login_required(login_url='/login')
def add_product(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_template')
    
    context = {'form': form}
    return render(request, 'add_product.html', context)
```

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.

Untuk ini tinggal ambil context dari show_template lalu tambahkan ke html

```html
 {% extends 'base.html' %}
 {% block content %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ shop }}</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .header { text-align: center; margin-bottom: 20px; }
        .add-button {
            display: inline-block;
            margin: 10px 0;
            padding: 10px 20px;
            background: dodgerblue;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 16px;
        }
        .add-button:hover { background: royalblue; }

        /* Product grid */
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            max-width: 1000px;
            margin: auto;
        }
        .product-card {
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            text-align: center;
        }
        .product-card img {
            width: 250px;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 12px;
        }
        .product-card h2 {
            margin: 8px 0;
            font-size: 18px;
        }
        .price { font-weight: bold; color: green; margin: 5px 0; }
        .featured {
            color: #fff;
            background: crimson;
            padding: 3px 6px;
            border-radius: 5px;
            font-size: 11px;
            margin-left: 6px;
        }
        .details-button {
            display: inline-block;
            margin-top: 12px;
            padding: 8px 16px;
            background: #0b5ed7;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 14px;
        }
        .details-button:hover {
            background: #084298;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{ shop }}</h1>
        <h5>Name: {{ name }}</h5>
        <h5>Class: {{ class }}</h5>
        <a href="{% url 'main:add_product' %}" class="add-button">Add Product</a>
        <a href="{% url 'main:logout' %}" class="add-button">Logout</a>
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        <a href="?filter=all" class="add-button">All Products</a>
        <a href="?filter=my" class="add-button">My Products</a>
    </div>

    <div class="product-grid">
        {% for product in products %}
            <div class="product-card">
                <img src="{{ product.thumbnail }}" alt="{{ product.name }}">
                <h2>
                    {{ product.name }}
                    {% if product.is_featured %}
                        <span class="featured">Featured</span>
                    {% endif %}
                </h2>
                <p class="price">Rp {{ product.price }}</p>
                <p><strong>Brand:</strong> {{ product.brand }}</p>
                <p><strong>Stock:</strong> {{ product.stock }}</p>
                <a href="{% url 'main:show_product' product.id %}" class="details-button">View Details</a>
            </div>
        {% empty %}
            <p>No products available.</p>
        {% endfor %}
        
    </div>
</body>
</html>
{% endblock content %}
```

</details>

<details>
<summary> Tugas 5 </summary>

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Secara umum CSS memiliki 3 jenis, inline style, external dan internal style, dan browser default. Prioritasnya adalah inline style > external/internal style > browser default. Jika ada lebih dari 2 CSS dalam jenis CSS yang sama, maka selector CSS yang ditulis terbaru akan memiliki prioritas. Selain itu juga ada atribut !important yang dapat ditambahkan yang akan membuat selector tersebut memiliki prioritas tertinggi, lebih dari inline.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Layout dan penampilan dari website kita tergantung dengan ukuran dan jenis display yang digunakan oleh perangkat pengguna. Penampilan yang rapih dan bagus untuk dilihat di laptop belum tentu rapih dan bagus di mobile karena dimensinya yang berbeda. Sehingga penting membuat responsive design agar design kita bisa menyesuaikan dengan dimensi display yang berbeda sehingga semua pengguna dapat memiliki pengalaman yang sama-sama baik. 

Contoh yang paling mudah adalah navbar. Untuk mobile navbar sering kali menggunakan tombol "hamburger" yang akan mendisplay semua opsi ketika ditekan. Mengapa? Karena lebar dari perangkat mobile lebih kecil dipanding laptop atau tablet. Pada laptop kita bisa taruh semua opsinya langsung di navbar dan akan tetap terlihat rapih karena lebar display device kita. Namun apabila kita buat hal yang sama di mobile, maka antara satu opsi dengan opsi yang lain akan berdempetan atau bahkan bertimpaan karena kita mencoba memasukkan opsi yang banyak ke navbar yang memiliki lebar yang lebih pendek, maka untuk mengatasinya ditambahkan tombol yang akan mendisplay opsi secara vertikal dibanding horizontal

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin adalah jarak antara elemen satu dengan yang lain dan berwarna transparan. Contoh penggunaannya adalah :
```css
.box {
  margin: 20px; /
}
```

ini artinya .box akan memiliki jarak 20 pixel dari elemen yang lain

Border adalah garis yang menggelilingi sebuah elemen dan dapat kita tambahkan warna, ketebalan, dan styling. Contoh pengunaannya adalah :
```css
.box {
  border: 2px solid black;
}
```

Ini artinya .box akan memiliki garis solid seukuran 2 pixel berwarna hitam disekelilingnya

Padding adalah jarak antara konten elemen tersebut dengan bordernya. Contoh penggunaanya adalah :
```css
.box {
  padding: 15px; 
}
```
artinya antara isi dari .box dan bordernya memiliki jarak 15 pixel

Berikut adalah visualisasinya (ref : https://blog.hubspot.com/website/css-margin-vs-padding)

![](/images/margin-vs-padding-vs-border.webp)

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flex box dan grid adalah sebuah modul css yang memungkinkan kita untuk mengatur layout dari website kita. Untuk grid, menggunakan sistem dua dimensi yaitu row dan coloumn. Oleh sebab itu, grid cocok untuk mengatur layout dua dimensi. Sedangkan untuk flexbox hanya bisa satu dimensi, row atau column sehingga cocok untuk layout 1 dimensi. Ref : https://www.geeksforgeeks.org/css/comparison-between-css-grid-css-flexbox/

Untuk flex box terdapat 2 elemen yaitu flex container dan item, flex container adalah tempat menyimpan flex items. Flexbox juga memiliki property flex-direction yang dapat memudahkan kita untuk menentukan arah display dari flex item di dalam flex box tersebut. Ada 4 value: row, column, row-reverse, dan column reverse(ref : https://www.w3schools.com/css/css3_flexbox_container.asp)

grid juga memiliki grid container dan item dengan konsep yang mirip. Di dalam grid container ada property grid-template-columns yang memungkinkan kita untuk mengatur ukuran-ukuran dari kolom di grid tersebut, hal yang sama juga ada untuk rows yaitu grid-template-rows (ref:https://www.w3schools.com/css/css_grid_container.asp)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Implementasikan fungsi untuk menghapus dan mengedit product. 

Untuk ini cukup menambahkan 2 fungsi ke `views.py`

```python
def delete_product(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return redirect('main:show_template')

def edit_product(request, id):
    product = get_object_or_404(Products, id=id)
    form = ProductsForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_template')
    
    context = {'form': form}
    return render(request, 'edit_product.html', context)
```
fungsi delete_product akan menghapus product dengan id `id` sedangkan untuk edit_product akan membuat form yang memungkinkan kita untuk mengedit detail dari product tersebut

2. Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.

Untuk styling saya menggunakan tailwind css, pertama-tama kita perlu tambahkan tailwind ke base.html

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

Setelah itu kita akan membuat folder `static` yang akan menyimpan css kita, di dalam folder tersebut kita akan buat `global.css`
```css
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #16a34a;
    box-shadow: 0 0 0 3px #16a34a;
}

.form-style input[type="checkbox"] {
    width: 1.25rem;
    height: 1.25rem;
    padding: 0;
    border: 2px solid #d1d5db;
    border-radius: 0.375rem;
    background-color: white;
    cursor: pointer;
    position: relative;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
}

.form-style input[type="checkbox"]:checked {
    background-color: #16a34a;
    border-color: #16a34a;
}

.form-style input[type="checkbox"]:checked::after {
    content: '✓';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-weight: bold;
    font-size: 0.875rem;
}

.form-style input[type="checkbox"]:focus {
    outline: none;
    border-color: #16a34a;
    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.1);
}
```
Di base.html sudah ada load static sehingga semua template yang mengextend base.html dapat menggunakan elemen css, kita tinggal mengubah html dari login, product detail, register, add product, dan edit product agar lebih menarik. Untuk sebagian besar, kodenya masih sama dengan tutorial namun untuk register dan login saya menambahkan fitur untuk show dan hide password menggunakan javascript. Berikut html untuk login

```html
{% extends 'base.html' %}

{% block meta %}
<title>Login - FullTime Gear</title>
{% endblock meta %}

{% block content %}
<div class="bg-gradient-to-br from-green-50 via-white to-green-100 w-full min-h-screen flex items-center justify-center p-8">
  <div class="max-w-md w-full">
    <div class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style">
      <div class="text-center mb-8">
        <h1 class="text-2xl font-bold text-gray-900 mb-2">Sign In</h1>
        <p class="text-gray-600">Welcome back to FullTime Gear</p>
      </div>

      
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-6">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 mb-2">Username</label>
          <input 
            id="username" 
            name="username" 
            type="text" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500 transition-colors" 
            placeholder="Enter your username">
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
          <div class="relative">
            <input 
              id="password" 
              name="password" 
              type="password" 
              required 
              class="w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:border-green-500 transition-colors" 
              placeholder="Enter your password">
            
            <button type="button" onclick="togglePassword()" 
              class="absolute inset-y-0 right-3 flex items-center text-gray-400 hover:text-gray-600">

              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="#000000" aria-hidden="true" id="open-eye" height="16" width="16">
                <path d="M8 10a2 2 0 1 0 0 -4 2 2 0 0 0 0 4Z" stroke-width="0.6667"></path>
                <path fill-rule="evenodd" d="M0.8819999999999999 7.631333333333332C1.8739999999999999 4.650666666666666 4.6853333333333325 2.5 8.000666666666666 2.5c3.313333333333333 0 6.123333333333333 2.1486666666666663 7.116666666666667 5.126666666666667 0.07999999999999999 0.24133333333333332 0.07999999999999999 0.5013333333333333 0 0.742 -0.9913333333333334 2.9806666666666666 -3.8033333333333332 5.131333333333333 -7.117999999999999 5.131333333333333 -3.313333333333333 0 -6.124 -2.1486666666666663 -7.116666666666667 -5.126666666666667a1.1746666666666665 1.1746666666666665 0 0 1 0 -0.742ZM11.5 8a3.5 3.5 0 1 1 -7 0 3.5 3.5 0 0 1 7 0Z" clip-rule="evenodd" stroke-width="0.6667"></path>
              </svg>
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="#000000" aria-hidden="true" id="close-eye" height="16" width="16" class="hidden">
                <desc>
                  Eye Slash Streamline Icon: https://streamlinehq.com
                </desc>
                <path d="M2.353333333333333 1.6466666666666667a0.5 0.5 0 0 0 -0.7066666666666667 0.7066666666666667l12 12a0.5 0.5 0 1 0 0.7066666666666667 -0.7066666666666667l-12 -12Zm12.764 6.7219999999999995a7.499333333333333 7.499333333333333 0 0 1 -1.7539999999999998 2.873333333333333l-2.066 -2.066a3.5 3.5 0 0 0 -4.473333333333333 -4.473333333333333L5.172666666666666 3.051333333333333a7.478 7.478 0 0 1 2.828 -0.5513333333333332c3.313333333333333 0 6.123333333333333 2.1486666666666663 7.116666666666667 5.126666666666667 0.07999999999999999 0.24133333333333332 0.07999999999999999 0.5013333333333333 0 0.742Z" stroke-width="0.6667"></path>
                <path d="M10.5 8c0 0.12 -0.008666666666666666 0.238 -0.024666666666666663 0.35333333333333333l-2.829333333333333 -2.828666666666667A2.5 2.5 0 0 1 10.5 8Zm-2.1466666666666665 2.4753333333333334 -2.828666666666667 -2.829333333333333a2.5 2.5 0 0 0 2.829333333333333 2.828666666666667Z" stroke-width="0.6667"></path>
                <path d="M4.5 8c0 -0.4126666666666666 0.07133333333333333 -0.8086666666666666 0.20266666666666666 -1.176l-2.0666666666666664 -2.0666666666666664a7.5 7.5 0 0 0 -1.7533333333333332 2.873333333333333c-0.07999999999999999 0.24133333333333332 -0.07999999999999999 0.5013333333333333 0 0.7426666666666667 0.9926666666666667 2.9779999999999998 3.802666666666666 5.126666666666667 7.116666666666667 5.126666666666667 1 0 1.9553333333333331 -0.19599999999999998 2.828 -0.5513333333333332l-1.651333333333333 -1.651333333333333A3.5 3.5 0 0 1 4.5 8Z" stroke-width="0.6667"></path>
              </svg>
            </button>
          </div>
        </div>


        <button 
          type="submit" 
          class="w-full bg-green-600 text-white font-medium py-3 px-4 rounded-md hover:bg-green-700 transition-colors">
          Sign In
        </button>
      </form>

      
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded-md text-sm border mb-2
                {% if message.tags == 'success' %}
                  bg-green-50 border-green-200 text-green-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

     
      <div class="mt-6 text-center pt-6 border-t border-gray-200">
        <p class="text-gray-500 text-sm">
          Don't have an account? 
          <a href="{% url 'main:register' %}" class="text-green-600 hover:text-green-700 font-medium">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>

<script>
  function togglePassword() {
    const input = document.getElementById("password");
    const openEye = document.getElementById("open-eye");
    const closeEye = document.getElementById("close-eye");

    if (input.type === "password") {
      input.type = "text";
      openEye.classList.add("hidden");
      closeEye.classList.remove("hidden");
    } else {
      input.type = "password";
      closeEye.classList.add("hidden");
      openEye.classList.remove("hidden");
    }
  }
</script>
{% endblock content %}
```

Selain itu saya juga menambahkan gradient pada background

Untuk product_detail.html saya memodifikasi dikit agar thumbnailnya dapat selalu terlihat secara penuh dan berada di tengah dan menambahkan border hijau.

```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>{{ product.name }} - FullTime Gear</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-50 w-full min-h-screen">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Back Navigation -->
        <div class="mb-6">
            <a href="{% url 'main:show_template' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
                ← Back to Products
            </a>
        </div>
        
        <!-- Product -->
        <article class="bg-white rounded-lg border border-gray-200 overflow-hidden">
            
            <!-- Header -->
            <div class="p-6 sm:p-8">
                <div class="flex flex-wrap items-center gap-2 mb-4">
                    {% if product.is_featured %}
                        <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-green-600 text-white">
                            Featured
                        </span>
                    {% endif %}
                </div>
                
                <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 leading-tight mb-4">
                    {{ product.name }}
                </h1>
                
                <div class="flex flex-wrap items-center text-sm text-gray-500 gap-4">
                    <span class="text-green-600 font-semibold text-lg">Rp {{ product.price }}</span>
                    <span>Stock: {{ product.stock }}</span>
                </div>
            </div>

            <!-- Product Image -->
            {% if product.thumbnail %}
                <div class="px-6 sm:px-8 flex justify-center items-center">
                    <img src="{{ product.thumbnail }}" 
                        alt="{{ product.name }}" 
                        class="max-h-96 w-auto object-contain rounded-lg">
                </div>
            {% endif %}

            <!-- Product Description -->
            <div class="p-6 sm:p-8">
                <div class="prose prose-lg max-w-none">
                    <div class="text-gray-700 leading-relaxed whitespace-pre-line text-base sm:text-lg">
                        {{ product.description }}
                    </div>
                </div>
            </div>

            <!-- Extra Info -->
            <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-50">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="font-medium text-gray-900">
                            Brand: {{ product.brand }}
                        </p>
                        {% if product.user %}
                            <p class="text-sm text-gray-500">Added by {{ product.user.username }}</p>
                        {% else %}
                            <p class="text-sm text-gray-500">Added by Anonymous</p>
                        {% endif %}
                    </div>
                </div>
            </div>
        </article>
    </div>
</div>
{% endblock content %}

```

3. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
 Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
 Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).


Pertama-tama kita buat product_card.css, isi dari css ini hanya css dari kode saya untuk tugas 2 (yang dibuat oleh AI), pada awalnya css tersebut masih inline, sekarang agar lebih rapih saya pindahkan ke static files, berikut kodenya

```css
body {
  font-family: Arial, sans-serif;
}

.header {
  text-align: center;
  margin-bottom: 20px;
}

.add-button {
  display: inline-block;
  margin: 10px 0;
  padding: 10px 20px;
  background: #16a34a; 
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 16px;
  transition: background 0.2s;
}
.add-button:hover {
  background: #15803d;
}

/* Product grid */
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
  max-width: 1000px;
  margin: auto;
}

.product-card {
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
  text-align: center;
  background: white;
}

.product-card img {
  max-width: 100%;
  max-height: 200px;   /* limit height */
  width: auto;         /* scale proportionally */
  height: auto;
  object-fit: contain; /* make sure full image is visible */
  display: block;
  margin: 0 auto 12px; /* center horizontally + add bottom margin */
}

.product-card h2 {
  margin: 8px 0;
  font-size: 18px;
}

.price {
  font-weight: bold;
  color: #16a34a; 
  margin: 5px 0;
}

.featured {
  color: #fff;
  background: #15803d; 
  padding: 3px 6px;
  border-radius: 5px;
  font-size: 11px;
  margin-left: 6px;
}

.details-button {
  display: inline-block;
  margin-top: 12px;
  padding: 8px 16px;
  background: #16a34a; 
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 14px;
  transition: background 0.2s;
}
.details-button:hover {
  background: #15803d; 
}
```
Setelah itu saya buat product_card.html yaitu html untuk product card yang akan menggunakan css dari product_card.css, berikut kodenya
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/product_card.css' %}">

<article class="product-card">
  <!-- Thumbnail -->
  {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="{{ product.name }}">
  {% else %}
    <div class="w-full h-48 bg-gray-200 rounded-md"></div>
  {% endif %}

  <!-- Title -->
  <h2>
    {{ product.name }}
    {% if product.is_featured %}
      <span class="featured">Featured</span>
    {% endif %}
  </h2>

  <!-- Price / Stock -->
  <p class="price">Rp {{ product.price }}</p>
  <p><strong>Brand:</strong> {{ product.brand }}</p>
  <p><strong>Stock:</strong> {{ product.stock }}</p>

  <!-- Action Buttons -->
  <div class="mt-4 flex justify-center space-x-3">
    <a href="{% url 'main:show_product' product.id %}" class="details-button">View Details</a>
    {% if user.is_authenticated and product.user == user %}
      <a href="{% url 'main:edit_product' product.id %}" class="details-button">Edit</a>
      <a href="{% url 'main:delete_product' product.id %}" class="details-button" style="background:#dc2626;">Delete</a>
    {% endif %}
  </div>
</article>

```
Untuk tombol delete, saya kasih background merah agar berbeda dengan edit supaya meminimalisir kemungkinan salah pencet oleh user. Terakhir tinggal memodifikasi template.html agar menggunakan product_card.html

```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>FullTime Gear - Products</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="bg-gray-50 w-full pt-16 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

    <!-- Header Section -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Football Products</h1>
      <p class="text-gray-600">Browse and shop the best football gear</p>
    </div>

    <!-- Filter Section -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 bg-white rounded-lg border border-gray-200 p-4">
      <div class="flex space-x-3 mb-4 sm:mb-0">
        <a href="?" class="{% if request.GET.filter == 'all' or not request.GET.filter %} bg-green-600 text-white{% else %} bg-white text-gray-700 border border-gray-300{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-green-600 hover:text-white">
          All Products
        </a>
        <a href="?filter=my" class="{% if request.GET.filter == 'my' %} bg-green-600 text-white{% else %} bg-white text-gray-700 border border-gray-300{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-green-600 hover:text-white">
          My Products
        </a>
      </div>
      {% if user.is_authenticated %}
        <div class="text-sm text-gray-500">
          Last login: {{ last_login }}
        </div>
      {% endif %}
    </div>

    <!-- Product Grid -->
    {% if not products %}
      <div class="bg-white rounded-lg border border-gray-200 p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'images/no-product.png' %}" alt="No products available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No products found</h3>
        <p class="text-gray-500 mb-6">Be the first to add a product.</p>
        <a href="{% url 'main:add_product' %}" class="inline-flex items-center px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors">
          Add Product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in products %}
          {% include 'product_card.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
</div>
{% endblock content %}

```
untuk no-product.png saya membuat folder baru di dalam static bernama images dan menggunakan gambar berikut
![](/static/images/no-product.png)


4. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

Untuk kodenya sudah ada di kode product_card.html di nomor sebelumnya, berikut snippet kode untuk tombolnya :
```html
    {% if user.is_authenticated and product.user == user %}
      <a href="{% url 'main:edit_product' product.id %}" class="details-button">Edit</a>
      <a href="{% url 'main:delete_product' product.id %}" class="details-button" style="background:#dc2626;">Delete</a>
    {% endif %}
```

tombol ini hanya akan muncul jika user sudah terautentikasi (logged in) and merupakan orang yang menambahkan produk tersebut (if user.is_authenticated and product.user == user)

5. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

Untuk navbar saya masih menggunakan navbar yang dari tutorial, untuk mengimplementasikannya kita hanya perlu membuat `navbar.html` (di folder yang sama dengan `base.html`) lalu menambahkannya ke `template.html`

```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>FullTime Gear - Products</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
```

berikut kode untuk navbar.html

```html
<nav class="fixed top-0 left-0 w-full bg-white border-b border-gray-200 shadow-sm z-50">
  <div class="max-w-7xl mx-auto px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      
      <!-- Logo / Branding -->
      <div class="flex items-center">
        <h1 class="text-xl font-semibold text-gray-900">
          <span class="text-green-600">FullTime</span> Gear
        </h1>
      </div>
      
      <!-- Desktop Navigation -->
      <div class="hidden md:flex items-center space-x-8">
        <a href="{% url 'main:show_template' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
          Home
        </a>
        <a href="{% url 'main:add_product' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
          Add Product
        </a>
      </div>
      
      <!-- Desktop User Section -->
      <div class="hidden md:flex items-center space-x-6">
        {% if user.is_authenticated %}
          <div class="text-right">
            <div class="text-sm font-medium text-gray-900">{{ name|default:user.username }}</div>
            <div class="text-xs text-gray-500">{{ class|default:"PBP F" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="text-red-600 hover:text-red-700 font-medium transition-colors">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded font-medium transition-colors">
            Register
          </a>
        {% endif %}
      </div>
      
      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button p-2 text-gray-600 hover:text-gray-900 transition-colors">
          <span class="sr-only">Open menu</span>
          <div class="w-6 h-6 flex flex-col justify-center items-center">
            <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
            <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"></span>
            <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
          </div>
        </button>
      </div>
    </div>
  </div>
  
  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden bg-white border-t border-gray-200">
    <div class="px-6 py-4 space-y-4">
      
      <!-- Mobile Navigation Links -->
      <div class="space-y-1">
        <a href="{% url 'main:show_template' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
          Home
        </a>
        <a href="{% url 'main:add_product' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
          Add Product
        </a>
      </div>
      
      <!-- Mobile User Section -->
      <div class="border-t border-gray-200 pt-4">
        {% if user.is_authenticated %}
          <div class="mb-4">
            <div class="font-medium text-gray-900">{{ name|default:user.username }}</div>
            <div class="text-sm text-gray-500">{{ class|default:"PBP F" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="block text-red-600 hover:text-red-700 font-medium py-3 transition-colors">
            Logout
          </a>
        {% else %}
          <div class="space-y-3">
            <a href="{% url 'main:login' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="block bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded text-center transition-colors">
              Register
            </a>
          </div>
        {% endif %}
      </div>
    </div>
  </div>
  
  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>

```

Disclaimer: Kode html dan css dibuat dengan bantuan dari AI.
</details>



