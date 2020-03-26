## @package python-tutorials-for-fatihtuz.com
## @author: M.Fatih Tüz
#
## Mail: iletisim@fatihtuz.com, m.fatihtuz@gmail.com
#
# Bu program 2. dereceden bir bilinmeyenli denklemin köklerini bulmaya yarayan basit bir konsol uygulamasýdýr.
# Denklem: Denklem : ax^2 + bx + c
# Delta Hesaplama :  b ** 2 -  4 * a * c
# Birinci kök : (-b - delta ** 0.5) / (2*a)
# Ýkinci kök  : (-b + delta ** 0.5) / (2*a)


a = int(input("Denklemin a deðeri:"))
b = int(input("Denklemin b deðeri:"))
c = int(input("Denklemin c deðeri:"))


delta = b ** 2 - 4  * a * c

x1 = (-b - delta ** 0.5)/ (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci Kök: {}\nÝkinci Kök : {}".format(x1,x2))


