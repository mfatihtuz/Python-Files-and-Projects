from urllib.request import urlopen
import urllib.request

while(True):
    
    # URL'deki okunacak .txt dosyasına erişme
    # Accessing the .txt file to be read in the URL
    url = "https://www.yourwebsite.com/your_text_file.txt"
    file = urllib.request.urlopen(url)

    kullanicilar = [] #users
    user_kontrol = "your-user-kontrol-text"
    
    # url'deki .txt dosyasını oku ve listeye ata
    # read txt file in url and assing to the list
    for line in file:
        kullanicilar.append(str(line.strip(), 'utf-8'))
        print(kullanicilar)
    
    # If the user is finded, then set '1' the flag
    users_flag = 0 
    for i in kullanicilar:
        if i == user_kontrol:
            users_flag = 1
            break
        else:
            users_flag = 0

    if (users_flag == 1):
        print("Tebrikler! Listedesiniz :) ")
    else:
        print("Üzgünüm! Listede değilsiniz :( ")


