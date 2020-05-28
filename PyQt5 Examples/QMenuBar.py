"""
Fatih Tüz - PyQt5 Dersleri

Konu : PyQt5'te obje ile pencere kapatma

Author: Fatih Tüz
Website: fatihtuz.com
Düzenlenme Tarihi: Mayıs 2020
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Ornek(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        #Pencere Özellikleri ayarlandı
        self.setGeometry(200,300,500,200)
        self.setWindowTitle("Basit Bir Menü")

        #QMenuBar sınıfından Menü Çubuğu Objesi Tanımlaması, ve Çubuğa Menü eklenmesi
        menu_cubugu = self.menuBar()
        dosya_menusu = menu_cubugu.addMenu("&Dosya")
        
        #Menü ile alakalı bilgileri durum çubuğunda göstermek için, durum çubuğu oluşturmak
        self.statusBar()
        
        #Menü'nün yapacağı işlevin belirlenmesi
        cikis_eylemi = QAction(QIcon('cikis.png'), '&Çıkış', self)
        cikis_eylemi.setShortcut('Ctrl+Ç')
        cikis_eylemi.setStatusTip("Bu menü programdan çıkış yapmanızı sağlar")
        cikis_eylemi.triggered.connect(qApp.quit)

        #Oluşturulan menüye belirlenen eylemin atanması
        dosya_menusu.addAction(cikis_eylemi)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Ornek()
    sys.exit(app.exec_())
