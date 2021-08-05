## Django Web Vaka Projesi
* * *

Django web vaka projesi.

 **Başlarken**
* * *

Projeyi indirmek için aşağıdaki komutu çalıştırın.

`
git clone https://github.com/MuratCanOrak/web-uygulama.git
`



Proje dizinine geçmek için aşağıdaki komutu çalıştırın.

`
cd web-uygulama
`

Gerekli paketleri kurmak için aşağıdaki komutu çalıştırın.
`
pip3 install -r requirements.txt
`

Veri tabanı ile ilgili bilgileri .env.sample dosyası içerisine eklemeniz gerekmektedir.

- Veri Tabanı adı DB_NAME değişkenine eklenmelidir.
- Veri Tabanı kullanıcısı DB_USER değişkenine eklenmelidir
- Veri Tabanı parolası DB_PASS değişkenine eklenmelidir.

Veri Tabanını oluşturmak için aşağıdaki kodu çalışrırın.

`
python3 manage.py migrate
`


Projenin iki dil olarak çalışmasını sağlamak için aşağıdaki komutu çalıştırın.

`
django-admin compilemessages
`

Projeyi ayağa kaldırmak için aşağıdaki komutu çalıştırın.

`
python3 manage.py runserver
`


Projeye ayağa aşağıdaki linkten erişebilirsiniz.

[proje linki](http://localhost:8000)
