# Program that gives warning when entering a program from X different number of IPs.
# Bir programa X adet farklı sayıda IP'den giriş yapıldığında, uyarı veren program.

from requests import get

#Check your Public IP
ip_flag = 0
my_ip = get('https://ipapi.co/ip/').text

check_my_ip_list = []

# Checking the previous saved IP addresses
# Önceki kaydedilen IP adreslerinin kontrol edilmesi
f_ip = open("ips.txt", "r", encoding="UTF-8")
for i in f_ip:
    check_my_ip_list.append(i.strip())   
if len(check_my_ip_list) > 10:
    # X (burada 10) adet farklı IP adresinden giriş yapıldığı için, program uyarı veriyor.
    # Since the program is logged in from X (in this case 10) different IP addresses, the program gives a warning.
    print("Çok fazla sayıda IP girişi oldu, lütfen programcıyla iletişime geçin")
else:
    print(check_my_ip_list)
    for i in check_my_ip_list:
        if my_ip == i:
            ip_flag = 1
            break
        else:
            ip_flag = 0

    if ip_flag == 1:
        # IP Adresi Bulunmakta. İşleme Sorunsuz Şekilde Devam Edilebilir
        # IP Address has found in the list. Process can continue seamlessly
        print(my_ip + " IP Adresi Bulunmakta. İşleme Sorunsuz Şekilde Devam Edilebilir")
    else:
        # Yeni IP Adresi Dosyaya Eklendi
        # New IP adress is added to the list
        print(my_ip + " Yeni IP Adresi Ekleniyor")
        f = open("ips.txt", "a+")
        f.write("\n" + my_ip)
        f.close()
