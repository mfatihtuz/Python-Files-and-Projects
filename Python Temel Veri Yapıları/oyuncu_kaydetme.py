## @package python-tutorials-for-fatihtuz.com
## @author: M.Fatih Tüz
#
## Mail: iletisim@fatihtuz.com, m.fatihtuz@gmail.com
#
# Bu program Oyuncu Kaydetmeye yarayan basit bir konsol uygulamasıdır.


print("Oyuncu Kaydetme Programı")

bilgiler = [] # Oyuncu bilgilerini saklayacağımız listemizi boş oluşturuyoruz.

ad =  input("Oyuncunun Adı:") # Kullanıcıdan Oyuncunun Ad Bilgisini alıyoruz.
soyad = input("Oyuncunun Soyadı:") # Kullanıcıdan Oyuncunun Soyad Bilgisini alıyoruz.
takım = input("Oyuncunun Takımı:") # Kullanıcıdan Oyuncunun Takım Bilgisini alıyoruz.

bilgiler = [ad,soyad,takım] # Aldığımız bilgileri listeye atıyoruz.


print("Bilgiler Kaydediliyor....\n")
print("Oyuncu Adı: {}\nOyuncu Soyadı: {}\nTakım: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("Bilgiler Kaydedildi...")
