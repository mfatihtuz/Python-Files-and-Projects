## @package python-tutorials-for-fatihtuz.com
## @author: M.Fatih T�z
#
## Mail: iletisim@fatihtuz.com, m.fatihtuz@gmail.com
#
# Bu program 2. dereceden bir bilinmeyenli denklemin k�klerini bulmaya yarayan basit bir konsol uygulamas�d�r.
# Denklem: Denklem : ax^2 + bx + c
# Delta Hesaplama :  b ** 2 -  4 * a * c
# Birinci k�k : (-b - delta ** 0.5) / (2*a)
# �kinci k�k  : (-b + delta ** 0.5) / (2*a)


a = int(input("Denklemin a de�eri:"))
b = int(input("Denklemin b de�eri:"))
c = int(input("Denklemin c de�eri:"))


delta = b ** 2 - 4  * a * c

x1 = (-b - delta ** 0.5)/ (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("Birinci K�k: {}\n�kinci K�k : {}".format(x1,x2))


