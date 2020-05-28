from requests import get

check_my_ip_list = []

f_ip = open("ips.txt", "r", encoding="UTF-8")
for i in f_ip:
    check_my_ip_list.append(i.strip())
if len(check_my_ip_list) > 10:
    print("Çok fazla sayıda IP girişi oldu, lütfen satıcıyla iletişime geçin")
else:
    print(check_my_ip_list)
    ip_flag = 0
    my_ip = get('https://ipapi.co/ip/').text
    for i in check_my_ip_list:
        if my_ip == i:
            ip_flag = 1
            break
        else:
            ip_flag = 0

    if ip_flag == 1:
        print(my_ip + " IP Adresi Bulunmakta. İşleme Sorunsuz Şekilde Devam Edilebilir")
    else:
        # Yeni IP Adresi Dosyaya Eklendi
        print(my_ip + " Yeni IP Adresi Ekleniyor")
        f = open("ips.txt", "a+")
        f.write("\n" + my_ip)
        f.close()

cks = input("Kapatmak için y/Y tuşuna basın : ")
if (cks == 'y' or cks == 'Y'):
    break
else:
    print("\n\nProgram Tekrardan Başlatılıyor\n\n")