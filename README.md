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
</details>







