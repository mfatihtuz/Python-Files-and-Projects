from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
from PandasModel import PandasModel
import datetime
import os
import re
import numpy as np
import time
import random


gecerliTarih_gun = datetime.date.today().day
gecerliTarih_ay = datetime.date.today().month
gecerliTarih_yil = datetime.date.today().year


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        self.splash = QSplashScreen(QPixmap('icons/WELCOME.png'))
        self.splash.show()
        QTimer.singleShot(2500, self.splash.close)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 758)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/supplier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.menu_layout = QtWidgets.QHBoxLayout()
        self.menu_layout.setContentsMargins(0, -1, -1, -1)
        self.menu_layout.setSpacing(6)
        self.menu_layout.setObjectName("menu_layout")
        self.button_anasayfa = QtWidgets.QToolButton(self.centralwidget)
        self.button_anasayfa.setStyleSheet("background:transparent;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home-page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_anasayfa.setIcon(icon1)
        self.button_anasayfa.setIconSize(QtCore.QSize(48, 48))
        self.button_anasayfa.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_anasayfa.setObjectName("button_anasayfa")
        self.menu_layout.addWidget(self.button_anasayfa)
        self.button_mustahsil = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_mustahsil.setFont(font)
        self.button_mustahsil.setStyleSheet("background:transparent;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/vegetable (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mustahsil.setIcon(icon2)
        self.button_mustahsil.setIconSize(QtCore.QSize(48, 48))
        self.button_mustahsil.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_mustahsil.setObjectName("button_mustahsil")
        self.menu_layout.addWidget(self.button_mustahsil)
        self.button_musteri = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_musteri.setFont(font)
        self.button_musteri.setStyleSheet("background:transparent;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/sell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_musteri.setIcon(icon3)
        self.button_musteri.setIconSize(QtCore.QSize(48, 48))
        self.button_musteri.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_musteri.setObjectName("button_musteri")
        self.menu_layout.addWidget(self.button_musteri)
        self.button_kisi_ekle = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_kisi_ekle.setFont(font)
        self.button_kisi_ekle.setStyleSheet("background:transparent;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_kisi_ekle.setIcon(icon4)
        self.button_kisi_ekle.setIconSize(QtCore.QSize(48, 48))
        self.button_kisi_ekle.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_kisi_ekle.setObjectName("button_kisi_ekle")
        self.menu_layout.addWidget(self.button_kisi_ekle)
        self.button_urun_goruntule = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_urun_goruntule.setFont(font)
        self.button_urun_goruntule.setStyleSheet("background:transparent;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/order.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_urun_goruntule.setIcon(icon5)
        self.button_urun_goruntule.setIconSize(QtCore.QSize(48, 48))
        self.button_urun_goruntule.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_urun_goruntule.setObjectName("button_urun_goruntule")
        self.menu_layout.addWidget(self.button_urun_goruntule)
        self.button_kisi_goruntule = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_kisi_goruntule.setFont(font)
        self.button_kisi_goruntule.setStyleSheet("background:transparent;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/customer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_kisi_goruntule.setIcon(icon6)
        self.button_kisi_goruntule.setIconSize(QtCore.QSize(48, 48))
        self.button_kisi_goruntule.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_kisi_goruntule.setObjectName("button_kisi_goruntule")
        self.menu_layout.addWidget(self.button_kisi_goruntule)
        self.button_alacak_borc_bilgisi = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_alacak_borc_bilgisi.setFont(font)
        self.button_alacak_borc_bilgisi.setStyleSheet("background:transparent;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/money (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_alacak_borc_bilgisi.setIcon(icon7)
        self.button_alacak_borc_bilgisi.setIconSize(QtCore.QSize(48, 48))
        self.button_alacak_borc_bilgisi.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_alacak_borc_bilgisi.setObjectName("button_alacak_borc_bilgisi")
        self.menu_layout.addWidget(self.button_alacak_borc_bilgisi)
        self.button_kasa_hesabi = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_kasa_hesabi.setFont(font)
        self.button_kasa_hesabi.setStyleSheet("background:transparent;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/bank-statement.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_kasa_hesabi.setIcon(icon8)
        self.button_kasa_hesabi.setIconSize(QtCore.QSize(48, 48))
        self.button_kasa_hesabi.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_kasa_hesabi.setObjectName("button_kasa_hesabi")
        self.menu_layout.addWidget(self.button_kasa_hesabi)
        self.button_sera = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_sera.setFont(font)
        self.button_sera.setStyleSheet("background:transparent;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/greenhouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sera.setIcon(icon9)
        self.button_sera.setIconSize(QtCore.QSize(48, 48))
        self.button_sera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_sera.setObjectName("button_sera")
        self.menu_layout.addWidget(self.button_sera)
        self.gridLayout_11.addLayout(self.menu_layout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_anasayfa = QtWidgets.QWidget()
        self.page_anasayfa.setObjectName("page_anasayfa")
        self.gridLayout = QtWidgets.QGridLayout(self.page_anasayfa)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_anasayfa)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_anasayfa)
        self.page_mustahsilden_urun_al = QtWidgets.QWidget()
        self.page_mustahsilden_urun_al.setObjectName("page_mustahsilden_urun_al")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_mustahsilden_urun_al)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_mustahsildenUrunAl = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.label_mustahsildenUrunAl.setFont(font)
        self.label_mustahsildenUrunAl.setStyleSheet("background: #0B7EB4;")
        self.label_mustahsildenUrunAl.setWordWrap(True)
        self.label_mustahsildenUrunAl.setObjectName("label_mustahsildenUrunAl")
        self.gridLayout_4.addWidget(self.label_mustahsildenUrunAl, 0, 0, 1, 1)
        self.gridLayout_mustahsildenUrunAl = QtWidgets.QGridLayout()
        self.gridLayout_mustahsildenUrunAl.setObjectName("gridLayout_mustahsildenUrunAl")
        self.label_mustahsildenUrunAl_islemKimligi = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_islemKimligi.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_islemKimligi.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_mustahsildenUrunAl_islemKimligi.setFont(font)
        self.label_mustahsildenUrunAl_islemKimligi.setWordWrap(True)
        self.label_mustahsildenUrunAl_islemKimligi.setObjectName("label_mustahsildenUrunAl_islemKimligi")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_islemKimligi, 4, 0, 1, 1)
        self.label_mustahsildenUrunAl_kayitliMustahsil = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_kayitliMustahsil.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_kayitliMustahsil.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsildenUrunAl_kayitliMustahsil.setFont(font)
        self.label_mustahsildenUrunAl_kayitliMustahsil.setWordWrap(True)
        self.label_mustahsildenUrunAl_kayitliMustahsil.setObjectName("label_mustahsildenUrunAl_kayitliMustahsil")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_kayitliMustahsil, 5, 0, 1, 1)
        self.label_mustahsildenUrunAl_adet = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_adet.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_adet.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsildenUrunAl_adet.setFont(font)
        self.label_mustahsildenUrunAl_adet.setWordWrap(True)
        self.label_mustahsildenUrunAl_adet.setObjectName("label_mustahsildenUrunAl_adet")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_adet, 3, 0, 1, 1)
        self.label_mustahsildenUrunAl_maliyet = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_maliyet.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_maliyet.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsildenUrunAl_maliyet.setFont(font)
        self.label_mustahsildenUrunAl_maliyet.setWordWrap(True)
        self.label_mustahsildenUrunAl_maliyet.setObjectName("label_mustahsildenUrunAl_maliyet")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_maliyet, 2, 0, 1, 1)
        self.horizontalLayout_urunAdi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_urunAdi.setObjectName("horizontalLayout_urunAdi")
        self.comboBox_mustahsildenUrunAl_urunAdi = QtWidgets.QComboBox(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsildenUrunAl_urunAdi.setFont(font)
        self.comboBox_mustahsildenUrunAl_urunAdi.setObjectName("comboBox_mustahsildenUrunAl_urunAdi")
        self.comboBox_mustahsildenUrunAl_urunAdi.addItem("Ürün Seçiniz")
        self.horizontalLayout_urunAdi.addWidget(self.comboBox_mustahsildenUrunAl_urunAdi)
        self.button_mustahsildenUrunAl_urunEkleme = QtWidgets.QPushButton(self.page_mustahsilden_urun_al)
        self.button_mustahsildenUrunAl_urunEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_mustahsildenUrunAl_urunEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_mustahsildenUrunAl_urunEkleme.setStyleSheet("background: transparent;")
        self.button_mustahsildenUrunAl_urunEkleme.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mustahsildenUrunAl_urunEkleme.setIcon(icon10)
        self.button_mustahsildenUrunAl_urunEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_mustahsildenUrunAl_urunEkleme.setObjectName("button_mustahsildenUrunAl_urunEkleme")
        self.horizontalLayout_urunAdi.addWidget(self.button_mustahsildenUrunAl_urunEkleme)
        self.gridLayout_mustahsildenUrunAl.addLayout(self.horizontalLayout_urunAdi, 1, 1, 1, 1)
        self.horizontalLayout_mustahsildenUrunAl_tarih = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsildenUrunAl_tarih.setObjectName("horizontalLayout_mustahsildenUrunAl_tarih")
        self.comboBox_mustahsildenUrunAl_gun = QtWidgets.QComboBox(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsildenUrunAl_gun.setFont(font)
        self.comboBox_mustahsildenUrunAl_gun.setObjectName("comboBox_mustahsildenUrunAl_gun")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.setItemText(0, "")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.comboBox_mustahsildenUrunAl_gun.addItem("")
        self.horizontalLayout_mustahsildenUrunAl_tarih.addWidget(self.comboBox_mustahsildenUrunAl_gun)
        self.comboBox_mustahsildenUrunAl_ay = QtWidgets.QComboBox(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsildenUrunAl_ay.setFont(font)
        self.comboBox_mustahsildenUrunAl_ay.setObjectName("comboBox_mustahsildenUrunAl_ay")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.setItemText(0, "")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.comboBox_mustahsildenUrunAl_ay.addItem("")
        self.horizontalLayout_mustahsildenUrunAl_tarih.addWidget(self.comboBox_mustahsildenUrunAl_ay)
        self.comboBox_mustahsildenUrunAl_yil = QtWidgets.QComboBox(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsildenUrunAl_yil.setFont(font)
        self.comboBox_mustahsildenUrunAl_yil.setObjectName("comboBox_mustahsildenUrunAl_yil")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.setItemText(0, "")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.comboBox_mustahsildenUrunAl_yil.addItem("")
        self.horizontalLayout_mustahsildenUrunAl_tarih.addWidget(self.comboBox_mustahsildenUrunAl_yil)
        self.gridLayout_mustahsildenUrunAl.addLayout(self.horizontalLayout_mustahsildenUrunAl_tarih, 0, 1, 1, 1)
        self.label_mustahsildenUrunAl_urunAdi = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_urunAdi.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_urunAdi.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsildenUrunAl_urunAdi.setFont(font)
        self.label_mustahsildenUrunAl_urunAdi.setWordWrap(True)
        self.label_mustahsildenUrunAl_urunAdi.setObjectName("label_mustahsildenUrunAl_urunAdi")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_urunAdi, 1, 0, 1, 1)
        self.label_mustahsildenUrunAl_tarih = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_tarih.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_tarih.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_mustahsildenUrunAl_tarih.setFont(font)
        self.label_mustahsildenUrunAl_tarih.setWordWrap(True)
        self.label_mustahsildenUrunAl_tarih.setObjectName("label_mustahsildenUrunAl_tarih")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_tarih, 0, 0, 1, 1)
        self.label_mustahsildenUrunAl_islemKimligi_detay = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_mustahsildenUrunAl_islemKimligi_detay.setFont(font)
        self.label_mustahsildenUrunAl_islemKimligi_detay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mustahsildenUrunAl_islemKimligi_detay.setWordWrap(True)
        self.label_mustahsildenUrunAl_islemKimligi_detay.setObjectName("label_mustahsildenUrunAl_islemKimligi_detay")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_islemKimligi_detay, 4, 1, 1, 1)
        self.horizontalLayout_mustahsildenUrunAl_maliyet = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsildenUrunAl_maliyet.setObjectName("horizontalLayout_mustahsildenUrunAl_maliyet")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.page_mustahsilden_urun_al)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMaximum(1000000000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_mustahsildenUrunAl_maliyet.addWidget(self.doubleSpinBox)
        self.label_mustahsildenUrunAl_maliyet_TL = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_maliyet_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_mustahsildenUrunAl_maliyet_TL.setMaximumSize(QtCore.QSize(32, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_mustahsildenUrunAl_maliyet_TL.setFont(font)
        self.label_mustahsildenUrunAl_maliyet_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mustahsildenUrunAl_maliyet_TL.setWordWrap(True)
        self.label_mustahsildenUrunAl_maliyet_TL.setObjectName("label_mustahsildenUrunAl_maliyet_TL")
        self.horizontalLayout_mustahsildenUrunAl_maliyet.addWidget(self.label_mustahsildenUrunAl_maliyet_TL)
        self.gridLayout_mustahsildenUrunAl.addLayout(self.horizontalLayout_mustahsildenUrunAl_maliyet, 2, 1, 1, 1)
        self.spinBox_mustahsildenUrunAl_adet = QtWidgets.QSpinBox(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_mustahsildenUrunAl_adet.setFont(font)
        self.spinBox_mustahsildenUrunAl_adet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_mustahsildenUrunAl_adet.setMaximum(1000000000)
        self.spinBox_mustahsildenUrunAl_adet.setObjectName("spinBox_mustahsildenUrunAl_adet")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.spinBox_mustahsildenUrunAl_adet, 3, 1, 1, 1)
        self.horizontalLayout_mustahsildenUrunAl_kayitliMustahsil = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsildenUrunAl_kayitliMustahsil.setObjectName("horizontalLayout_mustahsildenUrunAl_kayitliMustahsil")
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil = QtWidgets.QComboBox(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.setFont(font)
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.setObjectName("comboBox_mustahsildenUrunAl_kayitliMustahsil")
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem("Müstahsil Seçiniz")

        self.horizontalLayout_mustahsildenUrunAl_kayitliMustahsil.addWidget(self.comboBox_mustahsildenUrunAl_kayitliMustahsil)
        self.button_mustahsildenUrunAl_mustahsilEkleme = QtWidgets.QPushButton(self.page_mustahsilden_urun_al)
        self.button_mustahsildenUrunAl_mustahsilEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_mustahsildenUrunAl_mustahsilEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_mustahsildenUrunAl_mustahsilEkleme.setStyleSheet("background: transparent;")
        self.button_mustahsildenUrunAl_mustahsilEkleme.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/add-user (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mustahsildenUrunAl_mustahsilEkleme.setIcon(icon11)
        self.button_mustahsildenUrunAl_mustahsilEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_mustahsildenUrunAl_mustahsilEkleme.setObjectName("button_mustahsildenUrunAl_mustahsilEkleme")
        self.horizontalLayout_mustahsildenUrunAl_kayitliMustahsil.addWidget(self.button_mustahsildenUrunAl_mustahsilEkleme)
        self.gridLayout_mustahsildenUrunAl.addLayout(self.horizontalLayout_mustahsildenUrunAl_kayitliMustahsil, 5, 1, 1, 1)
        self.label_mustahsildenUrunAl_tutar = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_tutar.setMinimumSize(QtCore.QSize(250, 0))
        self.label_mustahsildenUrunAl_tutar.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsildenUrunAl_tutar.setFont(font)
        self.label_mustahsildenUrunAl_tutar.setObjectName("label_mustahsildenUrunAl_tutar")
        self.gridLayout_mustahsildenUrunAl.addWidget(self.label_mustahsildenUrunAl_tutar, 6, 0, 1, 1)
        self.horizontalLayout_mustahsildenUrunAl_tutar = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsildenUrunAl_tutar.setObjectName("horizontalLayout_mustahsildenUrunAl_tutar")
        self.label_mustahsildenUrunAl_tutar_sonuc = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsildenUrunAl_tutar_sonuc.setFont(font)
        self.label_mustahsildenUrunAl_tutar_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mustahsildenUrunAl_tutar_sonuc.setObjectName("label_mustahsildenUrunAl_tutar_sonuc")
        self.horizontalLayout_mustahsildenUrunAl_tutar.addWidget(self.label_mustahsildenUrunAl_tutar_sonuc)
        self.label_mustahsildenUrunAl_tutar_sonuc_TL = QtWidgets.QLabel(self.page_mustahsilden_urun_al)
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setMaximumSize(QtCore.QSize(32, 39))
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setFont(font)
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setWordWrap(True)
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setObjectName("label_mustahsildenUrunAl_tutar_sonuc_TL")
        self.horizontalLayout_mustahsildenUrunAl_tutar.addWidget(self.label_mustahsildenUrunAl_tutar_sonuc_TL)
        self.gridLayout_mustahsildenUrunAl.addLayout(self.horizontalLayout_mustahsildenUrunAl_tutar, 6, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_mustahsildenUrunAl, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 0, 1, 1)
        self.verticalLayout_mustahsildenUrunAl_butonlar = QtWidgets.QVBoxLayout()
        self.verticalLayout_mustahsildenUrunAl_butonlar.setObjectName("verticalLayout_mustahsildenUrunAl_butonlar")
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit = QtWidgets.QPushButton(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.setFont(font)
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.setStyleSheet("color: red;background: #FCCBC5;")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/basket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.setIcon(icon12)
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.setObjectName("pushButton_mustahsildenUrunAl_odemeSayfasinaGit")
        self.verticalLayout_mustahsildenUrunAl_butonlar.addWidget(self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit)
        self.pushButton_mustahsildenUrunAl_Onayla = QtWidgets.QPushButton(self.page_mustahsilden_urun_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mustahsildenUrunAl_Onayla.setFont(font)
        self.pushButton_mustahsildenUrunAl_Onayla.setStyleSheet("color: green; background: #D7FAC6;")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/tick (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_mustahsildenUrunAl_Onayla.setIcon(icon13)
        self.pushButton_mustahsildenUrunAl_Onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mustahsildenUrunAl_Onayla.setObjectName("pushButton_mustahsildenUrunAl_Onayla")
        self.verticalLayout_mustahsildenUrunAl_butonlar.addWidget(self.pushButton_mustahsildenUrunAl_Onayla)
        self.gridLayout_4.addLayout(self.verticalLayout_mustahsildenUrunAl_butonlar, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_mustahsilden_urun_al)
        self.page_mustahsile_odeme_yap = QtWidgets.QWidget()
        self.page_mustahsile_odeme_yap.setObjectName("page_mustahsile_odeme_yap")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page_mustahsile_odeme_yap)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_mustahsilOdemeDetaylari = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari.setStyleSheet("background: #0B7EB4;")
        self.label_mustahsilOdemeDetaylari.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari.setObjectName("label_mustahsilOdemeDetaylari")
        self.gridLayout_13.addWidget(self.label_mustahsilOdemeDetaylari, 0, 0, 1, 1)
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler = QtWidgets.QGridLayout()
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.setObjectName("gridLayout_mustahsilOdemeDetaylari_bilgiler")
        self.horizontalLayout_mustahsilOdemeDetaylari_kayitliMustahsil = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilOdemeDetaylari_kayitliMustahsil.setObjectName("horizontalLayout_mustahsilOdemeDetaylari_kayitliMustahsil")
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil = QtWidgets.QComboBox(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.setFont(font)
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.setObjectName("comboBox_mustahsilOdemeDetaylari_kayitliMustahsil")
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.addItem("Müstahsil Seçiniz")
        self.horizontalLayout_mustahsilOdemeDetaylari_kayitliMustahsil.addWidget(self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil)
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme = QtWidgets.QPushButton(self.page_mustahsile_odeme_yap)
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setStyleSheet("background: transparent;")
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setText("")
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setIcon(icon11)
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setObjectName("button_mustahsilOdemeDetaylari_mustahsilEkleme")
        self.horizontalLayout_mustahsilOdemeDetaylari_kayitliMustahsil.addWidget(self.button_mustahsilOdemeDetaylari_mustahsilEkleme)
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addLayout(self.horizontalLayout_mustahsilOdemeDetaylari_kayitliMustahsil, 0, 1, 1, 1)
        self.label_mustahsilOdemeDetaylari_kayitliMustahsil = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_kayitliMustahsil.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsilOdemeDetaylari_kayitliMustahsil.setFont(font)
        self.label_mustahsilOdemeDetaylari_kayitliMustahsil.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_kayitliMustahsil.setObjectName("label_mustahsilOdemeDetaylari_kayitliMustahsil")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_kayitliMustahsil, 0, 0, 1, 1)
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeSekli = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeSekli.setObjectName("horizontalLayout_mustahsilOdemeDetaylari_odemeSekli")
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli = QtWidgets.QComboBox(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.setFont(font)
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.setObjectName("comboBox_mustahsilOdemeDetaylari_odemeSekli")
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.addItem("")
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeSekli.addWidget(self.comboBox_mustahsilOdemeDetaylari_odemeSekli)
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme = QtWidgets.QPushButton(self.page_mustahsile_odeme_yap)
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setStyleSheet("background: transparent;")
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setIcon(icon14)
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setObjectName("button_mustahsilOdemeDetaylari_odemeSekliEkleme")
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeSekli.addWidget(self.button_mustahsilOdemeDetaylari_odemeSekliEkleme)
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addLayout(self.horizontalLayout_mustahsilOdemeDetaylari_odemeSekli, 2, 1, 1, 1)
        self.label_mustahsilOdemeDetaylari_odemeSekli = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_odemeSekli.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsilOdemeDetaylari_odemeSekli.setFont(font)
        self.label_mustahsilOdemeDetaylari_odemeSekli.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_odemeSekli.setObjectName("label_mustahsilOdemeDetaylari_odemeSekli")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_odemeSekli, 2, 0, 1, 1)
        self.label_mustahsilOdemeDetaylari_araciKurum = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_araciKurum.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsilOdemeDetaylari_araciKurum.setFont(font)
        self.label_mustahsilOdemeDetaylari_araciKurum.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_araciKurum.setObjectName("label_mustahsilOdemeDetaylari_araciKurum")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_araciKurum, 3, 0, 1, 1)
        self.horizontalLayout_mustahsilOdemeDetaylari_araciKurum = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilOdemeDetaylari_araciKurum.setObjectName("horizontalLayout_mustahsilOdemeDetaylari_araciKurum")
        self.comboBox_mustahsilOdemeKurumu = QtWidgets.QComboBox(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilOdemeKurumu.setFont(font)
        self.comboBox_mustahsilOdemeKurumu.setObjectName("comboBox_mustahsilOdemeKurumu")

        ################################################################################################################
        ## MÜSTAHSİL ÖDEME SAYFASININ ARACI KURUM COMBOBOX'I DATASTORE'DAN EKLENDİ
        self.comboBox_mustahsilOdemeKurumu.addItem("Aracı Kurum Seçiniz")
        listFor_comboBox_mustahsilOdemeKurumu = []
        self.file_comboBox_mustahsilOdemeKurumu = open("datastore/araciKurumlar.dat", "r", encoding="UTF-8")
        for i in self.file_comboBox_mustahsilOdemeKurumu:
            listFor_comboBox_mustahsilOdemeKurumu.append(i.strip())
        for i in range(len(listFor_comboBox_mustahsilOdemeKurumu)):
            self.comboBox_mustahsilOdemeKurumu.addItem(listFor_comboBox_mustahsilOdemeKurumu[i])
        ################################################################################################################

        self.horizontalLayout_mustahsilOdemeDetaylari_araciKurum.addWidget(self.comboBox_mustahsilOdemeKurumu)
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme = QtWidgets.QPushButton(self.page_mustahsile_odeme_yap)
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setStyleSheet("background: transparent;")
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/real-estate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setIcon(icon15)
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setObjectName("button_mustahsilOdemeDetaylari_araciKurumEkleme")
        self.horizontalLayout_mustahsilOdemeDetaylari_araciKurum.addWidget(self.button_mustahsilOdemeDetaylari_araciKurumEkleme)
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addLayout(self.horizontalLayout_mustahsilOdemeDetaylari_araciKurum, 3, 1, 1, 1)
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeTutari = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeTutari.setObjectName("horizontalLayout_mustahsilOdemeDetaylari_odemeTutari")
        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari = QtWidgets.QDoubleSpinBox(self.page_mustahsile_odeme_yap)
        #self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.setFont(font)
        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.setDecimals(2)
        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.setMaximum(1000000000)
        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.setObjectName("doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari")
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeTutari.addWidget(self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari)
        self.label_mustahsilOdemeDetaylari_TL = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_TL.setMaximumSize(QtCore.QSize(32, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_mustahsilOdemeDetaylari_TL.setFont(font)
        self.label_mustahsilOdemeDetaylari_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mustahsilOdemeDetaylari_TL.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_TL.setObjectName("label_mustahsilOdemeDetaylari_TL")
        self.horizontalLayout_mustahsilOdemeDetaylari_odemeTutari.addWidget(self.label_mustahsilOdemeDetaylari_TL)
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addLayout(self.horizontalLayout_mustahsilOdemeDetaylari_odemeTutari, 4, 1, 1, 1)
        self.label_mustahsilOdemeDetaylari_odemeTutari = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_odemeTutari.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsilOdemeDetaylari_odemeTutari.setFont(font)
        self.label_mustahsilOdemeDetaylari_odemeTutari.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_odemeTutari.setObjectName("label_mustahsilOdemeDetaylari_odemeTutari")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_odemeTutari, 4, 0, 1, 1)
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.setFont(font)
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.setObjectName("label_mustahsilOdemeDetaylari_islemKimligi_detay")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_islemKimligi_detay, 5, 1, 1, 1)
        self.label_mustahsilOdemeDetaylari_islemKimligi = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_islemKimligi.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_mustahsilOdemeDetaylari_islemKimligi.setFont(font)
        self.label_mustahsilOdemeDetaylari_islemKimligi.setWordWrap(True)
        self.label_mustahsilOdemeDetaylari_islemKimligi.setObjectName("label_mustahsilOdemeDetaylari_islemKimligi")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_islemKimligi, 5, 0, 1, 1)
        self.label_mustahsilOdemeDetaylari_tarih = QtWidgets.QLabel(self.page_mustahsile_odeme_yap)
        self.label_mustahsilOdemeDetaylari_tarih.setObjectName("label_mustahsilOdemeDetaylari_tarih")
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addWidget(self.label_mustahsilOdemeDetaylari_tarih, 1, 0, 1, 1)
        self.horizontalLayout_mustahsilOdemeDetaylari_tarih = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilOdemeDetaylari_tarih.setObjectName("horizontalLayout_mustahsilOdemeDetaylari_tarih")
        self.comboBox_mustahsilOdemeDetaylari_gun = QtWidgets.QComboBox(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilOdemeDetaylari_gun.setFont(font)
        self.comboBox_mustahsilOdemeDetaylari_gun.setObjectName("comboBox_mustahsilOdemeDetaylari_gun")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(0, "")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_gun.addItem("")
        self.horizontalLayout_mustahsilOdemeDetaylari_tarih.addWidget(self.comboBox_mustahsilOdemeDetaylari_gun)
        self.comboBox_mustahsilOdemeDetaylari_ay = QtWidgets.QComboBox(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilOdemeDetaylari_ay.setFont(font)
        self.comboBox_mustahsilOdemeDetaylari_ay.setObjectName("comboBox_mustahsilOdemeDetaylari_ay")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(0, "")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_ay.addItem("")
        self.horizontalLayout_mustahsilOdemeDetaylari_tarih.addWidget(self.comboBox_mustahsilOdemeDetaylari_ay)
        self.comboBox_mustahsilOdemeDetaylari_yil = QtWidgets.QComboBox(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilOdemeDetaylari_yil.setFont(font)
        self.comboBox_mustahsilOdemeDetaylari_yil.setObjectName("comboBox_mustahsilOdemeDetaylari_yil")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(0, "")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.comboBox_mustahsilOdemeDetaylari_yil.addItem("")
        self.horizontalLayout_mustahsilOdemeDetaylari_tarih.addWidget(self.comboBox_mustahsilOdemeDetaylari_yil)
        self.gridLayout_mustahsilOdemeDetaylari_bilgiler.addLayout(self.horizontalLayout_mustahsilOdemeDetaylari_tarih, 1, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_mustahsilOdemeDetaylari_bilgiler, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton_mustahsilOdemeOnay = QtWidgets.QPushButton(self.page_mustahsile_odeme_yap)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mustahsilOdemeOnay.setFont(font)
        self.pushButton_mustahsilOdemeOnay.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_mustahsilOdemeOnay.setIcon(icon13)
        self.pushButton_mustahsilOdemeOnay.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mustahsilOdemeOnay.setObjectName("pushButton_mustahsilOdemeOnay")
        self.gridLayout_13.addWidget(self.pushButton_mustahsilOdemeOnay, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_mustahsile_odeme_yap)
        self.page_musteri_urun_satis = QtWidgets.QWidget()
        self.page_musteri_urun_satis.setObjectName("page_musteri_urun_satis")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_musteri_urun_satis)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_musteriUrunSatis = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis.setStyleSheet("background: #0B7EB4;")
        self.label_musteriUrunSatis.setWordWrap(True)
        self.label_musteriUrunSatis.setObjectName("label_musteriUrunSatis")
        self.gridLayout_6.addWidget(self.label_musteriUrunSatis, 0, 0, 1, 1)
        self.gridLayout_musteriUrunSatis = QtWidgets.QGridLayout()
        self.gridLayout_musteriUrunSatis.setObjectName("gridLayout_musteriUrunSatis")

        ################################################################################################################
        ##Manuel Olarak Müşteri Ürün Satış Kısmına Ürün Eklendi
        self.horizontalLayout_musteriUrunSatis_urunAdi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_urunAdi.setObjectName("horizontalLayout_musteriUrunSatis_urunAdi")
        self.comboBox_musteriUrunSatis_urunAdi = QtWidgets.QComboBox(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_urunAdi.setFont(font)
        self.comboBox_musteriUrunSatis_urunAdi.setObjectName("comboBox_musteriUrunSatis_urunAdi")
        self.comboBox_musteriUrunSatis_urunAdi.addItem("Ürün Seçiniz")
        self.horizontalLayout_musteriUrunSatis_urunAdi.addWidget(self.comboBox_musteriUrunSatis_urunAdi)
        self.button_musteriUrunSatis_urunEkleme = QtWidgets.QPushButton(self.page_mustahsilden_urun_al)
        self.button_musteriUrunSatis_urunEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_urunEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_urunEkleme.setStyleSheet("background: transparent;")
        self.button_musteriUrunSatis_urunEkleme.setText("")
        icon_musteriUrunSatis_urunEkleme = QtGui.QIcon()
        icon_musteriUrunSatis_urunEkleme.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_musteriUrunSatis_urunEkleme.setIcon(icon_musteriUrunSatis_urunEkleme)
        self.button_musteriUrunSatis_urunEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_urunEkleme.setObjectName("button_musteriUrunSatis_urunEkleme")
        self.horizontalLayout_musteriUrunSatis_urunAdi.addWidget(self.button_musteriUrunSatis_urunEkleme)
        self.gridLayout_musteriUrunSatis.addLayout(self.horizontalLayout_musteriUrunSatis_urunAdi, 3, 1, 1, 1)
        #self.gridLayout_musteriUrunSatis.addWidget(self.comboBox_musteriUrunSatis_urunAdi, 3, 1, 1, 1)
        ################################################################################################################

        self.label_musteriUrunSatis_tutar = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_tutar.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_tutar.setFont(font)
        self.label_musteriUrunSatis_tutar.setObjectName("label_musteriUrunSatis_tutar")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_tutar, 7, 0, 1, 1)
        self.horizontalLayout_musteriUrunSatis_kayitliMusteri = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_kayitliMusteri.setObjectName("horizontalLayout_musteriUrunSatis_kayitliMusteri")
        self.comboBox_musteriUrunSatis_KayitliMusteri = QtWidgets.QComboBox(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_KayitliMusteri.setFont(font)
        self.comboBox_musteriUrunSatis_KayitliMusteri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_musteriUrunSatis_KayitliMusteri.setObjectName("comboBox_musteriUrunSatis_KayitliMusteri")
        self.comboBox_musteriUrunSatis_KayitliMusteri.addItem("Müşteri Seçiniz")
        self.horizontalLayout_musteriUrunSatis_kayitliMusteri.addWidget(self.comboBox_musteriUrunSatis_KayitliMusteri)
        self.button_musteriUrunSatis_kayitliMusteriEkleme = QtWidgets.QPushButton(self.page_musteri_urun_satis)
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setStyleSheet("background: transparent;")
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setText("")
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setIcon(icon11)
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_kayitliMusteriEkleme.setObjectName("button_musteriUrunSatis_kayitliMusteriEkleme")
        self.horizontalLayout_musteriUrunSatis_kayitliMusteri.addWidget(self.button_musteriUrunSatis_kayitliMusteriEkleme)
        self.gridLayout_musteriUrunSatis.addLayout(self.horizontalLayout_musteriUrunSatis_kayitliMusteri, 1, 1, 1, 1)
        self.label_musteriUrunSatis_adet = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_adet.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_adet.setFont(font)
        self.label_musteriUrunSatis_adet.setObjectName("label_musteriUrunSatis_adet")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_adet, 5, 0, 1, 1)
        self.label_musteriUrunSatis_fiyat = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_fiyat.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_fiyat.setFont(font)
        self.label_musteriUrunSatis_fiyat.setObjectName("label_musteriUrunSatis_fiyat")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_fiyat, 4, 0, 1, 1)
        self.horizontalLayout_musteriUrunSatis_maliyet = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_maliyet.setObjectName("horizontalLayout_musteriUrunSatis_maliyet")
        self.doubleSpinBox_musteriUrunSatis_maliyet = QtWidgets.QDoubleSpinBox(self.page_musteri_urun_satis)
        self.doubleSpinBox_musteriUrunSatis_maliyet.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_musteriUrunSatis_maliyet.setDecimals(2)
        self.doubleSpinBox_musteriUrunSatis_maliyet.setMaximum(1000000000.0)
        self.doubleSpinBox_musteriUrunSatis_maliyet.setObjectName("doubleSpinBox_musteriUrunSatis_maliyet")
        self.horizontalLayout_musteriUrunSatis_maliyet.addWidget(self.doubleSpinBox_musteriUrunSatis_maliyet)
        self.label_musteriUrunSatis_TL = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_musteriUrunSatis_TL.setMaximumSize(QtCore.QSize(32, 39))
        self.label_musteriUrunSatis_TL.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_musteriUrunSatis_TL.setFont(font)
        self.label_musteriUrunSatis_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_musteriUrunSatis_TL.setWordWrap(True)
        self.label_musteriUrunSatis_TL.setObjectName("label_musteriUrunSatis_TL")
        self.horizontalLayout_musteriUrunSatis_maliyet.addWidget(self.label_musteriUrunSatis_TL)
        self.gridLayout_musteriUrunSatis.addLayout(self.horizontalLayout_musteriUrunSatis_maliyet, 4, 1, 1, 1)
        self.label_musteriUrunSatis_islemKimligi = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_islemKimligi.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_musteriUrunSatis_islemKimligi.setFont(font)
        self.label_musteriUrunSatis_islemKimligi.setWordWrap(True)
        self.label_musteriUrunSatis_islemKimligi.setObjectName("label_musteriUrunSatis_islemKimligi")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_islemKimligi, 6, 0, 1, 1)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet = QtWidgets.QSpinBox(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.setFont(font)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.setMaximum(1000000000)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.setObjectName("spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet")
        self.gridLayout_musteriUrunSatis.addWidget(self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet, 5, 1, 1, 1)
        self.label_musteriUrunSatis_islemKimligi_detay = QtWidgets.QLabel(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_musteriUrunSatis_islemKimligi_detay.setFont(font)
        self.label_musteriUrunSatis_islemKimligi_detay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_musteriUrunSatis_islemKimligi_detay.setWordWrap(True)
        self.label_musteriUrunSatis_islemKimligi_detay.setObjectName("label_musteriUrunSatis_islemKimligi_detay")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_islemKimligi_detay, 6, 1, 1, 1)
        self.label_musteriUrunSatis_tarih = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_tarih.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_musteriUrunSatis_tarih.setFont(font)
        self.label_musteriUrunSatis_tarih.setWordWrap(True)
        self.label_musteriUrunSatis_tarih.setObjectName("label_musteriUrunSatis_tarih")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_tarih, 2, 0, 1, 1)
        self.label_musteriUrunSatis_kayitliMusteri = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_kayitliMusteri.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_kayitliMusteri.setFont(font)
        self.label_musteriUrunSatis_kayitliMusteri.setWordWrap(True)
        self.label_musteriUrunSatis_kayitliMusteri.setObjectName("label_musteriUrunSatis_kayitliMusteri")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_kayitliMusteri, 1, 0, 1, 1)
        self.horizontalLayout_musteriUrunSatis_tarih = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_tarih.setObjectName("horizontalLayout_musteriUrunSatis_tarih")
        self.comboBox_musteriUrunSatis_Gun = QtWidgets.QComboBox(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_Gun.setFont(font)
        self.comboBox_musteriUrunSatis_Gun.setObjectName("comboBox_musteriUrunSatis_Gun")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.setItemText(0, "")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.comboBox_musteriUrunSatis_Gun.addItem("")
        self.horizontalLayout_musteriUrunSatis_tarih.addWidget(self.comboBox_musteriUrunSatis_Gun)
        self.comboBox_musteriUrunSatis_Ay = QtWidgets.QComboBox(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_Ay.setFont(font)
        self.comboBox_musteriUrunSatis_Ay.setObjectName("comboBox_musteriUrunSatis_Ay")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.setItemText(0, "")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.comboBox_musteriUrunSatis_Ay.addItem("")
        self.horizontalLayout_musteriUrunSatis_tarih.addWidget(self.comboBox_musteriUrunSatis_Ay)
        self.comboBox_musteriUrunSatis_Yil = QtWidgets.QComboBox(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_Yil.setFont(font)
        self.comboBox_musteriUrunSatis_Yil.setObjectName("comboBox_musteriUrunSatis_Yil")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.setItemText(0, "")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.comboBox_musteriUrunSatis_Yil.addItem("")
        self.horizontalLayout_musteriUrunSatis_tarih.addWidget(self.comboBox_musteriUrunSatis_Yil)
        self.gridLayout_musteriUrunSatis.addLayout(self.horizontalLayout_musteriUrunSatis_tarih, 2, 1, 1, 1)
        self.label_musteriUrunSatis_urunAdi = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_urunAdi.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_urunAdi.setFont(font)
        self.label_musteriUrunSatis_urunAdi.setWordWrap(True)
        self.label_musteriUrunSatis_urunAdi.setObjectName("label_musteriUrunSatis_urunAdi")
        self.gridLayout_musteriUrunSatis.addWidget(self.label_musteriUrunSatis_urunAdi, 3, 0, 1, 1)
        self.horizontalLayout_musteriUrunSatis_tutar = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_tutar.setObjectName("horizontalLayout_musteriUrunSatis_tutar")
        self.label_musteriUrunSatis_tutar_sonuc = QtWidgets.QLabel(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_tutar_sonuc.setFont(font)
        self.label_musteriUrunSatis_tutar_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_musteriUrunSatis_tutar_sonuc.setObjectName("label_musteriUrunSatis_tutar_sonuc")
        self.horizontalLayout_musteriUrunSatis_tutar.addWidget(self.label_musteriUrunSatis_tutar_sonuc)
        self.label_musteriUrunSatis_tutar_sonuc_TL = QtWidgets.QLabel(self.page_musteri_urun_satis)
        self.label_musteriUrunSatis_tutar_sonuc_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_musteriUrunSatis_tutar_sonuc_TL.setMaximumSize(QtCore.QSize(32, 39))
        self.label_musteriUrunSatis_tutar_sonuc_TL.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_musteriUrunSatis_tutar_sonuc_TL.setFont(font)
        self.label_musteriUrunSatis_tutar_sonuc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_musteriUrunSatis_tutar_sonuc_TL.setWordWrap(True)
        self.label_musteriUrunSatis_tutar_sonuc_TL.setObjectName("label_musteriUrunSatis_tutar_sonuc_TL")
        self.horizontalLayout_musteriUrunSatis_tutar.addWidget(self.label_musteriUrunSatis_tutar_sonuc_TL)
        self.gridLayout_musteriUrunSatis.addLayout(self.horizontalLayout_musteriUrunSatis_tutar, 7, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_musteriUrunSatis, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem2, 2, 0, 1, 1)
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit = QtWidgets.QPushButton(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.setFont(font)
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.setStyleSheet("color: #008FFF;background: #A2DDFF;")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/turkish-lira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.setIcon(icon16)
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.setObjectName("pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit")
        self.gridLayout_6.addWidget(self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit, 3, 0, 1, 1)
        self.pushButton_musteriUrunSatis_Onayla = QtWidgets.QPushButton(self.page_musteri_urun_satis)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriUrunSatis_Onayla.setFont(font)
        self.pushButton_musteriUrunSatis_Onayla.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_musteriUrunSatis_Onayla.setIcon(icon13)
        self.pushButton_musteriUrunSatis_Onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriUrunSatis_Onayla.setObjectName("pushButton_musteriUrunSatis_Onayla")
        self.gridLayout_6.addWidget(self.pushButton_musteriUrunSatis_Onayla, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_musteri_urun_satis)
        self.page_musteriden_odeme_al = QtWidgets.QWidget()
        self.page_musteriden_odeme_al.setObjectName("page_musteriden_odeme_al")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_musteriden_odeme_al)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_musteriUrunSatis_AlinanOdeme_ = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_.setStyleSheet("background: #0B7EB4;")
        self.label_musteriUrunSatis_AlinanOdeme_.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_.setObjectName("label_musteriUrunSatis_AlinanOdeme_")
        self.gridLayout_5.addWidget(self.label_musteriUrunSatis_AlinanOdeme_, 0, 0, 1, 1)
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler = QtWidgets.QGridLayout()
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.setObjectName("gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler")
        self.label_musteriUrunSatis_AlinanOdeme_turu = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_turu.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_musteriUrunSatis_AlinanOdeme_turu.setFont(font)
        self.label_musteriUrunSatis_AlinanOdeme_turu.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_turu.setObjectName("label_musteriUrunSatis_AlinanOdeme_turu")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_turu, 4, 0, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_kurumu = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_kurumu.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_AlinanOdeme_kurumu.setFont(font)
        self.label_musteriUrunSatis_AlinanOdeme_kurumu.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_kurumu.setObjectName("label_musteriUrunSatis_AlinanOdeme_kurumu")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_kurumu, 5, 0, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_miktari = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_miktari.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_AlinanOdeme_miktari.setFont(font)
        self.label_musteriUrunSatis_AlinanOdeme_miktari.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_miktari.setObjectName("label_musteriUrunSatis_AlinanOdeme_miktari")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_miktari, 3, 0, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri.setFont(font)
        self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri.setObjectName("label_musteriUrunSatis_AlinanOdeme_KayitliMusteri")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri, 1, 0, 1, 1)
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_kayitliMusteri = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_kayitliMusteri.setObjectName("horizontalLayout_musteriUrunSatis_AlinanOdeme_kayitliMusteri")
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri = QtWidgets.QComboBox(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.setFont(font)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.setObjectName("comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri")
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addItem("Müşteri Seçiniz")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addWidget(self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri)
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme = QtWidgets.QPushButton(self.page_musteriden_odeme_al)
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setStyleSheet("background: transparent;")
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setText("")
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setIcon(icon11)
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setObjectName("button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addWidget(self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme)
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addLayout(self.horizontalLayout_musteriUrunSatis_AlinanOdeme_kayitliMusteri, 1, 1, 1, 1)
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_araciKurumEkle = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_araciKurumEkle.setObjectName("horizontalLayout_musteriUrunSatis_AlinanOdeme_araciKurumEkle")
        self.comboBox_musteriUrunSatis_AlinanOdeme_kurum = QtWidgets.QComboBox(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.setFont(font)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.setObjectName("comboBox_musteriUrunSatis_AlinanOdeme_kurum")
        ################################################################################################################
        ## MÜŞTERİ ÜRÜN SATIŞ SAYFASININ ARACI KURUM COMBOBOX'I DATASTORE'DAN EKLENDİ
        self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.addItem("Aracı Kurum Seçiniz")
        listFor_musteriUrunSatis_AlinanOdeme_kurum = []
        self.file_musteriUrunSatis_AlinanOdeme_kurum = open("datastore/araciKurumlar.dat", "r", encoding="UTF-8")
        for i in self.file_musteriUrunSatis_AlinanOdeme_kurum:
            listFor_musteriUrunSatis_AlinanOdeme_kurum.append(i.strip())
        for i in range(len(listFor_musteriUrunSatis_AlinanOdeme_kurum)):
            self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.addItem(listFor_musteriUrunSatis_AlinanOdeme_kurum[i])
        ################################################################################################################

        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_araciKurumEkle.addWidget(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum)
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme = QtWidgets.QPushButton(self.page_musteriden_odeme_al)
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setStyleSheet("background: transparent;")
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setText("")
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setIcon(icon15)
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setObjectName("button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_araciKurumEkle.addWidget(self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme)
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addLayout(self.horizontalLayout_musteriUrunSatis_AlinanOdeme_araciKurumEkle, 5, 1, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi.setFont(font)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi.setObjectName("label_musteriUrunSatis_AlinanOdeme_islemKimligi")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_islemKimligi, 7, 0, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.setMinimumSize(QtCore.QSize(250, 0))
        self.label_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.setObjectName("label_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi, 6, 0, 1, 1)
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_AlinanOdemeTuru = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_AlinanOdemeTuru.setObjectName("horizontalLayout_musteriUrunSatis_AlinanOdeme_AlinanOdemeTuru")
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu = QtWidgets.QComboBox(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.setFont(font)
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.setObjectName("comboBox_musteriUrunSatis_AlinanOdeme_turu")
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.addItem("")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_AlinanOdemeTuru.addWidget(self.comboBox_musteriUrunSatis_AlinanOdeme_turu)
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme = QtWidgets.QPushButton(self.page_musteriden_odeme_al)
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setMinimumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setMaximumSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setStyleSheet("background: transparent;")
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setText("")
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setIcon(icon14)
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setIconSize(QtCore.QSize(32, 32))
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setObjectName("button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_AlinanOdemeTuru.addWidget(self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme)
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addLayout(self.horizontalLayout_musteriUrunSatis_AlinanOdeme_AlinanOdemeTuru, 4, 1, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_tarih = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        self.label_musteriUrunSatis_AlinanOdeme_tarih.setObjectName("label_musteriUrunSatis_AlinanOdeme_tarih")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_tarih, 2, 0, 1, 1)
        self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi = QtWidgets.QLineEdit(self.page_musteriden_odeme_al)
        self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.setObjectName("lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi, 6, 1, 1, 1)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc = QtWidgets.QLabel(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.setFont(font)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.setWordWrap(True)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.setObjectName("label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc, 7, 1, 1, 1)
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih.setObjectName("horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun = QtWidgets.QComboBox(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setFont(font)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setObjectName("comboBox_musteriUrunSatis_AlinanOdeme_Gun")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(0, "")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.addItem("")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih.addWidget(self.comboBox_musteriUrunSatis_AlinanOdeme_Gun)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay = QtWidgets.QComboBox(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setFont(font)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setObjectName("comboBox_musteriUrunSatis_AlinanOdeme_Ay")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(0, "")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.addItem("")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih.addWidget(self.comboBox_musteriUrunSatis_AlinanOdeme_Ay)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil = QtWidgets.QComboBox(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setFont(font)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setObjectName("comboBox_musteriUrunSatis_AlinanOdeme_Yil")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(0, "")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.addItem("")
        self.horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih.addWidget(self.comboBox_musteriUrunSatis_AlinanOdeme_Yil)
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addLayout(self.horizontalLayout_musteriUrunSatis_AlinanOdeme_tarih, 2, 1, 1, 1)
        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar = QtWidgets.QDoubleSpinBox(self.page_musteriden_odeme_al)
        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.setDecimals(2)
        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.setMaximum(1000000000.0)
        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.setObjectName("doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar")
        self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler.addWidget(self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar, 3, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_musteriUrunSatis_AlinanOdeme_bilgiler, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 2, 0, 1, 1)
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla = QtWidgets.QPushButton(self.page_musteriden_odeme_al)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.setFont(font)
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.setIcon(icon13)
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.setObjectName("pushButton_musteriUrunSatis_AlinanOdeme_onayla")
        self.gridLayout_5.addWidget(self.pushButton_musteriUrunSatis_AlinanOdeme_onayla, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_musteriden_odeme_al)
        self.page_yeni_kisi = QtWidgets.QWidget()
        self.page_yeni_kisi.setObjectName("page_yeni_kisi")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_yeni_kisi)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_yeniKisi_baslik = QtWidgets.QLabel(self.page_yeni_kisi)
        self.label_yeniKisi_baslik.setStyleSheet("background: #DC7633;")
        self.label_yeniKisi_baslik.setWordWrap(True)
        self.label_yeniKisi_baslik.setObjectName("label_yeniKisi_baslik")
        self.gridLayout_2.addWidget(self.label_yeniKisi_baslik, 0, 0, 1, 2)
        self.gridLayout_yeniKisi = QtWidgets.QGridLayout()
        self.gridLayout_yeniKisi.setObjectName("gridLayout_yeniKisi")
        self.label_yeniKisi_adi = QtWidgets.QLabel(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_yeniKisi_adi.setFont(font)
        self.label_yeniKisi_adi.setWordWrap(True)
        self.label_yeniKisi_adi.setObjectName("label_yeniKisi_adi")
        self.gridLayout_yeniKisi.addWidget(self.label_yeniKisi_adi, 0, 0, 1, 1)
        self.lineEdit_yeniKisi_ad = QtWidgets.QLineEdit(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_yeniKisi_ad.setFont(font)
        self.lineEdit_yeniKisi_ad.setText("")
        self.lineEdit_yeniKisi_ad.setObjectName("lineEdit_yeniKisi_ad")
        self.gridLayout_yeniKisi.addWidget(self.lineEdit_yeniKisi_ad, 0, 1, 1, 1)
        self.label_yeniKisi_tel = QtWidgets.QLabel(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_yeniKisi_tel.setFont(font)
        self.label_yeniKisi_tel.setWordWrap(True)
        self.label_yeniKisi_tel.setObjectName("label_yeniKisi_tel")
        self.gridLayout_yeniKisi.addWidget(self.label_yeniKisi_tel, 2, 0, 1, 1)
        self.lineEdit_yeniKisi_soyad = QtWidgets.QLineEdit(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_yeniKisi_soyad.setFont(font)
        self.lineEdit_yeniKisi_soyad.setObjectName("lineEdit_yeniKisi_soyad")
        self.gridLayout_yeniKisi.addWidget(self.lineEdit_yeniKisi_soyad, 1, 1, 1, 1)
        self.label_yeniKisi_soyadi = QtWidgets.QLabel(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_yeniKisi_soyadi.setFont(font)
        self.label_yeniKisi_soyadi.setWordWrap(True)
        self.label_yeniKisi_soyadi.setObjectName("label_yeniKisi_soyadi")
        self.gridLayout_yeniKisi.addWidget(self.label_yeniKisi_soyadi, 1, 0, 1, 1)
        self.label_yeniKisi_sehir = QtWidgets.QLabel(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_yeniKisi_sehir.setFont(font)
        self.label_yeniKisi_sehir.setWordWrap(True)
        self.label_yeniKisi_sehir.setObjectName("label_yeniKisi_sehir")
        self.gridLayout_yeniKisi.addWidget(self.label_yeniKisi_sehir, 3, 0, 1, 1)
        self.lineEdit_yeniKisi_sehir = QtWidgets.QLineEdit(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_yeniKisi_sehir.setFont(font)
        self.lineEdit_yeniKisi_sehir.setObjectName("lineEdit_yeniKisi_sehir")
        self.gridLayout_yeniKisi.addWidget(self.lineEdit_yeniKisi_sehir, 3, 1, 1, 1)
        self.horizontalLayout_yeniKisi_tel = QtWidgets.QHBoxLayout()
        self.horizontalLayout_yeniKisi_tel.setObjectName("horizontalLayout_yeniKisi_tel")
        self.label_yeniKisi_90 = QtWidgets.QLabel(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_yeniKisi_90.setFont(font)
        self.label_yeniKisi_90.setWordWrap(True)
        self.label_yeniKisi_90.setObjectName("label_yeniKisi_90")
        self.horizontalLayout_yeniKisi_tel.addWidget(self.label_yeniKisi_90)
        self.lineEdit_yeniKisi_tel = QtWidgets.QLineEdit(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_yeniKisi_tel.setFont(font)
        self.lineEdit_yeniKisi_tel.setObjectName("lineEdit_yeniKisi_tel")
        self.horizontalLayout_yeniKisi_tel.addWidget(self.lineEdit_yeniKisi_tel)
        self.gridLayout_yeniKisi.addLayout(self.horizontalLayout_yeniKisi_tel, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_yeniKisi, 1, 0, 1, 2)

        self.tableView_yeniKisiEkle_kayitlilariGoruntule = QtWidgets.QTableView(self.page_yeni_kisi)
        self.tableView_yeniKisiEkle_kayitlilariGoruntule.setObjectName("tableView_yeniKisiEkle_kayitlilariGoruntule")
        self.gridLayout_2.addWidget(self.tableView_yeniKisiEkle_kayitlilariGoruntule, 2, 0, 1, 2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableView_yeniKisiEkle_kayitlilariGoruntule.setFont(font)
        """ ÖNEMLİ KISIM TABLE VIEW YERLESTIRMEK ICIN """
        ###############################################################
        self.df_yeniKisiEkle_kayitlilariGoruntule = pd.read_csv("datastore/kisiler.csv")
        model_yeniKisiEkle_kayitlilariGoruntule = PandasModel(self.df_yeniKisiEkle_kayitlilariGoruntule)
        self.tableView_yeniKisiEkle_kayitlilariGoruntule.setModel(model_yeniKisiEkle_kayitlilariGoruntule)
        self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setStretchLastSection(True)
        self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_yeniKisiEkle_kayitlilariGoruntule.setSortingEnabled(True)
        ###############################################################

        self.button_yeniKisi_mustahsilOnay = QtWidgets.QPushButton(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_yeniKisi_mustahsilOnay.setFont(font)
        self.button_yeniKisi_mustahsilOnay.setStyleSheet("color: #E9E9E9; background: #1A75C9;")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/tractor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_yeniKisi_mustahsilOnay.setIcon(icon17)
        self.button_yeniKisi_mustahsilOnay.setIconSize(QtCore.QSize(32, 32))
        self.button_yeniKisi_mustahsilOnay.setObjectName("button_yeniKisi_mustahsilOnay")
        self.gridLayout_2.addWidget(self.button_yeniKisi_mustahsilOnay, 3, 0, 1, 1)
        self.button_yeniKisi_musteriOnay = QtWidgets.QPushButton(self.page_yeni_kisi)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_yeniKisi_musteriOnay.setFont(font)
        self.button_yeniKisi_musteriOnay.setStyleSheet("color: #E9E9E9; background: #1A75C9;")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/buy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_yeniKisi_musteriOnay.setIcon(icon18)
        self.button_yeniKisi_musteriOnay.setIconSize(QtCore.QSize(32, 32))
        self.button_yeniKisi_musteriOnay.setObjectName("button_yeniKisi_musteriOnay")
        self.gridLayout_2.addWidget(self.button_yeniKisi_musteriOnay, 3, 1, 1, 1)
        ## TABLEVIEW EKLENDİĞİ İÇİN GEREK KALMADI İLERDE KULLANILABİLİR!
        # spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_yeni_kisi)
        self.page_musterinin_aldigi_malzemeler = QtWidgets.QWidget()
        self.page_musterinin_aldigi_malzemeler.setObjectName("page_musterinin_aldigi_malzemeler")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_musterinin_aldigi_malzemeler)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_musteriAldigiMalzemeler_tarih = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriAldigiMalzemeler_tarih.setObjectName("horizontalLayout_musteriAldigiMalzemeler_tarih")
        self.horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi.setObjectName("horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setObjectName("comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.addItem("")
        self.horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi.addWidget(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setObjectName("comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.addItem("")
        self.horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi.addWidget(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setObjectName("comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.addItem("")
        self.horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi.addWidget(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil)
        self.horizontalLayout_musteriAldigiMalzemeler_tarih.addLayout(self.horizontalLayout_musteriAldigiMalzemeler__baslangicTarihi)
        self.line_musteriAldigiMalzemeler_tarihlerArasiAyrac = QtWidgets.QFrame(self.page_musterinin_aldigi_malzemeler)
        self.line_musteriAldigiMalzemeler_tarihlerArasiAyrac.setStyleSheet("background: black;")
        self.line_musteriAldigiMalzemeler_tarihlerArasiAyrac.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_musteriAldigiMalzemeler_tarihlerArasiAyrac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_musteriAldigiMalzemeler_tarihlerArasiAyrac.setObjectName("line_musteriAldigiMalzemeler_tarihlerArasiAyrac")
        self.horizontalLayout_musteriAldigiMalzemeler_tarih.addWidget(self.line_musteriAldigiMalzemeler_tarihlerArasiAyrac)
        self.horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi.setObjectName("horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setObjectName("comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.addItem("")
        self.horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi.addWidget(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setObjectName("comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.addItem("")
        self.horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi.addWidget(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setObjectName("comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.addItem("")
        self.horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi.addWidget(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil)
        self.horizontalLayout_musteriAldigiMalzemeler_tarih.addLayout(self.horizontalLayout_musteriAldigiMalzemeler_baslangicTarihi)
        self.gridLayout_3.addLayout(self.horizontalLayout_musteriAldigiMalzemeler_tarih, 3, 0, 1, 2)
        self.label_musteriAldigiMalzemeler = QtWidgets.QLabel(self.page_musterinin_aldigi_malzemeler)
        self.label_musteriAldigiMalzemeler.setStyleSheet("background: #44BD00;")
        self.label_musteriAldigiMalzemeler.setWordWrap(True)
        self.label_musteriAldigiMalzemeler.setObjectName("label_musteriAldigiMalzemeler")
        self.gridLayout_3.addWidget(self.label_musteriAldigiMalzemeler, 0, 0, 1, 2)
        self.tableView_musteriAldigiMalzemeler = QtWidgets.QTableView(self.page_musterinin_aldigi_malzemeler)
        self.tableView_musteriAldigiMalzemeler.setObjectName("tableView_musteriAldigiMalzemeler")
        self.gridLayout_3.addWidget(self.tableView_musteriAldigiMalzemeler, 2, 0, 1, 2)
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap = QtWidgets.QPushButton(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.setFont(font)
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.setStyleSheet("color: #FF4F00; background: #FFD0BB;")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/search (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.setIcon(icon19)
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.setObjectName("pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap")
        self.gridLayout_3.addWidget(self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap, 4, 0, 1, 2)
        icon_tumVerileriGoster = QtGui.QIcon()
        icon_tumVerileriGoster.addPixmap(QtGui.QPixmap("icons/020-survey.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster = QtWidgets.QPushButton(
            self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.setFont(font)
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.setStyleSheet(
            "color: green; background: #D7FAC6;")
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.setIcon(icon_tumVerileriGoster)
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.setObjectName(
            "pushButton_musteriAldigiMalzemeler_tumVerileriGoster")
        self.gridLayout_3.addWidget(self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster, 5, 0, 1, 2)

        self.horizontalLayout_musteriAldigiMalzemeler_kayitliMusteri = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriAldigiMalzemeler_kayitliMusteri.setObjectName("horizontalLayout_musteriAldigiMalzemeler_kayitliMusteri")
        self.label_musteriAldigiMalzemeler_KayitliMusteri = QtWidgets.QLabel(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriAldigiMalzemeler_KayitliMusteri.setFont(font)
        self.label_musteriAldigiMalzemeler_KayitliMusteri.setWordWrap(True)
        self.label_musteriAldigiMalzemeler_KayitliMusteri.setObjectName("label_musteriAldigiMalzemeler_KayitliMusteri")
        self.horizontalLayout_musteriAldigiMalzemeler_kayitliMusteri.addWidget(self.label_musteriAldigiMalzemeler_KayitliMusteri)
        self.comboBox_musteriAldigiMalzemeler_kayitliMusteri = QtWidgets.QComboBox(self.page_musterinin_aldigi_malzemeler)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.setFont(font)
        self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.setObjectName("comboBox_musteriAldigiMalzemeler_kayitliMusteri")
        self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.addItem("Müşteri Seçiniz")
        self.horizontalLayout_musteriAldigiMalzemeler_kayitliMusteri.addWidget(self.comboBox_musteriAldigiMalzemeler_kayitliMusteri)
        self.gridLayout_3.addLayout(self.horizontalLayout_musteriAldigiMalzemeler_kayitliMusteri, 1, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_musterinin_aldigi_malzemeler)
        self.page_kisi_goruntule = QtWidgets.QWidget()
        self.page_kisi_goruntule.setObjectName("page_kisi_goruntule")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_kisi_goruntule)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.toolButton_musteri = QtWidgets.QToolButton(self.page_kisi_goruntule)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_musteri.sizePolicy().hasHeightForWidth())
        self.toolButton_musteri.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_musteri.setFont(font)
        self.toolButton_musteri.setStyleSheet("color: #801C03; background: #FAD4CA;")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/buyer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_musteri.setIcon(icon20)
        self.toolButton_musteri.setIconSize(QtCore.QSize(225, 225))
        self.toolButton_musteri.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_musteri.setObjectName("toolButton_musteri")
        self.gridLayout_10.addWidget(self.toolButton_musteri, 0, 2, 1, 1)
        self.toolButton_mustahsil = QtWidgets.QToolButton(self.page_kisi_goruntule)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_mustahsil.sizePolicy().hasHeightForWidth())
        self.toolButton_mustahsil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_mustahsil.setFont(font)
        self.toolButton_mustahsil.setStyleSheet("color: #4C7102; background: #EDFFC8;")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/farmer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_mustahsil.setIcon(icon21)
        self.toolButton_mustahsil.setIconSize(QtCore.QSize(225, 225))
        self.toolButton_mustahsil.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_mustahsil.setObjectName("toolButton_mustahsil")
        self.gridLayout_10.addWidget(self.toolButton_mustahsil, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_kisi_goruntule)
        self.page_mustahsilBilgileri = QtWidgets.QWidget()
        self.page_mustahsilBilgileri.setObjectName("page_mustahsilBilgileri")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_mustahsilBilgileri)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_mustahsilBilgileri_tarihAraligi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilBilgileri_tarihAraligi.setObjectName("horizontalLayout_mustahsilBilgileri_tarihAraligi")
        self.horizontalLayout_mustahsilBilgileri_baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilBilgileri_baslangicTarihi.setObjectName("horizontalLayout_mustahsilBilgileri_baslangicTarihi")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setFont(font)
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setObjectName("comboBox_mustahsilBilgileri_baslangicTarihiGun")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.addItem("")
        self.horizontalLayout_mustahsilBilgileri_baslangicTarihi.addWidget(self.comboBox_mustahsilBilgileri_baslangicTarihiGun)
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setFont(font)
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setObjectName("comboBox_mustahsilBilgileri_baslangicTarihiAy")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.addItem("")
        self.horizontalLayout_mustahsilBilgileri_baslangicTarihi.addWidget(self.comboBox_mustahsilBilgileri_baslangicTarihiAy)
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setFont(font)
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setObjectName("comboBox_mustahsilBilgileri_baslangicTarihiYil")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.addItem("")
        self.horizontalLayout_mustahsilBilgileri_baslangicTarihi.addWidget(self.comboBox_mustahsilBilgileri_baslangicTarihiYil)
        self.horizontalLayout_mustahsilBilgileri_tarihAraligi.addLayout(self.horizontalLayout_mustahsilBilgileri_baslangicTarihi)
        self.line_mustahsilBilgileri_tarihlerArasiAyrac = QtWidgets.QFrame(self.page_mustahsilBilgileri)
        self.line_mustahsilBilgileri_tarihlerArasiAyrac.setStyleSheet("background: black;")
        self.line_mustahsilBilgileri_tarihlerArasiAyrac.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_mustahsilBilgileri_tarihlerArasiAyrac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_mustahsilBilgileri_tarihlerArasiAyrac.setObjectName("line_mustahsilBilgileri_tarihlerArasiAyrac")
        self.horizontalLayout_mustahsilBilgileri_tarihAraligi.addWidget(self.line_mustahsilBilgileri_tarihlerArasiAyrac)
        self.horizontalLayout_mustahsilBilgileri_bitisTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilBilgileri_bitisTarihi.setObjectName("horizontalLayout_mustahsilBilgileri_bitisTarihi")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setFont(font)
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setObjectName("comboBox_mustahsilBilgileri_bitisTarihiGun")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.addItem("")
        self.horizontalLayout_mustahsilBilgileri_bitisTarihi.addWidget(self.comboBox_mustahsilBilgileri_bitisTarihiGun)
        self.comboBox_mustahsilBilgileri_bitisTarihiAy = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setFont(font)
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setObjectName("comboBox_mustahsilBilgileri_bitisTarihiAy")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.addItem("")
        self.horizontalLayout_mustahsilBilgileri_bitisTarihi.addWidget(self.comboBox_mustahsilBilgileri_bitisTarihiAy)
        self.comboBox_mustahsilBilgileri_bitisTarihiYil = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setFont(font)
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setObjectName("comboBox_mustahsilBilgileri_bitisTarihiYil")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.addItem("")
        self.horizontalLayout_mustahsilBilgileri_bitisTarihi.addWidget(self.comboBox_mustahsilBilgileri_bitisTarihiYil)
        self.horizontalLayout_mustahsilBilgileri_tarihAraligi.addLayout(self.horizontalLayout_mustahsilBilgileri_bitisTarihi)
        self.gridLayout_12.addLayout(self.horizontalLayout_mustahsilBilgileri_tarihAraligi, 3, 0, 1, 2)
        self.horizontalLayout_mustahsilBilgileri_kayitliMustahsil = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mustahsilBilgileri_kayitliMustahsil.setObjectName("horizontalLayout_mustahsilBilgileri_kayitliMustahsil")
        self.label_mustahsilBilgileri_kayitliMustahsil = QtWidgets.QLabel(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_mustahsilBilgileri_kayitliMustahsil.setFont(font)
        self.label_mustahsilBilgileri_kayitliMustahsil.setWordWrap(True)
        self.label_mustahsilBilgileri_kayitliMustahsil.setObjectName("label_mustahsilBilgileri_kayitliMustahsil")
        self.horizontalLayout_mustahsilBilgileri_kayitliMustahsil.addWidget(self.label_mustahsilBilgileri_kayitliMustahsil)
        self.comboBox_mustahsilBilgileri_kayitliMustahsil = QtWidgets.QComboBox(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_mustahsilBilgileri_kayitliMustahsil.setFont(font)
        self.comboBox_mustahsilBilgileri_kayitliMustahsil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_mustahsilBilgileri_kayitliMustahsil.setObjectName("comboBox_mustahsilBilgileri_kayitliMustahsil")
        self.comboBox_mustahsilBilgileri_kayitliMustahsil.addItem("Müstahsil Seçiniz")
        self.horizontalLayout_mustahsilBilgileri_kayitliMustahsil.addWidget(self.comboBox_mustahsilBilgileri_kayitliMustahsil)
        self.gridLayout_12.addLayout(self.horizontalLayout_mustahsilBilgileri_kayitliMustahsil, 1, 0, 1, 2)
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap = QtWidgets.QPushButton(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.setFont(font)
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.setStyleSheet("color: #FF4F00; background: #FFD0BB;")
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.setIcon(icon19)
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.setObjectName("pushButton_mustahsilBilgileri_tarihlerArasiAramaYap")
        self.gridLayout_12.addWidget(self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap, 4, 0, 1, 2)
        self.pushButton_mustahsilBilgileri_tumVerileriGoster = QtWidgets.QPushButton(self.page_mustahsilBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.setFont(font)
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.setIcon(icon_tumVerileriGoster)
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.setObjectName("pushButton_mustahsilBilgileri_tumVerileriGoster")
        self.gridLayout_12.addWidget(self.pushButton_mustahsilBilgileri_tumVerileriGoster, 5, 0, 1, 2)
        self.label_mustahsilBilgileri = QtWidgets.QLabel(self.page_mustahsilBilgileri)
        self.label_mustahsilBilgileri.setStyleSheet("background: #FFC100;")
        self.label_mustahsilBilgileri.setWordWrap(True)
        self.label_mustahsilBilgileri.setObjectName("label_mustahsilBilgileri")
        self.gridLayout_12.addWidget(self.label_mustahsilBilgileri, 0, 0, 1, 2)
        self.tableView_mustahsilBilgileri = QtWidgets.QTableView(self.page_mustahsilBilgileri)
        self.tableView_mustahsilBilgileri.setObjectName("tableView_mustahsilBilgileri")
        self.gridLayout_12.addWidget(self.tableView_mustahsilBilgileri, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_mustahsilBilgileri)
        self.page_musteriBilgileri = QtWidgets.QWidget()
        self.page_musteriBilgileri.setObjectName("page_musteriBilgileri")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_musteriBilgileri)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_musteriBilgileri = QtWidgets.QLabel(self.page_musteriBilgileri)
        self.label_musteriBilgileri.setStyleSheet("background: #FFC100;")
        self.label_musteriBilgileri.setWordWrap(True)
        self.label_musteriBilgileri.setObjectName("label_musteriBilgileri")
        self.gridLayout_9.addWidget(self.label_musteriBilgileri, 0, 0, 1, 1)
        self.horizontalLayout_musteriBilgileri_kayitliMusteri = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriBilgileri_kayitliMusteri.setObjectName("horizontalLayout_musteriBilgileri_kayitliMusteri")
        self.label_musteriBilgileri_kayitliMusteri = QtWidgets.QLabel(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_musteriBilgileri_kayitliMusteri.setFont(font)
        self.label_musteriBilgileri_kayitliMusteri.setWordWrap(True)
        self.label_musteriBilgileri_kayitliMusteri.setObjectName("label_musteriBilgileri_kayitliMusteri")
        self.horizontalLayout_musteriBilgileri_kayitliMusteri.addWidget(self.label_musteriBilgileri_kayitliMusteri)
        self.comboBox_musteriBilgileri_kayitliMusteri = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_kayitliMusteri.setFont(font)
        self.comboBox_musteriBilgileri_kayitliMusteri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_musteriBilgileri_kayitliMusteri.setObjectName("comboBox_musteriBilgileri_kayitliMusteri")
        self.comboBox_musteriBilgileri_kayitliMusteri.addItem("Müşteri Seçiniz")
        self.horizontalLayout_musteriBilgileri_kayitliMusteri.addWidget(self.comboBox_musteriBilgileri_kayitliMusteri)
        self.gridLayout_9.addLayout(self.horizontalLayout_musteriBilgileri_kayitliMusteri, 1, 0, 1, 1)
        self.tableView_musteriBilgileri = QtWidgets.QTableView(self.page_musteriBilgileri)
        self.tableView_musteriBilgileri.setObjectName("tableView_musteriBilgileri")
        self.gridLayout_9.addWidget(self.tableView_musteriBilgileri, 2, 0, 1, 1)
        self.horizontalLayout_musteriBilgileri_tarihAraligi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musteriBilgileri_tarihAraligi.setObjectName("horizontalLayout_musteriBilgileri_tarihAraligi")
        self.horizontalLayout_musterilBilgileri_baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musterilBilgileri_baslangicTarihi.setObjectName("horizontalLayout_musterilBilgileri_baslangicTarihi")
        self.comboBox_musteriBilgileri_baslangicTarihiGun = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setFont(font)
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setObjectName("comboBox_musteriBilgileri_baslangicTarihiGun")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiGun.addItem("")
        self.horizontalLayout_musterilBilgileri_baslangicTarihi.addWidget(self.comboBox_musteriBilgileri_baslangicTarihiGun)
        self.comboBox_musteriBilgileri_baslangicTarihiAy = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setFont(font)
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setObjectName("comboBox_musteriBilgileri_baslangicTarihiAy")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiAy.addItem("")
        self.horizontalLayout_musterilBilgileri_baslangicTarihi.addWidget(self.comboBox_musteriBilgileri_baslangicTarihiAy)
        self.comboBox_musteriBilgileri_baslangicTarihiYil = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setFont(font)
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setObjectName("comboBox_musteriBilgileri_baslangicTarihiYil")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_baslangicTarihiYil.addItem("")
        self.horizontalLayout_musterilBilgileri_baslangicTarihi.addWidget(self.comboBox_musteriBilgileri_baslangicTarihiYil)
        self.horizontalLayout_musteriBilgileri_tarihAraligi.addLayout(self.horizontalLayout_musterilBilgileri_baslangicTarihi)
        self.line_musteriBilgileri_tarihlerArasiAyrac = QtWidgets.QFrame(self.page_musteriBilgileri)
        self.line_musteriBilgileri_tarihlerArasiAyrac.setStyleSheet("background: black;")
        self.line_musteriBilgileri_tarihlerArasiAyrac.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_musteriBilgileri_tarihlerArasiAyrac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_musteriBilgileri_tarihlerArasiAyrac.setObjectName("line_musteriBilgileri_tarihlerArasiAyrac")
        self.horizontalLayout_musteriBilgileri_tarihAraligi.addWidget(self.line_musteriBilgileri_tarihlerArasiAyrac)
        self.horizontalLayout_musterilBilgileri_bitisTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_musterilBilgileri_bitisTarihi.setObjectName("horizontalLayout_musterilBilgileri_bitisTarihi")
        self.comboBox_musteriBilgileri_bitisTarihiGun = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_bitisTarihiGun.setFont(font)
        self.comboBox_musteriBilgileri_bitisTarihiGun.setObjectName("comboBox_musteriBilgileri_bitisTarihiGun")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiGun.addItem("")
        self.horizontalLayout_musterilBilgileri_bitisTarihi.addWidget(self.comboBox_musteriBilgileri_bitisTarihiGun)
        self.comboBox_musteriBilgileri_bitisTarihiAy = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_bitisTarihiAy.setFont(font)
        self.comboBox_musteriBilgileri_bitisTarihiAy.setObjectName("comboBox_musteriBilgileri_bitisTarihiAy")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiAy.addItem("")
        self.horizontalLayout_musterilBilgileri_bitisTarihi.addWidget(self.comboBox_musteriBilgileri_bitisTarihiAy)
        self.comboBox_musteriBilgileri_bitisTarihiYil = QtWidgets.QComboBox(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_musteriBilgileri_bitisTarihiYil.setFont(font)
        self.comboBox_musteriBilgileri_bitisTarihiYil.setObjectName("comboBox_musteriBilgileri_bitisTarihiYil")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.comboBox_musteriBilgileri_bitisTarihiYil.addItem("")
        self.horizontalLayout_musterilBilgileri_bitisTarihi.addWidget(self.comboBox_musteriBilgileri_bitisTarihiYil)
        self.horizontalLayout_musteriBilgileri_tarihAraligi.addLayout(self.horizontalLayout_musterilBilgileri_bitisTarihi)
        self.gridLayout_9.addLayout(self.horizontalLayout_musteriBilgileri_tarihAraligi, 3, 0, 1, 1)
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap = QtWidgets.QPushButton(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.setFont(font)
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.setStyleSheet("color: #FF4F00; background: #FFD0BB;")
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.setIcon(icon19)
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.setObjectName("pushButton_musteriBilgileri_tarihlerArasiAramaYap")
        self.gridLayout_9.addWidget(self.pushButton_musteriBilgileri_tarihlerArasiAramaYap, 4, 0, 1, 1)
        self.pushButton_musteriBilgileri_tumVerileriGoster = QtWidgets.QPushButton(self.page_musteriBilgileri)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_musteriBilgileri_tumVerileriGoster.setFont(font)
        self.pushButton_musteriBilgileri_tumVerileriGoster.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_musteriBilgileri_tumVerileriGoster.setIcon(icon_tumVerileriGoster)
        self.pushButton_musteriBilgileri_tumVerileriGoster.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_musteriBilgileri_tumVerileriGoster.setObjectName("pushButton_musteriBilgileri_tumVerileriGoster")
        self.gridLayout_9.addWidget(self.pushButton_musteriBilgileri_tumVerileriGoster, 5, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_musteriBilgileri)

        self.page_hesap_ozeti = QtWidgets.QWidget()
        self.page_hesap_ozeti.setObjectName("page_hesap_ozeti")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_hesap_ozeti)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_hesapOzeti_alacakBilgileri = QtWidgets.QVBoxLayout()
        self.verticalLayout_hesapOzeti_alacakBilgileri.setObjectName("verticalLayout_hesapOzeti_alacakBilgileri")
        self.label_hesapOzeti_alacakBilgileri = QtWidgets.QLabel(self.page_hesap_ozeti)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.label_hesapOzeti_alacakBilgileri.setFont(font)
        self.label_hesapOzeti_alacakBilgileri.setStyleSheet("background: green;")
        self.label_hesapOzeti_alacakBilgileri.setWordWrap(True)
        self.label_hesapOzeti_alacakBilgileri.setObjectName("label_hesapOzeti_alacakBilgileri")
        self.verticalLayout_hesapOzeti_alacakBilgileri.addWidget(self.label_hesapOzeti_alacakBilgileri)
        self.tableView_alacakBilgileri = QtWidgets.QTableView(self.page_hesap_ozeti)
        self.tableView_alacakBilgileri.setObjectName("tableView_alacakBilgileri")
        self.verticalLayout_hesapOzeti_alacakBilgileri.addWidget(self.tableView_alacakBilgileri)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_hesapOzeti_toplamAlacak = QtWidgets.QLabel(self.page_hesap_ozeti)
        self.label_hesapOzeti_toplamAlacak.setMinimumSize(QtCore.QSize(215, 35))
        self.label_hesapOzeti_toplamAlacak.setMaximumSize(QtCore.QSize(215, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_hesapOzeti_toplamAlacak.setFont(font)
        self.label_hesapOzeti_toplamAlacak.setStyleSheet("color:green;")
        self.label_hesapOzeti_toplamAlacak.setWordWrap(True)
        self.label_hesapOzeti_toplamAlacak.setObjectName("label_hesapOzeti_toplamAlacak")
        self.horizontalLayout.addWidget(self.label_hesapOzeti_toplamAlacak)
        self.label_hesapOzeti_toplamAlacak_TL = QtWidgets.QLabel(self.page_hesap_ozeti)
        self.label_hesapOzeti_toplamAlacak_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_hesapOzeti_toplamAlacak_TL.setWordWrap(True)
        self.label_hesapOzeti_toplamAlacak_TL.setObjectName("label_hesapOzeti_toplamAlacak_TL")
        self.horizontalLayout.addWidget(self.label_hesapOzeti_toplamAlacak_TL)
        self.verticalLayout_hesapOzeti_alacakBilgileri.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_hesapOzeti_alacakBilgileri)
        self.verticalLayout_hesapOzeti_borcBilgisi = QtWidgets.QVBoxLayout()
        self.verticalLayout_hesapOzeti_borcBilgisi.setObjectName("verticalLayout_hesapOzeti_borcBilgisi")
        self.label_hesapOzeti_borcBilgileri = QtWidgets.QLabel(self.page_hesap_ozeti)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.label_hesapOzeti_borcBilgileri.setFont(font)
        self.label_hesapOzeti_borcBilgileri.setStyleSheet("background: red;")
        self.label_hesapOzeti_borcBilgileri.setWordWrap(True)
        self.label_hesapOzeti_borcBilgileri.setObjectName("label_hesapOzeti_borcBilgileri")
        self.verticalLayout_hesapOzeti_borcBilgisi.addWidget(self.label_hesapOzeti_borcBilgileri)
        self.tableView_borcBilgileri = QtWidgets.QTableView(self.page_hesap_ozeti)
        self.tableView_borcBilgileri.setObjectName("tableView_borcBilgileri")
        self.verticalLayout_hesapOzeti_borcBilgisi.addWidget(self.tableView_borcBilgileri)
        self.horizontalLayout_hesapOzeti_toplamBorc = QtWidgets.QHBoxLayout()
        self.horizontalLayout_hesapOzeti_toplamBorc.setObjectName("horizontalLayout_hesapOzeti_toplamBorc")
        self.label_hesapOzeti_toplamBorc = QtWidgets.QLabel(self.page_hesap_ozeti)
        self.label_hesapOzeti_toplamBorc.setMinimumSize(QtCore.QSize(195, 35))
        self.label_hesapOzeti_toplamBorc.setMaximumSize(QtCore.QSize(195, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_hesapOzeti_toplamBorc.setFont(font)
        self.label_hesapOzeti_toplamBorc.setStyleSheet("color:red;")
        self.label_hesapOzeti_toplamBorc.setWordWrap(True)
        self.label_hesapOzeti_toplamBorc.setObjectName("label_hesapOzeti_toplamBorc")
        self.horizontalLayout_hesapOzeti_toplamBorc.addWidget(self.label_hesapOzeti_toplamBorc)
        self.label_hesapOzeti_toplamBorc_TL = QtWidgets.QLabel(self.page_hesap_ozeti)
        self.label_hesapOzeti_toplamBorc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_hesapOzeti_toplamBorc_TL.setWordWrap(True)
        self.label_hesapOzeti_toplamBorc_TL.setObjectName("label_hesapOzeti_toplamBorc_TL")
        self.horizontalLayout_hesapOzeti_toplamBorc.addWidget(self.label_hesapOzeti_toplamBorc_TL)
        self.verticalLayout_hesapOzeti_borcBilgisi.addLayout(self.horizontalLayout_hesapOzeti_toplamBorc)
        self.horizontalLayout_3.addLayout(self.verticalLayout_hesapOzeti_borcBilgisi)
        self.stackedWidget.addWidget(self.page_hesap_ozeti)

        self.page_kasa_hesabi = QtWidgets.QWidget()
        self.page_kasa_hesabi.setObjectName("page_kasa_hesabi")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.page_kasa_hesabi)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_kasaHesabi = QtWidgets.QLabel(self.page_kasa_hesabi)
        self.label_kasaHesabi.setStyleSheet("background: #0049FF;")
        self.label_kasaHesabi.setWordWrap(True)
        self.label_kasaHesabi.setObjectName("label_kasaHesabi")
        self.gridLayout_21.addWidget(self.label_kasaHesabi, 0, 0, 1, 1)
        self.horizontalLayout_kasaHesabi_odemeTuru = QtWidgets.QHBoxLayout()
        self.horizontalLayout_kasaHesabi_odemeTuru.setObjectName("horizontalLayout_kasaHesabi_odemeTuru")
        self.label_kasaHesabi_odemeTuru = QtWidgets.QLabel(self.page_kasa_hesabi)
        self.label_kasaHesabi_odemeTuru.setMinimumSize(QtCore.QSize(260, 39))
        self.label_kasaHesabi_odemeTuru.setMaximumSize(QtCore.QSize(260, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_kasaHesabi_odemeTuru.setFont(font)
        self.label_kasaHesabi_odemeTuru.setWordWrap(True)
        self.label_kasaHesabi_odemeTuru.setObjectName("label_kasaHesabi_odemeTuru")
        self.horizontalLayout_kasaHesabi_odemeTuru.addWidget(self.label_kasaHesabi_odemeTuru)
        self.comboBox_kasaHesabi_odemeTuru = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_odemeTuru.setFont(font)
        self.comboBox_kasaHesabi_odemeTuru.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_kasaHesabi_odemeTuru.setObjectName("comboBox_kasaHesabi_odemeTuru")
        self.comboBox_kasaHesabi_odemeTuru.addItem("")
        self.comboBox_kasaHesabi_odemeTuru.addItem("")
        self.comboBox_kasaHesabi_odemeTuru.addItem("")
        self.horizontalLayout_kasaHesabi_odemeTuru.addWidget(self.comboBox_kasaHesabi_odemeTuru)
        self.gridLayout_21.addLayout(self.horizontalLayout_kasaHesabi_odemeTuru, 1, 0, 1, 1)
        self.tableView_kasaHesabi = QtWidgets.QTableView(self.page_kasa_hesabi)
        self.tableView_kasaHesabi.setObjectName("tableView_kasaHesabi")
        self.gridLayout_21.addWidget(self.tableView_kasaHesabi, 2, 0, 1, 1)
        self.horizontalLayout_kasaHesabi_tarihAraligi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_kasaHesabi_tarihAraligi.setObjectName("horizontalLayout_kasaHesabi_tarihAraligi")
        self.horizontalLayout_kasaHesabi_baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_kasaHesabi_baslangicTarihi.setObjectName("horizontalLayout_kasaHesabi_baslangicTarihi")
        self.comboBox_kasaHesabi_baslangicTarihiGun = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_baslangicTarihiGun.setFont(font)
        self.comboBox_kasaHesabi_baslangicTarihiGun.setObjectName("comboBox_kasaHesabi_baslangicTarihiGun")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiGun.addItem("")
        self.horizontalLayout_kasaHesabi_baslangicTarihi.addWidget(self.comboBox_kasaHesabi_baslangicTarihiGun)
        self.comboBox_kasaHesabi_baslangicTarihiAy = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_baslangicTarihiAy.setFont(font)
        self.comboBox_kasaHesabi_baslangicTarihiAy.setObjectName("comboBox_kasaHesabi_baslangicTarihiAy")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiAy.addItem("")
        self.horizontalLayout_kasaHesabi_baslangicTarihi.addWidget(self.comboBox_kasaHesabi_baslangicTarihiAy)
        self.comboBox_kasaHesabi_baslangicTarihiYil = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_baslangicTarihiYil.setFont(font)
        self.comboBox_kasaHesabi_baslangicTarihiYil.setObjectName("comboBox_kasaHesabi_baslangicTarihiYil")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.comboBox_kasaHesabi_baslangicTarihiYil.addItem("")
        self.horizontalLayout_kasaHesabi_baslangicTarihi.addWidget(self.comboBox_kasaHesabi_baslangicTarihiYil)
        self.horizontalLayout_kasaHesabi_tarihAraligi.addLayout(self.horizontalLayout_kasaHesabi_baslangicTarihi)
        self.line_kasaHesabi_tarihlerArasiAyrac = QtWidgets.QFrame(self.page_kasa_hesabi)
        self.line_kasaHesabi_tarihlerArasiAyrac.setStyleSheet("background: black;")
        self.line_kasaHesabi_tarihlerArasiAyrac.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_kasaHesabi_tarihlerArasiAyrac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_kasaHesabi_tarihlerArasiAyrac.setObjectName("line_kasaHesabi_tarihlerArasiAyrac")
        self.horizontalLayout_kasaHesabi_tarihAraligi.addWidget(self.line_kasaHesabi_tarihlerArasiAyrac)
        self.horizontalLayout_kasaHesabi_bitisTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_kasaHesabi_bitisTarihi.setObjectName("horizontalLayout_kasaHesabi_bitisTarihi")
        self.comboBox_kasaHesabi_bitisTarihiGun = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_bitisTarihiGun.setFont(font)
        self.comboBox_kasaHesabi_bitisTarihiGun.setObjectName("comboBox_kasaHesabi_bitisTarihiGun")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiGun.addItem("")
        self.horizontalLayout_kasaHesabi_bitisTarihi.addWidget(self.comboBox_kasaHesabi_bitisTarihiGun)
        self.comboBox_kasaHesabi_bitisTarihiAy = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_bitisTarihiAy.setFont(font)
        self.comboBox_kasaHesabi_bitisTarihiAy.setObjectName("comboBox_kasaHesabi_bitisTarihiAy")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiAy.addItem("")
        self.horizontalLayout_kasaHesabi_bitisTarihi.addWidget(self.comboBox_kasaHesabi_bitisTarihiAy)
        self.comboBox_kasaHesabi_bitisTarihiYil = QtWidgets.QComboBox(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_kasaHesabi_bitisTarihiYil.setFont(font)
        self.comboBox_kasaHesabi_bitisTarihiYil.setObjectName("comboBox_kasaHesabi_bitisTarihiYil")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.comboBox_kasaHesabi_bitisTarihiYil.addItem("")
        self.horizontalLayout_kasaHesabi_bitisTarihi.addWidget(self.comboBox_kasaHesabi_bitisTarihiYil)
        self.horizontalLayout_kasaHesabi_tarihAraligi.addLayout(self.horizontalLayout_kasaHesabi_bitisTarihi)
        self.gridLayout_21.addLayout(self.horizontalLayout_kasaHesabi_tarihAraligi, 3, 0, 1, 1)
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap = QtWidgets.QPushButton(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.setFont(font)
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.setStyleSheet("color: #FF4F00; background: #FFD0BB;")
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.setIcon(icon19)
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.setObjectName("pushButton_kasaHesabi_tarihlerArasiAramaYap")
        self.gridLayout_21.addWidget(self.pushButton_kasaHesabi_tarihlerArasiAramaYap, 4, 0, 1, 1)
        self.pushButton_kasaHesabi_onayla = QtWidgets.QPushButton(self.page_kasa_hesabi)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_kasaHesabi_onayla.setFont(font)
        self.pushButton_kasaHesabi_onayla.setStyleSheet(
            "color: green; background: #D7FAC6;")
        self.pushButton_kasaHesabi_onayla.setIcon(icon_tumVerileriGoster)
        self.pushButton_kasaHesabi_onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_kasaHesabi_onayla.setObjectName(
            "pushButton_kasaHesabi_onayla")
        self.gridLayout_21.addWidget(self.pushButton_kasaHesabi_onayla, 5, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_kasa_hesabi)
        self.page_seraAnasayfasi = QtWidgets.QWidget()
        self.page_seraAnasayfasi.setObjectName("page_seraAnasayfasi")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.page_seraAnasayfasi)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.toolButton_seraGelirSayfasinaGit = QtWidgets.QToolButton(self.page_seraAnasayfasi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_seraGelirSayfasinaGit.sizePolicy().hasHeightForWidth())
        self.toolButton_seraGelirSayfasinaGit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_seraGelirSayfasinaGit.setFont(font)
        self.toolButton_seraGelirSayfasinaGit.setStyleSheet("color: white; background: #17ace8;")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icons/005-income.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_seraGelirSayfasinaGit.setIcon(icon22)
        self.toolButton_seraGelirSayfasinaGit.setIconSize(QtCore.QSize(225, 225))
        self.toolButton_seraGelirSayfasinaGit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_seraGelirSayfasinaGit.setObjectName("toolButton_seraGelirSayfasinaGit")
        self.gridLayout_17.addWidget(self.toolButton_seraGelirSayfasinaGit, 0, 0, 1, 1)
        self.toolButton_seraGiderSayfasinaGit = QtWidgets.QToolButton(self.page_seraAnasayfasi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_seraGiderSayfasinaGit.sizePolicy().hasHeightForWidth())
        self.toolButton_seraGiderSayfasinaGit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_seraGiderSayfasinaGit.setFont(font)
        self.toolButton_seraGiderSayfasinaGit.setStyleSheet("color: white; background: #D63D19;")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icons/006-outcome.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_seraGiderSayfasinaGit.setIcon(icon23)
        self.toolButton_seraGiderSayfasinaGit.setIconSize(QtCore.QSize(225, 225))
        self.toolButton_seraGiderSayfasinaGit.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_seraGiderSayfasinaGit.setObjectName("toolButton_seraGiderSayfasinaGit")
        self.gridLayout_17.addWidget(self.toolButton_seraGiderSayfasinaGit, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_seraAnasayfasi)
        self.page_sera_gelir_ekle = QtWidgets.QWidget()
        self.page_sera_gelir_ekle.setObjectName("page_sera_gelir_ekle")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page_sera_gelir_ekle)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButton_seraGelir_islemGecmisiniGoruntule = QtWidgets.QPushButton(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seraGelir_islemGecmisiniGoruntule.setFont(font)
        self.pushButton_seraGelir_islemGecmisiniGoruntule.setStyleSheet("color: #844ED6; background: #FFD7A8;")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icons/history (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_seraGelir_islemGecmisiniGoruntule.setIcon(icon24)
        self.pushButton_seraGelir_islemGecmisiniGoruntule.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelir_islemGecmisiniGoruntule.setObjectName("pushButton_seraGelir_islemGecmisiniGoruntule")
        self.gridLayout_14.addWidget(self.pushButton_seraGelir_islemGecmisiniGoruntule, 4, 0, 1, 2)
        self.pushButton_seraGelir_onayla = QtWidgets.QPushButton(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seraGelir_onayla.setFont(font)
        self.pushButton_seraGelir_onayla.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_seraGelir_onayla.setIcon(icon13)
        self.pushButton_seraGelir_onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelir_onayla.setObjectName("pushButton_seraGelir_onayla")
        self.gridLayout_14.addWidget(self.pushButton_seraGelir_onayla, 5, 0, 1, 2)
        self.gridLayout_seraGelir_bilgiler = QtWidgets.QGridLayout()
        self.gridLayout_seraGelir_bilgiler.setObjectName("gridLayout_seraGelir_bilgiler")
        self.spinBox_seraGelir_adet = QtWidgets.QSpinBox(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_seraGelir_adet.setFont(font)
        self.spinBox_seraGelir_adet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_seraGelir_adet.setMaximum(1000000000)
        self.spinBox_seraGelir_adet.setObjectName("spinBox_seraGelir_adet")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.spinBox_seraGelir_adet, 4, 1, 1, 1)
        self.label_seraGelir_tarihSec = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelir_tarihSec.setFont(font)
        self.label_seraGelir_tarihSec.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_tarihSec.setObjectName("label_seraGelir_tarihSec")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_tarihSec, 1, 0, 1, 1)
        self.horizontalLayout_seraGelir_bilgiler_tarih = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelir_bilgiler_tarih.setObjectName("horizontalLayout_seraGelir_bilgiler_tarih")
        self.comboBox_seraGelir_tarihSec_gun = QtWidgets.QComboBox(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelir_tarihSec_gun.setFont(font)
        self.comboBox_seraGelir_tarihSec_gun.setObjectName("comboBox_seraGelir_tarihSec_gun")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.comboBox_seraGelir_tarihSec_gun.addItem("")
        self.horizontalLayout_seraGelir_bilgiler_tarih.addWidget(self.comboBox_seraGelir_tarihSec_gun)
        self.comboBox_seraGelir_tarihSec_ay = QtWidgets.QComboBox(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelir_tarihSec_ay.setFont(font)
        self.comboBox_seraGelir_tarihSec_ay.setObjectName("comboBox_seraGelir_tarihSec_ay")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.comboBox_seraGelir_tarihSec_ay.addItem("")
        self.horizontalLayout_seraGelir_bilgiler_tarih.addWidget(self.comboBox_seraGelir_tarihSec_ay)
        self.comboBox_seraGelir_tarihSec_yil = QtWidgets.QComboBox(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelir_tarihSec_yil.setFont(font)
        self.comboBox_seraGelir_tarihSec_yil.setObjectName("comboBox_seraGelir_tarihSec_yil")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.comboBox_seraGelir_tarihSec_yil.addItem("")
        self.horizontalLayout_seraGelir_bilgiler_tarih.addWidget(self.comboBox_seraGelir_tarihSec_yil)
        self.gridLayout_seraGelir_bilgiler.addLayout(self.horizontalLayout_seraGelir_bilgiler_tarih, 1, 1, 1, 1)
        self.horizontalLayout_seraGelir_bilgiler_maliyet = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelir_bilgiler_maliyet.setObjectName("horizontalLayout_seraGelir_bilgiler_maliyet")
        self.doublespinBox_seraGelir_maliyet = QtWidgets.QDoubleSpinBox(self.page_sera_gelir_ekle)
        #self.doublespinBox_seraGelir_maliyet.setFont(font)
        self.doublespinBox_seraGelir_maliyet.setDecimals(2)
        self.doublespinBox_seraGelir_maliyet.setMaximum(1000000000)
        self.doublespinBox_seraGelir_maliyet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doublespinBox_seraGelir_maliyet.setObjectName("doublespinBox_seraGelir_maliyet")
        self.horizontalLayout_seraGelir_bilgiler_maliyet.addWidget(self.doublespinBox_seraGelir_maliyet)
        self.label_seraGelir_maliyet_TL = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        self.label_seraGelir_maliyet_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGelir_maliyet_TL.setMaximumSize(QtCore.QSize(32, 393))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGelir_maliyet_TL.setFont(font)
        self.label_seraGelir_maliyet_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_maliyet_TL.setWordWrap(True)
        self.label_seraGelir_maliyet_TL.setObjectName("label_seraGelir_maliyet_TL")
        self.horizontalLayout_seraGelir_bilgiler_maliyet.addWidget(self.label_seraGelir_maliyet_TL)
        self.gridLayout_seraGelir_bilgiler.addLayout(self.horizontalLayout_seraGelir_bilgiler_maliyet, 3, 1, 1, 1)
        self.horizontalLayout_seraGelir_bilgiler_seraAdi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelir_bilgiler_seraAdi.setObjectName("horizontalLayout_seraGelir_bilgiler_seraAdi")
        self.comboBox_seraGelir_seralar = QtWidgets.QComboBox(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelir_seralar.setFont(font)
        self.comboBox_seraGelir_seralar.setObjectName("comboBox_seraGelir_seralar")
        self.comboBox_seraGelir_seralar.addItem("Sera Seçiniz")
        self.horizontalLayout_seraGelir_bilgiler_seraAdi.addWidget(self.comboBox_seraGelir_seralar)
        self.pushButton_seraGelir_seraEkle = QtWidgets.QPushButton(self.page_sera_gelir_ekle)
        self.pushButton_seraGelir_seraEkle.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelir_seraEkle.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelir_seraEkle.setStyleSheet("background: transparent;")
        self.pushButton_seraGelir_seraEkle.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("icons/sun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_seraGelir_seraEkle.setIcon(icon25)
        self.pushButton_seraGelir_seraEkle.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelir_seraEkle.setObjectName("pushButton_seraGelir_seraEkle")
        self.horizontalLayout_seraGelir_bilgiler_seraAdi.addWidget(self.pushButton_seraGelir_seraEkle)
        self.gridLayout_seraGelir_bilgiler.addLayout(self.horizontalLayout_seraGelir_bilgiler_seraAdi, 0, 1, 1, 1)
        self.label_seraGelir_urunAdi = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelir_urunAdi.setFont(font)
        self.label_seraGelir_urunAdi.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_urunAdi.setWordWrap(True)
        self.label_seraGelir_urunAdi.setObjectName("label_seraGelir_urunAdi")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_urunAdi, 2, 0, 1, 1)
        self.label_seraGelir_maliyet = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelir_maliyet.setFont(font)
        self.label_seraGelir_maliyet.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_maliyet.setWordWrap(True)
        self.label_seraGelir_maliyet.setObjectName("label_seraGelir_maliyet")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_maliyet, 3, 0, 1, 1)
        self.label_seraGelir_seraSec = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        self.label_seraGelir_seraSec.setMinimumSize(QtCore.QSize(0, 0))
        self.label_seraGelir_seraSec.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelir_seraSec.setFont(font)
        self.label_seraGelir_seraSec.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_seraSec.setObjectName("label_seraGelir_seraSec")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_seraSec, 0, 0, 1, 1)
        self.label_seraGelir_adet = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelir_adet.setFont(font)
        self.label_seraGelir_adet.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_adet.setWordWrap(True)
        self.label_seraGelir_adet.setObjectName("label_seraGelir_adet")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_adet, 4, 0, 1, 1)
        self.label_seraGelir_tutar = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGelir_tutar.setFont(font)
        self.label_seraGelir_tutar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_tutar.setObjectName("label_seraGelir_tutar")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_tutar, 5, 0, 1, 1)
        self.comboBox_seraGelir_urunAdi = QtWidgets.QComboBox(self.page_sera_gelir_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelir_urunAdi.setFont(font)
        self.comboBox_seraGelir_urunAdi.setObjectName("comboBox_seraGelir_urunAdi")
        self.comboBox_seraGelir_urunAdi.addItem("")
        self.gridLayout_seraGelir_bilgiler.addWidget(self.comboBox_seraGelir_urunAdi, 2, 1, 1, 1)
        self.horizontalLayout_seraGelir_bilgiler_bugununGeliri = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelir_bilgiler_bugununGeliri.setObjectName("horizontalLayout_seraGelir_bilgiler_bugununGeliri")
        self.label_seraGelir_bugununGeliriTutarSonuc = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        self.label_seraGelir_bugununGeliriTutarSonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_seraGelir_bugununGeliriTutarSonuc.setObjectName("label_seraGelir_bugununGeliriTutarSonuc")
        self.horizontalLayout_seraGelir_bilgiler_bugununGeliri.addWidget(self.label_seraGelir_bugununGeliriTutarSonuc)
        self.label_seraGelir_bugununGeliriTutarSonuc_TL = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_seraGelir_bugununGeliriTutarSonuc_TL.sizePolicy().hasHeightForWidth())
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setSizePolicy(sizePolicy)
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setMaximumSize(QtCore.QSize(32, 39))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setFont(font)
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setObjectName("label_seraGelir_bugununGeliriTutarSonuc_TL")
        self.horizontalLayout_seraGelir_bilgiler_bugununGeliri.addWidget(self.label_seraGelir_bugununGeliriTutarSonuc_TL)
        self.gridLayout_seraGelir_bilgiler.addLayout(self.horizontalLayout_seraGelir_bilgiler_bugununGeliri, 5, 1, 1, 1)
        # self.label_seraGelir_devir = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_seraGelir_devir.setFont(font)
        # self.label_seraGelir_devir.setStyleSheet("background: green; color: white;")
        # self.label_seraGelir_devir.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        # self.label_seraGelir_devir.setObjectName("label_seraGelir_devir")
        # self.gridLayout_seraGelir_bilgiler.addWidget(self.label_seraGelir_devir, 6, 0, 1, 1)
        # self.horizontalLayout_seraGelir_bilgiler_seraDevir = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_seraGelir_bilgiler_seraDevir.setObjectName("horizontalLayout_seraGelir_bilgiler_seraDevir")
        # self.label_seraGelir_devirSonuc = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        # self.label_seraGelir_devirSonuc.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_seraGelir_devirSonuc.setObjectName("label_seraGelir_devirSonuc")
        # self.horizontalLayout_seraGelir_bilgiler_seraDevir.addWidget(self.label_seraGelir_devirSonuc)
        # self.label_seraGelir_devirSonuc_TL = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_seraGelir_devirSonuc_TL.sizePolicy().hasHeightForWidth())
        # self.label_seraGelir_devirSonuc_TL.setSizePolicy(sizePolicy)
        # self.label_seraGelir_devirSonuc_TL.setMinimumSize(QtCore.QSize(32, 39))
        # self.label_seraGelir_devirSonuc_TL.setMaximumSize(QtCore.QSize(32, 39))
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_seraGelir_devirSonuc_TL.setFont(font)
        # self.label_seraGelir_devirSonuc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.label_seraGelir_devirSonuc_TL.setObjectName("label_seraGelir_devirSonuc_TL")
        # self.horizontalLayout_seraGelir_bilgiler_seraDevir.addWidget(self.label_seraGelir_devirSonuc_TL)
        # self.gridLayout_seraGelir_bilgiler.addLayout(self.horizontalLayout_seraGelir_bilgiler_seraDevir, 6, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_seraGelir_bilgiler, 1, 0, 2, 2)
        self.label_seraGelir = QtWidgets.QLabel(self.page_sera_gelir_ekle)
        self.label_seraGelir.setStyleSheet("background: #442837;")
        self.label_seraGelir.setWordWrap(True)
        self.label_seraGelir.setObjectName("label_seraGelir")
        self.gridLayout_14.addWidget(self.label_seraGelir, 0, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem5, 3, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_sera_gelir_ekle)
        self.page_sera_gelir_sonuc = QtWidgets.QWidget()
        self.page_sera_gelir_sonuc.setObjectName("page_sera_gelir_sonuc")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.page_sera_gelir_sonuc)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout_seraGelirSonuc_seraAdi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelirSonuc_seraAdi.setObjectName("horizontalLayout_seraGelirSonuc_seraAdi")
        self.label_seraGelirSonuc_seraSec = QtWidgets.QLabel(self.page_sera_gelir_sonuc)
        self.label_seraGelirSonuc_seraSec.setMinimumSize(QtCore.QSize(24, 40))
        self.label_seraGelirSonuc_seraSec.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelirSonuc_seraSec.setFont(font)
        self.label_seraGelirSonuc_seraSec.setWordWrap(True)
        self.label_seraGelirSonuc_seraSec.setObjectName("label_seraGelirSonuc_seraSec")
        self.horizontalLayout_seraGelirSonuc_seraAdi.addWidget(self.label_seraGelirSonuc_seraSec)
        self.comboBox_seraGelirSonuc_seralar = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_seralar.setFont(font)
        self.comboBox_seraGelirSonuc_seralar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_seraGelirSonuc_seralar.setObjectName("comboBox_seraGelirSonuc_seralar")
        self.comboBox_seraGelirSonuc_seralar.addItem("Hepsi")
        self.horizontalLayout_seraGelirSonuc_seraAdi.addWidget(self.comboBox_seraGelirSonuc_seralar)
        self.button_seraGelirSonuc_seraEkle = QtWidgets.QPushButton(self.page_sera_gelir_sonuc)
        self.button_seraGelirSonuc_seraEkle.setMinimumSize(QtCore.QSize(32, 32))
        self.button_seraGelirSonuc_seraEkle.setMaximumSize(QtCore.QSize(32, 32))
        self.button_seraGelirSonuc_seraEkle.setStyleSheet("background: transparent;")
        self.button_seraGelirSonuc_seraEkle.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("icons/sun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_seraGelirSonuc_seraEkle.setIcon(icon26)
        self.button_seraGelirSonuc_seraEkle.setIconSize(QtCore.QSize(32, 32))
        self.button_seraGelirSonuc_seraEkle.setObjectName("button_seraGelirSonuc_seraEkle")
        self.horizontalLayout_seraGelirSonuc_seraAdi.addWidget(self.button_seraGelirSonuc_seraEkle)
        self.gridLayout_15.addLayout(self.horizontalLayout_seraGelirSonuc_seraAdi, 1, 0, 1, 1)

        ###1313
        self.horizontalLayout_seraGelirSonuc_urunAdi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelirSonuc_urunAdi.setObjectName("horizontalLayout_seraGelirSonuc_urunAdi")
        self.label_seraGelirSonuc_urunSec = QtWidgets.QLabel(self.page_sera_gelir_sonuc)
        self.label_seraGelirSonuc_urunSec.setMinimumSize(QtCore.QSize(24, 40))
        self.label_seraGelirSonuc_urunSec.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGelirSonuc_urunSec.setFont(font)
        self.label_seraGelirSonuc_urunSec.setWordWrap(True)
        self.label_seraGelirSonuc_urunSec.setObjectName("label_seraGelirSonuc_urunSec")
        self.horizontalLayout_seraGelirSonuc_urunAdi.addWidget(self.label_seraGelirSonuc_urunSec)
        self.comboBox_seraGelirSonuc_urunler = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_urunler.setFont(font)
        self.comboBox_seraGelirSonuc_urunler.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_seraGelirSonuc_urunler.setObjectName("comboBox_seraGelirSonuc_urunler")
        self.comboBox_seraGelirSonuc_urunler.addItem("Hepsi")
        ################################################################################################################
        ## SERA GELİR DURUMUNU GÖRÜNTÜLE SAYFASINA SERALAR DOSYASINDAN EKLEME YAPILDI
        listFor_comboBox_seraGelirSonuc_urunler = []
        self.file_comboBox_seraGelirSonuc_urunler = open("datastore/urunler.dat", "r", encoding="UTF-8")
        for i in self.file_comboBox_seraGelirSonuc_urunler:
            listFor_comboBox_seraGelirSonuc_urunler.append(i.strip())
        sorted_listFor_comboBox_seraGelirSonuc_urunler = sorted(listFor_comboBox_seraGelirSonuc_urunler, key=str.lower)
        for i in range(len(sorted_listFor_comboBox_seraGelirSonuc_urunler)):
            self.comboBox_seraGelirSonuc_urunler.addItem(sorted_listFor_comboBox_seraGelirSonuc_urunler[i])
        ################################################################################################################
        self.horizontalLayout_seraGelirSonuc_urunAdi.addWidget(self.comboBox_seraGelirSonuc_urunler)
        self.gridLayout_15.addLayout(self.horizontalLayout_seraGelirSonuc_urunAdi, 2, 0, 1, 1)

        self.tableView_seraGelirSonuc = QtWidgets.QTableView(self.page_sera_gelir_sonuc)
        self.tableView_seraGelirSonuc.setObjectName("tableView_seraGelirSonuc")
        self.gridLayout_15.addWidget(self.tableView_seraGelirSonuc, 3, 0, 1, 1)

        #123123
        self.horizontalLayout_seraGelirSonuc_tarihAraligi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelirSonuc_tarihAraligi.setObjectName("horizontalLayout_seraGelirSonuc_tarihAraligi")
        self.horizontalLayout_seraGelirSonuc_baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelirSonuc_baslangicTarihi.setObjectName(
            "horizontalLayout_seraGelirSonuc_baslangicTarihi")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setFont(font)
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setObjectName("comboBox_seraGelirSonuc_baslangicTarihiGun")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.addItem("")
        self.horizontalLayout_seraGelirSonuc_baslangicTarihi.addWidget(self.comboBox_seraGelirSonuc_baslangicTarihiGun)
        self.comboBox_seraGelirSonuc_baslangicTarihiAy = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setFont(font)
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setObjectName("comboBox_seraGelirSonuc_baslangicTarihiAy")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.addItem("")
        self.horizontalLayout_seraGelirSonuc_baslangicTarihi.addWidget(self.comboBox_seraGelirSonuc_baslangicTarihiAy)
        self.comboBox_seraGelirSonuc_baslangicTarihiYil = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setFont(font)
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setObjectName("comboBox_seraGelirSonuc_baslangicTarihiYil")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.addItem("")
        self.horizontalLayout_seraGelirSonuc_baslangicTarihi.addWidget(self.comboBox_seraGelirSonuc_baslangicTarihiYil)
        self.horizontalLayout_seraGelirSonuc_tarihAraligi.addLayout(
            self.horizontalLayout_seraGelirSonuc_baslangicTarihi)
        self.line_seraGelirSonuc_tarihlerArasiAyrac = QtWidgets.QFrame(self.page_sera_gelir_sonuc)
        self.line_seraGelirSonuc_tarihlerArasiAyrac.setStyleSheet("background: black;")
        self.line_seraGelirSonuc_tarihlerArasiAyrac.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_seraGelirSonuc_tarihlerArasiAyrac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_seraGelirSonuc_tarihlerArasiAyrac.setObjectName("line_seraGelirSonuc_tarihlerArasiAyrac")
        self.horizontalLayout_seraGelirSonuc_tarihAraligi.addWidget(self.line_seraGelirSonuc_tarihlerArasiAyrac)
        self.horizontalLayout_seraGelirSonuc_bitisTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGelirSonuc_bitisTarihi.setObjectName("horizontalLayout_seraGelirSonuc_bitisTarihi")
        self.comboBox_seraGelirSonuc_bitisTarihiGun = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setFont(font)
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setObjectName("comboBox_seraGelirSonuc_bitisTarihiGun")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiGun.addItem("")
        self.horizontalLayout_seraGelirSonuc_bitisTarihi.addWidget(self.comboBox_seraGelirSonuc_bitisTarihiGun)
        self.comboBox_seraGelirSonuc_bitisTarihiAy = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setFont(font)
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setObjectName("comboBox_seraGelirSonuc_bitisTarihiAy")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiAy.addItem("")
        self.horizontalLayout_seraGelirSonuc_bitisTarihi.addWidget(self.comboBox_seraGelirSonuc_bitisTarihiAy)
        self.comboBox_seraGelirSonuc_bitisTarihiYil = QtWidgets.QComboBox(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setFont(font)
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setObjectName("comboBox_seraGelirSonuc_bitisTarihiYil")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGelirSonuc_bitisTarihiYil.addItem("")
        self.horizontalLayout_seraGelirSonuc_bitisTarihi.addWidget(self.comboBox_seraGelirSonuc_bitisTarihiYil)
        self.horizontalLayout_seraGelirSonuc_tarihAraligi.addLayout(self.horizontalLayout_seraGelirSonuc_bitisTarihi)
        self.gridLayout_15.addLayout(self.horizontalLayout_seraGelirSonuc_tarihAraligi, 4, 0, 1, 1)
        self.label_seraGelirSonuc = QtWidgets.QLabel(self.page_sera_gelir_sonuc)
        self.label_seraGelirSonuc.setStyleSheet("background: #442837;")
        self.label_seraGelirSonuc.setWordWrap(True)
        self.label_seraGelirSonuc.setObjectName("label_seraGelirSonuc")
        self.gridLayout_15.addWidget(self.label_seraGelirSonuc, 0, 0, 1, 1)
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap = QtWidgets.QPushButton(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        icon_seraGelirSonucIcon = QtGui.QIcon()
        icon_seraGelirSonucIcon.addPixmap(QtGui.QPixmap("icons/009-growth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.setFont(font)
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.setStyleSheet("color: #F3E8E8; background: #3095EE;")
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.setIcon(icon_seraGelirSonucIcon)
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.setObjectName("pushButton_seraGelirSonuc_tarihlerArasiAramaYap")
        self.gridLayout_15.addWidget(self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap, 5, 0, 1, 1)
        self.pushButton_seraGelirSonuc_onayla = QtWidgets.QPushButton(self.page_sera_gelir_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seraGelirSonuc_onayla.setFont(font)
        self.pushButton_seraGelirSonuc_onayla.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_seraGelirSonuc_onayla.setIcon(icon_tumVerileriGoster)
        self.pushButton_seraGelirSonuc_onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGelirSonuc_onayla.setObjectName(
            "pushButton_seraGelirSonuc_onayla")
        self.gridLayout_15.addWidget(self.pushButton_seraGelirSonuc_onayla, 6, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_sera_gelir_sonuc)
        self.page_sera_gider_ekle = QtWidgets.QWidget()
        self.page_sera_gider_ekle.setObjectName("page_sera_gider_ekle")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.page_sera_gider_ekle)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButton_seraGider_islemGecmisiniGoruntule = QtWidgets.QPushButton(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seraGider_islemGecmisiniGoruntule.setFont(font)
        self.pushButton_seraGider_islemGecmisiniGoruntule.setStyleSheet("color: #844ED6; background: #FFD7A8;")
        self.pushButton_seraGider_islemGecmisiniGoruntule.setIcon(icon24)
        self.pushButton_seraGider_islemGecmisiniGoruntule.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGider_islemGecmisiniGoruntule.setObjectName("pushButton_seraGider_islemGecmisiniGoruntule")
        self.gridLayout_19.addWidget(self.pushButton_seraGider_islemGecmisiniGoruntule, 3, 0, 1, 1)
        self.pushButton_seraGider_onayla = QtWidgets.QPushButton(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seraGider_onayla.setFont(font)
        self.pushButton_seraGider_onayla.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_seraGider_onayla.setIcon(icon13)
        self.pushButton_seraGider_onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGider_onayla.setObjectName("pushButton_seraGider_onayla")
        self.gridLayout_19.addWidget(self.pushButton_seraGider_onayla, 4, 0, 1, 1)
        self.label_seraGider = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider.setStyleSheet("background: #442837;")
        self.label_seraGider.setWordWrap(True)
        self.label_seraGider.setObjectName("label_seraGider")
        self.gridLayout_19.addWidget(self.label_seraGider, 0, 0, 1, 1)
        self.gridLayout_seraGider_bilgiler = QtWidgets.QGridLayout()
        self.gridLayout_seraGider_bilgiler.setObjectName("gridLayout_seraGider_bilgiler")
        self.horizontalLayout_seraGider_diger = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_diger.setObjectName("horizontalLayout_seraGider_diger")
        self.doubleSpinBox_seraGider_digerGiderler = QtWidgets.QDoubleSpinBox(self.page_sera_gider_ekle)
        #self.doubleSpinBox_seraGider_digerGiderler.setFont(font)
        self.doubleSpinBox_seraGider_digerGiderler.setDecimals(2)
        self.doubleSpinBox_seraGider_digerGiderler.setMaximum(1000000000)
        self.doubleSpinBox_seraGider_digerGiderler.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_seraGider_digerGiderler.setObjectName("doubleSpinBox_seraGider_digerGiderler")
        self.horizontalLayout_seraGider_diger.addWidget(self.doubleSpinBox_seraGider_digerGiderler)
        self.label_seraGider_digerGiderler_TL = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_digerGiderler_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGider_digerGiderler_TL.setMaximumSize(QtCore.QSize(32, 393))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGider_digerGiderler_TL.setFont(font)
        self.label_seraGider_digerGiderler_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGider_digerGiderler_TL.setWordWrap(True)
        self.label_seraGider_digerGiderler_TL.setObjectName("label_seraGider_digerGiderler_TL")
        self.horizontalLayout_seraGider_diger.addWidget(self.label_seraGider_digerGiderler_TL)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_diger, 5, 1, 1, 1)
        self.label_seraGider_aciklama = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_aciklama.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_aciklama.setObjectName("label_seraGider_aciklama")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_aciklama, 6, 0, 1, 1)
        self.label_seraGider_tarihSec = QtWidgets.QLabel(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGider_tarihSec.setFont(font)
        self.label_seraGider_tarihSec.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_tarihSec.setObjectName("label_seraGider_tarihSec")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_tarihSec, 1, 0, 1, 1)
        self.horizontalLayout_seraGider_tarihSec = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_tarihSec.setObjectName("horizontalLayout_seraGider_tarihSec")
        self.comboBox_seraGider_tarihSec_gun = QtWidgets.QComboBox(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGider_tarihSec_gun.setFont(font)
        self.comboBox_seraGider_tarihSec_gun.setObjectName("comboBox_seraGider_tarihSec_gun")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.comboBox_seraGider_tarihSec_gun.addItem("")
        self.horizontalLayout_seraGider_tarihSec.addWidget(self.comboBox_seraGider_tarihSec_gun)
        self.comboBox_seraGider_tarihSec_ay = QtWidgets.QComboBox(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGider_tarihSec_ay.setFont(font)
        self.comboBox_seraGider_tarihSec_ay.setObjectName("comboBox_seraGider_tarihSec_ay")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.comboBox_seraGider_tarihSec_ay.addItem("")
        self.horizontalLayout_seraGider_tarihSec.addWidget(self.comboBox_seraGider_tarihSec_ay)
        self.comboBox_seraGider_tarihSec_yil = QtWidgets.QComboBox(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGider_tarihSec_yil.setFont(font)
        self.comboBox_seraGider_tarihSec_yil.setObjectName("comboBox_seraGider_tarihSec_yil")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.comboBox_seraGider_tarihSec_yil.addItem("")
        self.horizontalLayout_seraGider_tarihSec.addWidget(self.comboBox_seraGider_tarihSec_yil)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_tarihSec, 1, 1, 1, 1)
        self.horizontalLayout_seraGider_seraSec = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_seraSec.setObjectName("horizontalLayout_seraGider_seraSec")
        self.comboBox_seraGider_seralar = QtWidgets.QComboBox(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGider_seralar.setFont(font)
        self.comboBox_seraGider_seralar.setObjectName("comboBox_seraGider_seralar")
        self.comboBox_seraGelirSonuc_seralar.addItem("Sera Seçiniz")
        self.horizontalLayout_seraGider_seraSec.addWidget(self.comboBox_seraGider_seralar)
        self.pushButton_seraGider_seraEkle = QtWidgets.QPushButton(self.page_sera_gider_ekle)
        self.pushButton_seraGider_seraEkle.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButton_seraGider_seraEkle.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_seraGider_seraEkle.setStyleSheet("background: transparent;")
        self.pushButton_seraGider_seraEkle.setText("")
        self.pushButton_seraGider_seraEkle.setIcon(icon25)
        self.pushButton_seraGider_seraEkle.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGider_seraEkle.setObjectName("pushButton_seraGider_seraEkle")
        self.horizontalLayout_seraGider_seraSec.addWidget(self.pushButton_seraGider_seraEkle)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_seraSec, 0, 1, 1, 1)
        self.horizontalLayout_seraGider_bugununGideri = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_bugununGideri.setObjectName("horizontalLayout_seraGider_bugununGideri")
        self.label_seraGider_bugununToplamGideri_sonuc = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_bugununToplamGideri_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_seraGider_bugununToplamGideri_sonuc.setObjectName("label_seraGider_bugununToplamGideri_sonuc")
        self.horizontalLayout_seraGider_bugununGideri.addWidget(self.label_seraGider_bugununToplamGideri_sonuc)
        self.label_seraGider_bugununToplamGideri_sonuc_TL = QtWidgets.QLabel(self.page_sera_gider_ekle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_seraGider_bugununToplamGideri_sonuc_TL.sizePolicy().hasHeightForWidth())
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setSizePolicy(sizePolicy)
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setMaximumSize(QtCore.QSize(32, 39))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setFont(font)
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setObjectName("label_seraGider_bugununToplamGideri_sonuc_TL")
        self.horizontalLayout_seraGider_bugununGideri.addWidget(self.label_seraGider_bugununToplamGideri_sonuc_TL)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_bugununGideri, 7, 1, 1, 1)
        self.label_seraGider_seraSec = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_seraSec.setMinimumSize(QtCore.QSize(0, 0))
        self.label_seraGider_seraSec.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGider_seraSec.setFont(font)
        self.label_seraGider_seraSec.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_seraSec.setObjectName("label_seraGider_seraSec")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_seraSec, 0, 0, 1, 1)
        self.label_seraGider_yemekGideri = QtWidgets.QLabel(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGider_yemekGideri.setFont(font)
        self.label_seraGider_yemekGideri.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_yemekGideri.setWordWrap(True)
        self.label_seraGider_yemekGideri.setObjectName("label_seraGider_yemekGideri")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_yemekGideri, 3, 0, 1, 1)
        self.label_seraGider_mazotGideri = QtWidgets.QLabel(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGider_mazotGideri.setFont(font)
        self.label_seraGider_mazotGideri.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_mazotGideri.setWordWrap(True)
        self.label_seraGider_mazotGideri.setObjectName("label_seraGider_mazotGideri")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_mazotGideri, 4, 0, 1, 1)
        self.label_seraGider_elemanGideri = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_elemanGideri.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGider_elemanGideri.setFont(font)
        self.label_seraGider_elemanGideri.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_elemanGideri.setWordWrap(True)
        self.label_seraGider_elemanGideri.setObjectName("label_seraGider_elemanGideri")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_elemanGideri, 2, 0, 1, 1)
        self.horizontalLayout_seraGider_yemek = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_yemek.setObjectName("horizontalLayout_seraGider_yemek")
        self.doubleSpinBox_seraGider_yemekGideri = QtWidgets.QDoubleSpinBox(self.page_sera_gider_ekle)
        #self.doubleSpinBox_seraGider_yemekGideri.setFont(font)
        self.doubleSpinBox_seraGider_yemekGideri.setDecimals(2)
        self.doubleSpinBox_seraGider_yemekGideri.setMaximum(1000000000)
        self.doubleSpinBox_seraGider_yemekGideri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_seraGider_yemekGideri.setObjectName("doubleSpinBox_seraGider_yemekGideri")
        self.horizontalLayout_seraGider_yemek.addWidget(self.doubleSpinBox_seraGider_yemekGideri)
        self.label_seraGider_yemekGideri_TL = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_yemekGideri_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGider_yemekGideri_TL.setMaximumSize(QtCore.QSize(32, 393))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGider_yemekGideri_TL.setFont(font)
        self.label_seraGider_yemekGideri_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGider_yemekGideri_TL.setWordWrap(True)
        self.label_seraGider_yemekGideri_TL.setObjectName("label_seraGider_yemekGideri_TL")
        self.horizontalLayout_seraGider_yemek.addWidget(self.label_seraGider_yemekGideri_TL)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_yemek, 3, 1, 1, 1)
        self.label_seraGider_bugunToplamGider = QtWidgets.QLabel(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGider_bugunToplamGider.setFont(font)
        self.label_seraGider_bugunToplamGider.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_bugunToplamGider.setObjectName("label_seraGider_bugunToplamGider")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_bugunToplamGider, 7, 0, 1, 1)
        self.horizontalLayout_seraGider_mazot = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_mazot.setObjectName("horizontalLayout_seraGider_mazot")
        self.doubleSpinBox_seraGider_mazotGideri = QtWidgets.QDoubleSpinBox(self.page_sera_gider_ekle)
        #self.doubleSpinBox_seraGider_mazotGideri.setFont(font)
        self.doubleSpinBox_seraGider_mazotGideri.setDecimals(2)
        self.doubleSpinBox_seraGider_mazotGideri.setMaximum(1000000000)
        self.doubleSpinBox_seraGider_mazotGideri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_seraGider_mazotGideri.setObjectName("doubleSpinBox_seraGider_mazotGideri")
        self.horizontalLayout_seraGider_mazot.addWidget(self.doubleSpinBox_seraGider_mazotGideri)
        self.label_seraGider_mazotGideri_TL = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_mazotGideri_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGider_mazotGideri_TL.setMaximumSize(QtCore.QSize(32, 393))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGider_mazotGideri_TL.setFont(font)
        self.label_seraGider_mazotGideri_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGider_mazotGideri_TL.setWordWrap(True)
        self.label_seraGider_mazotGideri_TL.setObjectName("label_seraGider_mazotGideri_TL")
        self.horizontalLayout_seraGider_mazot.addWidget(self.label_seraGider_mazotGideri_TL)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_mazot, 4, 1, 1, 1)
        self.horizontalLayout_seraGider_eleman = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGider_eleman.setObjectName("horizontalLayout_seraGider_eleman")
        self.doubleSpinBox_seraGider_elemanGideri = QtWidgets.QDoubleSpinBox(self.page_sera_gider_ekle)
        # self.doubleSpinBox_seraGider_elemanGideri.setFont(font)
        self.doubleSpinBox_seraGider_elemanGideri.setDecimals(2)
        self.doubleSpinBox_seraGider_elemanGideri.setMaximum(1000000000)
        self.doubleSpinBox_seraGider_elemanGideri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_seraGider_elemanGideri.setObjectName("doubleSpinBox_seraGider_elemanGideri")
        self.horizontalLayout_seraGider_eleman.addWidget(self.doubleSpinBox_seraGider_elemanGideri)
        self.label_seraGider_elemanGideri_TL = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_elemanGideri_TL.setMinimumSize(QtCore.QSize(32, 39))
        self.label_seraGider_elemanGideri_TL.setMaximumSize(QtCore.QSize(32, 393))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_seraGider_elemanGideri_TL.setFont(font)
        self.label_seraGider_elemanGideri_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_seraGider_elemanGideri_TL.setWordWrap(True)
        self.label_seraGider_elemanGideri_TL.setObjectName("label_seraGider_elemanGideri_TL")
        self.horizontalLayout_seraGider_eleman.addWidget(self.label_seraGider_elemanGideri_TL)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_eleman, 2, 1, 1, 1)
        self.horizontalLayout_aciklama = QtWidgets.QHBoxLayout()
        self.horizontalLayout_aciklama.setObjectName("horizontalLayout_aciklama")
        self.lineEdit_seraGider_aciklama = QtWidgets.QLineEdit(self.page_sera_gider_ekle)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_seraGider_aciklama.setFont(font)
        self.lineEdit_seraGider_aciklama.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_seraGider_aciklama.setObjectName("lineEdit_seraGider_aciklama")
        self.horizontalLayout_aciklama.addWidget(self.lineEdit_seraGider_aciklama)
        self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_aciklama, 6, 1, 1, 1)
        self.label_seraGider_digerGiderler = QtWidgets.QLabel(self.page_sera_gider_ekle)
        self.label_seraGider_digerGiderler.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_seraGider_digerGiderler.setObjectName("label_seraGider_digerGiderler")
        self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_digerGiderler, 5, 0, 1, 1)
        # self.label_seraGider_devir = QtWidgets.QLabel(self.page_sera_gider_ekle)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_seraGider_devir.setFont(font)
        # self.label_seraGider_devir.setAutoFillBackground(False)
        # self.label_seraGider_devir.setStyleSheet("background: red; color: white;")
        # self.label_seraGider_devir.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        # self.label_seraGider_devir.setObjectName("label_seraGider_devir")
        # self.gridLayout_seraGider_bilgiler.addWidget(self.label_seraGider_devir, 8, 0, 1, 1)
        # self.horizontalLayout_seraGider_seraDevir = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_seraGider_seraDevir.setObjectName("horizontalLayout_seraGider_seraDevir")
        # self.label_seraGider_devir_sonuc = QtWidgets.QLabel(self.page_sera_gider_ekle)
        # self.label_seraGider_devir_sonuc.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_seraGider_devir_sonuc.setObjectName("label_seraGider_devir_sonuc")
        # self.horizontalLayout_seraGider_seraDevir.addWidget(self.label_seraGider_devir_sonuc)
        # self.label_seraGider_devir_sonuc_TL = QtWidgets.QLabel(self.page_sera_gider_ekle)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.label_seraGider_devir_sonuc_TL.sizePolicy().hasHeightForWidth())
        # self.label_seraGider_devir_sonuc_TL.setSizePolicy(sizePolicy)
        # self.label_seraGider_devir_sonuc_TL.setMinimumSize(QtCore.QSize(32, 39))
        # self.label_seraGider_devir_sonuc_TL.setMaximumSize(QtCore.QSize(32, 39))
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_seraGider_devir_sonuc_TL.setFont(font)
        # self.label_seraGider_devir_sonuc_TL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.label_seraGider_devir_sonuc_TL.setObjectName("label_seraGider_devir_sonuc_TL")
        # self.horizontalLayout_seraGider_seraDevir.addWidget(self.label_seraGider_devir_sonuc_TL)
        # self.gridLayout_seraGider_bilgiler.addLayout(self.horizontalLayout_seraGider_seraDevir, 8, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_seraGider_bilgiler, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem6, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_sera_gider_ekle)
        self.page_sera_gider_sonuc = QtWidgets.QWidget()
        self.page_sera_gider_sonuc.setObjectName("page_sera_gider_sonuc")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.page_sera_gider_sonuc)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_seraGiderSonuc = QtWidgets.QLabel(self.page_sera_gider_sonuc)
        self.label_seraGiderSonuc.setStyleSheet("background: #442837;")
        self.label_seraGiderSonuc.setWordWrap(True)
        self.label_seraGiderSonuc.setObjectName("label_seraGiderSonuc")
        self.gridLayout_20.addWidget(self.label_seraGiderSonuc, 0, 0, 1, 1)
        self.horizontalLayout_seraGiderSonuc_seraAdi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGiderSonuc_seraAdi.setObjectName("horizontalLayout_seraGiderSonuc_seraAdi")
        self.label_seraGiderSonuc_seraSec = QtWidgets.QLabel(self.page_sera_gider_sonuc)
        self.label_seraGiderSonuc_seraSec.setMinimumSize(QtCore.QSize(24, 40))
        self.label_seraGiderSonuc_seraSec.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_seraGiderSonuc_seraSec.setFont(font)
        self.label_seraGiderSonuc_seraSec.setWordWrap(True)
        self.label_seraGiderSonuc_seraSec.setObjectName("label_seraGiderSonuc_seraSec")
        self.horizontalLayout_seraGiderSonuc_seraAdi.addWidget(self.label_seraGiderSonuc_seraSec)
        self.comboBox_seraGiderSonuc_seralar = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_seralar.setFont(font)
        self.comboBox_seraGiderSonuc_seralar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_seraGiderSonuc_seralar.setObjectName("comboBox_seraGiderSonuc_seralar")
        self.comboBox_seraGelirSonuc_seralar.addItem("Hepsi")
        self.horizontalLayout_seraGiderSonuc_seraAdi.addWidget(self.comboBox_seraGiderSonuc_seralar)
        self.button_seraGiderSonuc_seraEkle = QtWidgets.QPushButton(self.page_sera_gider_sonuc)
        self.button_seraGiderSonuc_seraEkle.setMinimumSize(QtCore.QSize(32, 32))
        self.button_seraGiderSonuc_seraEkle.setMaximumSize(QtCore.QSize(32, 32))
        self.button_seraGiderSonuc_seraEkle.setStyleSheet("background: transparent;")
        self.button_seraGiderSonuc_seraEkle.setText("")
        self.button_seraGiderSonuc_seraEkle.setIcon(icon26)
        self.button_seraGiderSonuc_seraEkle.setIconSize(QtCore.QSize(32, 32))
        self.button_seraGiderSonuc_seraEkle.setObjectName("button_seraGiderSonuc_seraEkle")
        self.horizontalLayout_seraGiderSonuc_seraAdi.addWidget(self.button_seraGiderSonuc_seraEkle)
        self.gridLayout_20.addLayout(self.horizontalLayout_seraGiderSonuc_seraAdi, 1, 0, 1, 1)
        self.tableView_seraGiderSonuc = QtWidgets.QTableView(self.page_sera_gider_sonuc)
        self.tableView_seraGiderSonuc.setObjectName("tableView_seraGiderSonuc")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableView_seraGiderSonuc.setFont(font)
        self.gridLayout_20.addWidget(self.tableView_seraGiderSonuc, 2, 0, 1, 1)
        self.horizontalLayout_seraGiderSonuc_tarihAraligi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGiderSonuc_tarihAraligi.setObjectName("horizontalLayout_seraGiderSonuc_tarihAraligi")
        self.horizontalLayout_seraGiderSonuc_baslangicTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGiderSonuc_baslangicTarihi.setObjectName(
            "horizontalLayout_seraGiderSonuc_baslangicTarihi")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setFont(font)
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setObjectName("comboBox_seraGiderSonuc_baslangicTarihiGun")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.addItem("")
        self.horizontalLayout_seraGiderSonuc_baslangicTarihi.addWidget(self.comboBox_seraGiderSonuc_baslangicTarihiGun)
        self.comboBox_seraGiderSonuc_baslangicTarihiAy = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setFont(font)
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setObjectName("comboBox_seraGiderSonuc_baslangicTarihiAy")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.addItem("")
        self.horizontalLayout_seraGiderSonuc_baslangicTarihi.addWidget(self.comboBox_seraGiderSonuc_baslangicTarihiAy)
        self.comboBox_seraGiderSonuc_baslangicTarihiYil = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setFont(font)
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setObjectName("comboBox_seraGiderSonuc_baslangicTarihiYil")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.addItem("")
        self.horizontalLayout_seraGiderSonuc_baslangicTarihi.addWidget(self.comboBox_seraGiderSonuc_baslangicTarihiYil)
        self.horizontalLayout_seraGiderSonuc_tarihAraligi.addLayout(
            self.horizontalLayout_seraGiderSonuc_baslangicTarihi)
        self.line_seraGiderSonuc_tarihlerArasiAyrac = QtWidgets.QFrame(self.page_sera_gider_sonuc)
        self.line_seraGiderSonuc_tarihlerArasiAyrac.setStyleSheet("background: black;")
        self.line_seraGiderSonuc_tarihlerArasiAyrac.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_seraGiderSonuc_tarihlerArasiAyrac.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_seraGiderSonuc_tarihlerArasiAyrac.setObjectName("line_seraGiderSonuc_tarihlerArasiAyrac")
        self.horizontalLayout_seraGiderSonuc_tarihAraligi.addWidget(self.line_seraGiderSonuc_tarihlerArasiAyrac)
        self.horizontalLayout_seraGiderSonuc_bitisTarihi = QtWidgets.QHBoxLayout()
        self.horizontalLayout_seraGiderSonuc_bitisTarihi.setObjectName("horizontalLayout_seraGiderSonuc_bitisTarihi")
        self.comboBox_seraGiderSonuc_bitisTarihiGun = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setFont(font)
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setObjectName("comboBox_seraGiderSonuc_bitisTarihiGun")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiGun.addItem("")
        self.horizontalLayout_seraGiderSonuc_bitisTarihi.addWidget(self.comboBox_seraGiderSonuc_bitisTarihiGun)
        self.comboBox_seraGiderSonuc_bitisTarihiAy = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setFont(font)
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setObjectName("comboBox_seraGiderSonuc_bitisTarihiAy")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiAy.addItem("")
        self.horizontalLayout_seraGiderSonuc_bitisTarihi.addWidget(self.comboBox_seraGiderSonuc_bitisTarihiAy)
        self.comboBox_seraGiderSonuc_bitisTarihiYil = QtWidgets.QComboBox(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setFont(font)
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setObjectName("comboBox_seraGiderSonuc_bitisTarihiYil")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.comboBox_seraGiderSonuc_bitisTarihiYil.addItem("")
        self.horizontalLayout_seraGiderSonuc_bitisTarihi.addWidget(self.comboBox_seraGiderSonuc_bitisTarihiYil)
        self.horizontalLayout_seraGiderSonuc_tarihAraligi.addLayout(self.horizontalLayout_seraGiderSonuc_bitisTarihi)
        self.gridLayout_20.addLayout(self.horizontalLayout_seraGiderSonuc_tarihAraligi, 3, 0, 1, 1)
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap = QtWidgets.QPushButton(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        icon_seraGiderSonucIcon = QtGui.QIcon()
        icon_seraGiderSonucIcon.addPixmap(QtGui.QPixmap("icons/010-loss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.setFont(font)
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.setStyleSheet("color: #F3E8E8; background: #E83D3D;")
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.setIcon(icon_seraGiderSonucIcon)
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.setObjectName("pushButton_seraGiderSonuc_tarihlerArasiAramaYap")
        self.gridLayout_20.addWidget(self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap, 4, 0, 1, 1)
        self.pushButton_seraGiderSonuc_onayla = QtWidgets.QPushButton(self.page_sera_gider_sonuc)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_seraGiderSonuc_onayla.setFont(font)
        self.pushButton_seraGiderSonuc_onayla.setStyleSheet("color: green; background: #D7FAC6;")
        self.pushButton_seraGiderSonuc_onayla.setIcon(icon_tumVerileriGoster)
        self.pushButton_seraGiderSonuc_onayla.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_seraGiderSonuc_onayla.setObjectName(
            "pushButton_seraGiderSonuc_onayla")
        self.gridLayout_20.addWidget(self.pushButton_seraGiderSonuc_onayla, 5, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_sera_gider_sonuc)
        self.gridLayout_11.addWidget(self.stackedWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuMenuAyarlar.setObjectName("menuMenuAyarlar")
        self.menuGorunum = QtWidgets.QMenu(self.menubar)
        self.menuGorunum.setObjectName("menuGorunum")
        # self.menuTemaSec = QtWidgets.QMenu(self.menuGorunum)
        # self.menuTemaSec.setObjectName("menuTemaSec")
        self.menuYardim = QtWidgets.QMenu(self.menubar)
        self.menuYardim.setObjectName("menuYardim")
        self.menuContact = QtWidgets.QMenu(self.menuYardim)
        self.menuContact.setObjectName("menuContact")
        self.menuHakkinda = QtWidgets.QMenu(self.menuYardim)
        self.menuHakkinda.setObjectName("menuHakkinda")
        MainWindow.setMenuBar(self.menubar)
        self.actionMail = QtWidgets.QAction(MainWindow)
        self.actionMail.setObjectName("actionMail")
        self.actionWebsite = QtWidgets.QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")
        self.actionm_fatihtuz_gmail_com = QtWidgets.QAction(MainWindow)
        self.actionm_fatihtuz_gmail_com.setObjectName("actionm_fatihtuz_gmail_com")
        self.action_M_Fatih_TUZ_2020 = QtWidgets.QAction(MainWindow)
        self.action_M_Fatih_TUZ_2020.setObjectName("action_M_Fatih_TUZ_2020")
        self.action_k = QtWidgets.QAction(MainWindow)
        self.action_k.setObjectName("action_k")
        self.actionKes = QtWidgets.QAction(MainWindow)
        self.actionKes.setShortcutVisibleInContextMenu(False)
        # self.actionKes.setObjectName("actionKes")
        # self.actionKopyala = QtWidgets.QAction(MainWindow)
        # self.actionKopyala.setObjectName("actionKopyala")
        # self.actionYapistir = QtWidgets.QAction(MainWindow)
        # self.actionYapistir.setObjectName("actionYapistir")
        self.actionCikis = QtWidgets.QAction(MainWindow)
        self.actionCikis.setObjectName("actionCikis")
        # self.actionMenuCubugunuGizle = QtWidgets.QAction(MainWindow)
        # self.actionMenuCubugunuGizle.setCheckable(True)
        # self.actionMenuCubugunuGizle.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        # self.actionMenuCubugunuGizle.setFont(font)
        # self.actionMenuCubugunuGizle.setObjectName("actionMenuCubugunuGizle")
        self.actionCopyright = QtWidgets.QAction(MainWindow)
        self.actionCopyright.setObjectName("actionCopyright")
        self.actionKullanimKilavuzu = QtWidgets.QAction(MainWindow)
        self.actionKullanimKilavuzu.setObjectName("actionKullanimKilavuzu")
        self.actionHerIslemdeOnaySor = QtWidgets.QAction(MainWindow)
        self.actionHerIslemdeOnaySor.setCheckable(True)
        self.actionHerIslemdeOnaySor.setChecked(True)
        self.actionHerIslemdeOnaySor.setObjectName("actionHerIslemdeOnaySor")
        self.menuMenuAyarlar.addAction(self.actionHerIslemdeOnaySor)
        # self.menuMenuAyarlar.addAction(self.actionMenuCubugunuGizle)
        # self.menuMenuAyarlar.addSeparator()
        # self.menuMenuAyarlar.addAction(self.actionKes)
        # self.menuMenuAyarlar.addAction(self.actionKopyala)
        # self.menuMenuAyarlar.addAction(self.actionYapistir)
        self.menuMenuAyarlar.addSeparator()
        self.menuMenuAyarlar.addAction(self.actionCikis)
        self.menuContact.addAction(self.actionMail)
        self.menuContact.addAction(self.actionWebsite)
        self.menuHakkinda.addAction(self.actionKullanimKilavuzu)
        self.menuHakkinda.addAction(self.actionCopyright)
        self.menuYardim.addAction(self.menuHakkinda.menuAction())
        self.menuYardim.addAction(self.menuContact.menuAction())
        self.menubar.addAction(self.menuMenuAyarlar.menuAction())
        self.menubar.addAction(self.menuYardim.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.button_anasayfa.clicked.connect(self.anasayfaGit)
        self.button_mustahsil.clicked.connect(self.mustahsilGit)
        self.button_musteri.clicked.connect(self.musteriGit)
        self.button_kisi_ekle.clicked.connect(self.kisiEkleGit)
        self.button_urun_goruntule.clicked.connect(self.urunGoruntuleGit)
        self.button_kisi_goruntule.clicked.connect(self.kisiGoruntuleGit)
        self.button_mustahsildenUrunAl_mustahsilEkleme.clicked.connect(self.kisiEkleGit)
        self.button_sera.clicked.connect(self.seraGit)
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.clicked.connect(self.kisiEkleGit)
        self.button_musteriUrunSatis_kayitliMusteriEkleme.clicked.connect(self.kisiEkleGit)
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.clicked.connect(self.kisiEkleGit)
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.clicked.connect(self.musteridenOdemeAlGit)
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.clicked.connect(self.mustahsileOdemeYapGit)
        self.toolButton_mustahsil.clicked.connect(self.mustahsilDurumunuGoruntuleGit)
        self.toolButton_musteri.clicked.connect(self.musteriDurumunuGoruntuleGit)
        self.button_kasa_hesabi.clicked.connect(self.kasaHesabGit)
        self.button_alacak_borc_bilgisi.clicked.connect(self.alacaklarBorclarGit)
        self.toolButton_seraGelirSayfasinaGit.clicked.connect(self.seraGelirSayfasinaGit)
        self.toolButton_seraGiderSayfasinaGit.clicked.connect(self.seraGiderSayfasinaGit)
        self.pushButton_seraGelir_islemGecmisiniGoruntule.clicked.connect(self.seraGelirGecmisKayitlaraGit)
        self.pushButton_seraGider_islemGecmisiniGoruntule.clicked.connect(self.seraGiderGecmisKayitlaraGit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_anasayfa, self.button_mustahsil)
        MainWindow.setTabOrder(self.button_mustahsil, self.button_musteri)
        MainWindow.setTabOrder(self.button_musteri, self.button_kisi_ekle)
        MainWindow.setTabOrder(self.button_kisi_ekle, self.button_urun_goruntule)
        MainWindow.setTabOrder(self.button_urun_goruntule, self.button_kisi_goruntule)
        MainWindow.setTabOrder(self.button_kisi_goruntule, self.button_alacak_borc_bilgisi)
        MainWindow.setTabOrder(self.button_alacak_borc_bilgisi, self.button_kasa_hesabi)
        MainWindow.setTabOrder(self.button_kasa_hesabi, self.button_sera)
        MainWindow.setTabOrder(self.button_sera, self.comboBox_mustahsildenUrunAl_gun)
        MainWindow.setTabOrder(self.comboBox_mustahsildenUrunAl_gun, self.comboBox_mustahsildenUrunAl_ay)
        MainWindow.setTabOrder(self.comboBox_mustahsildenUrunAl_ay, self.comboBox_mustahsildenUrunAl_yil)
        MainWindow.setTabOrder(self.comboBox_mustahsildenUrunAl_yil, self.comboBox_mustahsildenUrunAl_urunAdi)
        MainWindow.setTabOrder(self.comboBox_mustahsildenUrunAl_urunAdi, self.button_mustahsildenUrunAl_urunEkleme)
        MainWindow.setTabOrder(self.button_mustahsildenUrunAl_urunEkleme, self.doubleSpinBox)
        MainWindow.setTabOrder(self.doubleSpinBox, self.spinBox_mustahsildenUrunAl_adet)
        MainWindow.setTabOrder(self.spinBox_mustahsildenUrunAl_adet, self.comboBox_mustahsildenUrunAl_kayitliMustahsil)
        MainWindow.setTabOrder(self.comboBox_mustahsildenUrunAl_kayitliMustahsil, self.button_mustahsildenUrunAl_mustahsilEkleme)
        MainWindow.setTabOrder(self.button_mustahsildenUrunAl_mustahsilEkleme, self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit)
        MainWindow.setTabOrder(self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit, self.pushButton_mustahsildenUrunAl_Onayla)
        MainWindow.setTabOrder(self.pushButton_mustahsildenUrunAl_Onayla, self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil)
        MainWindow.setTabOrder(self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil, self.button_mustahsilOdemeDetaylari_mustahsilEkleme)
        MainWindow.setTabOrder(self.button_mustahsilOdemeDetaylari_mustahsilEkleme, self.comboBox_mustahsilOdemeDetaylari_gun)
        MainWindow.setTabOrder(self.comboBox_mustahsilOdemeDetaylari_gun, self.comboBox_mustahsilOdemeDetaylari_ay)
        MainWindow.setTabOrder(self.comboBox_mustahsilOdemeDetaylari_ay, self.comboBox_mustahsilOdemeDetaylari_yil)
        MainWindow.setTabOrder(self.comboBox_mustahsilOdemeDetaylari_yil, self.comboBox_mustahsilOdemeDetaylari_odemeSekli)
        MainWindow.setTabOrder(self.comboBox_mustahsilOdemeDetaylari_odemeSekli, self.button_mustahsilOdemeDetaylari_odemeSekliEkleme)
        MainWindow.setTabOrder(self.button_mustahsilOdemeDetaylari_odemeSekliEkleme, self.comboBox_mustahsilOdemeKurumu)
        MainWindow.setTabOrder(self.comboBox_mustahsilOdemeKurumu, self.button_mustahsilOdemeDetaylari_araciKurumEkleme)
        MainWindow.setTabOrder(self.button_mustahsilOdemeDetaylari_araciKurumEkleme, self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari)
        MainWindow.setTabOrder(self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari, self.pushButton_mustahsilOdemeOnay)
        MainWindow.setTabOrder(self.pushButton_mustahsilOdemeOnay, self.comboBox_musteriUrunSatis_KayitliMusteri)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_KayitliMusteri, self.button_musteriUrunSatis_kayitliMusteriEkleme)
        MainWindow.setTabOrder(self.button_musteriUrunSatis_kayitliMusteriEkleme, self.comboBox_musteriUrunSatis_Gun)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_Gun, self.comboBox_musteriUrunSatis_Ay)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_Ay, self.comboBox_musteriUrunSatis_Yil)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_Yil, self.comboBox_musteriUrunSatis_urunAdi)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_urunAdi, self.doubleSpinBox_musteriUrunSatis_maliyet)
        MainWindow.setTabOrder(self.doubleSpinBox_musteriUrunSatis_maliyet, self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet)
        MainWindow.setTabOrder(self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet, self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit)
        MainWindow.setTabOrder(self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit, self.pushButton_musteriUrunSatis_Onayla)
        MainWindow.setTabOrder(self.pushButton_musteriUrunSatis_Onayla, self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri, self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme)
        MainWindow.setTabOrder(self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme, self.comboBox_musteriUrunSatis_AlinanOdeme_Gun)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_AlinanOdeme_Gun, self.comboBox_musteriUrunSatis_AlinanOdeme_Ay)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_AlinanOdeme_Ay, self.comboBox_musteriUrunSatis_AlinanOdeme_Yil)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_AlinanOdeme_Yil, self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar)
        MainWindow.setTabOrder(self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar, self.comboBox_musteriUrunSatis_AlinanOdeme_turu)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_AlinanOdeme_turu, self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme)
        MainWindow.setTabOrder(self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme, self.comboBox_musteriUrunSatis_AlinanOdeme_kurum)
        MainWindow.setTabOrder(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum, self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme)
        MainWindow.setTabOrder(self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme, self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi)
        MainWindow.setTabOrder(self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi, self.pushButton_musteriUrunSatis_AlinanOdeme_onayla)
        MainWindow.setTabOrder(self.pushButton_musteriUrunSatis_AlinanOdeme_onayla, self.lineEdit_yeniKisi_ad)
        MainWindow.setTabOrder(self.lineEdit_yeniKisi_ad, self.lineEdit_yeniKisi_soyad)
        MainWindow.setTabOrder(self.lineEdit_yeniKisi_soyad, self.lineEdit_yeniKisi_tel)
        MainWindow.setTabOrder(self.lineEdit_yeniKisi_tel, self.lineEdit_yeniKisi_sehir)
        MainWindow.setTabOrder(self.lineEdit_yeniKisi_sehir, self.button_yeniKisi_mustahsilOnay)
        MainWindow.setTabOrder(self.button_yeniKisi_mustahsilOnay, self.button_yeniKisi_musteriOnay)
        MainWindow.setTabOrder(self.button_yeniKisi_musteriOnay, self.comboBox_musteriAldigiMalzemeler_kayitliMusteri)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_kayitliMusteri, self.tableView_musteriAldigiMalzemeler)
        MainWindow.setTabOrder(self.tableView_musteriAldigiMalzemeler, self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun, self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay, self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil, self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun, self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay, self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil)
        MainWindow.setTabOrder(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil, self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap)
        MainWindow.setTabOrder(self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap, self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster)
        MainWindow.setTabOrder(self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster, self.toolButton_mustahsil)
        MainWindow.setTabOrder(self.toolButton_mustahsil, self.toolButton_musteri)
        MainWindow.setTabOrder(self.toolButton_musteri, self.comboBox_mustahsilBilgileri_kayitliMustahsil)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_kayitliMustahsil, self.tableView_mustahsilBilgileri)
        MainWindow.setTabOrder(self.tableView_mustahsilBilgileri, self.comboBox_mustahsilBilgileri_baslangicTarihiGun)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_baslangicTarihiGun, self.comboBox_mustahsilBilgileri_baslangicTarihiAy)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_baslangicTarihiAy, self.comboBox_mustahsilBilgileri_baslangicTarihiYil)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_baslangicTarihiYil, self.comboBox_mustahsilBilgileri_bitisTarihiGun)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_bitisTarihiGun, self.comboBox_mustahsilBilgileri_bitisTarihiAy)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_bitisTarihiAy, self.comboBox_mustahsilBilgileri_bitisTarihiYil)
        MainWindow.setTabOrder(self.comboBox_mustahsilBilgileri_bitisTarihiYil, self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap)
        MainWindow.setTabOrder(self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap, self.pushButton_mustahsilBilgileri_tumVerileriGoster)
        MainWindow.setTabOrder(self.pushButton_mustahsilBilgileri_tumVerileriGoster, self.comboBox_musteriBilgileri_kayitliMusteri)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_kayitliMusteri, self.tableView_musteriBilgileri)
        MainWindow.setTabOrder(self.tableView_musteriBilgileri, self.comboBox_musteriBilgileri_baslangicTarihiGun)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_baslangicTarihiGun, self.comboBox_musteriBilgileri_baslangicTarihiAy)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_baslangicTarihiAy, self.comboBox_musteriBilgileri_baslangicTarihiYil)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_baslangicTarihiYil, self.comboBox_musteriBilgileri_bitisTarihiGun)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_bitisTarihiGun, self.comboBox_musteriBilgileri_bitisTarihiAy)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_bitisTarihiAy, self.comboBox_musteriBilgileri_bitisTarihiYil)
        MainWindow.setTabOrder(self.comboBox_musteriBilgileri_bitisTarihiYil, self.pushButton_musteriBilgileri_tarihlerArasiAramaYap)
        MainWindow.setTabOrder(self.pushButton_musteriBilgileri_tarihlerArasiAramaYap, self.pushButton_musteriBilgileri_tumVerileriGoster)
        MainWindow.setTabOrder(self.pushButton_musteriBilgileri_tumVerileriGoster, self.tableView_alacakBilgileri)
        MainWindow.setTabOrder(self.tableView_alacakBilgileri, self.tableView_borcBilgileri)
        MainWindow.setTabOrder(self.tableView_borcBilgileri, self.comboBox_kasaHesabi_odemeTuru)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_odemeTuru, self.tableView_kasaHesabi)
        MainWindow.setTabOrder(self.tableView_kasaHesabi, self.comboBox_kasaHesabi_baslangicTarihiGun)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_baslangicTarihiGun, self.comboBox_kasaHesabi_baslangicTarihiAy)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_baslangicTarihiAy, self.comboBox_kasaHesabi_baslangicTarihiYil)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_baslangicTarihiYil, self.comboBox_kasaHesabi_bitisTarihiGun)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_bitisTarihiGun, self.comboBox_kasaHesabi_bitisTarihiAy)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_bitisTarihiAy, self.comboBox_kasaHesabi_bitisTarihiYil)
        MainWindow.setTabOrder(self.comboBox_kasaHesabi_bitisTarihiYil, self.pushButton_kasaHesabi_tarihlerArasiAramaYap)
        MainWindow.setTabOrder(self.pushButton_kasaHesabi_tarihlerArasiAramaYap, self.pushButton_kasaHesabi_onayla)
        MainWindow.setTabOrder(self.pushButton_kasaHesabi_onayla, self.toolButton_seraGelirSayfasinaGit)
        MainWindow.setTabOrder(self.toolButton_seraGelirSayfasinaGit, self.toolButton_seraGiderSayfasinaGit)
        MainWindow.setTabOrder(self.toolButton_seraGiderSayfasinaGit, self.comboBox_seraGelir_seralar)
        MainWindow.setTabOrder(self.comboBox_seraGelir_seralar, self.pushButton_seraGelir_seraEkle)
        MainWindow.setTabOrder(self.pushButton_seraGelir_seraEkle, self.comboBox_seraGelir_tarihSec_gun)
        MainWindow.setTabOrder(self.comboBox_seraGelir_tarihSec_gun, self.comboBox_seraGelir_tarihSec_ay)
        MainWindow.setTabOrder(self.comboBox_seraGelir_tarihSec_ay, self.comboBox_seraGelir_tarihSec_yil)
        MainWindow.setTabOrder(self.comboBox_seraGelir_tarihSec_yil, self.comboBox_seraGelir_urunAdi)
        MainWindow.setTabOrder(self.comboBox_seraGelir_urunAdi, self.doublespinBox_seraGelir_maliyet)
        MainWindow.setTabOrder(self.doublespinBox_seraGelir_maliyet, self.spinBox_seraGelir_adet)
        MainWindow.setTabOrder(self.spinBox_seraGelir_adet, self.pushButton_seraGelir_islemGecmisiniGoruntule)
        MainWindow.setTabOrder(self.pushButton_seraGelir_islemGecmisiniGoruntule, self.pushButton_seraGelir_onayla)
        MainWindow.setTabOrder(self.pushButton_seraGelir_onayla, self.comboBox_seraGelirSonuc_urunler)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_urunler, self.comboBox_seraGelirSonuc_seralar)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_seralar, self.button_seraGelirSonuc_seraEkle)
        MainWindow.setTabOrder(self.button_seraGelirSonuc_seraEkle, self.tableView_seraGelirSonuc)
        # MainWindow.setTabOrder(self.tableView_seraGelirSonuc, self.comboBox_seraGelirSonuc_tarihFiltresi_ay)
        # MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_tarihFiltresi_ay, self.comboBox_seraGelirSonuc_tarihFiltresi_yil)
        # MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_tarihFiltresi_yil, self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap)
        # MainWindow.setTabOrder(self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap, self.pushButton_seraGelirSonuc_onayla)
        MainWindow.setTabOrder(self.tableView_seraGelirSonuc, self.comboBox_seraGelirSonuc_baslangicTarihiGun)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_baslangicTarihiGun, self.comboBox_seraGelirSonuc_baslangicTarihiAy)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_baslangicTarihiAy, self.comboBox_seraGelirSonuc_baslangicTarihiYil)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_baslangicTarihiYil, self.comboBox_seraGelirSonuc_bitisTarihiGun)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_bitisTarihiGun, self.comboBox_seraGelirSonuc_bitisTarihiAy)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_bitisTarihiAy, self.comboBox_seraGelirSonuc_bitisTarihiYil)
        MainWindow.setTabOrder(self.comboBox_seraGelirSonuc_bitisTarihiYil, self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap)
        MainWindow.setTabOrder(self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap, self.pushButton_seraGelirSonuc_onayla)
        MainWindow.setTabOrder(self.pushButton_seraGelirSonuc_onayla, self.comboBox_seraGider_seralar)
        MainWindow.setTabOrder(self.comboBox_seraGider_seralar, self.pushButton_seraGider_seraEkle)
        MainWindow.setTabOrder(self.pushButton_seraGider_seraEkle, self.comboBox_seraGider_tarihSec_gun)
        MainWindow.setTabOrder(self.comboBox_seraGider_tarihSec_gun, self.comboBox_seraGider_tarihSec_ay)
        MainWindow.setTabOrder(self.comboBox_seraGider_tarihSec_ay, self.comboBox_seraGider_tarihSec_yil)
        MainWindow.setTabOrder(self.comboBox_seraGider_tarihSec_yil, self.doubleSpinBox_seraGider_elemanGideri)
        MainWindow.setTabOrder(self.doubleSpinBox_seraGider_elemanGideri, self.doubleSpinBox_seraGider_yemekGideri)
        MainWindow.setTabOrder(self.doubleSpinBox_seraGider_yemekGideri, self.doubleSpinBox_seraGider_mazotGideri)
        MainWindow.setTabOrder(self.doubleSpinBox_seraGider_mazotGideri, self.doubleSpinBox_seraGider_digerGiderler)
        MainWindow.setTabOrder(self.doubleSpinBox_seraGider_digerGiderler, self.lineEdit_seraGider_aciklama)
        MainWindow.setTabOrder(self.lineEdit_seraGider_aciklama, self.pushButton_seraGider_islemGecmisiniGoruntule)
        MainWindow.setTabOrder(self.pushButton_seraGider_islemGecmisiniGoruntule, self.pushButton_seraGider_onayla)
        MainWindow.setTabOrder(self.pushButton_seraGider_onayla, self.comboBox_seraGiderSonuc_seralar)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_seralar, self.button_seraGiderSonuc_seraEkle)
        MainWindow.setTabOrder(self.button_seraGiderSonuc_seraEkle, self.tableView_seraGiderSonuc)
        # MainWindow.setTabOrder(self.tableView_seraGiderSonuc, self.comboBox_seraGiderSonuc_tarihFiltresi_ay)
        # MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_tarihFiltresi_ay, self.comboBox_seraGiderSonuc_tarihFiltresi_yil)
        # MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_tarihFiltresi_yil, self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap)
        # MainWindow.setTabOrder(self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap, self.pushButton_seraGiderSonuc_onayla)
        MainWindow.setTabOrder(self.tableView_seraGiderSonuc, self.comboBox_seraGiderSonuc_baslangicTarihiGun)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_baslangicTarihiGun, self.comboBox_seraGiderSonuc_baslangicTarihiAy)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_baslangicTarihiAy, self.comboBox_seraGiderSonuc_baslangicTarihiYil)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_baslangicTarihiYil, self.comboBox_seraGiderSonuc_bitisTarihiGun)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_bitisTarihiGun, self.comboBox_seraGiderSonuc_bitisTarihiAy)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_bitisTarihiAy, self.comboBox_seraGiderSonuc_bitisTarihiYil)
        MainWindow.setTabOrder(self.comboBox_seraGiderSonuc_bitisTarihiYil, self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap)
        MainWindow.setTabOrder(self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap, self.pushButton_seraGiderSonuc_onayla)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ürün Takip Programı"))
        self.button_anasayfa.setText(_translate("MainWindow", "Ana Sayfa"))
        self.button_mustahsil.setText(_translate("MainWindow", "Müstahsil"))
        self.button_musteri.setText(_translate("MainWindow", "Müşteri"))
        self.button_kisi_ekle.setText(_translate("MainWindow", "Kişi Ekle"))
        self.button_urun_goruntule.setText(_translate("MainWindow", "Alınan\n"
"Malzemeler"))
        self.button_kisi_goruntule.setText(_translate("MainWindow", "Kişi\n"
"Görüntüle"))
        self.button_alacak_borc_bilgisi.setText(_translate("MainWindow", "Alacaklar\n"
"Borçlar"))
        self.button_kasa_hesabi.setText(_translate("MainWindow", "Kasa\n"
"Hesabı"))
        self.button_sera.setText(_translate("MainWindow", "Sera"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#4472c4;\">ÜRÜN TAKİP PROGRAMINA HOŞGELDİNİZ</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">1.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">MÜSTAHSİL</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image002.png\" width=\"605\" height=\"44\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menülerden Müstahsil simgesine tıkladığımızda karşımıza aşağıdaki gibi bir sayfa açılmaktadır, ve 2 adet işlevi vardır. Bunlar </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müstahsil’den Ürün Alma</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> ve </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müstahsil’e Ödeme Yapma</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-size:18pt; color:#000000;\">Ø</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#000000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; font-weight:600; color:#000000;\">MÜSTAHSİLDEN ÜRÜN ALMA</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image004.png\" width=\"605\" height=\"270\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu menü </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">MÜSTAHSİL</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">’den </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">ÜRÜN ALMA</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> işlemi için tasarlanmıştır. Tarih kısmı, kullanılan bilgisayar yardımıyla güncel tarihi otomatik olarak seçer. Eğer seçimde bir yanlış varsa, bilgisayarınızın yerel saatini güncellemelisiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Ürün adı</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Maliyet</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Adet</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, ve ürünü aldığınız </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müsatahsili</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> seçtikten sonra, program size otomatik olarak girdiğiniz işlemin </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Tutar</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">’ını göstermektedir. Müstahsilden ürün aldığınızı belirten </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">URNAL </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">koduyla başlayan rasgele ve tekrarsız olacak şekilde kullanıcıya bir işlem kimliği oluşturmaktadır. Müstahsili onayla dedikten sonra işleminiz tamamlanır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-size:18pt; color:#000000;\">Ø</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#000000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; font-weight:600; color:#000000;\">MÜSTAHSİLE ÖDEME YAPMA</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Müstahsil’den ürün alma sayfasında bulunan kırmızı renkli, Müstahsil Ödeme Sayfası’na git butonuna basıldığında bu sayfaya yönlendirilirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image006.png\" width=\"604\" height=\"272\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu sayfa, daha önce Müstahsillerden satın aldığımız ürünlerin ödemesini kaydetmek için kullanılır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Yine Tarih kutularını bilgisayar yardımıyla güncel tarih ile eşleştirir. Kullanıcının girmesi gereken parametreler şu şekildedir;</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müstahsil</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Yapılan Ödeme Türü</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Aracı Kurum(varsa)</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Ödeme Tutarı</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Yine işlemin karışıklığa sebebiyet vermemesi için, ODMYP-xxxxxxxxx şeklinde otomatik ve rasgele, tekrarsız bir işlem kimliği oluştururlur.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image008.png\" width=\"605\" height=\"268\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Ve en sonunda </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">ONAYLA </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">tuşuna basarak girilen işlem onaylanır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; color:#000000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">MÜŞTERİ</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image010.png\" width=\"605\" height=\"43\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menülerden Müşteri simgesine tıkladığımızda karşımıza aşağıdaki gibi bir sayfa açılmaktadır, ve 2 adet işlevi vardır. Bunlar </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşteri’ye Ürün Satma</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> ve </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşteri’den Ödeme Alma</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#000000;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#000000;\">       </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; color:#000000;\">MÜŞTERİ ÜRÜN SATIŞ</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image012.png\" width=\"605\" height=\"270\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu menü </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">MÜŞTERİ’</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">ye </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">ÜRÜN SATMA</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> işlemi için tasarlanmıştır. Tarih kısmı, kullanılan bilgisayar yardımıyla güncel tarihi otomatik olarak seçer. Eğer seçimde bir yanlış varsa, bilgisayarınızın yerel saatini güncellemelisiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Ürün adı</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Fiyat</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Adet</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> ve ürünü aldığınız </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşteriyi</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> seçtikten sonra, program size otomatik olarak girdiğiniz işlemin </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Tutar</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">’ını göstermektedir. Müşteriye ürün sattığınızı belirten </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">URNST </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">koduyla başlayan rasgele ve tekrarsız olacak şekilde kullanıcıya bir işlem kimliği oluşturmaktadır. Müşteriye Ürün Satış İşlemini Onayla dedikten sonra işleminiz tamamlanır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#000000;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#000000;\">       </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; color:#000000;\">MÜŞTERİDEN ÖDEME AL</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Müşteri’ye ürün satma sayfasında bulunan mavi renkli, Müşteriden Ödeme Al butonuna basıldığında bu sayfaya yönlendirilirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image014.png\" width=\"604\" height=\"270\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu sayfa, daha önce Müşterilere almış olduğunuz ürünlerin ödemeleri kaydetmek için kullanılır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Yine Tarih kutularını bilgisayar yardımıyla güncel tarih ile eşleştirir. Kullanıcının girmesi gereken parametreler şu şekildedir;</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşteri</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Yapılan Ödeme Türü</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Aracı Kurum(varsa)</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Ödeme Tutarı</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">         </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Yine işlemin karışıklığa sebebiyet vermemesi için, ODMAL-xxxxxxxxx şeklinde otomatik ve rasgele, tekrarsız bir işlem kimliği oluştururlur.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#000000;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#000000;\">       </span><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image016.png\" width=\"605\" height=\"268\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:18pt; color:#000000;\">·</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#000000;\">       </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Ve en sonunda </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">ONAYLA </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">tuşuna basarak girilen işlem onaylanır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; color:#000000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">KİŞİ EKLE</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image018.png\" width=\"604\" height=\"44\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menüler’de bulunan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Kişi Ekle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgesine tıkladığımızda aşağıdaki resimdeki sayfaya yönlendirlirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image020.png\" width=\"604\" height=\"269\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Yönlendirlirsini Ad, Soyad, Telefon, Şehir parametrelerini girdikten sonra, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Yeni Kişi</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">’yi</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> MÜSTAHSİL</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> olarak eklemek için </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Yeni Müstahsil Olarak Ekle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">MÜŞTERİ</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> olarak eklemek için </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Yeni Müşteri Olarak Ekle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklamalısınz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Ayrıca bu sayfa erişmek için, Başlık 1 ve Başlık 2’de bahsedilen Müstahsil ve Müşteri seçme seçeneklerinin yanında bulunan şekildeki </span><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image022.png\" width=\"36\" height=\"36\" /><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgeye tıklayarakta bu sayfaya ulaşabilirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">4.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">MÜŞTERİNİN ALDIĞI MALZEMELER</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image023.png\" width=\"604\" height=\"44\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menüler’de bulunan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Alınan Malzemeler</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgesine tıkladığımızda aşağıdaki resimdeki sayfaya yönlendirlirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image025.png\" width=\"604\" height=\"272\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Burada, öncelikle Müşteri’yi seçmelisiniz. Daha sonra ilgili müşterinin tüm zamanlardaki işlemlerini görüntülemek için </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Tüm Verileri Göster</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklayınız. Burada </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; text-decoration: underline;\">kronlojik sıralama yerine, kullanıcının uygulamaya yaptığı giriş sıralamasına göre görüntüleme yapılır</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">. </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; text-decoration: underline;\">Kronolojik sıralama yapmak için ve Tarih Filtresi uygulamak</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> için </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Tarih Aralığında Arama Yap</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklamalısınız. Sol taraftaki başlangıç tarihi her seferinde </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">01/01/2020</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> varsayılan olarak seçili gelir, sağ taraftaki bitiş tarihi ise daha önceki kısımlarda bahsettiğimiz gibi bilgisayar yardımıyla </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Güncel Tarihi</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> seçer. Dilediğiniz tarih aralıklarında işlem yapmak için, başlangıç ve bitiş tarihlerini seçtikten sonra Tarih Aralığında Arama Yap butonuna tıklamanız yeterli.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">5.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">KİŞİ DETAYLARINI GÖRÜNTÜLEME</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image027.png\" width=\"604\" height=\"45\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menüler’de bulunan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Kişi Görüntüle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgesine tıkladığımızda aşağıdaki resimdeki sayfaya yönlendirlirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image029.png\" width=\"605\" height=\"275\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Müstahsil ya da Müşteri detaylarını ilgili butonlara tıklayarak ilgili sayfalara gidebilirsiniz. İkiside benzer mantığa ve arayüze sahiptir.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Önce </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müstahsil Bilgilerini Görüntüle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> kısmını inceleyelim.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image031.png\" width=\"605\" height=\"269\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Şimdi ise </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşteri Bilgilerini Görüntüle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> kısmını inceleyelim. Bunun için tekrardan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Kişi Görüntüle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> menüsüne tıklayıp oradan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşteri Bilgilerini Görüntüle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklamanız gerekmektedir.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image033.png\" width=\"605\" height=\"268\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu iki sayfada da öncelikle </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müstahsil/Müşteri</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> seçimi yapmalısınız. Daha sonra ilgili müşterinin tüm zamanlardaki işlemlerini görüntülemek için </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Tüm Verileri Göster</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklayınız. Burada </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; text-decoration: underline;\">kronlojik sıralama yerine, kullanıcının uygulamaya yaptığı giriş sıralamasına göre görüntüleme yapılır</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">. </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; text-decoration: underline;\">Kronolojik sıralama yapmak için ve Tarih Filtresi uygulamak</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> için </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Tarih Aralığında Arama Yap</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklamalısınız. Sol taraftaki başlangıç tarihi her seferinde </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">01/01/2020</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> varsayılan olarak seçili gelir, sağ taraftaki bitiş tarihi ise daha önceki kısımlarda bahsettiğimiz gibi bilgisayar yardımıyla </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Güncel Tarihi</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> seçer. Dilediğiniz tarih aralıklarında işlem yapmak için, başlangıç ve bitiş tarihlerini seçtikten sonra Tarih Aralığında Arama Yap butonuna tıklamanız yeterli.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">6.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">ALACAKLAR ve BORÇLAR</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image035.png\" width=\"604\" height=\"47\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menüler’de bulunan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Alacaklar Borçlar</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgesine tıkladığımızda aşağıdaki resimdeki sayfaya yönlendirlirsiniz.</span><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image037.png\" width=\"605\" height=\"277\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu bölümde, daha önceki menülerden yapılmış olunan girdiler sonucunda, hangi müşteriden ne kadar alacak var veya hangi müstahsile ne kadar borç var bunları takip edilebilecek.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; color:#000000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">7.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">KASAYA GİREN PARA HESABI</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image039.png\" width=\"605\" height=\"48\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menüler’de bulunan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Kasa Hesabı</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgesine tıkladığımızda aşağıdaki resimdeki sayfaya yönlendirlirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image041.png\" width=\"604\" height=\"272\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu bölüm ise müşteriden aldığımız ödemeler ile oluşturulan kasanın takibi içindir. </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Nakit</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> ve </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Çek</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> olmak üzere 2 adet ödeme alınmaktadır. Bu ödemelerden birisini seçerek Tüm Verileri Göster butonuna tıklandığında tüm müşterilerden gelen ilgili ödeme ile alakalı sonuçlar görüntülenir. Tarih Filtresi ve Tüm Verileri Gösterme mantığı </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Müşterinin Aldığı Malzemeler</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Müstah Görüntüleme</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">,</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\"> Müşteri Görüntüleme</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> bölümlerindekiyle aynıdır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">8.</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#ff0000;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:20pt; font-weight:600; color:#ff0000;\">SERA İŞLEMLERİ</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image043.png\" width=\"605\" height=\"41\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Menüler’de bulunan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> simgesine tıkladığımızda aşağıdaki resimdeki sayfaya yönlendirlirsiniz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image045.png\" width=\"605\" height=\"271\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Sera Geliri ya da Sera Gideri butonlarına tıklayarak yapılmak istenen işlemin sayfasına gidilebilir. İkiside benzer mantığa ve arayüze sahiptir.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Önce </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera Gelir</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> kısmını inceleyelim.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image047.png\" width=\"605\" height=\"361\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Girilmesi gereken parametreler;</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera Seç</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Ürün</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Seç</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Maliyet</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">, </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Adet</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> olmak üzere 4 tanedir. Yine tarih kutuları otomatik olarak güncel tarihe ayarlanır, ancak farklı tarihlere giriş yapmak imkanı da vardır. </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Mavi Ok</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> ile gösterilen butona tıklayarak </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:8pt; font-style:italic;\">(bu buton diğer 4 sera bölümünde de aynı işlevi yapmaktadır) </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera Ekleme</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> işlemi yapılabilir. </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Kırmızı Ok</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> ile ise daha önce yapılan </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera Gelir Geçmiş Girdileri</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> görüntülenir.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image049.png\" width=\"605\" height=\"359\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Sera Gelir Bilgileri sayfasında, seçilen serada daha önce hangi malların hangi tarihte ekildiği, kaç adet ve kaç liraya satıldığı bilgileri bulunmaktadır. Ayrıca belirli tarih arasında veya tüm tarihlerde hangi ortalama ile toplam ne kadar gelir getirdiği bilgileri de bulunmaktadır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Burada </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; color:#ff0000;\">önemli bir nokta var</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">. Öncelik seçmeniz gereken parametre </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera Seç</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Kullanıcı seradan çıkan malın ortalamasını ve toplam gelirini görmek istiyorsa, ürün de seçmek zorundadır. Yoksa farklı mallardan ortalama fiyat çıkarılması mantığa ters düşer. Ancak Ortalama ve Genel Toplam harici de tüm gelirleri görmek istiyorsa Hepsi seçeneğini seçerek görüntüleme imkanı da vardır.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Ortalama ve Dip Toplam görmek için ürün de seçilmesi gerekmektedir.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Sera Giderlerini işlemek için ise bu bölümün başında göstermiş olduğumuz menüye giderek, Sera Gider butonuna tıklanması gerekmektedir.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image051.png\" width=\"605\" height=\"367\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Sera Gider kısmının girdileri şekildeki gibidir. Uygun giderler girildikten sonra toplam maliyet otomatik hesaplanmaktadır. Tarih yine güncel kısma ayarlanmış olup, işlem açıklaması da girilince onaylama gerçekleşebilir. Burada bir şey hatırlatmakta fayda var, zaten program da uyaracaktır. Açıklama kısmına </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-style:italic; text-decoration: underline;\">virgül girmemeniz gerekiyor</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">. Çünkü programın yapısına açıklamadaki virgüller zarar vermektedir. Geçmiş görüntülemek için Gelir Geçmişini Görüntüle’deki aynı mantıkla </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt; font-weight:600;\">Sera Gider Geçmişini Görüntüle</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\"> butonuna tıklıyoruz.</span><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"file:///C:/Users/MFT/AppData/Local/Temp/msohtmlclip1/01/clip_image053.png\" width=\"605\" height=\"367\" /><span style=\" font-size:8pt;\"> </span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:12pt;\">Bu kısımda da yine tarih filtreleri veya tüm veri gösterme işlemleri aynı mantalite ile çalışmaktadır. Ve ortalama dip toplam işlemleri burada da geçerlidir.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))

        self.label_mustahsildenUrunAl.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜSTAHSİLDEN ÜRÜN AL</span></p></body></html>"))
        self.label_mustahsildenUrunAl_islemKimligi.setText(_translate("MainWindow", "İşlem Kimliği : "))
        self.label_mustahsildenUrunAl_kayitliMustahsil.setText(_translate("MainWindow", "Kayıtlı Müstahsil : "))
        self.label_mustahsildenUrunAl_adet.setText(_translate("MainWindow", "Adet/Miktar : "))
        self.label_mustahsildenUrunAl_maliyet.setText(_translate("MainWindow", "Maliyet : "))

        ################################################################################################################
        ## MÜSTAHSİL ÜRÜN ALIŞ SAYFASININ ÜRÜN COMBOBOX'I DATASTORE'DAN EKLENDİ
        listFor_mustahsildenUrunAl_urunAdi = []
        self.file_mustahsildenUrunAl_urunAdi =  open("datastore/urunler.dat", "r", encoding="UTF-8")
        for i in self.file_mustahsildenUrunAl_urunAdi:
            listFor_mustahsildenUrunAl_urunAdi.append(i.strip())
        sorted_listFor_mustahsildenUrunAl_urunAdi = sorted(listFor_mustahsildenUrunAl_urunAdi, key=str.lower)
        for i in range(len(sorted_listFor_mustahsildenUrunAl_urunAdi)):
            self.comboBox_mustahsildenUrunAl_urunAdi.addItem(sorted_listFor_mustahsildenUrunAl_urunAdi[i])
        ################################################################################################################

        self.button_mustahsildenUrunAl_urunEkleme.setToolTip(_translate("MainWindow", "Ürün Ekle"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_mustahsildenUrunAl_gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(1, _translate("MainWindow", "Ocak"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(2, _translate("MainWindow", "Şubak"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(3, _translate("MainWindow", "Mart"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(4, _translate("MainWindow", "Nisan"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(5, _translate("MainWindow", "Mayıs"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(6, _translate("MainWindow", "Haziran"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(7, _translate("MainWindow", "Temmuz"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(8, _translate("MainWindow", "Ağustos"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(9, _translate("MainWindow", "Eylül"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(10, _translate("MainWindow", "Ekim"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(11, _translate("MainWindow", "Kasım"))
        self.comboBox_mustahsildenUrunAl_ay.setItemText(12, _translate("MainWindow", "Aralık"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_mustahsildenUrunAl_yil.setItemText(11, _translate("MainWindow", "2030"))
        self.label_mustahsildenUrunAl_urunAdi.setText(_translate("MainWindow", "Ürün Adı(Cinsi) : "))
        self.label_mustahsildenUrunAl_tarih.setText(_translate("MainWindow", "Tarih : "))
        #self.label_mustahsildenUrunAl_islemKimligi_detay.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aa0000;\">102020xxxxxxxxxxx</span></p></body></html>"))
        self.label_mustahsildenUrunAl_islemKimligi_detay.setText(_translate("MainWindow", "URNAL-xxxxxxxxxxx"))
        self.label_mustahsildenUrunAl_maliyet_TL.setText(_translate("MainWindow", "₺"))
        ################################################################################################################
        ## MÜSTAHSİLDEN ÜRÜN AL SAYFASINA MÜSTAHSİLLER DOSYASINDAN EKLEME YAPILDI
        # listFor_comboBox_mustahsildenUrunAl_kayitliMustahsil = []
        # self.file_comboBox_mustahsildenUrunAl_kayitliMustahsil =  open("datastore/mustahsiller.dat", "r", encoding="UTF-8")
        # for i in self.file_comboBox_mustahsildenUrunAl_kayitliMustahsil:
        #     listFor_comboBox_mustahsildenUrunAl_kayitliMustahsil.append(i.strip())
        # sorted_listFor_comboBox_mustahsildenUrunAl_kayitliMustahsil = sorted(listFor_comboBox_mustahsildenUrunAl_kayitliMustahsil, key=str.lower)
        # for i in range(len(sorted_listFor_comboBox_mustahsildenUrunAl_kayitliMustahsil)):
        #     self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem(sorted_listFor_comboBox_mustahsildenUrunAl_kayitliMustahsil[i])
        ################################################################################################################
        self.button_mustahsildenUrunAl_mustahsilEkleme.setToolTip(_translate("MainWindow", "Müstahsil Ekle"))
        self.label_mustahsildenUrunAl_tutar.setText(_translate("MainWindow", "Tutar : "))
        self.label_mustahsildenUrunAl_tutar_sonuc.setText(_translate("MainWindow", "0"))
        self.label_mustahsildenUrunAl_tutar_sonuc_TL.setText(_translate("MainWindow", "₺"))
        self.pushButton_mustahsildenUrunAl_odemeSayfasinaGit.setText(_translate("MainWindow", "MÜSTAHSİL ÖDEME SAYFASINA GİT"))
        self.pushButton_mustahsildenUrunAl_Onayla.setText(_translate("MainWindow", "MÜSTAHSİLDEN ÜRÜN ALIŞINI ONAYLA"))
        self.label_mustahsilOdemeDetaylari.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜSTAHSİL ÖDEME DETAYLARI</span></p></body></html>"))
        self.button_mustahsilOdemeDetaylari_mustahsilEkleme.setToolTip(_translate("MainWindow", "Müstahsil Ekleme Bölümüne Git"))
        self.label_mustahsilOdemeDetaylari_kayitliMustahsil.setText(_translate("MainWindow", "Kayıtlı Müstahsil : "))
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.setItemText(0, _translate("MainWindow", "Ödeme Şekli Seçiniz"))
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.setItemText(1, _translate("MainWindow", "Nakit"))
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.setItemText(2, _translate("MainWindow", "Çek"))
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.setToolTip(_translate("MainWindow", "Ödeme Şekli Ekle"))
        self.label_mustahsilOdemeDetaylari_odemeSekli.setText(_translate("MainWindow", "Ödeme Şekli : "))
        self.label_mustahsilOdemeDetaylari_araciKurum.setText(_translate("MainWindow", "Aracı Kurum : "))
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.setToolTip(_translate("MainWindow", "Aracı Kurum Ekle"))
        self.label_mustahsilOdemeDetaylari_TL.setText(_translate("MainWindow", "₺"))
        self.label_mustahsilOdemeDetaylari_odemeTutari.setText(_translate("MainWindow", "Ödeme Tutarı : "))
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.setText(_translate("MainWindow", "ODMYP-xxxxxxxxxxx"))
        self.label_mustahsilOdemeDetaylari_islemKimligi.setText(_translate("MainWindow", "İşlem Kimliği : "))
        self.label_mustahsilOdemeDetaylari_tarih.setText(_translate("MainWindow", "Tarih : "))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_mustahsilOdemeDetaylari_gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(1, _translate("MainWindow", "Ocak"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(2, _translate("MainWindow", "Şubak"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(3, _translate("MainWindow", "Mart"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(4, _translate("MainWindow", "Nisan"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(5, _translate("MainWindow", "Mayıs"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(6, _translate("MainWindow", "Haziran"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(7, _translate("MainWindow", "Temmuz"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(8, _translate("MainWindow", "Ağustos"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(9, _translate("MainWindow", "Eylül"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(10, _translate("MainWindow", "Ekim"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(11, _translate("MainWindow", "Kasım"))
        self.comboBox_mustahsilOdemeDetaylari_ay.setItemText(12, _translate("MainWindow", "Aralık"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_mustahsilOdemeDetaylari_yil.setItemText(11, _translate("MainWindow", "2030"))
        self.pushButton_mustahsilOdemeOnay.setText(_translate("MainWindow", "MÜSTAHSİLE YAPILAN ÖDEMEYİ ONAYLA"))
        self.label_musteriUrunSatis.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜŞTERİYE SATILAN ÜRÜN BİLGİLERİ</span></p></body></html>"))

        ################################################################################################################
        ## MÜŞTERİ ÜRÜN SATIŞ SAYFASININ ÜRÜN COMBOBOX'I DATASTORE'DAN EKLENDİ
        self.comboBox_musteriUrunSatis_urunAdi.setItemText(0, _translate("MainWindow", "Ürün Seçiniz"))
        listFor_musteriUrunSatis_urunAdi = []
        self.file_musteriUrunSatis_urunAdi =  open("datastore/urunler.dat", "r", encoding="UTF-8")
        for i in self.file_musteriUrunSatis_urunAdi:
            listFor_musteriUrunSatis_urunAdi.append(i.strip())
        sorted_listFor_musteriUrunSatis_urunAdi = sorted(listFor_musteriUrunSatis_urunAdi, key=str.lower)
        for i in range(len(sorted_listFor_musteriUrunSatis_urunAdi)):
            self.comboBox_musteriUrunSatis_urunAdi.addItem(sorted_listFor_musteriUrunSatis_urunAdi[i])
        ################################################################################################################

        self.label_musteriUrunSatis_tutar.setText(_translate("MainWindow", "Tutar : "))

        ################################################################################################################
        ## MÜŞTERİ ÜRÜN SATIŞ SAYFASINA MÜŞTERİLER DOSYASINDAN EKLEME YAPILDI
        # listFor_comboBox_musteriUrunSatis_KayitliMusteri = []
        # self.file_comboBox_musteriUrunSatis_KayitliMusteri =  open("datastore/musteriler.dat", "r", encoding="UTF-8")
        # for i in self.file_comboBox_musteriUrunSatis_KayitliMusteri:
        #     listFor_comboBox_musteriUrunSatis_KayitliMusteri.append(i.strip())
        # sorted_listFor_comboBox_musteriUrunSatis_KayitliMusteri = sorted(listFor_comboBox_musteriUrunSatis_KayitliMusteri, key=str.lower)
        # for i in range(len(sorted_listFor_comboBox_musteriUrunSatis_KayitliMusteri)):
        #     self.comboBox_musteriUrunSatis_KayitliMusteri.addItem(sorted_listFor_comboBox_musteriUrunSatis_KayitliMusteri[i])
        ################################################################################################################

        self.button_musteriUrunSatis_kayitliMusteriEkleme.setToolTip(_translate("MainWindow", "Müşteri Ekleme Bölümüne Git"))
        self.label_musteriUrunSatis_adet.setText(_translate("MainWindow", "Adet/Miktar : "))
        self.label_musteriUrunSatis_fiyat.setText(_translate("MainWindow", "Fiyat : "))
        self.label_musteriUrunSatis_TL.setText(_translate("MainWindow", "₺"))
        self.label_musteriUrunSatis_islemKimligi.setText(_translate("MainWindow", "İşlem Kimliği : "))
        self.label_musteriUrunSatis_islemKimligi_detay.setText(_translate("MainWindow", "URNST-xxxxxxxxxxx"))
        self.label_musteriUrunSatis_tarih.setText(_translate("MainWindow", "Tarih : "))
        self.label_musteriUrunSatis_kayitliMusteri.setText(_translate("MainWindow", "Kayıtlı Müşteri : "))
        self.comboBox_musteriUrunSatis_Gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_musteriUrunSatis_Gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(1, _translate("MainWindow", "Ocak"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(2, _translate("MainWindow", "Şubak"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(3, _translate("MainWindow", "Mart"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(4, _translate("MainWindow", "Nisan"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(5, _translate("MainWindow", "Mayıs"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(6, _translate("MainWindow", "Haziran"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(7, _translate("MainWindow", "Temmuz"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(8, _translate("MainWindow", "Ağustos"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(9, _translate("MainWindow", "Eylül"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(10, _translate("MainWindow", "Ekim"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(11, _translate("MainWindow", "Kasım"))
        self.comboBox_musteriUrunSatis_Ay.setItemText(12, _translate("MainWindow", "Aralık"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_musteriUrunSatis_Yil.setItemText(11, _translate("MainWindow", "2030"))
        self.label_musteriUrunSatis_urunAdi.setText(_translate("MainWindow", "Ürün Adı : "))
        self.label_musteriUrunSatis_tutar_sonuc.setText(_translate("MainWindow", "0"))
        self.label_musteriUrunSatis_tutar_sonuc_TL.setText(_translate("MainWindow", "₺"))
        self.pushButton_musteriUrunSatis_musteridenOdemeAlmaSayfasnaGit.setText(_translate("MainWindow", "MÜŞTERİDEN ÖDEME AL"))
        self.pushButton_musteriUrunSatis_Onayla.setText(_translate("MainWindow", "MÜŞTERİYE ÜRÜN SATIŞ İŞLEMİNİ ONAYLA"))
        self.label_musteriUrunSatis_AlinanOdeme_.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜŞTERİDEN ALINAN ÖDEME</span></p></body></html>"))
        self.label_musteriUrunSatis_AlinanOdeme_turu.setText(_translate("MainWindow", "Alınan Ödeme Türü : "))
        self.label_musteriUrunSatis_AlinanOdeme_kurumu.setText(_translate("MainWindow", "Aracı Kurum : "))
        self.label_musteriUrunSatis_AlinanOdeme_miktari.setText(_translate("MainWindow", "Alınan Nakit Tutarı :  "))
        self.label_musteriUrunSatis_AlinanOdeme_KayitliMusteri.setText(_translate("MainWindow", "Kayıtlı Müşteri : "))
        self.button_musteriUrunSatis_AlinanOdeme_kayitliMusteriEkleme.setToolTip(_translate("MainWindow", "Müşteri Ekleme Bölümüne Git"))
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.setToolTip(_translate("MainWindow", "Aracı Kurum Ekle"))
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi.setText(_translate("MainWindow", "İşlem Kimliği : "))
        self.label_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.setText(_translate("MainWindow", "Ödemeyi Alan Kişi : "))
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.setItemText(0, _translate("MainWindow", "Alınan Ödeme Türünü Seçiniz"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.setItemText(1, _translate("MainWindow", "Nakit"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.setItemText(2, _translate("MainWindow", "Çek"))
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.setToolTip(_translate("MainWindow", "Ödeme Şekli Ekle"))
        self.label_musteriUrunSatis_AlinanOdeme_tarih.setText(_translate("MainWindow", "Tarih : "))
        self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.setPlaceholderText(_translate("MainWindow", "Ödemeyi kimin aldığını giriniz)"))
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.setText(_translate("MainWindow", "ODMAL-xxxxxxxxxxx"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(1, _translate("MainWindow", "Ocak"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(2, _translate("MainWindow", "Şubak"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(3, _translate("MainWindow", "Mart"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(4, _translate("MainWindow", "Nisan"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(5, _translate("MainWindow", "Mayıs"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(6, _translate("MainWindow", "Haziran"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(7, _translate("MainWindow", "Temmuz"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(8, _translate("MainWindow", "Ağustos"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(9, _translate("MainWindow", "Eylül"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(10, _translate("MainWindow", "Ekim"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(11, _translate("MainWindow", "Kasım"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setItemText(12, _translate("MainWindow", "Aralık"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setItemText(11, _translate("MainWindow", "2030"))
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.setText(_translate("MainWindow", "MÜŞTERİDEN ALINAN ÖDEME İŞLEMİNİ ONAYLA"))
        self.label_yeniKisi_baslik.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">YENİ MÜŞTERİ VEYA MÜSTAHSİL EKLE</span></p></body></html>"))
        self.label_yeniKisi_adi.setText(_translate("MainWindow", "Adı : "))
        self.lineEdit_yeniKisi_ad.setPlaceholderText(_translate("MainWindow", "İsim giriniz"))
        self.label_yeniKisi_tel.setText(_translate("MainWindow", "Telefonu : "))
        self.lineEdit_yeniKisi_soyad.setPlaceholderText(_translate("MainWindow", "Soyisim giriniz"))
        self.label_yeniKisi_soyadi.setText(_translate("MainWindow", "Soyadı : "))
        self.label_yeniKisi_sehir.setText(_translate("MainWindow", "Şehir : "))
        self.lineEdit_yeniKisi_sehir.setPlaceholderText(_translate("MainWindow", "Şehir giriniz"))
        self.label_yeniKisi_90.setText(_translate("MainWindow", "+90"))
        self.lineEdit_yeniKisi_tel.setPlaceholderText(_translate("MainWindow", "5xx xxx xxxx"))
        self.button_yeniKisi_mustahsilOnay.setText(_translate("MainWindow", "YENİ MÜSTAHSİL OLARAK EKLE"))
        self.button_yeniKisi_musteriOnay.setText(_translate("MainWindow", "YENİ MÜŞTERİ OLARAK EKLE"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setItemText(11, _translate("MainWindow", "2030"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setItemText(11, _translate("MainWindow", "2030"))
        self.label_musteriAldigiMalzemeler.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜŞTERİNİN ALDIĞI MALZEMELER</span></p></body></html>"))
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.setText(_translate("MainWindow", "TARİH ARALIĞINDA ARAMA YAP"))
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.setText(_translate("MainWindow", "TÜM VERİLERİ GÖSTER"))
        self.pushButton_kasaHesabi_onayla.setText(_translate("MainWindow", "TÜM VERİLERİ GÖSTER"))
        self.label_musteriAldigiMalzemeler_KayitliMusteri.setText(_translate("MainWindow", "Kayıtlı Müşteri : "))
        self.toolButton_musteri.setText(_translate("MainWindow", "MÜŞTERİ DURUMUNU\n"
"\n"
"GÖRÜNTÜLE"))
        self.toolButton_mustahsil.setText(_translate("MainWindow", "MÜSTAHSİL DURUMUNU\n"
"\n"
"GÖRÜNTÜLE"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.label_mustahsilBilgileri_kayitliMustahsil.setText(_translate("MainWindow", "Kayıtlı Müstahsil : "))
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.setText(_translate("MainWindow", "TARİH ARALIĞINDA ARAMA YAP"))
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.setText(_translate("MainWindow", "TÜM VERİLERİ GÖSTER"))
        self.label_mustahsilBilgileri.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜSTAHSİL BİLGİLERİ</span></p></body></html>"))
        self.label_musteriBilgileri.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">MÜŞTERİ BİLGİLERİ</span></p></body></html>"))
        self.label_musteriBilgileri_kayitliMusteri.setText(_translate("MainWindow", "Kayıtlı Müşteri : "))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_musteriBilgileri_baslangicTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_musteriBilgileri_bitisTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_musteriBilgileri_bitisTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_musteriBilgileri_bitisTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.setText(_translate("MainWindow", "TARİH ARALIĞINDA ARAMA YAP"))
        self.pushButton_musteriBilgileri_tumVerileriGoster.setText(_translate("MainWindow", "TÜM VERİLERİ GÖSTER"))
        self.label_hesapOzeti_alacakBilgileri.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">ALACAK BİLGİLERİ</span></p></body></html>"))
        self.label_hesapOzeti_toplamAlacak.setText(_translate("MainWindow", "Toplam Alacak : "))
        self.label_hesapOzeti_toplamAlacak_TL.setText(_translate("MainWindow", "0 ₺"))
        self.label_hesapOzeti_borcBilgileri.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">BORÇ BİLGİLERİ</span></p></body></html>"))
        self.label_hesapOzeti_toplamBorc.setText(_translate("MainWindow", "Toplam Borç : "))
        self.label_hesapOzeti_toplamBorc_TL.setText(_translate("MainWindow", "0 ₺"))
        self.label_kasaHesabi.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">KASA HESABI</span></p></body></html>"))
        self.label_kasaHesabi_odemeTuru.setText(_translate("MainWindow", "Ödeme Türünü Seç : "))
        self.comboBox_kasaHesabi_odemeTuru.setItemText(0, _translate("MainWindow", "Kasaya Gelen Paranın Ödeme Türünü Seçin"))
        self.comboBox_kasaHesabi_odemeTuru.setItemText(1, _translate("MainWindow", "Nakit"))
        self.comboBox_kasaHesabi_odemeTuru.setItemText(2, _translate("MainWindow", "Çek"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_kasaHesabi_baslangicTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_kasaHesabi_baslangicTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_kasaHesabi_baslangicTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_kasaHesabi_bitisTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_kasaHesabi_bitisTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_kasaHesabi_bitisTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.setText(_translate("MainWindow", "TARİH ARALIĞINDA ARAMA YAP"))
        self.toolButton_seraGelirSayfasinaGit.setText(_translate("MainWindow", "SERİ GELİRİ"))
        self.toolButton_seraGiderSayfasinaGit.setText(_translate("MainWindow", "SERA GİDERİ"))
        self.pushButton_seraGelir_islemGecmisiniGoruntule.setText(_translate("MainWindow", "SERA GELİR GEÇMİŞİNİ GÖRÜNTÜLE"))
        self.pushButton_seraGelir_onayla.setText(_translate("MainWindow", "SERA GELİRİNİ ONAYLA"))
        self.label_seraGelir_tarihSec.setText(_translate("MainWindow", "Tarih Seç : "))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_seraGelir_tarihSec_gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_seraGelir_tarihSec_ay.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_seraGelir_tarihSec_yil.setItemText(11, _translate("MainWindow", "2030"))
        self.label_seraGelir_maliyet_TL.setText(_translate("MainWindow", "₺"))
        self.pushButton_seraGelir_seraEkle.setToolTip(_translate("MainWindow", "Sera Ekle"))
        self.label_seraGelir_urunAdi.setText(_translate("MainWindow", "Ürün Adı(Cinsi) : "))
        self.label_seraGelir_maliyet.setText(_translate("MainWindow", "Maliyet : "))
        self.label_seraGelir_seraSec.setText(_translate("MainWindow", "Sera Seç : "))
        self.label_seraGelir_adet.setText(_translate("MainWindow", "Adet/Miktar : "))
        self.label_seraGelir_tutar.setText(_translate("MainWindow", "Toplam Gelir : "))

        ################################################################################################################
        ## SERA GELİR SAYFASININ ÜRÜN COMBOBOX'I DATASTORE'DAN EKLENDİ
        self.comboBox_seraGelir_urunAdi.setItemText(0, _translate("MainWindow", "Ürün Seçiniz"))
        listFor_comboBox_seraGelir_urunAdi = []
        self.file_comboBox_seraGelir_urunAdi =  open("datastore/urunler.dat", "r", encoding="UTF-8")
        for i in self.file_comboBox_seraGelir_urunAdi:
            listFor_comboBox_seraGelir_urunAdi.append(i.strip())
        sorted_listFor_mustahsildenUrunAl_urunAdi = sorted(listFor_comboBox_seraGelir_urunAdi, key=str.lower)
        for i in range(len(sorted_listFor_mustahsildenUrunAl_urunAdi)):
            self.comboBox_seraGelir_urunAdi.addItem(sorted_listFor_mustahsildenUrunAl_urunAdi[i])
        ################################################################################################################

        self.label_seraGelir_bugununGeliriTutarSonuc.setText(_translate("MainWindow", "0"))
        self.label_seraGelir_bugununGeliriTutarSonuc_TL.setText(_translate("MainWindow", "₺"))
        # self.label_seraGelir_devir.setText(_translate("MainWindow", "Sera Gelir Devir : "))
        # self.label_seraGelir_devirSonuc.setText(_translate("MainWindow", "0"))
        # self.label_seraGelir_devirSonuc_TL.setText(_translate("MainWindow", "₺"))
        self.label_seraGelir.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">SERA GELİR EKLE</span></p></body></html>"))
        self.label_seraGelirSonuc_seraSec.setText(_translate("MainWindow", "Sera Seç : "))
        self.button_seraGelirSonuc_seraEkle.setToolTip(_translate("MainWindow", "Sera Ekle"))
        self.label_seraGelirSonuc_urunSec.setText(_translate("MainWindow", "Ürün Seç : "))
        #123123
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_seraGelirSonuc_bitisTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        #123123
        self.label_seraGelirSonuc.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">SERA GELİR BİLGİLERİ</span></p></body></html>"))
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.setText(_translate("MainWindow", "SERA GELİRLERİNİ AYLIK OLARAK GÖSTER"))
        self.pushButton_seraGelirSonuc_onayla.setText(_translate("MainWindow", "TÜM VERİLERİ GÖSTER"))
        self.pushButton_seraGider_islemGecmisiniGoruntule.setText(_translate("MainWindow", "SERA GİDER GEÇMİŞİNİ GÖRÜNTÜLE"))
        self.pushButton_seraGider_onayla.setText(_translate("MainWindow", "SERA GİDERİNİ ONAYLA"))
        self.label_seraGider.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">SERA GİDER EKLE</span></p></body></html>"))
        self.label_seraGider_digerGiderler_TL.setText(_translate("MainWindow", "₺"))
        self.label_seraGider_aciklama.setText(_translate("MainWindow", "Açıklama : "))
        # self.label_seraGider_tarihSec.setText(_translate("MainWindow", "Tarih Seç : "))
        self.comboBox_seraGider_tarihSec_gun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_seraGider_tarihSec_gun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_seraGider_tarihSec_ay.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_seraGider_tarihSec_yil.setItemText(11, _translate("MainWindow", "2030"))
        self.pushButton_seraGider_seraEkle.setToolTip(_translate("MainWindow", "Sera Ekle"))
        self.label_seraGider_bugununToplamGideri_sonuc.setText(_translate("MainWindow", "0"))
        self.label_seraGider_bugununToplamGideri_sonuc_TL.setText(_translate("MainWindow", "₺"))
        self.label_seraGider_seraSec.setText(_translate("MainWindow", "Sera Seç : "))
        self.label_seraGider_yemekGideri.setText(_translate("MainWindow", "Yemek Gideri : "))
        self.label_seraGider_mazotGideri.setText(_translate("MainWindow", "Mazot Gideri : "))
        self.label_seraGider_elemanGideri.setText(_translate("MainWindow", "Eleman Gideri : "))
        self.label_seraGider_yemekGideri_TL.setText(_translate("MainWindow", "₺"))
        self.label_seraGider_bugunToplamGider.setText(_translate("MainWindow", "Toplam Gider : "))
        self.label_seraGider_mazotGideri_TL.setText(_translate("MainWindow", "₺"))
        self.label_seraGider_elemanGideri_TL.setText(_translate("MainWindow", "₺"))
        self.lineEdit_seraGider_aciklama.setPlaceholderText(_translate("MainWindow", "İşlem açıklaması giriniz"))
        self.label_seraGider_digerGiderler.setText(_translate("MainWindow", "Diğer Giderler : "))
        # self.label_seraGider_devir.setText(_translate("MainWindow", "Sera Gider Devir : "))
        # self.label_seraGider_devir_sonuc.setText(_translate("MainWindow", "0"))
        # self.label_seraGider_devir_sonuc_TL.setText(_translate("MainWindow", "₺"))
        self.label_seraGiderSonuc.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">SERA GİDER BİLGİLERİ</span></p></body></html>"))
        self.label_seraGiderSonuc_seraSec.setText(_translate("MainWindow", "Sera Seç : "))
        self.button_seraGiderSonuc_seraEkle.setToolTip(_translate("MainWindow", "Sera Ekle"))
        # self.label_seraGiderSonuc_tarihSec.setText(_translate("MainWindow", "Tarih Seç : "))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(0, _translate("MainWindow", "GÜN"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(13, _translate("MainWindow", "13"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(14, _translate("MainWindow", "14"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(15, _translate("MainWindow", "15"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(16, _translate("MainWindow", "16"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(17, _translate("MainWindow", "17"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(18, _translate("MainWindow", "18"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(19, _translate("MainWindow", "19"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(20, _translate("MainWindow", "20"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(21, _translate("MainWindow", "21"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(22, _translate("MainWindow", "22"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(23, _translate("MainWindow", "23"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(24, _translate("MainWindow", "24"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(25, _translate("MainWindow", "25"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(26, _translate("MainWindow", "26"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(27, _translate("MainWindow", "27"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(28, _translate("MainWindow", "28"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(29, _translate("MainWindow", "29"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(30, _translate("MainWindow", "30"))
        self.comboBox_seraGiderSonuc_bitisTarihiGun.setItemText(31, _translate("MainWindow", "31"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(0, _translate("MainWindow", "AY"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(1, _translate("MainWindow", "OCAK"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(2, _translate("MainWindow", "ŞUBAT"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(3, _translate("MainWindow", "MART"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(4, _translate("MainWindow", "NİSAN"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(5, _translate("MainWindow", "MAYIS"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(6, _translate("MainWindow", "HAZİRAN"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(7, _translate("MainWindow", "TEMMUZ"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(8, _translate("MainWindow", "AĞUSTOS"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(9, _translate("MainWindow", "EYLÜL"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(10, _translate("MainWindow", "EKİM"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(11, _translate("MainWindow", "KASIM"))
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setItemText(12, _translate("MainWindow", "ARALIK"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(0, _translate("MainWindow", "YIL"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(1, _translate("MainWindow", "2020"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(2, _translate("MainWindow", "2021"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(3, _translate("MainWindow", "2022"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(4, _translate("MainWindow", "2023"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(5, _translate("MainWindow", "2024"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(6, _translate("MainWindow", "2025"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(7, _translate("MainWindow", "2026"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(8, _translate("MainWindow", "2027"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(9, _translate("MainWindow", "2028"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(10, _translate("MainWindow", "2029"))
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setItemText(11, _translate("MainWindow", "2030"))
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.setText(_translate("MainWindow", "SERA GİDERLERİNİ AYLIK OLARAK GÖSTER"))
        self.pushButton_seraGiderSonuc_onayla.setText(_translate("MainWindow", "TÜM VERİLERİ GÖSTER"))
        self.menuMenuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardım"))
        self.menuContact.setTitle(_translate("MainWindow", "İletişim"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkında"))
        self.actionMail.setText(_translate("MainWindow", "info@mfatihtuz.com"))
        self.actionWebsite.setText(_translate("MainWindow", "http://mfatihtuz.com"))
        self.actionm_fatihtuz_gmail_com.setText(_translate("MainWindow", "m.fatihtuz@gmail.com"))
        self.action_M_Fatih_TUZ_2020.setText(_translate("MainWindow", "© M.Fatih TÜZ - 2020"))
        # self.actionKes.setText(_translate("MainWindow", "Kes"))
        # self.actionKes.setShortcut(_translate("MainWindow", "Ctrl+X"))
        # self.actionKopyala.setText(_translate("MainWindow", "Kopyala"))
        # self.actionKopyala.setShortcut(_translate("MainWindow", "Ctrl+C"))
        # self.actionYapistir.setText(_translate("MainWindow", "Yapıştır"))
        # self.actionYapistir.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionCikis.setText(_translate("MainWindow", "Çıkış"))
        self.actionCikis.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        # self.actionMenuCubugunuGizle.setText(_translate("MainWindow", "Menü Çubuğunu Göster"))
        self.actionCopyright.setText(_translate("MainWindow", "© M.Fatih TÜZ - 2020"))
        self.actionKullanimKilavuzu.setText(_translate("MainWindow", "Kullanım Kılavuzu"))
        self.actionHerIslemdeOnaySor.setText(_translate("MainWindow", "Her İşlemde Onay Sor"))

        ####################
        ## Ödeme Şekli ve Aracı Kuruma şu anda ihtiyaç duymadığım için gizledim,
        ## İlerde kullanırsam diye de arayüzden çıkarmadım...
        self.button_mustahsilOdemeDetaylari_odemeSekliEkleme.hide()
        self.button_mustahsilOdemeDetaylari_araciKurumEkleme.hide()
        self.button_musteriUrunSatis_AlinanOdeme_odemeSekliEkleme.hide()
        self.button_musteriUrunSatis_AlinanOdeme_araciKurumEkleme.hide()
        ####################

        #gerekli fonksiyonları çağır fresh start için
        self.freshStartComboBoxFill()
        self.bugununTarihleriniTumTarihQComboBoxlarinaYerlestir()
        self.otomatikTutarLabellariniYazdirma()

        ####################
        ## Index Sıfır Olan Yerler Seçiniz Bildirisi Yaptığı İçin Bunları Seçtirmiyor

        ####################


        self.mustahsil_MUSTAHSIL_CSVfileHeaders = "TARİH,ÜRÜN ADI,MALİYET,ADET,ÖDEME TÜRÜ,KURUM,İŞLEM TUTARI,DEVİR,İŞLEM NUMARASI"
        self.musteri_MUSTERI_CSVfileHeaders = "TARİH,ÜRÜN ADI,MALİYET,ADET,ÖDEME TÜRÜ,KURUM,İŞLEM TUTARI,ÖDEMEYİ ALAN,DEVİR,İŞLEM NUMARASI"

        # sinyol slot
        self.pushButton_mustahsildenUrunAl_Onayla.clicked.connect(self.mustahsildenUrunAl_Idx0Control_csvYazdir)
        self.pushButton_musteriUrunSatis_Onayla.clicked.connect(self.musteriUrunSatis_Idx0Control_csvYazdir)
        self.pushButton_mustahsilOdemeOnay.clicked.connect(self.mustahsilOdemeDetaylari_Idx0Control_csvYazdir)
        self.pushButton_musteriUrunSatis_AlinanOdeme_onayla.clicked.connect(self.musteridenAlinanOdemeDetaylari_Idx0Control_csvYazdir)
        self.button_mustahsildenUrunAl_urunEkleme.clicked.connect(self.yeniUrunEkle)
        self.button_musteriUrunSatis_urunEkleme.clicked.connect(self.yeniUrunEkle)
        self.button_yeniKisi_mustahsilOnay.clicked.connect(self.yeniMustahsiliCSVdosyasinaYaz)
        self.button_yeniKisi_musteriOnay.clicked.connect(self.yeniMusteriyiCSVdosyasinaYaz)
        #self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.clicked.connect(self.sirala)
        self.pushButton_musteriAldigiMalzemeler_tumVerileriGoster.clicked.connect(self.xTekrarDEF)
        self.pushButton_seraGelir_seraEkle.clicked.connect(self.seraEkle)
        self.pushButton_seraGider_seraEkle.clicked.connect(self.seraEkle)
        self.button_seraGelirSonuc_seraEkle.clicked.connect(self.seraEkle)
        self.button_seraGiderSonuc_seraEkle.clicked.connect(self.seraEkle)
        self.pushButton_seraGelir_onayla.clicked.connect(self.seraGelirOnayla)
        self.pushButton_seraGider_onayla.clicked.connect(self.seraGiderOnayla)
        self.pushButton_seraGelirSonuc_onayla.clicked.connect(self.seraGelirTablosu)
        self.pushButton_seraGiderSonuc_onayla.clicked.connect(self.seraGiderTablosu)
        self.pushButton_musteriAldigiMalzemeler_tarihlerArasiAramaYap.clicked.connect(self.mau_tarihFiltresi)
        self.pushButton_mustahsilBilgileri_tarihlerArasiAramaYap.clicked.connect(self.mustahsil_tarihFiltresi)
        self.pushButton_musteriBilgileri_tarihlerArasiAramaYap.clicked.connect(self.musteri_tarihFiltresi)
        self.pushButton_seraGiderSonuc_tarihlerArasiAramaYap.clicked.connect(self.seraGiderTablosu_tarihFiltresi)
        self.pushButton_seraGelirSonuc_tarihlerArasiAramaYap.clicked.connect(self.seraGelirTablosu_tarihFiltresi)

        self.actionWebsite.triggered.connect(self.myWebsite)
        self.actionMail.triggered.connect(self.myMail)
        self.actionCopyright.triggered.connect(self.copyrights)
        self.actionCikis.setShortcut('Ctrl+Q')
        self.actionCikis.setStatusTip('Uygulamayı Kapat')
        self.actionCikis.triggered.connect(qApp.quit)

        self.copyrgihtTEXT ='''
© Copyright - 2020 
Muhammed Fatih Tüz (GraphLab)

Bu yazılımın (Ürün Takip Programı)  ve ilgili belge dosyaları, kullanıcıya lisanslı halde gelmektedir. Bu programın bir kopyasını herhangi bir tüzel kişiye/kuruma dağıtımı yapılması GraphLab firması lisans anlaşmasına aykırıdır. Herhangi bir türden kopyalama hakkını ihlal edecek kopyalama, değiştirme, birleştirme gibi işlemlerde kullanıcıya ait lisans anahtarı ile tespit sağlanır. Kayıtlı lisans anahtarı üzerinden hangi tür hak ihlali işlemi yapıldıysa, bu işlemlerden lisans sahibi olan tüzel kişi veya kurum sorumlu tutulacaktır. Kopyalama hakları haricinde hiç bir sınırlama ve kısıtlama olmaksızın Ürün Takip Programı üzerinde işlem yapma izni verilmektedir. Lisans anahtarı haricen belirtilmediği sürece tüzel kişiye/kuruma Hayat Boyu kapsamında verilir, ve sınırsız sürede kullanım hakkına sahiptir. Bu lisans konusu patente, ek patentler alma hakkı lisans verene ait olacak ve bu değişikliklere ait patent başvuru yapıldıktan sonra lisans sözleşmesi bu patentler için de geçerli olacaktır. Lisans alan kişi/kurum, lisans verenin yazılı izni olmaksızın bir başka gerçek veya tüzel kişiye bu lisans sözleşmesine konu olan patentlerin kullanılması konusunda lisans veremez. Lisans alanın tali lisans verme yetkisi yoktur.

Program kullanıcıya teslim edilmeden önce, belirli testlerden geçirilmiştir. Ancak, testlerde karşılaşılmayan her türlü problemler bir hata koduyla ekranda belirlenecek olup, tüm revizyon işlerinden lisans veren sorumludur. Karşılaşılan bir hata olması durumunda, lütfen yapımcıyla iletişime geçiniz.
'''
    def copyrights(self):
        try:
            self.stackedWidget.setCurrentIndex(0)
            self.label.setText(self.copyrgihtTEXT)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    def myWebsite(self):
        url = QtCore.QUrl('http://mfatihtuz.com')
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')
    def myMail(self):
        url = QtCore.QUrl('mailto:info@mfatihtuz.com')
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')


    def mau_tarihFiltresi(self):
        if self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentIndex() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen <b>MÜŞTERİ</b> seçerek işleme devam edin...")
            msg.setWindowTitle("Müşteri Seçilmedi")
            msg.exec_()
        else:
            try:
                font = QtGui.QFont()
                font.setPointSize(12)
                self.tableView_musteriAldigiMalzemeler.setFont(font)
                df_tarihFilter = pd.read_csv(
                    "datastore/MUSTERI/" + self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv")

                df_tarihFilter['TARİH'] = pd.to_datetime(df_tarihFilter['TARİH'])


                start_date = ""
                start_date += str(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.currentIndex() + 2019) + "-"
                start_date += str(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.currentIndex()).zfill(2) + "-"
                start_date += str(self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.currentIndex()).zfill(2)


                end_date = ""
                end_date += str(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.currentIndex() + 2019) + "-"
                end_date += str(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.currentIndex()).zfill(2) + "-"
                end_date += str(self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.currentIndex()).zfill(2)

                if start_date > end_date:
                    self.lutfenTarihDengesizligiMessageBox()
                else:
                    print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")

                mask = (df_tarihFilter['TARİH'] >= start_date) & (df_tarihFilter['TARİH'] <= end_date)

                df_tarihFilter = df_tarihFilter.loc[mask]
                df_tarihFilter['TARİH'] = df_tarihFilter['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
                print(df_tarihFilter['TARİH'].values)

                model_df_tarihFilter = PandasModel(df_tarihFilter)
                self.tableView_musteriAldigiMalzemeler.setModel(model_df_tarihFilter)
                self.tableView_musteriAldigiMalzemeler.setSortingEnabled(True)
                self.tableView_musteriAldigiMalzemeler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView_musteriAldigiMalzemeler.horizontalHeader().setStretchLastSection(True)
            except Exception as e:
                self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    def mustahsil_tarihFiltresi(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_mustahsilBilgileri.setFont(font)
            df_tarihFilter = pd.read_csv(
                "datastore/MUSTAHSIL/" + self.comboBox_mustahsilBilgileri_kayitliMustahsil.currentText() + ".csv")

            df_tarihFilter['TARİH'] = pd.to_datetime(df_tarihFilter['TARİH'])

            start_date = ""
            start_date += str(self.comboBox_mustahsilBilgileri_baslangicTarihiYil.currentIndex() + 2019) + "-"
            start_date += str(self.comboBox_mustahsilBilgileri_baslangicTarihiAy.currentIndex()).zfill(2) + "-"
            start_date += str(self.comboBox_mustahsilBilgileri_baslangicTarihiGun.currentIndex()).zfill(2)


            end_date = ""
            end_date += str(self.comboBox_mustahsilBilgileri_bitisTarihiYil.currentIndex() + 2019) + "-"
            end_date += str(self.comboBox_mustahsilBilgileri_bitisTarihiAy.currentIndex()).zfill(2) + "-"
            end_date += str(self.comboBox_mustahsilBilgileri_bitisTarihiGun.currentIndex()).zfill(2)

            if start_date > end_date:
                self.lutfenTarihDengesizligiMessageBox()
            else:
                print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")

            mask = (df_tarihFilter['TARİH'] >= start_date) & (df_tarihFilter['TARİH'] <= end_date)

            df_tarihFilter = df_tarihFilter.loc[mask]
            df_tarihFilter['TARİH'] = df_tarihFilter['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
            print(df_tarihFilter['TARİH'].values)

            model_df_tarihFilter = PandasModel(df_tarihFilter)
            self.tableView_mustahsilBilgileri.setModel(model_df_tarihFilter)
            self.tableView_mustahsilBilgileri.setSortingEnabled(True)
            self.tableView_mustahsilBilgileri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    def musteri_tarihFiltresi(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_musteriBilgileri.setFont(font)
            df_tarihFilter = pd.read_csv(
                "datastore/MUSTERI/" + self.comboBox_musteriBilgileri_kayitliMusteri.currentText() + ".csv")

            df_tarihFilter['TARİH'] = pd.to_datetime(df_tarihFilter['TARİH'])

            start_date = ""
            start_date += str(self.comboBox_musteriBilgileri_baslangicTarihiYil.currentIndex() + 2019) + "-"
            start_date += str(self.comboBox_musteriBilgileri_baslangicTarihiAy.currentIndex()).zfill(2) + "-"
            start_date += str(self.comboBox_musteriBilgileri_baslangicTarihiGun.currentIndex()).zfill(2)

            end_date = ""
            end_date += str(self.comboBox_musteriBilgileri_bitisTarihiYil.currentIndex() + 2019) + "-"
            end_date += str(self.comboBox_musteriBilgileri_bitisTarihiAy.currentIndex()).zfill(2) + "-"
            end_date += str(self.comboBox_musteriBilgileri_bitisTarihiGun.currentIndex()).zfill(2)

            if start_date > end_date:
                self.lutfenTarihDengesizligiMessageBox()
            else:
                print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")

            mask = (df_tarihFilter['TARİH'] >= start_date) & (df_tarihFilter['TARİH'] <= end_date)

            df_tarihFilter = df_tarihFilter.loc[mask]
            df_tarihFilter['TARİH'] = df_tarihFilter['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
            print(df_tarihFilter['TARİH'].values)

            model_df_tarihFilter = PandasModel(df_tarihFilter)
            self.tableView_musteriBilgileri.setModel(model_df_tarihFilter)
            #self.tableView_musteriBilgileri.setSortingEnabled(True)
            self.tableView_musteriBilgileri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView_musteriBilgileri.horizontalHeader().setStretchLastSection(True)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    def kasaHesabi_tarihFiltresi(self):
        if self.comboBox_kasaHesabi_odemeTuru.currentIndex() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen <b>ÖDEME TÜRÜ</b> seçerek işleme devam edin...")
            msg.setWindowTitle("Müşteri Seçilmedi")
            msg.exec_()
        else:
            try:
                font = QtGui.QFont()
                font.setPointSize(12)
                self.tableView_kasaHesabi.setFont(font)
                df_tarihFilter = pd.read_csv(
                    "datastore/KASAHESABI/" + self.comboBox_kasaHesabi_odemeTuru.currentText() + ".csv")

                df_tarihFilter['TARİH'] = pd.to_datetime(df_tarihFilter['TARİH'])


                start_date = ""
                start_date += str(self.comboBox_kasaHesabi_baslangicTarihiYil.currentIndex() + 2019) + "-"
                start_date += str(self.comboBox_kasaHesabi_baslangicTarihiAy.currentIndex()).zfill(2) + "-"
                start_date += str(self.comboBox_kasaHesabi_baslangicTarihiGun.currentIndex()).zfill(2)

                end_date = ""
                end_date += str(self.comboBox_kasaHesabi_bitisTarihiYil.currentIndex() + 2019) + "-"
                end_date += str(self.comboBox_kasaHesabi_bitisTarihiAy.currentIndex()).zfill(2) + "-"
                end_date += str(self.comboBox_kasaHesabi_bitisTarihiGun.currentIndex()).zfill(2)

                if start_date > end_date:
                    self.lutfenTarihDengesizligiMessageBox()
                else:
                    print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")

                mask = (df_tarihFilter['TARİH'] >= start_date) & (df_tarihFilter['TARİH'] <= end_date)

                df_tarihFilter = df_tarihFilter.loc[mask]
                df_tarihFilter['TARİH'] = df_tarihFilter['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
                print(df_tarihFilter['TARİH'].values)

                model_df_tarihFilter = PandasModel(df_tarihFilter)
                self.tableView_kasaHesabi.setModel(model_df_tarihFilter)
                self.tableView_kasaHesabi.setSortingEnabled(True)
                self.tableView_kasaHesabi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.tableView_kasaHesabi.horizontalHeader().setStretchLastSection(True)
            except Exception as e:
                self.lutfenYapimciylaIletisimeGecinMessageBox(e)

    ####################################################################################################################
    ## Yeni Kişi İşlemleri
    def yeniMustahsiliCSVdosyasinaYaz(self):
        if self.lineEdit_yeniKisi_ad.text()=="":
            self.lutfenAdGirinizMessageBox()
        elif self.lineEdit_yeniKisi_soyad.text()=="":
            self.lutfenSoyadGirinizMessageBox()
        elif self.lineEdit_yeniKisi_tel.text()=="":
            self.lutfenTelefonGirinizMessageBox()
        elif self.lineEdit_yeniKisi_sehir.text()=="":
            self.lutfenSehirGirinizMessageBox()
        else:
            if self.actionHerIslemdeOnaySor.isChecked() == True:
                box = QMessageBox()
                box.setIcon(QMessageBox.Question)
                box.setWindowTitle('İşlem Kontrolü!')
                box.setText("Yeni Kaydı yapılan ve detayları;\n\n" +
                            "Tür : MÜSTAHSİL"  + "\n" +
                            "Adı : " + self.lineEdit_yeniKisi_ad.text() + "\n" +
                            "Soyadı : " + self.lineEdit_yeniKisi_soyad.text() + "\n" +
                            "Telefonu : " + self.lineEdit_yeniKisi_tel.text() + "\n" +
                            "Şehiri : " + self.lineEdit_yeniKisi_sehir.text() + "\n\n" +
                            "olan KİŞİ EKLEME işlemi onaylıyor musunuz?")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                buttonY = box.button(QMessageBox.Yes)
                buttonY.setText('Evet')
                buttonN = box.button(QMessageBox.No)
                buttonN.setText('İptal')
                box.exec_()
                if box.clickedButton() == buttonY:
                    f = open("datastore/kisiler.csv", "a+", encoding="UTF-8")
                    f.write(self.lineEdit_yeniKisi_ad.text() + " " + self.lineEdit_yeniKisi_soyad.text() + "," +
                            self.lineEdit_yeniKisi_tel.text() + "," + self.lineEdit_yeniKisi_sehir.text() + "," + "MÜSTAHSİL" + "\n")
                    f.close()

                    self.df_yeniKisiEkle_kayitlilariGoruntule = pd.read_csv("datastore/kisiler.csv")
                    model_yeniKisiEkle_kayitlilariGoruntule = PandasModel(self.df_yeniKisiEkle_kayitlilariGoruntule)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.setModel(model_yeniKisiEkle_kayitlilariGoruntule)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setStretchLastSection(True)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setSectionResizeMode(
                        QHeaderView.Stretch)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.setSortingEnabled(True)

                    # self.mustahsilleriComboBoxaVeDosyaYolunaEkle()

                    self.comboBox_mustahsildenUrunAl_kayitliMustahsil.clear()
                    self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem("Müstahsil Seçiniz")
                    self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.clear()
                    self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.addItem("Müstahsil Seçiniz")
                    self.comboBox_mustahsilBilgileri_kayitliMustahsil.clear()
                    self.comboBox_mustahsilBilgileri_kayitliMustahsil.addItem("Müstahsil Seçiniz")
                    ################################################################################################################
                    ## MÜSTAHSİLLER QComboBox'ları dolduruluyor
                    self.df_mustahsilleriKisilerdenCek = pd.read_csv("datastore/kisiler.csv")
                    self.df_mustahsilleriKisilerdenCek = self.df_mustahsilleriKisilerdenCek[(
                            self.df_mustahsilleriKisilerdenCek["MÜŞTERİ/MÜSTAHSİL"] == "MÜSTAHSİL"
                    )]
                    self.mustahsiller_list = list(set(self.df_mustahsilleriKisilerdenCek["AD SOYAD"].values))
                    # genel liste oluşturuldu
                    self.sorted_mustahsiller_list = sorted(self.mustahsiller_list, key=str.lower)
                    print(self.sorted_mustahsiller_list)

                    for i in range(len(self.sorted_mustahsiller_list)):
                        self.mustahsillerinCSVdosyalariniOlustur_path = "datastore/MUSTAHSIL/" + str(
                            self.sorted_mustahsiller_list[i] + ".csv")
                        self.mustahsillerinDevirDATdosyalariniOlustur_path = "datastore/MUSTAHSIL/" + str(
                            self.sorted_mustahsiller_list[i] + " - Devir.dat")
                        if os.path.isfile(str(self.mustahsillerinCSVdosyalariniOlustur_path)) == False:
                            self.file_mustahsillerinCSVdosyalariniOlustur = open(
                                str(self.mustahsillerinCSVdosyalariniOlustur_path),
                                "a", encoding='utf-8')
                            self.file_mustahsillerinCSVdosyalariniOlustur.write(
                                self.mustahsil_MUSTAHSIL_CSVfileHeaders + "\n")
                            self.file_mustahsillerinCSVdosyalariniOlustur.close()
                            self.file_mustahsillerinDevirDATdosyalariniOlustur = open(
                                str(self.mustahsillerinDevirDATdosyalariniOlustur_path), "w", encoding='utf-8')
                            self.file_mustahsillerinDevirDATdosyalariniOlustur.write("0.0")
                            self.file_mustahsillerinDevirDATdosyalariniOlustur.close()
                        else:
                            print(
                                self.mustahsillerinCSVdosyalariniOlustur_path + " dosyaları mustahsilBilgileri dosya yolunda zaten var...")
                            print(
                                self.mustahsillerinDevirDATdosyalariniOlustur_path + " dosyası mustahsilBilgileri dosya yolunda zaten var...")
                        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
                        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
                        self.comboBox_mustahsilBilgileri_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
                else:
                    print("no")
            else:
                f = open("datastore/kisiler.csv", "a+", encoding="UTF-8")
                f.write(self.lineEdit_yeniKisi_ad.text() + " " + self.lineEdit_yeniKisi_soyad.text() + "," +
                        self.lineEdit_yeniKisi_tel.text() + "," + self.lineEdit_yeniKisi_sehir.text() + "," + "MÜSTAHSİL" + "\n")
                f.close()

                self.df_yeniKisiEkle_kayitlilariGoruntule = pd.read_csv("datastore/kisiler.csv")
                model_yeniKisiEkle_kayitlilariGoruntule = PandasModel(self.df_yeniKisiEkle_kayitlilariGoruntule)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.setModel(model_yeniKisiEkle_kayitlilariGoruntule)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setStretchLastSection(True)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.setSortingEnabled(True)

                # self.mustahsilleriComboBoxaVeDosyaYolunaEkle()

                self.comboBox_mustahsildenUrunAl_kayitliMustahsil.clear()
                self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem("Müstahsil Seçiniz")
                self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.clear()
                self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.addItem("Müstahsil Seçiniz")
                self.comboBox_mustahsilBilgileri_kayitliMustahsil.clear()
                self.comboBox_mustahsilBilgileri_kayitliMustahsil.addItem("Müstahsil Seçiniz")
                ################################################################################################################
                ## MÜSTAHSİLLER QComboBox'ları dolduruluyor
                self.df_mustahsilleriKisilerdenCek = pd.read_csv("datastore/kisiler.csv")
                self.df_mustahsilleriKisilerdenCek = self.df_mustahsilleriKisilerdenCek[(
                        self.df_mustahsilleriKisilerdenCek["MÜŞTERİ/MÜSTAHSİL"] == "MÜSTAHSİL"
                )]
                self.mustahsiller_list = list(set(self.df_mustahsilleriKisilerdenCek["AD SOYAD"].values))
                # genel liste oluşturuldu
                self.sorted_mustahsiller_list = sorted(self.mustahsiller_list, key=str.lower)
                print(self.sorted_mustahsiller_list)

                for i in range(len(self.sorted_mustahsiller_list)):
                    self.mustahsillerinCSVdosyalariniOlustur_path = "datastore/MUSTAHSIL/" + str(
                        self.sorted_mustahsiller_list[i] + ".csv")
                    self.mustahsillerinDevirDATdosyalariniOlustur_path = "datastore/MUSTAHSIL/" + str(
                        self.sorted_mustahsiller_list[i] + " - Devir.dat")
                    if os.path.isfile(str(self.mustahsillerinCSVdosyalariniOlustur_path)) == False:
                        self.file_mustahsillerinCSVdosyalariniOlustur = open(
                            str(self.mustahsillerinCSVdosyalariniOlustur_path),
                            "a", encoding='utf-8')
                        self.file_mustahsillerinCSVdosyalariniOlustur.write(
                            self.mustahsil_MUSTAHSIL_CSVfileHeaders + "\n")
                        self.file_mustahsillerinCSVdosyalariniOlustur.close()
                        self.file_mustahsillerinDevirDATdosyalariniOlustur = open(
                            str(self.mustahsillerinDevirDATdosyalariniOlustur_path), "w", encoding='utf-8')
                        self.file_mustahsillerinDevirDATdosyalariniOlustur.write("0.0")
                        self.file_mustahsillerinDevirDATdosyalariniOlustur.close()
                    else:
                        print(
                            self.mustahsillerinCSVdosyalariniOlustur_path + " dosyaları mustahsilBilgileri dosya yolunda zaten var...")
                        print(
                            self.mustahsillerinDevirDATdosyalariniOlustur_path + " dosyası mustahsilBilgileri dosya yolunda zaten var...")
                    self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
                    self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
                    self.comboBox_mustahsilBilgileri_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
    def yeniMusteriyiCSVdosyasinaYaz(self):
        if self.lineEdit_yeniKisi_ad.text()=="":
            self.lutfenAdGirinizMessageBox()
        elif self.lineEdit_yeniKisi_soyad.text()=="":
            self.lutfenSoyadGirinizMessageBox()
        elif self.lineEdit_yeniKisi_tel.text()=="":
            self.lutfenTelefonGirinizMessageBox()
        elif self.lineEdit_yeniKisi_sehir.text()=="":
            self.lutfenSehirGirinizMessageBox()
        else:
            if self.actionHerIslemdeOnaySor.isChecked() == True:
                box = QMessageBox()
                box.setIcon(QMessageBox.Question)
                box.setWindowTitle('İşlem Kontrolü!')
                box.setText("Yeni Kaydı yapılan ve detayları;\n\n" +
                            "Tür : MÜŞTERİ"  + "\n" +
                            "Adı : " + self.lineEdit_yeniKisi_ad.text() + "\n" +
                            "Soyadı : " + self.lineEdit_yeniKisi_soyad.text() + "\n" +
                            "Telefonu : " + self.lineEdit_yeniKisi_tel.text() + "\n" +
                            "Şehiri : " + self.lineEdit_yeniKisi_sehir.text() + "\n\n" +
                            "olan KİŞİ EKLEME işlemi onaylıyor musunuz?")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                buttonY = box.button(QMessageBox.Yes)
                buttonY.setText('Evet')
                buttonN = box.button(QMessageBox.No)
                buttonN.setText('İptal')
                box.exec_()
                if box.clickedButton() == buttonY:
                    f = open("datastore/kisiler.csv", "a+", encoding="UTF-8")
                    f.write(self.lineEdit_yeniKisi_ad.text() + " " + self.lineEdit_yeniKisi_soyad.text() + "," +
                            self.lineEdit_yeniKisi_tel.text() + "," + self.lineEdit_yeniKisi_sehir.text() + "," + "MÜŞTERİ" + "\n")
                    f.close()

                    self.df_yeniKisiEkle_kayitlilariGoruntule = pd.read_csv("datastore/kisiler.csv")
                    model_yeniKisiEkle_kayitlilariGoruntule = PandasModel(self.df_yeniKisiEkle_kayitlilariGoruntule)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.setModel(model_yeniKisiEkle_kayitlilariGoruntule)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setStretchLastSection(True)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setSectionResizeMode(
                        QHeaderView.Stretch)
                    self.tableView_yeniKisiEkle_kayitlilariGoruntule.setSortingEnabled(True)

                    self.comboBox_musteriUrunSatis_KayitliMusteri.clear()
                    self.comboBox_musteriUrunSatis_KayitliMusteri.addItem("Müşteri Seçiniz")
                    self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.clear()
                    self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addItem("Müşteri Seçiniz")
                    self.comboBox_musteriBilgileri_kayitliMusteri.clear()
                    self.comboBox_musteriBilgileri_kayitliMusteri.addItem("Müşteri Seçiniz")
                    self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.clear()
                    self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.addItem("Müşteri Seçiniz")
                    ################################################################################################################
                    ## MÜSTAHSİLLER QComboBox'ları dolduruluyor
                    self.df_musterileriKisilerdenCek = pd.read_csv("datastore/kisiler.csv")
                    self.df_musterileriKisilerdenCek = self.df_musterileriKisilerdenCek[(
                            self.df_musterileriKisilerdenCek["MÜŞTERİ/MÜSTAHSİL"] == "MÜŞTERİ"
                    )]
                    self.musteriler_list = list(set(self.df_musterileriKisilerdenCek["AD SOYAD"].values))
                    # genel liste oluşturuldu
                    self.sorted_musteriler_list = sorted(self.musteriler_list, key=str.lower)
                    print(self.sorted_musteriler_list)

                    for i in range(len(self.sorted_musteriler_list)):
                        self.musterilerinCSVdosyalariniOlustur_path = "datastore/MUSTERI/" + str(
                            self.sorted_musteriler_list[i] + ".csv")
                        self.musterilerinDevirDATdosyalariniOlustur_path = "datastore/MUSTERI/" + str(
                            self.sorted_musteriler_list[i] + " - Devir.dat")
                        self.musteriAldigiMalzemelerCSV_path = "datastore/MUSTERI/" + str(
                            self.sorted_musteriler_list[i] + " - Aldığı Malzemeler.csv")
                        if os.path.isfile(str(self.musterilerinCSVdosyalariniOlustur_path)) == False:

                            self.file_musterilerinCSVdosyalariniOlustur = open(
                                str(self.musterilerinCSVdosyalariniOlustur_path), "a", encoding='utf-8')
                            self.file_musterilerinCSVdosyalariniOlustur.write(
                                self.musteri_MUSTERI_CSVfileHeaders + "\n")
                            self.file_musterilerinCSVdosyalariniOlustur.close()

                            self.file_musterilerinDevirDATdosyalariniOlustur = open(
                                str(self.musterilerinDevirDATdosyalariniOlustur_path), "w", encoding='utf-8')
                            self.file_musterilerinDevirDATdosyalariniOlustur.write("0.0")
                            self.file_musterilerinDevirDATdosyalariniOlustur.close()

                            self.myStringForAlinanMalzemeler = "TARİH"
                            listFor_musteriAldigiMalzemelerUrunler = []
                            self.file_musteriAldigiMalzemelerUrunler = open("datastore/urunler.dat", "r",
                                                                            encoding="UTF-8")
                            for j in self.file_musteriAldigiMalzemelerUrunler:
                                listFor_musteriAldigiMalzemelerUrunler.append(j.strip())
                            sorted_listFor_musteriAldigiMalzemelerUrunler = sorted(
                                listFor_musteriAldigiMalzemelerUrunler,
                                key=str.lower)
                            self.file_musteriAldigiMalzemelerUrunler.close()
                            for j in range(len(sorted_listFor_musteriAldigiMalzemelerUrunler)):
                                self.myStringForAlinanMalzemeler += "," + str(
                                    sorted_listFor_musteriAldigiMalzemelerUrunler[j])
                            self.file_musteriAldigiMalzemeler = open(str(self.musteriAldigiMalzemelerCSV_path), "w",
                                                                     encoding='utf-8')
                            self.file_musteriAldigiMalzemeler.write(self.myStringForAlinanMalzemeler)
                            self.file_musteriAldigiMalzemeler.close()
                        else:
                            print(
                                self.musterilerinCSVdosyalariniOlustur_path + " dosyaları mustahsilBilgileri dosya yolunda zaten var...")
                            print(
                                self.musterilerinDevirDATdosyalariniOlustur_path + " dosyası mustahsilBilgileri dosya yolunda zaten var...")
                        self.comboBox_musteriUrunSatis_KayitliMusteri.addItem(self.sorted_musteriler_list[i])
                        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addItem(
                            self.sorted_musteriler_list[i])
                        self.comboBox_musteriBilgileri_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
                        self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
                else:
                    print("no")
            else:
                f = open("datastore/kisiler.csv", "a+", encoding="UTF-8")
                f.write(self.lineEdit_yeniKisi_ad.text() + " " + self.lineEdit_yeniKisi_soyad.text() + "," +
                        self.lineEdit_yeniKisi_tel.text() + "," + self.lineEdit_yeniKisi_sehir.text() + "," + "MÜŞTERİ" + "\n")
                f.close()

                self.df_yeniKisiEkle_kayitlilariGoruntule = pd.read_csv("datastore/kisiler.csv")
                model_yeniKisiEkle_kayitlilariGoruntule = PandasModel(self.df_yeniKisiEkle_kayitlilariGoruntule)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.setModel(model_yeniKisiEkle_kayitlilariGoruntule)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setStretchLastSection(True)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.horizontalHeader().setSectionResizeMode(
                    QHeaderView.Stretch)
                self.tableView_yeniKisiEkle_kayitlilariGoruntule.setSortingEnabled(True)

                self.comboBox_musteriUrunSatis_KayitliMusteri.clear()
                self.comboBox_musteriUrunSatis_KayitliMusteri.addItem("Müşteri Seçiniz")
                self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.clear()
                self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addItem("Müşteri Seçiniz")
                self.comboBox_musteriBilgileri_kayitliMusteri.clear()
                self.comboBox_musteriBilgileri_kayitliMusteri.addItem("Müşteri Seçiniz")
                self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.clear()
                self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.addItem("Müşteri Seçiniz")
                ################################################################################################################
                ## MÜSTAHSİLLER QComboBox'ları dolduruluyor
                self.df_musterileriKisilerdenCek = pd.read_csv("datastore/kisiler.csv")
                self.df_musterileriKisilerdenCek = self.df_musterileriKisilerdenCek[(
                        self.df_musterileriKisilerdenCek["MÜŞTERİ/MÜSTAHSİL"] == "MÜŞTERİ"
                )]
                self.musteriler_list = list(set(self.df_musterileriKisilerdenCek["AD SOYAD"].values))
                # genel liste oluşturuldu
                self.sorted_musteriler_list = sorted(self.musteriler_list, key=str.lower)
                print(self.sorted_musteriler_list)

                for i in range(len(self.sorted_musteriler_list)):
                    self.musterilerinCSVdosyalariniOlustur_path = "datastore/MUSTERI/" + str(
                        self.sorted_musteriler_list[i] + ".csv")
                    self.musterilerinDevirDATdosyalariniOlustur_path = "datastore/MUSTERI/" + str(
                        self.sorted_musteriler_list[i] + " - Devir.dat")
                    self.musteriAldigiMalzemelerCSV_path = "datastore/MUSTERI/" + str(
                        self.sorted_musteriler_list[i] + " - Aldığı Malzemeler.csv")
                    if os.path.isfile(str(self.musterilerinCSVdosyalariniOlustur_path)) == False:

                        self.file_musterilerinCSVdosyalariniOlustur = open(
                            str(self.musterilerinCSVdosyalariniOlustur_path), "a", encoding='utf-8')
                        self.file_musterilerinCSVdosyalariniOlustur.write(self.musteri_MUSTERI_CSVfileHeaders + "\n")
                        self.file_musterilerinCSVdosyalariniOlustur.close()

                        self.file_musterilerinDevirDATdosyalariniOlustur = open(
                            str(self.musterilerinDevirDATdosyalariniOlustur_path), "w", encoding='utf-8')
                        self.file_musterilerinDevirDATdosyalariniOlustur.write("0.0")
                        self.file_musterilerinDevirDATdosyalariniOlustur.close()

                        self.myStringForAlinanMalzemeler = "TARİH"
                        listFor_musteriAldigiMalzemelerUrunler = []
                        self.file_musteriAldigiMalzemelerUrunler = open("datastore/urunler.dat", "r", encoding="UTF-8")
                        for j in self.file_musteriAldigiMalzemelerUrunler:
                            listFor_musteriAldigiMalzemelerUrunler.append(j.strip())
                        sorted_listFor_musteriAldigiMalzemelerUrunler = sorted(listFor_musteriAldigiMalzemelerUrunler,
                                                                               key=str.lower)
                        self.file_musteriAldigiMalzemelerUrunler.close()
                        for j in range(len(sorted_listFor_musteriAldigiMalzemelerUrunler)):
                            self.myStringForAlinanMalzemeler += "," + str(
                                sorted_listFor_musteriAldigiMalzemelerUrunler[j])
                        self.file_musteriAldigiMalzemeler = open(str(self.musteriAldigiMalzemelerCSV_path), "w",
                                                                 encoding='utf-8')
                        self.file_musteriAldigiMalzemeler.write(self.myStringForAlinanMalzemeler)
                        self.file_musteriAldigiMalzemeler.close()
                    else:
                        print(
                            self.musterilerinCSVdosyalariniOlustur_path + " dosyaları mustahsilBilgileri dosya yolunda zaten var...")
                        print(
                            self.musterilerinDevirDATdosyalariniOlustur_path + " dosyası mustahsilBilgileri dosya yolunda zaten var...")
                    self.comboBox_musteriUrunSatis_KayitliMusteri.addItem(self.sorted_musteriler_list[i])
                    self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
                    self.comboBox_musteriBilgileri_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
                    self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.addItem(self.sorted_musteriler_list[i])

            # self.musteriVerilileriniAlinanUrunlerSayfasinaAktar()
    ####################################################################################################################


    ####################################################################################################################
    ## MÜSTAHSİL/MÜŞTERİ ÜRÜN AL SAT TUTAR YAZDIRMA
    def mustahsildenUrunAl_SonucTutarYaz(self):
        self.mustahsildenUrunAl_SonucTutarYaz_temp = round(self.doubleSpinBox.value() * self.spinBox_mustahsildenUrunAl_adet.value(), 3)
        self.label_mustahsildenUrunAl_tutar_sonuc.setText('{:.2f}'.format(self.mustahsildenUrunAl_SonucTutarYaz_temp))
    def musteriyeUrunSat_SonucTutarYaz(self):
        self.musteriyeUrunSat_SonucTutarYaz_temp = round(
        self.doubleSpinBox_musteriUrunSatis_maliyet.value() * self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.value(), 3)
        self.label_musteriUrunSatis_tutar_sonuc.setText('{:.2f}'.format(self.musteriyeUrunSat_SonucTutarYaz_temp))
    ####################################################################################################################


    ####################################################################################################################
    ## MÜSTAHSİL ÜRÜN ALIŞ QComboBox İŞLEMLERİ
    def mustahsildenUrunAl_Idx0Control_csvYazdir(self):
        if self.comboBox_mustahsildenUrunAl_urunAdi.currentIndex() == 0:
            self.lutfenUrunSecinizMessageBox()
        elif self.doubleSpinBox.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.spinBox_mustahsildenUrunAl_adet.value()==0:
            self.lutfenGecerliBirAdetGiriniz()
        elif self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentIndex() == 0:
            self.lutfenMustahsilSecinizMessageBox()
        else:
            try:
                if self.actionHerIslemdeOnaySor.isChecked() == True:
                    box = QMessageBox()
                    box.setIcon(QMessageBox.Question)
                    box.setWindowTitle('İşlem Kontrolü!')
                    box.setText("MÜSTAHSİL'den alınan ürünün detayları;\n\n"
                                "Müstahsil Adı : " + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() + "\n" +
                                "Tarih : " + str(self.comboBox_mustahsildenUrunAl_yil.currentIndex() + 2019) + "-" +
                                str(self.comboBox_mustahsildenUrunAl_ay.currentIndex()).zfill(2) + "-" +
                                str(self.comboBox_mustahsildenUrunAl_gun.currentIndex()).zfill(2) + "\n" +
                                "Ürün Adı : " + self.comboBox_mustahsildenUrunAl_urunAdi.currentText() + "\n" +
                                "Maliyet : " + str(self.doubleSpinBox.value()) + " ₺\n" +
                                "Adet : " + str(self.spinBox_mustahsildenUrunAl_adet.value()) + "\n" +
                                "Tutar : " + str(self.label_mustahsildenUrunAl_tutar_sonuc.text()) + " ₺\n\n" +
                                "olan işlemi onaylıyor musunuz?")
                    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    buttonY = box.button(QMessageBox.Yes)
                    buttonY.setText('Evet')
                    buttonN = box.button(QMessageBox.No)
                    buttonN.setText('İptal')
                    box.exec_()

                    if box.clickedButton() == buttonY:
                        self.file_mustahsilUrunAl_anlikDevirDATfile = open(
                            "datastore/MUSTAHSIL/" + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() +
                            " - Devir.dat", "r", encoding='utf-8')
                        self.mustahsilUrunAl_Devir = float(self.file_mustahsilUrunAl_anlikDevirDATfile.read())
                        print("İşlem öncesi devir: " + str(self.mustahsilUrunAl_Devir))
                        self.file_mustahsilUrunAl_anlikDevirDATfile.close()

                        self.mustahsilUrunAl_Devir -= float(self.mustahsildenUrunAl_SonucTutarYaz_temp)
                        print("İşlem sonrası devir: " + str(self.mustahsilUrunAl_Devir))

                        yil_mustahsildenUrunAl_mustahsilBilgileriTablo = str(
                            self.comboBox_mustahsildenUrunAl_yil.currentIndex() + 2019)
                        ay_mustahsildenUrunAl_mustahsilBilgileriTablo = str(
                            self.comboBox_mustahsildenUrunAl_ay.currentIndex()).zfill(2)
                        gun_mustahsildenUrunAl_mustahsilBilgileriTablo = str(
                            self.comboBox_mustahsildenUrunAl_gun.currentIndex()).zfill(2)

                        self.file_mustahsilUrunAlDetaylariDosyayaIsle = open(
                            "datastore/MUSTAHSIL/" + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() + ".csv",
                            "a", encoding='utf-8')
                        self.file_mustahsilUrunAlDetaylariDosyayaIsle.write(
                            yil_mustahsildenUrunAl_mustahsilBilgileriTablo + "-" +
                            ay_mustahsildenUrunAl_mustahsilBilgileriTablo + "-" +
                            gun_mustahsildenUrunAl_mustahsilBilgileriTablo + "," +

                            self.comboBox_mustahsildenUrunAl_urunAdi.currentText() + "," +
                            "{:.2f}".format(self.doubleSpinBox.value()) + " ₺" + "," +
                            str(self.spinBox_mustahsildenUrunAl_adet.value()) + " ADET" + "," +
                            "-----" + "," + "-----" + "," +
                            str(self.label_mustahsildenUrunAl_tutar_sonuc.text()) + " ₺" + "," +
                            "{:.2f}".format(self.mustahsilUrunAl_Devir) + " ₺" + "," +
                            self.label_mustahsildenUrunAl_islemKimligi_detay.text() + "\n")
                        self.file_mustahsilUrunAlDetaylariDosyayaIsle.close()

                        self.file_mustahsilUrunAl_anlikDevirDATfile = open(
                            "datastore/MUSTAHSIL/" + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() +
                            " - Devir.dat", "w", encoding='utf-8')
                        self.file_mustahsilUrunAl_anlikDevirDATfile.write("{:.2f}".format(self.mustahsilUrunAl_Devir))
                        self.file_mustahsilUrunAl_anlikDevirDATfile.close()
                        self.randURNAL()
                    else:
                        print("no")
                else:
                    self.file_mustahsilUrunAl_anlikDevirDATfile = open(
                        "datastore/MUSTAHSIL/" + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() +
                        " - Devir.dat", "r", encoding='utf-8')
                    self.mustahsilUrunAl_Devir = float(self.file_mustahsilUrunAl_anlikDevirDATfile.read())
                    print("İşlem öncesi devir: " + str(self.mustahsilUrunAl_Devir))
                    self.file_mustahsilUrunAl_anlikDevirDATfile.close()

                    self.mustahsilUrunAl_Devir -= float(self.mustahsildenUrunAl_SonucTutarYaz_temp)
                    print("İşlem sonrası devir: " + str(self.mustahsilUrunAl_Devir))

                    yil_mustahsildenUrunAl_mustahsilBilgileriTablo = str(
                        self.comboBox_mustahsildenUrunAl_yil.currentIndex() + 2019)
                    ay_mustahsildenUrunAl_mustahsilBilgileriTablo = str(
                        self.comboBox_mustahsildenUrunAl_ay.currentIndex()).zfill(2)
                    gun_mustahsildenUrunAl_mustahsilBilgileriTablo = str(
                        self.comboBox_mustahsildenUrunAl_gun.currentIndex()).zfill(2)

                    self.file_mustahsilUrunAlDetaylariDosyayaIsle = open(
                        "datastore/MUSTAHSIL/" + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() + ".csv",
                        "a", encoding='utf-8')
                    self.file_mustahsilUrunAlDetaylariDosyayaIsle.write(
                        yil_mustahsildenUrunAl_mustahsilBilgileriTablo + "-" +
                        ay_mustahsildenUrunAl_mustahsilBilgileriTablo + "-" +
                        gun_mustahsildenUrunAl_mustahsilBilgileriTablo + "," +

                        self.comboBox_mustahsildenUrunAl_urunAdi.currentText() + "," +
                        "{:.2f}".format(self.doubleSpinBox.value()) + " ₺" + "," +
                        str(self.spinBox_mustahsildenUrunAl_adet.value()) + " ADET" + "," +
                        "-----" + "," + "-----" + "," +
                        str(self.label_mustahsildenUrunAl_tutar_sonuc.text()) + " ₺" + "," +
                        "{:.2f}".format(self.mustahsilUrunAl_Devir) + " ₺" + "," +
                        self.label_mustahsildenUrunAl_islemKimligi_detay.text() + "\n")
                    self.file_mustahsilUrunAlDetaylariDosyayaIsle.close()

                    self.file_mustahsilUrunAl_anlikDevirDATfile = open(
                        "datastore/MUSTAHSIL/" + self.comboBox_mustahsildenUrunAl_kayitliMustahsil.currentText() +
                        " - Devir.dat", "w", encoding='utf-8')
                    self.file_mustahsilUrunAl_anlikDevirDATfile.write("{:.2f}".format(self.mustahsilUrunAl_Devir))
                    self.file_mustahsilUrunAl_anlikDevirDATfile.close()
                    self.randURNAL()


            except Exception as e:
                self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    ## MÜSTAHSİLE YAPILAN ÖDEME QComboBox İŞLEMLERİ
    def mustahsilOdemeDetaylari_Idx0Control_csvYazdir(self):
        if self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentIndex() == 0:
            self.lutfenMustahsilSecinizMessageBox()
        elif self.comboBox_mustahsilOdemeDetaylari_odemeSekli.currentIndex() == 0:
            self.lutfenOdemeSekliSecinizMessageBox()
        elif self.comboBox_mustahsilOdemeKurumu.currentIndex() == 0:
            self.lutfenAraciKurumSecinizMessageBox()
        elif self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        else:
            try:
                if self.actionHerIslemdeOnaySor.isChecked() == True:
                    box = QMessageBox()
                    box.setIcon(QMessageBox.Question)
                    box.setWindowTitle('İşlem Kontrolü!')
                    box.setText("MÜSTAHSİL'e yapılan ÖDEME detayları;\n\n" +
                                "Müstahsil Adı : " + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() + "\n" +
                                "Tarih : " + str(self.comboBox_mustahsilOdemeDetaylari_yil.currentIndex() + 2019) + "-" +
                                str(self.comboBox_mustahsilOdemeDetaylari_ay.currentIndex()).zfill(2) + "-" +
                                str(self.comboBox_mustahsilOdemeDetaylari_gun.currentIndex()).zfill(2) + "\n" +
                                "Ödeme Şekli : " + str(self.comboBox_mustahsilOdemeDetaylari_odemeSekli.currentText()) + "\n" +
                                "Ödeme Kurumu : " + str(self.comboBox_mustahsilOdemeKurumu.currentText()) + "\n" +
                                "Tutar : " + str(self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.value()) + " ₺\n\n" +
                                "olan işlemi onaylıyor musunuz?")
                    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    buttonY = box.button(QMessageBox.Yes)
                    buttonY.setText('Evet')
                    buttonN = box.button(QMessageBox.No)
                    buttonN.setText('İptal')
                    box.exec_()
                    if box.clickedButton() == buttonY:
                        self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile = open(
                            "datastore/MUSTAHSIL/" + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() +
                            " - Devir.dat", "r", encoding='utf-8')
                        self.mustahsileYapilanOdemeDetaylari_Devir = float(
                            self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.read())
                        print("İşlem öncesi devir: " + str(self.mustahsileYapilanOdemeDetaylari_Devir))
                        self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.close()

                        self.mustahsileYapilanOdemeDetaylari_Devir += float(
                            self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.value())
                        print("İşlem sonrası devir: " + str(self.mustahsileYapilanOdemeDetaylari_Devir))

                        yil_musteriyeYapilanOdeme_mustahsilBilgileriTablo = str(
                            self.comboBox_mustahsilOdemeDetaylari_yil.currentIndex() + 2019)
                        ay_musteriyeYapilanOdeme_mustahsilBilgileriTablo = str(
                            self.comboBox_mustahsilOdemeDetaylari_ay.currentIndex()).zfill(2)
                        gun_musteriyeYapilanOdeme_mustahsilBilgileriTablo = str(
                            self.comboBox_mustahsilOdemeDetaylari_gun.currentIndex()).zfill(2)

                        self.file_mustahsileYapilanOdemeDetaylariDosyayaIsle = open(
                            "datastore/MUSTAHSIL/" + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() + ".csv",
                            "a", encoding='utf-8')
                        self.file_mustahsileYapilanOdemeDetaylariDosyayaIsle.write(
                            yil_musteriyeYapilanOdeme_mustahsilBilgileriTablo + "-" +
                            ay_musteriyeYapilanOdeme_mustahsilBilgileriTablo + "-" +
                            gun_musteriyeYapilanOdeme_mustahsilBilgileriTablo + "," +
                            "-----" + "," + "-----" + "," + "-----" + "," +
                            str(self.comboBox_mustahsilOdemeDetaylari_odemeSekli.currentText()) + "," +
                            str(self.comboBox_mustahsilOdemeKurumu.currentText()) + "," +
                            "{:.2f}".format(
                                self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.value()) + " ₺" + "," +
                            "{:.2f}".format(self.mustahsileYapilanOdemeDetaylari_Devir) + " ₺" + "," +
                            self.label_mustahsilOdemeDetaylari_islemKimligi_detay.text() + "\n")
                        self.file_mustahsileYapilanOdemeDetaylariDosyayaIsle.close()

                        self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile = open(
                            "datastore/MUSTAHSIL/" + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() +
                            " - Devir.dat", "w", encoding='utf-8')
                        self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.write(
                            str(self.mustahsileYapilanOdemeDetaylari_Devir))
                        self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.close()
                        self.randODMYP()
                    else:
                        print("no")
                else:
                    self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile = open(
                        "datastore/MUSTAHSIL/" + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() +
                        " - Devir.dat", "r", encoding='utf-8')
                    self.mustahsileYapilanOdemeDetaylari_Devir = float(
                        self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.read())
                    print("İşlem öncesi devir: " + str(self.mustahsileYapilanOdemeDetaylari_Devir))
                    self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.close()

                    self.mustahsileYapilanOdemeDetaylari_Devir += float(
                        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.value())
                    print("İşlem sonrası devir: " + str(self.mustahsileYapilanOdemeDetaylari_Devir))

                    yil_musteriyeYapilanOdeme_mustahsilBilgileriTablo = str(
                        self.comboBox_mustahsilOdemeDetaylari_yil.currentIndex() + 2019)
                    ay_musteriyeYapilanOdeme_mustahsilBilgileriTablo = str(
                        self.comboBox_mustahsilOdemeDetaylari_ay.currentIndex()).zfill(2)
                    gun_musteriyeYapilanOdeme_mustahsilBilgileriTablo = str(
                        self.comboBox_mustahsilOdemeDetaylari_gun.currentIndex()).zfill(2)

                    self.file_mustahsileYapilanOdemeDetaylariDosyayaIsle = open(
                        "datastore/MUSTAHSIL/" + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() + ".csv",
                        "a", encoding='utf-8')
                    self.file_mustahsileYapilanOdemeDetaylariDosyayaIsle.write(
                        yil_musteriyeYapilanOdeme_mustahsilBilgileriTablo + "-" +
                        ay_musteriyeYapilanOdeme_mustahsilBilgileriTablo + "-" +
                        gun_musteriyeYapilanOdeme_mustahsilBilgileriTablo + "," +
                        "-----" + "," + "-----" + "," + "-----" + "," +
                        str(self.comboBox_mustahsilOdemeDetaylari_odemeSekli.currentText()) + "," +
                        str(self.comboBox_mustahsilOdemeKurumu.currentText()) + "," +
                        "{:.2f}".format(
                            self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.value()) + " ₺" + "," +
                        "{:.2f}".format(self.mustahsileYapilanOdemeDetaylari_Devir) + " ₺" + "," +
                        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.text() + "\n")
                    self.file_mustahsileYapilanOdemeDetaylariDosyayaIsle.close()

                    self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile = open(
                        "datastore/MUSTAHSIL/" + self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.currentText() +
                        " - Devir.dat", "w", encoding='utf-8')
                    self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.write(
                        str(self.mustahsileYapilanOdemeDetaylari_Devir))
                    self.file_mustahsileYapilanOdemeDetaylari_anlikDevirDATfile.close()
                    self.randODMYP()
            except Exception as e: print(e)
    ## MÜŞTERİ ÜRÜN SATIŞ QComboBox İŞLEMLERİ
    def musteriUrunSatis_Idx0Control_csvYazdir(self):
        if self.comboBox_musteriUrunSatis_KayitliMusteri.currentIndex() == 0:
            self.lutfenMusteriSecinizMessageBox()
        elif self.comboBox_musteriUrunSatis_urunAdi.currentIndex() == 0:
            self.lutfenUrunSecinizMessageBox()
        elif self.doubleSpinBox_musteriUrunSatis_maliyet.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.value()==0:
            self.lutfenGecerliBirAdetGiriniz()
        else:
            try:
                if self.actionHerIslemdeOnaySor.isChecked() == True:
                    box = QMessageBox()
                    box.setIcon(QMessageBox.Question)
                    box.setWindowTitle('İşlem Kontrolü!')
                    box.setText("MÜŞTERİ'ye satılan ürünün detayları;\n\n" +
                                "Müşteri Adı : " + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() + "\n" +
                                "Tarih : " + str(self.comboBox_musteriUrunSatis_Yil.currentIndex() + 2019) + "-" +
                                str(self.comboBox_musteriUrunSatis_Ay.currentIndex()).zfill(2) + "-" +
                                str(self.comboBox_musteriUrunSatis_Gun.currentIndex()).zfill(2) + "\n" +
                                "Ürün Adı : " + self.comboBox_musteriUrunSatis_urunAdi.currentText() + "\n" +
                                "Maliyet : " + str(self.doubleSpinBox_musteriUrunSatis_maliyet.value()) + " ₺\n" +
                                "Adet : " + str(self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.value()) + "\n" +
                                "Tutar : " + str(self.label_musteriUrunSatis_tutar_sonuc.text()) + " ₺\n\n" +
                                "olan işlemi onaylıyor musunuz?")
                    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    buttonY = box.button(QMessageBox.Yes)
                    buttonY.setText('Evet')
                    buttonN = box.button(QMessageBox.No)
                    buttonN.setText('İptal')
                    box.exec_()

                    if box.clickedButton() == buttonY:
                        self.file_musteriUrunSatis_anlikDevirDATfile = open(
                            "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() +
                            " - Devir.dat", "r", encoding='utf-8')
                        self.musteriUrunSatis_Devir = float(self.file_musteriUrunSatis_anlikDevirDATfile.read())
                        print("İşlem öncesi devir: " + str(self.musteriUrunSatis_Devir))
                        self.file_musteriUrunSatis_anlikDevirDATfile.close()

                        self.musteriUrunSatis_Devir += float(self.musteriyeUrunSat_SonucTutarYaz_temp)
                        print("İşlem sonrası devir: " + str(self.musteriUrunSatis_Devir))

                        self.file_musteriUrunSatisDetaylariDosyayaIsle = open(
                            "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() + ".csv",
                            "a",
                            encoding='utf-8')
                        yil_musteriUrunSatis_musteriBilgileriTablo = str(
                            self.comboBox_musteriUrunSatis_Yil.currentIndex() + 2019)
                        ay_musteriUrunSatis_musteriBilgileriTablo = str(
                            self.comboBox_musteriUrunSatis_Ay.currentIndex()).zfill(2)
                        gun_musteriUrunSatis_musteriBilgileriTablo = str(
                            self.comboBox_musteriUrunSatis_Gun.currentIndex()).zfill(2)

                        self.tarih_musteriUrunSati_musteriBilgileriTablo = ""
                        self.tarih_musteriUrunSati_musteriBilgileriTablo += yil_musteriUrunSatis_musteriBilgileriTablo + "-"
                        self.tarih_musteriUrunSati_musteriBilgileriTablo += ay_musteriUrunSatis_musteriBilgileriTablo + "-"
                        self.tarih_musteriUrunSati_musteriBilgileriTablo += gun_musteriUrunSatis_musteriBilgileriTablo

                        self.musteriUrunSatisFiyatWithTL = "{:.2f}".format(self.musteriUrunSatis_Devir) + " ₺"

                        self.file_musteriUrunSatisDetaylariDosyayaIsle.write(
                            self.tarih_musteriUrunSati_musteriBilgileriTablo + "," +
                            self.comboBox_musteriUrunSatis_urunAdi.currentText() + "," +
                            "{:.2f}".format(self.doubleSpinBox_musteriUrunSatis_maliyet.value()) + " ₺" + "," +
                            str(self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.value()) + " ADET" + "," +
                            "-----" + "," + "-----" + "," +
                            str(self.label_musteriUrunSatis_tutar_sonuc.text()) + " ₺" + "," +
                            "-----" + "," +
                            self.musteriUrunSatisFiyatWithTL + "," +
                            self.label_musteriUrunSatis_islemKimligi_detay.text() + "\n")
                        self.file_musteriUrunSatisDetaylariDosyayaIsle.close()

                        self.file_musteriUrunSatis_anlikDevirDATfile = open(
                            "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() +
                            " - Devir.dat", "w", encoding='utf-8')
                        self.file_musteriUrunSatis_anlikDevirDATfile.write("{:.2f}".format(self.musteriUrunSatis_Devir))
                        self.file_musteriUrunSatis_anlikDevirDATfile.close()
                        self.randURNST()
                    else:
                        print("no")
                else:
                    self.file_musteriUrunSatis_anlikDevirDATfile = open(
                        "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() +
                        " - Devir.dat", "r", encoding='utf-8')
                    self.musteriUrunSatis_Devir = float(self.file_musteriUrunSatis_anlikDevirDATfile.read())
                    print("İşlem öncesi devir: " + str(self.musteriUrunSatis_Devir))
                    self.file_musteriUrunSatis_anlikDevirDATfile.close()

                    self.musteriUrunSatis_Devir += float(self.musteriyeUrunSat_SonucTutarYaz_temp)
                    print("İşlem sonrası devir: " + str(self.musteriUrunSatis_Devir))

                    self.file_musteriUrunSatisDetaylariDosyayaIsle = open(
                        "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() + ".csv",
                        "a",
                        encoding='utf-8')
                    yil_musteriUrunSatis_musteriBilgileriTablo = str(
                        self.comboBox_musteriUrunSatis_Yil.currentIndex() + 2019)
                    ay_musteriUrunSatis_musteriBilgileriTablo = str(
                        self.comboBox_musteriUrunSatis_Ay.currentIndex()).zfill(2)
                    gun_musteriUrunSatis_musteriBilgileriTablo = str(
                        self.comboBox_musteriUrunSatis_Gun.currentIndex()).zfill(2)

                    self.tarih_musteriUrunSati_musteriBilgileriTablo = ""
                    self.tarih_musteriUrunSati_musteriBilgileriTablo += yil_musteriUrunSatis_musteriBilgileriTablo + "-"
                    self.tarih_musteriUrunSati_musteriBilgileriTablo += ay_musteriUrunSatis_musteriBilgileriTablo + "-"
                    self.tarih_musteriUrunSati_musteriBilgileriTablo += gun_musteriUrunSatis_musteriBilgileriTablo

                    self.musteriUrunSatisFiyatWithTL = "{:.2f}".format(self.musteriUrunSatis_Devir) + " ₺"

                    self.file_musteriUrunSatisDetaylariDosyayaIsle.write(
                        self.tarih_musteriUrunSati_musteriBilgileriTablo + "," +
                        self.comboBox_musteriUrunSatis_urunAdi.currentText() + "," +
                        "{:.2f}".format(self.doubleSpinBox_musteriUrunSatis_maliyet.value()) + " ₺" + "," +
                        str(self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.value()) + " ADET" + "," +
                        "-----" + "," + "-----" + "," +
                        str(self.label_musteriUrunSatis_tutar_sonuc.text()) + " ₺" + "," +
                        "-----" + "," +
                        self.musteriUrunSatisFiyatWithTL + "," +
                        self.label_musteriUrunSatis_islemKimligi_detay.text() + "\n")
                    self.file_musteriUrunSatisDetaylariDosyayaIsle.close()

                    self.file_musteriUrunSatis_anlikDevirDATfile = open(
                        "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_KayitliMusteri.currentText() +
                        " - Devir.dat", "w", encoding='utf-8')
                    self.file_musteriUrunSatis_anlikDevirDATfile.write("{:.2f}".format(self.musteriUrunSatis_Devir))
                    self.file_musteriUrunSatis_anlikDevirDATfile.close()
                    self.randURNST()
            except Exception as e:
                self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    ## MÜŞTERİDEN ALINAN ÖDEME QComboBox İŞLEMLERİ
    def musteridenAlinanOdemeDetaylari_Idx0Control_csvYazdir(self):
        try:
            if self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentIndex() == 0:
                self.lutfenMusteriSecinizMessageBox()
            elif self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value() == 0:
                self.lutfenGecerliBirTutarGiriniz()
            elif self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentIndex() == 0:
                self.lutfenOdemeSekliSecinizMessageBox()
            elif self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentIndex() == 0:
                self.lutfenAraciKurumSecinizMessageBox()
            elif self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text() == "":
                self.lutfenAciklamaGirinizMessageBox()
            else:
                if self.actionHerIslemdeOnaySor.isChecked() == True:
                    box = QMessageBox()
                    box.setIcon(QMessageBox.Question)
                    box.setWindowTitle('İşlem Kontrolü!')
                    box.setText("MÜŞTERİ'den alınan ÖDEME detayları;\n\n" +
                                "Müşteri Adı : " + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() +"\n" +
                                "Tarih : " +
                                str(self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019) + "-" +
                                str(self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2) + "-" +
                                str(self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2) + "\n" +
                                "Ödeme Şekli : " + str(self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText()) + "\n" +
                                "Ödeme Kurumu : " + str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "\n" +
                                "Ödemeyi Alan Kişi : " + self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text() + "\n" +
                                "Tutar : " + str(self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺\n\n" +
                                "olan işlemi onaylıyor musunuz?")
                    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    buttonY = box.button(QMessageBox.Yes)
                    buttonY.setText('Evet')
                    buttonN = box.button(QMessageBox.No)
                    buttonN.setText('İptal')
                    box.exec_()
                    if box.clickedButton() == buttonY:
                        myCommaCheck = self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text()
                        regex = re.compile(',')
                        if (regex.search(myCommaCheck) == None):
                            # İlgili Müşteri Dosyasına Yaz
                            self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile = open(
                                "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() +
                                " - Devir.dat", "r", encoding='utf-8')
                            self.musteridenAlinanOdemeDetaylari_Devir = float(
                                self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.read())
                            print("İşlem öncesi devir: " + str(self.musteridenAlinanOdemeDetaylari_Devir))
                            self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.close()

                            self.musteridenAlinanOdemeDetaylari_Devir -= float(
                                self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value())
                            print("İşlem sonrası devir: " + str(self.musteridenAlinanOdemeDetaylari_Devir))

                            self.file_musteridenAlinanOdemeDetaylariDosyayaIsle = open(
                                "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() + ".csv",
                                "a",
                                encoding='utf-8')
                            yil_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019)
                            ay_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2)
                            gun_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2)

                            self.file_musteridenAlinanOdemeDetaylariDosyayaIsle.write(
                                yil_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                ay_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                gun_musteridenAlinanOdeme_musteriBilgileriTablo + "," +

                                "-----" + "," + "-----" + "," + "-----" + "," +
                                str(self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText()) + "," +
                                str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "," +
                                "{:.2f}".format(
                                    self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺" + "," +
                                str(self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text()) + "," +
                                "{:.2f}".format(self.musteridenAlinanOdemeDetaylari_Devir) + " ₺" + "," +
                                self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.text() + "\n")
                            self.file_musteridenAlinanOdemeDetaylariDosyayaIsle.close()

                            self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile = open(
                                "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() +
                                " - Devir.dat", "w", encoding='utf-8')
                            self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.write(
                                "{:.2f}".format(self.musteridenAlinanOdemeDetaylari_Devir))
                            self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.close()

                            try:
                                # Kasa Hesabına Yaz
                                self.file_kasaHesabi_anlikDevirDATfile = open(
                                    "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() +
                                    " - Devir.dat", "r", encoding='utf-8')
                                self.kasaHesabi_Devir = float(self.file_kasaHesabi_anlikDevirDATfile.read())
                                print("İşlem öncesi devir: " + str(self.kasaHesabi_Devir))
                                self.file_kasaHesabi_anlikDevirDATfile.close()

                                self.kasaHesabi_Devir += float(
                                    self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value())
                                print("İşlem sonrası devir: " + str(self.kasaHesabi_Devir))

                                if self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() == "Nakit":
                                    self.file_kasaHesabiDosyayaIsle = open(
                                        "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() + ".csv",
                                        "a",
                                        encoding='utf-8')

                                    gun_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2)
                                    ay_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2)
                                    yil_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019)
                                    self.file_kasaHesabiDosyayaIsle.write(
                                        yil_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                        ay_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                        gun_musteridenAlinanOdeme_musteriBilgileriTablo + "," +

                                        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() + "," +
                                        "{:.2f}".format(
                                            self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺" + "," +
                                        str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "," +
                                        "{:.2f}".format(self.kasaHesabi_Devir) + " ₺" + "\n")
                                    self.file_kasaHesabiDosyayaIsle.close()

                                    self.file_kasaHesabi_anlikDevirDATfile = open(
                                        "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() +
                                        " - Devir.dat", "w", encoding='utf-8')
                                    self.file_kasaHesabi_anlikDevirDATfile.write(
                                        "{:.2f}".format(self.kasaHesabi_Devir))
                                    self.file_kasaHesabi_anlikDevirDATfile.close()
                                elif self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() == "Çek":
                                    self.file_kasaHesabiDosyayaIsle = open(
                                        "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() + ".csv",
                                        "a",
                                        encoding='utf-8')

                                    gun_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2)
                                    ay_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2)
                                    yil_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019)
                                    self.file_kasaHesabiDosyayaIsle.write(
                                        yil_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                        ay_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                        gun_musteridenAlinanOdeme_musteriBilgileriTablo + "," +

                                        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() + "," +
                                        "{:.2f}".format(
                                            self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺" + "," +
                                        str(self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text()) + "," +
                                        str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "," +
                                        "{:.2f}".format(self.kasaHesabi_Devir) + " ₺" + "\n")
                                    self.file_kasaHesabiDosyayaIsle.close()

                                    self.file_kasaHesabi_anlikDevirDATfile = open(
                                        "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() +
                                        " - Devir.dat", "w", encoding='utf-8')
                                    self.file_kasaHesabi_anlikDevirDATfile.write(
                                        "{:.2f}".format(self.kasaHesabi_Devir))
                                    self.file_kasaHesabi_anlikDevirDATfile.close()
                                else:
                                    print("Farklı bir seçim yapıldığı için işleme devam edilemiyor.")
                            except Exception as e:
                                self.lutfenYapimciylaIletisimeGecinMessageBox(e)
                            self.randODMAL()
                        else:
                            self.lutfenVirgulKullanmayinMessageBox()
                    else:
                        print("no")

                else:
                    myCommaCheck = self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text()
                    regex = re.compile(',')
                    if (regex.search(myCommaCheck) == None):
                        # İlgili Müşteri Dosyasına Yaz
                        self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile = open(
                            "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() +
                            " - Devir.dat", "r", encoding='utf-8')
                        self.musteridenAlinanOdemeDetaylari_Devir = float(
                            self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.read())
                        print("İşlem öncesi devir: " + str(self.musteridenAlinanOdemeDetaylari_Devir))
                        self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.close()

                        self.musteridenAlinanOdemeDetaylari_Devir -= float(
                            self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value())
                        print("İşlem sonrası devir: " + str(self.musteridenAlinanOdemeDetaylari_Devir))

                        self.file_musteridenAlinanOdemeDetaylariDosyayaIsle = open(
                            "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() + ".csv",
                            "a",
                            encoding='utf-8')
                        yil_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                            self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019)
                        ay_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                            self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2)
                        gun_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                            self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2)

                        self.file_musteridenAlinanOdemeDetaylariDosyayaIsle.write(
                            yil_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                            ay_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                            gun_musteridenAlinanOdeme_musteriBilgileriTablo + "," +

                            "-----" + "," + "-----" + "," + "-----" + "," +
                            str(self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText()) + "," +
                            str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "," +
                            "{:.2f}".format(
                                self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺" + "," +
                            str(self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text()) + "," +
                            "{:.2f}".format(self.musteridenAlinanOdemeDetaylari_Devir) + " ₺" + "," +
                            self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.text() + "\n")
                        self.file_musteridenAlinanOdemeDetaylariDosyayaIsle.close()

                        self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile = open(
                            "datastore/MUSTERI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() +
                            " - Devir.dat", "w", encoding='utf-8')
                        self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.write(
                            "{:.2f}".format(self.musteridenAlinanOdemeDetaylari_Devir))
                        self.file_musteridenAlinanOdemeDetaylari_anlikDevirDATfile.close()

                        try:
                            # Kasa Hesabına Yaz
                            self.file_kasaHesabi_anlikDevirDATfile = open(
                                "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() +
                                " - Devir.dat", "r", encoding='utf-8')
                            self.kasaHesabi_Devir = float(self.file_kasaHesabi_anlikDevirDATfile.read())
                            print("İşlem öncesi devir: " + str(self.kasaHesabi_Devir))
                            self.file_kasaHesabi_anlikDevirDATfile.close()

                            self.kasaHesabi_Devir += float(
                                self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value())
                            print("İşlem sonrası devir: " + str(self.kasaHesabi_Devir))

                            if self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() == "Nakit":
                                self.file_kasaHesabiDosyayaIsle = open(
                                    "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() + ".csv",
                                    "a",
                                    encoding='utf-8')

                                gun_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                    self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2)
                                ay_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                    self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2)
                                yil_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                    self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019)
                                self.file_kasaHesabiDosyayaIsle.write(
                                    yil_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                    ay_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                    gun_musteridenAlinanOdeme_musteriBilgileriTablo + "," +

                                    self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() + "," +
                                    "{:.2f}".format(
                                        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺" + "," +
                                    str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "," +
                                    "{:.2f}".format(self.kasaHesabi_Devir) + " ₺" + "\n")
                                self.file_kasaHesabiDosyayaIsle.close()

                                self.file_kasaHesabi_anlikDevirDATfile = open(
                                    "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() +
                                    " - Devir.dat", "w", encoding='utf-8')
                                self.file_kasaHesabi_anlikDevirDATfile.write(
                                    "{:.2f}".format(self.kasaHesabi_Devir))
                                self.file_kasaHesabi_anlikDevirDATfile.close()
                            elif self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() == "Çek":
                                self.file_kasaHesabiDosyayaIsle = open(
                                    "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() + ".csv",
                                    "a",
                                    encoding='utf-8')

                                gun_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                    self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.currentIndex()).zfill(2)
                                ay_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                    self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.currentIndex()).zfill(2)
                                yil_musteridenAlinanOdeme_musteriBilgileriTablo = str(
                                    self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.currentIndex() + 2019)
                                self.file_kasaHesabiDosyayaIsle.write(
                                    yil_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                    ay_musteridenAlinanOdeme_musteriBilgileriTablo + "-" +
                                    gun_musteridenAlinanOdeme_musteriBilgileriTablo + "," +

                                    self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.currentText() + "," +
                                    "{:.2f}".format(
                                        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.value()) + " ₺" + "," +
                                    str(self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.text()) + "," +
                                    str(self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.currentText()) + "," +
                                    "{:.2f}".format(self.kasaHesabi_Devir) + " ₺" + "\n")
                                self.file_kasaHesabiDosyayaIsle.close()

                                self.file_kasaHesabi_anlikDevirDATfile = open(
                                    "datastore/KASAHESABI/" + self.comboBox_musteriUrunSatis_AlinanOdeme_turu.currentText() +
                                    " - Devir.dat", "w", encoding='utf-8')
                                self.file_kasaHesabi_anlikDevirDATfile.write(
                                    "{:.2f}".format(self.kasaHesabi_Devir))
                                self.file_kasaHesabi_anlikDevirDATfile.close()
                            else:
                                print("Farklı bir seçim yapıldığı için işleme devam edilemiyor.")
                        except Exception as e:
                            self.lutfenYapimciylaIletisimeGecinMessageBox(e)
                        self.randODMAL()
                    else:
                        self.lutfenVirgulKullanmayinMessageBox()

        except Exception as e:
            print(e)
    ####################################################################################################################


    ####################################################################################################################
    # Genel Para Durumu Bilgileri
    def alacakVerecekGoster(self):
        try:
            tum_musteriler = []
            df_file_tum_musteriler = pd.read_csv("datastore/kisiler.csv")
            df_file_tum_musteriler = df_file_tum_musteriler[(df_file_tum_musteriler["MÜŞTERİ/MÜSTAHSİL"] == "MÜŞTERİ")]
            tum_musteriler = list(set(df_file_tum_musteriler["AD SOYAD"].values))
            tum_musteriler = sorted(tum_musteriler)
            print(tum_musteriler)
            tmp_list_musteriler = []
            totalAlacak = 0
            for alacak in (tum_musteriler):
                tmp_file_musteriler = open("datastore/MUSTERI/" + alacak + " - Devir.dat", "r", encoding='utf-8')
                tmp_devir_musteriler = float(tmp_file_musteriler.read())
                if tmp_devir_musteriler == 0:
                    totalAlacak+=tmp_devir_musteriler
                    tmp_list_musteriler.append("{:.2f}".format(abs(tmp_devir_musteriler)) + " ₺ - (ALACAK YOK)")
                    tmp_file_musteriler.close()
                elif tmp_devir_musteriler > 0:
                    totalAlacak+=tmp_devir_musteriler
                    tmp_list_musteriler.append("{:.2f}".format(abs(tmp_devir_musteriler)) + " ₺ - (ALACAK)")
                    tmp_file_musteriler.close()
                else:
                    totalAlacak+=tmp_devir_musteriler
                    tmp_list_musteriler.append("{:.2f}".format(abs(tmp_devir_musteriler)) + " ₺ - (FAZLA ÖDEME)")
                    tmp_file_musteriler.close()
            alacakDict = {"MÜŞTERİLER": tum_musteriler, "ALACAK MİKTARI": tmp_list_musteriler}
            df_alacakBilgileri = pd.DataFrame.from_dict(alacakDict)
            print(df_alacakBilgileri)
            if totalAlacak == 0:
                self.label_hesapOzeti_toplamAlacak_TL.setText("{:.2f} ₺ - (ALACAK KALMADI)".format(abs(totalAlacak)))
            elif totalAlacak > 0:
                self.label_hesapOzeti_toplamAlacak_TL.setText("{:.2f} ₺ - (ALACAK VAR)".format(abs(totalAlacak)))
            else:
                self.label_hesapOzeti_toplamAlacak_TL.setText("{:.2f} ₺ - (FAZLA ÖDEME)".format(abs(totalAlacak)))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_alacakBilgileri.setFont(font)
            model_alacakBilgileri = PandasModel(df_alacakBilgileri)
            self.tableView_alacakBilgileri.setModel(model_alacakBilgileri)
            self.tableView_alacakBilgileri.horizontalHeader().setStretchLastSection(True)
            #self.tableView_alacakBilgileri.setSortingEnabled(True)
            self.tableView_alacakBilgileri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


            tum_mustahsiller = []
            df_file_tum_mustahsiller = pd.read_csv("datastore/kisiler.csv")
            df_file_tum_mustahsiller = df_file_tum_mustahsiller[
                (df_file_tum_mustahsiller["MÜŞTERİ/MÜSTAHSİL"] == "MÜSTAHSİL")]
            tum_mustahsiller = list(set(df_file_tum_mustahsiller["AD SOYAD"].values))
            tum_mustahsiller = sorted(tum_mustahsiller)
            print(tum_mustahsiller)
            totalBorc = 0
            tmp_list_mustahsiller = []
            for borc in (tum_mustahsiller):
                tmp_file_mustahsiller = open("datastore/MUSTAHSIL/" + borc + " - Devir.dat", "r", encoding='utf-8')
                tmp_devir_mustahsiller = float(tmp_file_mustahsiller.read())
                if tmp_devir_mustahsiller == 0:
                    totalBorc += tmp_devir_mustahsiller
                    tmp_list_mustahsiller.append("{:.2f}".format(abs(tmp_devir_mustahsiller)) + " ₺ - (BORÇ YOK)")
                    tmp_file_mustahsiller.close()
                elif tmp_devir_mustahsiller < 0:
                    totalBorc += tmp_devir_mustahsiller
                    tmp_list_mustahsiller.append("{:.2f}".format(abs(tmp_devir_mustahsiller)) + " ₺ - (BORÇ)")
                    tmp_file_mustahsiller.close()
                else:
                    totalBorc += tmp_devir_mustahsiller
                    tmp_list_mustahsiller.append("{:.2f}".format(abs(tmp_devir_mustahsiller)) + " ₺ - (FAZLA ÖDEME)")
                    tmp_file_mustahsiller.close()
            borcDict = {"MÜSTAHSİLLER": tum_mustahsiller, "BORÇ MİKTARI": tmp_list_mustahsiller}
            df_borcBilgileri = pd.DataFrame.from_dict(borcDict)
            print(df_borcBilgileri)
            if totalBorc == 0:
                self.label_hesapOzeti_toplamBorc_TL.setText("{:.2f} ₺ - (BORÇ KALMADI)".format(abs(totalBorc)))
            elif totalBorc < 0:
                self.label_hesapOzeti_toplamBorc_TL.setText("{:.2f} ₺ - (BORÇ VAR)".format(abs(totalBorc)))
            else:
                self.label_hesapOzeti_toplamBorc_TL.setText("{:.2f} ₺ - (FAZLA ÖDEME)".format(abs(totalBorc)))

            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_borcBilgileri.setFont(font)
            model_borcBilgileri = PandasModel(df_borcBilgileri)
            self.tableView_borcBilgileri.setModel(model_borcBilgileri)
            self.tableView_borcBilgileri.horizontalHeader().setStretchLastSection(True)
            #self.tableView_borcBilgileri.setSortingEnabled(True)
            self.tableView_borcBilgileri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        except Exception as e: print(e)
    def kasaHesabiGoster(self):
        if self.comboBox_kasaHesabi_odemeTuru.currentIndex() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen <b>ÖDEME TÜRÜ</b> seçerek işleme devam edin...")
            msg.setWindowTitle("Ödeme Türü Seçilmedi")
            msg.exec_()
        else:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_kasaHesabi.setFont(font)
            self.df_kasaHesabiGoster = pd.read_csv(
                "datastore/KASAHESABI/" + self.comboBox_kasaHesabi_odemeTuru.currentText() + ".csv")
            model_kasaHesabiGoster = PandasModel(self.df_kasaHesabiGoster)
            self.tableView_kasaHesabi.setModel(model_kasaHesabiGoster)
            self.tableView_kasaHesabi.horizontalHeader().setStretchLastSection(True)
            self.tableView_kasaHesabi.setSortingEnabled(True)
            self.tableView_kasaHesabi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ####################################################################################################################


    ####################################################################################################################
    ## MÜSTAHSİL BİLGİLERİNİ GÖSTERME FONKSİYONLARI
    def gosterilecekMustahsilSec(self):
        if self.comboBox_mustahsilBilgileri_kayitliMustahsil.currentIndex()==0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen <b>MÜSTAHSİL</b> seçerek işleme devam edin...")
            msg.setWindowTitle("Müstahsil Seçilmedi")
            msg.exec_()
        else:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_mustahsilBilgileri.setFont(font)
            self.df_mustahsilBilgileriniGoster = pd.read_csv(
                "datastore/MUSTAHSIL/" + self.comboBox_mustahsilBilgileri_kayitliMustahsil.currentText() + ".csv")
            model_mustahsilBilgileriniGoster = PandasModel(self.df_mustahsilBilgileriniGoster)
            self.tableView_mustahsilBilgileri.setModel(model_mustahsilBilgileriniGoster)
            #self.tableView_mustahsilBilgileri.setSortingEnabled(True)
            #self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
            self.tableView_mustahsilBilgileri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ## MÜŞTERİ BİLGİLERİNİ GÖSTERME FONKSİYONLARI
    def gosterilecekMusteriSec(self):
        if self.comboBox_musteriBilgileri_kayitliMusteri.currentIndex() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen <b>MÜŞTERİ</b> seçerek işleme devam edin...")
            msg.setWindowTitle("Müstahsil Seçilmedi")
            msg.exec_()
        else:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_musteriBilgileri.setFont(font)
            self.df_musteriBilgileriniGoster = pd.read_csv(
                "datastore/MUSTERI/" + self.comboBox_musteriBilgileri_kayitliMusteri.currentText() + ".csv")
            model_musteriBilgileriniGoster = PandasModel(self.df_musteriBilgileriniGoster)
            self.tableView_musteriBilgileri.setModel(model_musteriBilgileriniGoster)
            #self.tableView_musteriBilgileri.horizontalHeader().setStretchLastSection(True)
            self.tableView_musteriBilgileri.setSortingEnabled(False)
            self.tableView_musteriBilgileri.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ## MALZEMELER BİLGİLERİNİ GÖSTERME FONKSİYONLARI
    def musteriAldigiMalzelerGoster(self):
        if self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentIndex() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen <b>MÜŞTERİ</b> seçerek işleme devam edin...")
            msg.setWindowTitle("Müşteri Seçilmedi")
            msg.exec_()
        else:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_musteriAldigiMalzemeler.setFont(font)
            self.df_musteriAldigiMalzemelerGoster = pd.read_csv(
                "datastore/MUSTERI/" + self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv")
            model_musteriAldigiMalzemelerGoster = PandasModel(self.df_musteriAldigiMalzemelerGoster)
            self.tableView_musteriAldigiMalzemeler.setModel(model_musteriAldigiMalzemelerGoster)
            self.tableView_musteriAldigiMalzemeler.setSortingEnabled(True)
            self.tableView_musteriAldigiMalzemeler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView_musteriAldigiMalzemeler.horizontalHeader().setStretchLastSection(True)
    def xTekrarDEF(self):
        try:
            self.df_xTekrar = pd.read_csv("datastore/MUSTERI/" +
                                          self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + ".csv")
            list_xTekrar = list(set(self.df_xTekrar["TARİH"].values))

            if len(list_xTekrar) == 0:
                self.musteriAldigiMalzelerGoster()
            else:
                for i in range(len(list_xTekrar)):
                    xGonder = list_xTekrar[i]
                    self.musterininAldigiUrunler(xGonder)
        except Exception as e:
            print(e)
    def musterininAldigiUrunler(self,mau_tarih):
        try:
            self.df_tarihFiltresi = pd.read_csv("datastore/MUSTERI/" +
                                                self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + ".csv")
            self.df_forMAU = pd.read_csv("datastore/MUSTERI/" +
                                         self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv")
            print(mau_tarih + " var mı ?")
            print(mau_tarih in self.df_forMAU["TARİH"].values)
            if (self.df_forMAU['TARİH'] == mau_tarih).any():
                #self.df_forMAU.drop(self.df_forMAU.tail(1).index, inplace=True)
                self.df_forMAU.to_csv("datastore/MUSTERI/" +
                                      self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv",
                                      index=False, encoding='utf-8')
                listForFill = []
                for lsd in range(len(list(self.df_forMAU))):
                    listForFill.append("-----")
                myLc = self.df_forMAU[self.df_forMAU['TARİH'] == mau_tarih].index.item()
                self.df_forMAU.loc[myLc] = listForFill
                # self.df_forMAU.loc[-1] = listForFill
                self.df_forMAU.loc[self.df_forMAU["TARİH"] == "-----", "TARİH"] = str(mau_tarih)
                self.df_forMAU.to_csv("datastore/MUSTERI/" +
                                      self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv",
                                      index=False, encoding='utf-8')
            else:
                listForFill = []
                for lsd in range(len(list(self.df_forMAU))):
                    listForFill.append("-----")
                self.df_forMAU.loc[-1] = listForFill
                self.df_forMAU.loc[self.df_forMAU["TARİH"] == "-----", "TARİH"] = str(mau_tarih)
                self.df_forMAU.to_csv("datastore/MUSTERI/" +
                                      self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv",
                                      index=False, encoding='utf-8')

            self.df_tarihFiltresi = self.df_tarihFiltresi[(self.df_tarihFiltresi["TARİH"] == mau_tarih)]
            theProductList = list(set(self.df_tarihFiltresi["ÜRÜN ADI"].tolist()))
            theProductList = sorted(theProductList)
            print("Ürünler : ")
            print(theProductList)
            for theValueP in theProductList:
                try:
                    self.df_urunAdi_P = self.df_tarihFiltresi[(self.df_tarihFiltresi["ÜRÜN ADI"] == theValueP)]
                    theCostP = self.df_urunAdi_P["MALİYET"].values
                    for i in range(len(theCostP)):
                        theCostP[i] = theCostP[i][:-1]
                    theCostP[i] = list(map(float, theCostP))
                    theQtyP = self.df_urunAdi_P["ADET"].values
                    for i in range(len(theQtyP)):
                        theQtyP_tmp = theQtyP[i].split()
                        theQtyP[i] = theQtyP_tmp[0]
                    theQtyP[i] = list(map(int, theQtyP))
                    sum_theQtyP = sum(theQtyP[i])
                    the_total = [theQtyP[i][j] * theCostP[i][j] for j in range(len(theCostP[i]))]
                    sum_the_total = sum(the_total)
                    the_avg = round(sum_the_total / sum_theQtyP, 2)
                    print(".....{}.....{}.....{}".format(sum_theQtyP, sum_the_total, the_avg))
                    print("Ürün : {}\n"
                          "Ort. Maliyet : {:.2f}\n"
                          "Toplam Adet : {}".format(theValueP, the_avg, sum_theQtyP))
                    print()
                    contentP_tmp = str(the_avg) + " ₺ x " + str(sum_theQtyP) + " ADET"
                    self.df_newDFP = pd.read_csv("datastore/MUSTERI/" +
                                                 self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv")

                    self.df_newDFP.loc[self.df_newDFP["TARİH"] == str(mau_tarih), theValueP] = str(contentP_tmp)
                    self.df_newDFP.to_csv("datastore/MUSTERI/" +
                                          self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.currentText() + " - Aldığı Malzemeler.csv",
                                          index=False, encoding='utf-8')
                except ValueError:
                    continue
                except Exception as e: print(e)
            self.musteriAldigiMalzelerGoster()
        except Exception as e:
            print(e)
    ####################################################################################################################


    ####################################################################################################################
                                                ##### TÜM SERA İŞLEMLERİ #####
    ## SERA GELİR/GİDER TUTAR YAZDIRMA
    def seraGelirBugununGeliri_SonucTutarYaz(self):
        self.seraGelirBugununGeliri_SonucTutarYaz_temp = round(self.doublespinBox_seraGelir_maliyet.value() * self.spinBox_seraGelir_adet.value(), 3)
        self.label_seraGelir_bugununGeliriTutarSonuc.setText('{:.2f}'.format(self.seraGelirBugununGeliri_SonucTutarYaz_temp))
    def seraGiderBugununGeliri_SonucTutarYaz(self):
        self.seraGiderBugununGideri_SonucTutarYaz_temp = round(
            self.doubleSpinBox_seraGider_elemanGideri.value() + self.doubleSpinBox_seraGider_yemekGideri.value() +
            self.doubleSpinBox_seraGider_mazotGideri.value() + self.doubleSpinBox_seraGider_digerGiderler.value(), 3)
        self.label_seraGider_bugununToplamGideri_sonuc.setText('{:.2f}'.format(self.seraGiderBugununGideri_SonucTutarYaz_temp))

    ## Sera Ekle
    def seraEkle(self):
        yeniSeraEkle_text, ok = QInputDialog.getText(self, 'Yeni Sera Ekle',
                                                     'Eklenecek <b>YENİ SERA</b> ismini giriniz :')
        if ok:
            if self.actionHerIslemdeOnaySor.isChecked() == True:
                box = QMessageBox()
                box.setIcon(QMessageBox.Question)
                box.setWindowTitle('İşlem Kontrolü!')
                box.setText("Eklenecek olan sera adı: \n\n" +
                            str(yeniSeraEkle_text) + "\n\n" +
                            "işlemini onaylıyor musunuz?")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                buttonY = box.button(QMessageBox.Yes)
                buttonY.setText('Evet')
                buttonN = box.button(QMessageBox.No)
                buttonN.setText('İptal')
                box.exec_()
                if box.clickedButton() == buttonY:
                    self.ilgiliSeraDosyalariniOlustur(str(yeniSeraEkle_text))
                else:
                    print("no")
    def ilgiliSeraDosyalariniOlustur(self,YENISERA):
        try:
            # seralar.DAT dosyasina yeni sera ismi işlendi
            file_seralarDATdosyasinaEkle = open("datastore/SERALAR/seralar.dat", "a+", encoding='utf-8')
            file_seralarDATdosyasinaEkle.write(YENISERA + "\n")
            file_seralarDATdosyasinaEkle.close()

            # tablolar için sera gelir dosyasi oluşturuluyor
            seraGelirHeaders = "TARİH,SATILAN ÜRÜN,FİYAT,ADET,TUTAR,GELİR DEVİR"
            file_yeniSera_seraGelir = open("datastore/SERALAR/GELIR/" + YENISERA + ".csv", "a+", encoding='utf-8')
            file_yeniSera_seraGelir.write(seraGelirHeaders + "\n")
            file_yeniSera_seraGelir.close()
            # tablolar için sera gelir devir dosyalasi oluşturuluyor
            file_yeniSera_seraGelirDevir = open("datastore/SERALAR/GELIR/" + YENISERA + " - Devir.dat", "w+",
                                                encoding='utf-8')
            file_yeniSera_seraGelirDevir.write("0.0")
            file_yeniSera_seraGelirDevir.close()

            # tablolar için sera gider dosyasi oluşturuluyor
            seraGiderHeaders = "TARİH,ELEMAN GİDERİ,YEMEK GİDERİ,MAZOT GİDERİ,DİĞER GİDER,AÇIKLAMA,TOPLAM,GİDER DEVİR"
            file_yeniSera_seraGider = open("datastore/SERALAR/GIDER/" + YENISERA + ".csv", "a+", encoding='utf-8')
            file_yeniSera_seraGider.write(seraGiderHeaders + "\n")
            file_yeniSera_seraGider.close()
            # tablolar için sera gider devir dosyalasi oluşturuluyor
            file_yeniSera_seraGiderDevir = open("datastore/SERALAR/GIDER/" + YENISERA + " - Devir.dat", "w+",
                                                encoding='utf-8')
            file_yeniSera_seraGiderDevir.write("0.0")
            file_yeniSera_seraGiderDevir.close()
            self.tumSeraSecmeQComboBoxlariniDoldur()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Hata Kodu --> {}".format(e))
            msg.setWindowTitle("Exception")
            msg.exec_()

    ##SERALARI QComboBox'a yazdır
    def tumSeraSecmeQComboBoxlariniDoldur(self):
        self.comboBox_seraGelir_seralar.clear()
        self.comboBox_seraGelir_seralar.addItem("Sera Seçiniz")
        self.comboBox_seraGelirSonuc_seralar.clear()
        self.comboBox_seraGelirSonuc_seralar.addItem("Sera Seçiniz")
        self.comboBox_seraGider_seralar.clear()
        self.comboBox_seraGider_seralar.addItem("Sera Seçiniz")
        self.comboBox_seraGiderSonuc_seralar.clear()
        self.comboBox_seraGiderSonuc_seralar.addItem("Sera Seçiniz")
        listFor_seraComboBoxesFill = []
        self.file_seraComboBoxesFill =  open("datastore/SERALAR/seralar.dat", "r", encoding="UTF-8")
        for i in self.file_seraComboBoxesFill:
            listFor_seraComboBoxesFill.append(i.strip())
        sorted_listFor_seraComboBoxesFill = sorted(listFor_seraComboBoxesFill, key=str.lower)
        for i in range(len(sorted_listFor_seraComboBoxesFill)):
            self.comboBox_seraGelir_seralar.addItem(sorted_listFor_seraComboBoxesFill[i])
            self.comboBox_seraGelirSonuc_seralar.addItem(sorted_listFor_seraComboBoxesFill[i])
            self.comboBox_seraGider_seralar.addItem(sorted_listFor_seraComboBoxesFill[i])
            self.comboBox_seraGiderSonuc_seralar.addItem(sorted_listFor_seraComboBoxesFill[i])

    ## Sera Gelir-Gider Yazdırma
    def seraGelirOnayla(self):
        if self.comboBox_seraGelir_seralar.currentIndex() == 0:
            self.lutfenSeraSecinizMessageBox()
        elif self.comboBox_seraGelir_urunAdi.currentIndex() == 0:
            self.lutfenUrunSecinizMessageBox()
        elif self.doublespinBox_seraGelir_maliyet.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.spinBox_seraGelir_adet.value() == 0:
            self.lutfenGecerliBirAdetGiriniz()
        else:
            try:
                if self.actionHerIslemdeOnaySor.isChecked() == True:
                    box = QMessageBox()
                    box.setIcon(QMessageBox.Question)
                    box.setWindowTitle('İşlem Kontrolü!')
                    box.setText("Sera Gelir detayları;\n\n" +
                                "Sera Adı : " + self.comboBox_seraGelir_seralar.currentText() +"\n" +
                                "Tarih : " +
                                str(self.comboBox_seraGelir_tarihSec_yil.currentIndex() + 2019) + "-" +
                                str(self.comboBox_seraGelir_tarihSec_ay.currentIndex()).zfill(2) + "-" +
                                str(self.comboBox_seraGelir_tarihSec_gun.currentIndex()).zfill(2) + "\n" +
                                "Ürün Adı : " + self.comboBox_seraGelir_urunAdi.currentText() + "\n" +
                                "Maliyet : " + str(self.doublespinBox_seraGelir_maliyet.value()) + " ₺\n" +
                                "Adet : " + str(self.spinBox_seraGelir_adet.value()) + "\n" +
                                "Tutar : " + str(self.label_seraGelir_bugununGeliriTutarSonuc.text()) + " ₺\n\n" +
                                "olan işlemi onaylıyor musunuz?")
                    box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    buttonY = box.button(QMessageBox.Yes)
                    buttonY.setText('Evet')
                    buttonN = box.button(QMessageBox.No)
                    buttonN.setText('İptal')
                    box.exec_()
                    if box.clickedButton() == buttonY:
                        # Devir dosyadan oku ve yazdır
                        file_seraGelir_anlikDevirDATfile = open(
                            "datastore/SERALAR/GELIR/" + self.comboBox_seraGelir_seralar.currentText() +
                            " - Devir.dat", "r", encoding='utf-8')

                        seraGelir_Devir = float(file_seraGelir_anlikDevirDATfile.read())
                        print("İşlem öncesi devir: " + str(seraGelir_Devir))
                        file_seraGelir_anlikDevirDATfile.close()

                        seraGelir_Devir += float(self.seraGelirBugununGeliri_SonucTutarYaz_temp)
                        print("İşlem sonrası devir: " + str(seraGelir_Devir))

                        file_seraGelir_anlikDevirDATfile = open(
                            "datastore/SERALAR/GELIR/" + self.comboBox_seraGelir_seralar.currentText() +
                            " - Devir.dat", "w", encoding='utf-8')
                        file_seraGelir_anlikDevirDATfile.write("{:.2f}".format(seraGelir_Devir))
                        file_seraGelir_anlikDevirDATfile.close()

                        # Verilerin detaylarını csv dosyasına yaz

                        file_seraGelirDosyayaIsle = open(
                            "datastore/SERALAR/GELIR/" + self.comboBox_seraGelir_seralar.currentText() + ".csv", "a",
                            encoding='utf-8')

                        gun_seraGelir = str(self.comboBox_seraGelir_tarihSec_gun.currentIndex()).zfill(2)
                        ay_seraGelir = str(self.comboBox_seraGelir_tarihSec_ay.currentIndex()).zfill(2)
                        yil_seraGelir = str(self.comboBox_seraGelir_tarihSec_yil.currentIndex() + 2019)

                        tarih_seraGelir = ""
                        tarih_seraGelir += yil_seraGelir + "-"
                        tarih_seraGelir += ay_seraGelir + "-"
                        tarih_seraGelir += gun_seraGelir

                        # seraGelir_Devir_TL = "{:.2f}".format(seraGelir_Devir) + " ₺"

                        file_seraGelirDosyayaIsle.write(
                            tarih_seraGelir + "," +
                            # self.comboBox_seraGelir_seralar.currentText() + "," +
                            self.comboBox_seraGelir_urunAdi.currentText() + "," +
                            "{:.2f}".format(self.doublespinBox_seraGelir_maliyet.value()) + " ₺" + "," +
                            str(self.spinBox_seraGelir_adet.value()) + " ADET" + "," +
                            str(self.label_seraGelir_bugununGeliriTutarSonuc.text()) + " ₺" + "," +
                            "{:.2f}".format(seraGelir_Devir) + " ₺" + "\n")
                        file_seraGelirDosyayaIsle.close()
                    else:
                        print("no")
                else:
                    # Devir dosyadan oku ve yazdır
                    file_seraGelir_anlikDevirDATfile = open(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelir_seralar.currentText() +
                        " - Devir.dat", "r", encoding='utf-8')

                    seraGelir_Devir = float(file_seraGelir_anlikDevirDATfile.read())
                    print("İşlem öncesi devir: " + str(seraGelir_Devir))
                    file_seraGelir_anlikDevirDATfile.close()

                    seraGelir_Devir += float(self.seraGelirBugununGeliri_SonucTutarYaz_temp)
                    print("İşlem sonrası devir: " + str(seraGelir_Devir))

                    file_seraGelir_anlikDevirDATfile = open(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelir_seralar.currentText() +
                        " - Devir.dat", "w", encoding='utf-8')
                    file_seraGelir_anlikDevirDATfile.write("{:.2f}".format(seraGelir_Devir))
                    file_seraGelir_anlikDevirDATfile.close()

                    # Verilerin detaylarını csv dosyasına yaz

                    file_seraGelirDosyayaIsle = open(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelir_seralar.currentText() + ".csv", "a",
                        encoding='utf-8')

                    gun_seraGelir = str(self.comboBox_seraGelir_tarihSec_gun.currentIndex()).zfill(2)
                    ay_seraGelir = str(self.comboBox_seraGelir_tarihSec_ay.currentIndex()).zfill(2)
                    yil_seraGelir = str(self.comboBox_seraGelir_tarihSec_yil.currentIndex() + 2019)

                    tarih_seraGelir = ""
                    tarih_seraGelir += yil_seraGelir + "-"
                    tarih_seraGelir += ay_seraGelir + "-"
                    tarih_seraGelir += gun_seraGelir

                    # seraGelir_Devir_TL = "{:.2f}".format(seraGelir_Devir) + " ₺"

                    file_seraGelirDosyayaIsle.write(
                        tarih_seraGelir + "," +
                        # self.comboBox_seraGelir_seralar.currentText() + "," +
                        self.comboBox_seraGelir_urunAdi.currentText() + "," +
                        "{:.2f}".format(self.doublespinBox_seraGelir_maliyet.value()) + " ₺" + "," +
                        str(self.spinBox_seraGelir_adet.value()) + " ADET" + "," +
                        str(self.label_seraGelir_bugununGeliriTutarSonuc.text()) + " ₺" + "," +
                        "{:.2f}".format(seraGelir_Devir) + " ₺" + "\n")
                    file_seraGelirDosyayaIsle.close()
            except Exception as e:
                self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    def seraGiderOnayla(self):
        if self.comboBox_seraGider_seralar.currentIndex() == 0:
            self.lutfenSeraSecinizMessageBox()
        elif self.doubleSpinBox_seraGider_elemanGideri.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.doubleSpinBox_seraGider_yemekGideri.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.doubleSpinBox_seraGider_mazotGideri.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.doubleSpinBox_seraGider_digerGiderler.value() == 0.00:
            self.lutfenGecerliBirTutarGiriniz()
        elif self.lineEdit_seraGider_aciklama.text() == "":
            self.lutfenAciklamaGirinizMessageBox()
        else:
            if self.actionHerIslemdeOnaySor.isChecked() == True:
                box = QMessageBox()
                box.setIcon(QMessageBox.Question)
                box.setWindowTitle('İşlem Kontrolü!')
                box.setText("Sera Gelir detayları;\n\n" +
                            "Sera Adı : " + self.comboBox_seraGider_seralar.currentText() + "\n" +
                            "Tarih : " +
                            str(self.comboBox_seraGider_tarihSec_yil.currentIndex() + 2019) + "-" +
                            str(self.comboBox_seraGider_tarihSec_ay.currentIndex()).zfill(2) + "-" +
                            str(self.comboBox_seraGider_tarihSec_gun.currentIndex()).zfill(2) + "\n" +
                            "Eleman Gideri : " + str(self.doubleSpinBox_seraGider_elemanGideri.value()) + " ₺\n" +
                            "Yemek Gideri : " + str(self.doubleSpinBox_seraGider_yemekGideri.value()) + " ₺\n" +
                            "Mazot Gideri : " + str(self.doubleSpinBox_seraGider_mazotGideri.value()) + " ₺\n" +
                            "Diğer Giderler : " + str(self.doubleSpinBox_seraGider_digerGiderler.value()) + " ₺\n" +
                            "Açıklama : " + self.lineEdit_seraGider_aciklama.text() + "\n" +
                            "Tutar : " + str(self.label_seraGider_bugununToplamGideri_sonuc.text()) + " ₺\n\n" +
                            "olan işlemi onaylıyor musunuz?")
                box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                buttonY = box.button(QMessageBox.Yes)
                buttonY.setText('Evet')
                buttonN = box.button(QMessageBox.No)
                buttonN.setText('İptal')
                box.exec_()
                if box.clickedButton() == buttonY:
                    myCommaCheck = self.lineEdit_seraGider_aciklama.text()
                    regex = re.compile(',')
                    if (regex.search(myCommaCheck) == None):
                        try:
                            # Devir dosyadan oku ve yazdır
                            file_seraGider_anlikDevirDATfile = open(
                                "datastore/SERALAR/GIDER/" + self.comboBox_seraGider_seralar.currentText() +
                                " - Devir.dat", "r", encoding='utf-8')

                            seraGider_Devir = float(file_seraGider_anlikDevirDATfile.read())
                            print("İşlem öncesi devir: " + str(seraGider_Devir))
                            file_seraGider_anlikDevirDATfile.close()

                            seraGider_Devir += float(self.seraGiderBugununGideri_SonucTutarYaz_temp)
                            print("İşlem sonrası devir: " + str(seraGider_Devir))

                            file_seraGider_anlikDevirDATfile = open(
                                "datastore/SERALAR/GIDER/" + self.comboBox_seraGider_seralar.currentText() +
                                " - Devir.dat", "w", encoding='utf-8')
                            file_seraGider_anlikDevirDATfile.write("{:.2f}".format(seraGider_Devir))
                            file_seraGider_anlikDevirDATfile.close()

                            # Verilerin detaylarını csv dosyasına yaz

                            file_seraGiderDosyayaIsle = open(
                                "datastore/SERALAR/GIDER/" + self.comboBox_seraGider_seralar.currentText() + ".csv",
                                "a",
                                encoding='utf-8')

                            gun_seraGider = str(self.comboBox_seraGider_tarihSec_gun.currentIndex()).zfill(2)
                            ay_seraGider = str(self.comboBox_seraGider_tarihSec_ay.currentIndex()).zfill(2)
                            yil_seraGider = str(self.comboBox_seraGider_tarihSec_yil.currentIndex() + 2019)

                            tarih_seraGider = ""
                            tarih_seraGider += yil_seraGider + "-"
                            tarih_seraGider += ay_seraGider + "-"
                            tarih_seraGider += gun_seraGider

                            # seraGider_Devir_TL = "{:.2f}".format(seraGider_Devir) + " ₺"
                            '''TARİH,SERA İSMİ,ELEMAN GİDERİ,YEMEK GİDERİ,MAZOT GİDERİ,DİĞER GİDER,AÇIKLAMA,TOPLAM,GİDER DEVİR'''
                            file_seraGiderDosyayaIsle.write(
                                tarih_seraGider + "," +
                                # self.comboBox_seraGider_seralar.currentText() + "," +
                                "{:.2f}".format(self.doubleSpinBox_seraGider_elemanGideri.value()) + " ₺" + "," +
                                "{:.2f}".format(self.doubleSpinBox_seraGider_yemekGideri.value()) + " ₺" + "," +
                                "{:.2f}".format(self.doubleSpinBox_seraGider_mazotGideri.value()) + " ₺" + "," +
                                "{:.2f}".format(self.doubleSpinBox_seraGider_digerGiderler.value()) + " ₺" + "," +
                                self.lineEdit_seraGider_aciklama.text() + "," +
                                self.label_seraGider_bugununToplamGideri_sonuc.text() + " ₺" + "," +
                                "{:.2f}".format(seraGider_Devir) + " ₺" + "\n")
                            file_seraGiderDosyayaIsle.close()
                        except Exception as e:
                            print(e)
                    else:
                        self.lutfenVirgulKullanmayinMessageBox()
                else:
                    print("no")
            else:
                myCommaCheck = self.lineEdit_seraGider_aciklama.text()
                regex = re.compile(',')
                if (regex.search(myCommaCheck) == None):
                    try:
                        # Devir dosyadan oku ve yazdır
                        file_seraGider_anlikDevirDATfile = open(
                            "datastore/SERALAR/GIDER/" + self.comboBox_seraGider_seralar.currentText() +
                            " - Devir.dat", "r", encoding='utf-8')

                        seraGider_Devir = float(file_seraGider_anlikDevirDATfile.read())
                        print("İşlem öncesi devir: " + str(seraGider_Devir))
                        file_seraGider_anlikDevirDATfile.close()

                        seraGider_Devir += float(self.seraGiderBugununGideri_SonucTutarYaz_temp)
                        print("İşlem sonrası devir: " + str(seraGider_Devir))

                        file_seraGider_anlikDevirDATfile = open(
                            "datastore/SERALAR/GIDER/" + self.comboBox_seraGider_seralar.currentText() +
                            " - Devir.dat", "w", encoding='utf-8')
                        file_seraGider_anlikDevirDATfile.write("{:.2f}".format(seraGider_Devir))
                        file_seraGider_anlikDevirDATfile.close()

                        # Verilerin detaylarını csv dosyasına yaz

                        file_seraGiderDosyayaIsle = open(
                            "datastore/SERALAR/GIDER/" + self.comboBox_seraGider_seralar.currentText() + ".csv", "a",
                            encoding='utf-8')

                        gun_seraGider = str(self.comboBox_seraGider_tarihSec_gun.currentIndex()).zfill(2)
                        ay_seraGider = str(self.comboBox_seraGider_tarihSec_ay.currentIndex()).zfill(2)
                        yil_seraGider = str(self.comboBox_seraGider_tarihSec_yil.currentIndex() + 2019)

                        tarih_seraGider = ""
                        tarih_seraGider += yil_seraGider + "-"
                        tarih_seraGider += ay_seraGider + "-"
                        tarih_seraGider += gun_seraGider

                        # seraGider_Devir_TL = "{:.2f}".format(seraGider_Devir) + " ₺"
                        '''TARİH,SERA İSMİ,ELEMAN GİDERİ,YEMEK GİDERİ,MAZOT GİDERİ,DİĞER GİDER,AÇIKLAMA,TOPLAM,GİDER DEVİR'''
                        file_seraGiderDosyayaIsle.write(
                            tarih_seraGider + "," +
                            # self.comboBox_seraGider_seralar.currentText() + "," +
                            "{:.2f}".format(self.doubleSpinBox_seraGider_elemanGideri.value()) + " ₺" + "," +
                            "{:.2f}".format(self.doubleSpinBox_seraGider_yemekGideri.value()) + " ₺" + "," +
                            "{:.2f}".format(self.doubleSpinBox_seraGider_mazotGideri.value()) + " ₺" + "," +
                            "{:.2f}".format(self.doubleSpinBox_seraGider_digerGiderler.value()) + " ₺" + "," +
                            self.lineEdit_seraGider_aciklama.text() + "," +
                            self.label_seraGider_bugununToplamGideri_sonuc.text() + " ₺" + "," +
                            "{:.2f}".format(seraGider_Devir) + " ₺" + "\n")
                        file_seraGiderDosyayaIsle.close()
                    except Exception as e:
                        print(e)
                else:
                    self.lutfenVirgulKullanmayinMessageBox()


    ## Sera Tabloları
    def seraGelirTablosu(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_seraGelirSonuc.setFont(font)
            if self.comboBox_seraGelirSonuc_seralar.currentText() == "Sera Seçiniz":
                self.lutfenSeraSecinizMessageBox()
            else:
                if self.comboBox_seraGelirSonuc_urunler.currentText() == "Hepsi":
                    df_seraGelir = pd.read_csv(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelirSonuc_seralar.currentText() + ".csv")

                    model_seraGelir = PandasModel(df_seraGelir)
                    self.tableView_seraGelirSonuc.setModel(model_seraGelir)
                    # self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
                    self.tableView_seraGelirSonuc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                else:
                    df_seraGelir = pd.read_csv(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelirSonuc_seralar.currentText() + ".csv")
                    df_seraGelir = df_seraGelir[
                        (df_seraGelir["SATILAN ÜRÜN"] == self.comboBox_seraGelirSonuc_urunler.currentText())]

                    df_seraGelir['TUTAR'] = df_seraGelir['TUTAR'].str.replace(r' ₺', '')
                    df_seraGelir['TUTAR'] = df_seraGelir['TUTAR'].astype(float)
                    df_seraGelir['ADET'] = df_seraGelir['ADET'].str.replace(r' ADET', '')
                    df_seraGelir['ADET'] = df_seraGelir['ADET'].astype(int)
                    df_seraGelir['FİYAT'] = df_seraGelir['FİYAT'].str.replace(r' ₺', '')
                    df_seraGelir['FİYAT'] = df_seraGelir['FİYAT'].astype(float)

                    ortalama = round((df_seraGelir['TUTAR'].sum()) / (df_seraGelir['ADET'].sum()),2)

                    # df_seraGelir.loc['Column_Total'] = df_seraGelir.sum(numeric_only=True, axis=0)
                    df_seraGelir.loc['DİP TOPLAM'] = pd.Series(
                        [ortalama, df_seraGelir['ADET'].sum(), df_seraGelir['TUTAR'].sum()],
                        index=['FİYAT', 'ADET', 'TUTAR'])
                    df_seraGelir['FİYAT'] = df_seraGelir['FİYAT'].astype(str) + ' ₺'
                    df_seraGelir['ADET'] = df_seraGelir['ADET'].astype(str) + ' ADET'
                    df_seraGelir['TUTAR'] = df_seraGelir['TUTAR'].astype(str) + ' ₺'
                    df_seraGelir['FİYAT']['DİP TOPLAM'] = "ORTALAMA : " + df_seraGelir['FİYAT']['DİP TOPLAM']

                    df_seraGelir = df_seraGelir.replace(np.nan, '-', regex=True)

                    model_seraGelir = PandasModel(df_seraGelir)
                    self.tableView_seraGelirSonuc.setModel(model_seraGelir)
                    # self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
                    self.tableView_seraGelirSonuc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)

    ## Sera Tabloları
    def seraGelirTablosu_tarihFiltresi(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_seraGelirSonuc.setFont(font)
            if self.comboBox_seraGelirSonuc_seralar.currentText() == "Sera Seçiniz":
                self.lutfenSeraSecinizMessageBox()
            else:
                if self.comboBox_seraGelirSonuc_urunler.currentText() == "Hepsi":
                    df_seraGelir = pd.read_csv(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelirSonuc_seralar.currentText() + ".csv")

                    df_seraGelir['TARİH'] = pd.to_datetime(df_seraGelir['TARİH'])

                    start_date = ""
                    start_date += str(self.comboBox_seraGelirSonuc_baslangicTarihiYil.currentIndex() + 2019) + "-"
                    start_date += str(self.comboBox_seraGelirSonuc_baslangicTarihiAy.currentIndex()).zfill(2) + "-"
                    start_date += str(self.comboBox_seraGelirSonuc_baslangicTarihiGun.currentIndex()).zfill(2)

                    end_date = ""
                    end_date += str(self.comboBox_seraGelirSonuc_bitisTarihiYil.currentIndex() + 2019) + "-"
                    end_date += str(self.comboBox_seraGelirSonuc_bitisTarihiAy.currentIndex()).zfill(2) + "-"
                    end_date += str(self.comboBox_seraGelirSonuc_bitisTarihiGun.currentIndex()).zfill(2)

                    if start_date > end_date:
                        self.lutfenTarihDengesizligiMessageBox()
                    else:
                        print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")

                    print(start_date + " - " + end_date)

                    mask = (df_seraGelir['TARİH'] >= start_date) & (df_seraGelir['TARİH'] <= end_date)

                    df_seraGelir = df_seraGelir.loc[mask]
                    df_seraGelir['TARİH'] = df_seraGelir['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
                    print(df_seraGelir['TARİH'].values)

                    model_seraGelir = PandasModel(df_seraGelir)
                    self.tableView_seraGelirSonuc.setModel(model_seraGelir)
                    # self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
                    self.tableView_seraGelirSonuc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                else:
                    df_seraGelir = pd.read_csv(
                        "datastore/SERALAR/GELIR/" + self.comboBox_seraGelirSonuc_seralar.currentText() + ".csv")
                    df_seraGelir = df_seraGelir[
                        (df_seraGelir["SATILAN ÜRÜN"] == self.comboBox_seraGelirSonuc_urunler.currentText())]

                    df_seraGelir['TARİH'] = pd.to_datetime(df_seraGelir['TARİH'])

                    start_date = ""
                    start_date += str(self.comboBox_seraGelirSonuc_baslangicTarihiYil.currentIndex() + 2019) + "-"
                    start_date += str(self.comboBox_seraGelirSonuc_baslangicTarihiAy.currentIndex()).zfill(2) + "-"
                    start_date += str(self.comboBox_seraGelirSonuc_baslangicTarihiGun.currentIndex()).zfill(2)

                    end_date = ""
                    end_date += str(self.comboBox_seraGelirSonuc_bitisTarihiYil.currentIndex() + 2019) + "-"
                    end_date += str(self.comboBox_seraGelirSonuc_bitisTarihiAy.currentIndex()).zfill(2) + "-"
                    end_date += str(self.comboBox_seraGelirSonuc_bitisTarihiGun.currentIndex()).zfill(2)

                    if start_date > end_date:
                        self.lutfenTarihDengesizligiMessageBox()
                    else:
                        print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")
                    print(start_date + " - " + end_date)

                    mask = (df_seraGelir['TARİH'] >= start_date) & (df_seraGelir['TARİH'] <= end_date)

                    df_seraGelir = df_seraGelir.loc[mask]
                    df_seraGelir['TARİH'] = df_seraGelir['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
                    print(df_seraGelir['TARİH'].values)

                    df_seraGelir['TUTAR'] = df_seraGelir['TUTAR'].str.replace(r' ₺', '')
                    df_seraGelir['TUTAR'] = df_seraGelir['TUTAR'].astype(float)
                    df_seraGelir['ADET'] = df_seraGelir['ADET'].str.replace(r' ADET', '')
                    df_seraGelir['ADET'] = df_seraGelir['ADET'].astype(int)
                    df_seraGelir['FİYAT'] = df_seraGelir['FİYAT'].str.replace(r' ₺', '')
                    df_seraGelir['FİYAT'] = df_seraGelir['FİYAT'].astype(float)

                    ortalama = round((df_seraGelir['TUTAR'].sum()) / (df_seraGelir['ADET'].sum()),2)

                    # df_seraGelir.loc['Column_Total'] = df_seraGelir.sum(numeric_only=True, axis=0)
                    df_seraGelir.loc['DİP TOPLAM'] = pd.Series(
                        [ortalama, df_seraGelir['ADET'].sum(), df_seraGelir['TUTAR'].sum()],
                        index=['FİYAT', 'ADET', 'TUTAR'])
                    df_seraGelir['FİYAT'] = df_seraGelir['FİYAT'].astype(str) + ' ₺'
                    df_seraGelir['ADET'] = df_seraGelir['ADET'].astype(str) + ' ADET'
                    df_seraGelir['TUTAR'] = df_seraGelir['TUTAR'].astype(str) + ' ₺'
                    df_seraGelir['FİYAT']['DİP TOPLAM'] = "ORTALAMA : " + df_seraGelir['FİYAT']['DİP TOPLAM']

                    df_seraGelir = df_seraGelir.replace(np.nan, '-', regex=True)

                    model_seraGelir = PandasModel(df_seraGelir)
                    self.tableView_seraGelirSonuc.setModel(model_seraGelir)
                    # self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
                    self.tableView_seraGelirSonuc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)

    def seraGiderTablosu(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_seraGiderSonuc.setFont(font)
            if self.comboBox_seraGiderSonuc_seralar.currentText() == "Sera Seçiniz":
                self.lutfenSeraSecinizMessageBox()
            else:
                df_seraGider = pd.read_csv(
                    "datastore/SERALAR/GIDER/" + self.comboBox_seraGiderSonuc_seralar.currentText() + ".csv")

                df_seraGider['ELEMAN GİDERİ'] = df_seraGider['ELEMAN GİDERİ'].str.replace(r' ₺', '')
                df_seraGider['ELEMAN GİDERİ'] = df_seraGider['ELEMAN GİDERİ'].astype(float)
                df_seraGider['YEMEK GİDERİ'] = df_seraGider['YEMEK GİDERİ'].str.replace(r' ₺', '')
                df_seraGider['YEMEK GİDERİ'] = df_seraGider['YEMEK GİDERİ'].astype(float)
                df_seraGider['MAZOT GİDERİ'] = df_seraGider['MAZOT GİDERİ'].str.replace(r' ₺', '')
                df_seraGider['MAZOT GİDERİ'] = df_seraGider['MAZOT GİDERİ'].astype(float)
                df_seraGider['DİĞER GİDER'] = df_seraGider['DİĞER GİDER'].str.replace(r' ₺', '')
                df_seraGider['DİĞER GİDER'] = df_seraGider['DİĞER GİDER'].astype(float)
                df_seraGider['TOPLAM'] = df_seraGider['TOPLAM'].str.replace(r' ₺', '')
                df_seraGider['TOPLAM'] = df_seraGider['TOPLAM'].astype(float)

                elemanG = df_seraGider['ELEMAN GİDERİ'].sum()
                yemekG = df_seraGider['YEMEK GİDERİ'].sum()
                mazotG = df_seraGider['MAZOT GİDERİ'].sum()
                digerG = df_seraGider['DİĞER GİDER'].sum()
                toplamG = df_seraGider['TOPLAM'].sum()

                elemanO = df_seraGider['ELEMAN GİDERİ'].mean()
                yemekO = df_seraGider['YEMEK GİDERİ'].mean()
                mazotO = df_seraGider['MAZOT GİDERİ'].mean()
                digerO = df_seraGider['DİĞER GİDER'].mean()
                toplamO = df_seraGider['TOPLAM'].mean()

                df_seraGider.loc['DİP TOPLAM'] = pd.Series(
                    [elemanG, yemekG, mazotG,digerG,toplamG],
                    index=['ELEMAN GİDERİ', 'YEMEK GİDERİ', 'MAZOT GİDERİ','DİĞER GİDER','TOPLAM'])

                df_seraGider.loc['ORTALAMA'] = pd.Series(
                    [elemanO, yemekO, mazotO,digerO,toplamO],
                    index=['ELEMAN GİDERİ', 'YEMEK GİDERİ', 'MAZOT GİDERİ','DİĞER GİDER','TOPLAM'])





                df_seraGider['ELEMAN GİDERİ'] = df_seraGider['ELEMAN GİDERİ'].astype(str) + ' ₺'
                df_seraGider['YEMEK GİDERİ'] = df_seraGider['YEMEK GİDERİ'].astype(str) + ' ₺'
                df_seraGider['MAZOT GİDERİ'] = df_seraGider['MAZOT GİDERİ'].astype(str) + ' ₺'
                df_seraGider['DİĞER GİDER'] = df_seraGider['DİĞER GİDER'].astype(str) + ' ₺'
                df_seraGider['TOPLAM'] = df_seraGider['TOPLAM'].astype(str) + ' ₺'


                df_seraGider = df_seraGider.replace(np.nan, '-', regex=True)
                model_seraGider = PandasModel(df_seraGider)
                self.tableView_seraGiderSonuc.setModel(model_seraGider)
                # self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
                self.tableView_seraGiderSonuc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)
    def seraGiderTablosu_tarihFiltresi(self):
        try:
            font = QtGui.QFont()
            font.setPointSize(12)
            self.tableView_seraGiderSonuc.setFont(font)
            if self.comboBox_seraGiderSonuc_seralar.currentText() == "Sera Seçiniz":
                self.lutfenSeraSecinizMessageBox()
            else:
                df_seraGider = pd.read_csv(
                    "datastore/SERALAR/GIDER/" + self.comboBox_seraGiderSonuc_seralar.currentText() + ".csv")

                df_seraGider['TARİH'] = pd.to_datetime(df_seraGider['TARİH'])

                start_date = ""
                start_date += str(self.comboBox_seraGiderSonuc_baslangicTarihiYil.currentIndex() + 2019) + "-"
                start_date += str(self.comboBox_seraGiderSonuc_baslangicTarihiAy.currentIndex()).zfill(2) + "-"
                start_date += str(self.comboBox_seraGiderSonuc_baslangicTarihiGun.currentIndex()).zfill(2)

                end_date = ""
                end_date += str(self.comboBox_seraGiderSonuc_bitisTarihiYil.currentIndex() + 2019) + "-"
                end_date += str(self.comboBox_seraGiderSonuc_bitisTarihiAy.currentIndex()).zfill(2) + "-"
                end_date += str(self.comboBox_seraGiderSonuc_bitisTarihiGun.currentIndex()).zfill(2)

                if start_date > end_date:
                    self.lutfenTarihDengesizligiMessageBox()
                else:
                    print("Başlangıç ile Bitiş Tarihleri arasında herhangi bir sıkıntı yok")
                print(start_date + " - " + end_date)

                mask = (df_seraGider['TARİH'] >= start_date) & (df_seraGider['TARİH'] <= end_date)

                df_seraGider = df_seraGider.loc[mask]
                df_seraGider['TARİH'] = df_seraGider['TARİH'].apply(lambda x: x.strftime('%Y-%m-%d'))
                print(df_seraGider['TARİH'].values)

                df_seraGider['ELEMAN GİDERİ'] = df_seraGider['ELEMAN GİDERİ'].str.replace(r' ₺', '')
                df_seraGider['ELEMAN GİDERİ'] = df_seraGider['ELEMAN GİDERİ'].astype(float)
                df_seraGider['YEMEK GİDERİ'] = df_seraGider['YEMEK GİDERİ'].str.replace(r' ₺', '')
                df_seraGider['YEMEK GİDERİ'] = df_seraGider['YEMEK GİDERİ'].astype(float)
                df_seraGider['MAZOT GİDERİ'] = df_seraGider['MAZOT GİDERİ'].str.replace(r' ₺', '')
                df_seraGider['MAZOT GİDERİ'] = df_seraGider['MAZOT GİDERİ'].astype(float)
                df_seraGider['DİĞER GİDER'] = df_seraGider['DİĞER GİDER'].str.replace(r' ₺', '')
                df_seraGider['DİĞER GİDER'] = df_seraGider['DİĞER GİDER'].astype(float)
                df_seraGider['TOPLAM'] = df_seraGider['TOPLAM'].str.replace(r' ₺', '')
                df_seraGider['TOPLAM'] = df_seraGider['TOPLAM'].astype(float)

                elemanG = df_seraGider['ELEMAN GİDERİ'].sum()
                yemekG = df_seraGider['YEMEK GİDERİ'].sum()
                mazotG = df_seraGider['MAZOT GİDERİ'].sum()
                digerG = df_seraGider['DİĞER GİDER'].sum()
                toplamG = df_seraGider['TOPLAM'].sum()

                elemanO = round(df_seraGider['ELEMAN GİDERİ'].mean(),2)
                yemekO = round(df_seraGider['YEMEK GİDERİ'].mean(),2)
                mazotO = round(df_seraGider['MAZOT GİDERİ'].mean(),2)
                digerO = round(df_seraGider['DİĞER GİDER'].mean(),2)
                toplamO = round(df_seraGider['TOPLAM'].mean(),2)

                df_seraGider.loc['DİP TOPLAM'] = pd.Series(
                    [elemanG, yemekG, mazotG,digerG,toplamG],
                    index=['ELEMAN GİDERİ', 'YEMEK GİDERİ', 'MAZOT GİDERİ','DİĞER GİDER','TOPLAM'])

                df_seraGider.loc['ORTALAMA'] = pd.Series(
                    [elemanO, yemekO, mazotO,digerO,toplamO],
                    index=['ELEMAN GİDERİ', 'YEMEK GİDERİ', 'MAZOT GİDERİ','DİĞER GİDER','TOPLAM'])

                df_seraGider['ELEMAN GİDERİ'] = df_seraGider['ELEMAN GİDERİ'].astype(str) + ' ₺'
                df_seraGider['YEMEK GİDERİ'] = df_seraGider['YEMEK GİDERİ'].astype(str) + ' ₺'
                df_seraGider['MAZOT GİDERİ'] = df_seraGider['MAZOT GİDERİ'].astype(str) + ' ₺'
                df_seraGider['DİĞER GİDER'] = df_seraGider['DİĞER GİDER'].astype(str) + ' ₺'
                df_seraGider['TOPLAM'] = df_seraGider['TOPLAM'].astype(str) + ' ₺'

                df_seraGider = df_seraGider.replace(np.nan, '-', regex=True)
                model_seraGider = PandasModel(df_seraGider)
                self.tableView_seraGiderSonuc.setModel(model_seraGider)
                # self.tableView_mustahsilBilgileri.horizontalHeader().setStretchLastSection(True)
                self.tableView_seraGiderSonuc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            self.lutfenYapimciylaIletisimeGecinMessageBox(e)


    ####################################################################################################################
    # Ürün Ekleme İşlemleri İşlevleri
    def yeniUrunEkle(self):
        yeniUrunEkle_text, ok = QInputDialog.getText(self, 'Yeni Ürün Ekle',
                                                     'Müstahsillerden alınan yeni ürün ismini ekleyin :')
        if ok:
            self.urunlerDATdosyasinaUrunEkle(str(yeniUrunEkle_text))
    def urunlerDATdosyasinaUrunEkle(self,myStr):
        self.comboBox_mustahsildenUrunAl_urunAdi.clear()
        self.comboBox_musteriUrunSatis_urunAdi.clear()
        self.comboBox_seraGelir_urunAdi.clear()
        ################################################################################################################
        ## MÜSTAHSİL ÜRÜN ALIŞ SAYFASININ ÜRÜN COMBOBOX'I DATASTORE'DAN EKLENDİ
        file_urunlerDATdosyasinaUrunEkle = open("datastore/urunler.dat", "a", encoding="UTF-8")
        file_urunlerDATdosyasinaUrunEkle.write("\n"+myStr)
        file_urunlerDATdosyasinaUrunEkle.close()
        ################################################################################################################

        ################################################################################################################
        ## MÜSTAHSİL ÜRÜN ALIŞ SAYFASININ ÜRÜN COMBOBOX'I DATASTORE'DAN EKLENDİ
        self.comboBox_mustahsildenUrunAl_urunAdi.addItem("Ürün Seçiniz")
        self.comboBox_musteriUrunSatis_urunAdi.addItem("Ürün Seçiniz")
        self.comboBox_seraGelir_urunAdi.addItem("Ürün Seçiniz")

        listFor_yeniUrunEklendiktenSonrakiUrunAdi = []
        self.file_yeniUrunEklendiktenSonrakiUrunAdi = open("datastore/urunler.dat", "r", encoding="UTF-8")
        for i in self.file_yeniUrunEklendiktenSonrakiUrunAdi:
            listFor_yeniUrunEklendiktenSonrakiUrunAdi.append(i.strip())
        sorted_listFor_yeniUrunEklendiktenSonrakiUrunAdi = sorted(listFor_yeniUrunEklendiktenSonrakiUrunAdi, key=str.lower)
        for i in range(len(sorted_listFor_yeniUrunEklendiktenSonrakiUrunAdi)):
            self.comboBox_mustahsildenUrunAl_urunAdi.addItem(sorted_listFor_yeniUrunEklendiktenSonrakiUrunAdi[i])
            self.comboBox_musteriUrunSatis_urunAdi.addItem(sorted_listFor_yeniUrunEklendiktenSonrakiUrunAdi[i])
            self.comboBox_seraGelir_urunAdi.addItem(sorted_listFor_yeniUrunEklendiktenSonrakiUrunAdi[i])
        ################################################################################################################
    ####################################################################################################################


    ####################################################################################################################
    ## BOŞ QComboBox UYARILARI
    def lutfenYapimciylaIletisimeGecinMessageBox(self,x):
        print(x)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("<p>Daha önce karşılaşılmayan bir hata meydana geldi!</p>"
                    "<p>Lütfen yapımcıya hata kodunun fotoğrafını gönderiniz..!</p>"
                    "<p><b>Hata Kodu : {}</b></p>".format(x))
        msg.setWindowTitle("Bilinmeyen HATA!")
        msg.exec_()
    def lutfenMustahsilSecinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>MÜSTAHSİL</b> seçerek işleme devam edin...")
        msg.setWindowTitle("Müstahsil Seçilmedi")
        msg.exec_()
    def lutfenMusteriSecinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>MÜŞTERİ</b> seçerek işleme devam edin...")
        msg.setWindowTitle("Müşteri Seçilmedi")
        msg.exec_()
    def lutfenUrunSecinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>ÜRÜN</b> seçerek işleme devam edin...")
        msg.setWindowTitle("Ürün Seçilmedi")
        msg.exec_()
    def lutfenOdemeSekliSecinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>ÖDEME ŞEKLİ</b> seçerek işleme devam edin...")
        msg.setWindowTitle("Ödeme Şekli Seçilmedi")
        msg.exec_()
    def lutfenAraciKurumSecinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>ARACI KURUM</b> seçerek işleme devam edin...")
        msg.setWindowTitle("Aracı Kurum Seçilmedi")
        msg.exec_()
    def lutfenGecerliBirTutarGiriniz(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>0 ₺'den FARKLI, GEÇERLİ BİR TUTAR</b> girerek işleme devam edin...")
        msg.setWindowTitle("Tutar Girilmedi")
        msg.exec_()
    def lutfenGecerliBirAdetGiriniz(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>0'dan FARKLI, GEÇERLİ BİR ADET</b> girerek işleme devam edin...")
        msg.setWindowTitle("Adet Girilmedi")
        msg.exec_()
    def lutfenAciklamaGirinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>AÇIKLAMA</b> girerek işleme devam edin...")
        msg.setWindowTitle("Açıklama Girilmedi")
        msg.exec_()
    def lutfenAdGirinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>İSİM</b> kısmını boş bırakmayın...")
        msg.setWindowTitle("Açıklama Girilmedi")
        msg.exec_()
    def lutfenSoyadGirinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>SOYAD</b> kısmını boş bırakmayın...")
        msg.setWindowTitle("Açıklama Girilmedi")
        msg.exec_()
    def lutfenTelefonGirinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>TELEFON</b> kısmını boş bırakmayın...")
        msg.setWindowTitle("Açıklama Girilmedi")
        msg.exec_()
    def lutfenSehirGirinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>ŞEHİR</b> kısmını boş bırakmayın...")
        msg.setWindowTitle("Açıklama Girilmedi")
        msg.exec_()
    def lutfenVirgulKullanmayinMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>AÇIKLAMA KISIMLARINDA VİRGÜL</b> kullanmayın. Açıklamadaki virgül kullanımı "
                    "program yapısı gereği hataya sebebiyet verecektir!")
        msg.setWindowTitle("Virgül Kullanımı Hatası")
        msg.exec_()
    def lutfenSeraSecinizMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Lütfen <b>SERA</b> seçerek işleme devam edin...")
        msg.setWindowTitle("Sera Seçilmedi")
        msg.exec_()
    def lutfenTarihDengesizligiMessageBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("<b>Başlangıç Tarih</b>'i, <b>Bitiş Tarih</b>'den ileri bir zamanda OLAMAZ!")
        msg.setWindowTitle("Tarih Dengesizliği")
        msg.exec_()
    ####################################################################################################################
    def randURNAL(self):
        randNo = random.randint(1,9999999999)
        randNo_str = str(randNo).zfill(10)
        self.label_mustahsildenUrunAl_islemKimligi_detay.setText("URNAL-"+randNo_str)

    def randODMYP(self):
        randNo = random.randint(1, 9999999999)
        randNo_str = str(randNo).zfill(10)
        self.label_mustahsilOdemeDetaylari_islemKimligi_detay.setText("ODMYP-" + randNo_str)

    def randURNST(self):
        randNo = random.randint(1, 9999999999)
        randNo_str = str(randNo).zfill(10)
        self.label_musteriUrunSatis_islemKimligi_detay.setText("URNST-" + randNo_str)

    def randODMAL(self):
        randNo = random.randint(1, 9999999999)
        randNo_str = str(randNo).zfill(10)
        self.label_musteriUrunSatis_AlinanOdeme_islemKimligi_sonuc.setText("ODMAL-" + randNo_str)

    ####################################################################################################################
    ## STACKED WIDGET İŞLEMLERİ, SAYFA YÖNLENDİRMESİ
    def anasayfaGit(self):
        self.stackedWidget.setCurrentIndex(0)
    def mustahsilGit(self):
        self.stackedWidget.setCurrentIndex(1)
        self.randURNAL()
        self.comboBox_mustahsildenUrunAl_urunAdi.setCurrentIndex(0)
        self.doubleSpinBox.setValue(0)
        self.spinBox_mustahsildenUrunAl_adet.setValue(0)
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.setCurrentIndex(0)
        self.comboBox_mustahsildenUrunAl_urunAdi.model().item(0).setEnabled(False)
        self.comboBox_mustahsildenUrunAl_kayitliMustahsil.model().item(0).setEnabled(False)
    def mustahsileOdemeYapGit(self):
        self.stackedWidget.setCurrentIndex(2)
        self.randODMYP()
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.setCurrentIndex(0)
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.setCurrentIndex(0)
        self.comboBox_mustahsilOdemeKurumu.setCurrentIndex(0)
        self.doublespinBox_mustahsilOdemeDetaylari_mustahsilOdemeMiktari.setValue(0)
        self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.model().item(0).setEnabled(False)
        self.comboBox_mustahsilOdemeDetaylari_odemeSekli.model().item(0).setEnabled(False)
        self.comboBox_mustahsilOdemeKurumu.model().item(0).setEnabled(False)
    def musteriGit(self):
        self.stackedWidget.setCurrentIndex(3)
        self.randURNST()
        self.comboBox_musteriUrunSatis_KayitliMusteri.setCurrentIndex(0)
        self.comboBox_musteriUrunSatis_urunAdi.setCurrentIndex(0)
        self.doubleSpinBox_musteriUrunSatis_maliyet.setValue(0)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.setValue(0)
        self.comboBox_musteriUrunSatis_KayitliMusteri.model().item(0).setEnabled(False)
        self.comboBox_musteriUrunSatis_urunAdi.model().item(0).setEnabled(False)
    def musteridenOdemeAlGit(self):
        self.stackedWidget.setCurrentIndex(4)
        self.randODMAL()
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.setCurrentIndex(0)
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.setCurrentIndex(0)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.setCurrentIndex(0)
        self.doubleSpinBox_musteriUrunSatis_AlinanOdeme_miktar.setValue(0)
        self.lineEdit_musteriUrunSatis_AlinanOdeme_odemeyiAlanKisi.setText("")
        self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.model().item(0).setEnabled(False)
        self.comboBox_musteriUrunSatis_AlinanOdeme_turu.model().item(0).setEnabled(False)
        self.comboBox_musteriUrunSatis_AlinanOdeme_kurum.model().item(0).setEnabled(False)
    def kisiEkleGit(self):
        self.stackedWidget.setCurrentIndex(5)
        self.lineEdit_yeniKisi_ad.setText("")
        self.lineEdit_yeniKisi_soyad.setText("")
        self.lineEdit_yeniKisi_tel.setText("")
        self.lineEdit_yeniKisi_sehir.setText("")
    def urunGoruntuleGit(self):
        self.stackedWidget.setCurrentIndex(6)
    def kisiGoruntuleGit(self):
        self.stackedWidget.setCurrentIndex(7)
    def mustahsilDurumunuGoruntuleGit(self):
        self.stackedWidget.setCurrentIndex(8)
        self.pushButton_mustahsilBilgileri_tumVerileriGoster.clicked.connect(self.gosterilecekMustahsilSec)
    def musteriDurumunuGoruntuleGit(self):
        self.stackedWidget.setCurrentIndex(9)
        self.pushButton_musteriBilgileri_tumVerileriGoster.clicked.connect(self.gosterilecekMusteriSec)
    def alacaklarBorclarGit(self):
        self.stackedWidget.setCurrentIndex(10)
        self.alacakVerecekGoster()
    def kasaHesabGit(self):
        self.stackedWidget.setCurrentIndex(11)
        self.pushButton_kasaHesabi_onayla.clicked.connect(self.kasaHesabiGoster)
        self.pushButton_kasaHesabi_tarihlerArasiAramaYap.clicked.connect(self.kasaHesabi_tarihFiltresi)

    def seraGit(self):
        self.stackedWidget.setCurrentIndex(12)
        self.tumSeraSecmeQComboBoxlariniDoldur()
    def seraGelirSayfasinaGit(self):
        self.stackedWidget.setCurrentIndex(13)
        self.comboBox_seraGelir_seralar.model().item(0).setEnabled(False)
    def seraGelirGecmisKayitlaraGit(self):
        self.stackedWidget.setCurrentIndex(14)
        # self.comboBox_seraGelirSonuc_seralar.model().item(0).setEnabled(False)
    def seraGiderSayfasinaGit(self):
        self.stackedWidget.setCurrentIndex(15)
        self.comboBox_seraGider_seralar.model().item(0).setEnabled(False)
    def seraGiderGecmisKayitlaraGit(self):
        self.stackedWidget.setCurrentIndex(16)
        #self.comboBox_seraGiderSonuc_seralar.model().item(0).setEnabled(False)

    ####################################################################################################################





    ####################################################################################################################
    def bugununTarihleriniTumTarihQComboBoxlarinaYerlestir(self):
        ################################################################################################################
        # TARİHLERE BUGÜNÜN TARİHİNİ GİRME BAŞLANGIÇ
        self.comboBox_mustahsildenUrunAl_gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_mustahsildenUrunAl_ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_mustahsildenUrunAl_yil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_mustahsilOdemeDetaylari_gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_mustahsilOdemeDetaylari_ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_mustahsilOdemeDetaylari_yil.setCurrentIndex(gecerliTarih_yil - 2019)

        self.comboBox_musteriUrunSatis_Gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_musteriUrunSatis_Ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_musteriUrunSatis_Yil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_musteriUrunSatis_AlinanOdeme_Gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_musteriUrunSatis_AlinanOdeme_Yil.setCurrentIndex(gecerliTarih_yil - 2019)

        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Gun.setCurrentIndex(1)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Ay.setCurrentIndex(1)
        self.comboBox_musteriAldigiMalzemeler_baslangicTarihi_Yil.setCurrentIndex(1)

        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_musteriAldigiMalzemeler_bitisTarihi_Yil.setCurrentIndex(gecerliTarih_yil - 2019)

        self.comboBox_mustahsilBilgileri_baslangicTarihiGun.setCurrentIndex(1)
        self.comboBox_mustahsilBilgileri_baslangicTarihiAy.setCurrentIndex(1)
        self.comboBox_mustahsilBilgileri_baslangicTarihiYil.setCurrentIndex(1)

        self.comboBox_mustahsilBilgileri_bitisTarihiGun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_mustahsilBilgileri_bitisTarihiAy.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_mustahsilBilgileri_bitisTarihiYil.setCurrentIndex(gecerliTarih_yil - 2019)

        self.comboBox_musteriBilgileri_baslangicTarihiGun.setCurrentIndex(1)
        self.comboBox_musteriBilgileri_baslangicTarihiAy.setCurrentIndex(1)
        self.comboBox_musteriBilgileri_baslangicTarihiYil.setCurrentIndex(1)

        self.comboBox_musteriBilgileri_bitisTarihiGun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_musteriBilgileri_bitisTarihiAy.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_musteriBilgileri_bitisTarihiYil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_kasaHesabi_baslangicTarihiGun.setCurrentIndex(1)
        self.comboBox_kasaHesabi_baslangicTarihiAy.setCurrentIndex(1)
        self.comboBox_kasaHesabi_baslangicTarihiYil.setCurrentIndex(1)

        self.comboBox_kasaHesabi_bitisTarihiGun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_kasaHesabi_bitisTarihiAy.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_kasaHesabi_bitisTarihiYil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_seraGelir_tarihSec_gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_seraGelir_tarihSec_ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_seraGelir_tarihSec_yil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_seraGelirSonuc_baslangicTarihiGun.setCurrentIndex(1)
        self.comboBox_seraGelirSonuc_baslangicTarihiAy.setCurrentIndex(1)
        self.comboBox_seraGelirSonuc_baslangicTarihiYil.setCurrentIndex(1)

        self.comboBox_seraGelirSonuc_bitisTarihiGun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_seraGelirSonuc_bitisTarihiAy.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_seraGelirSonuc_bitisTarihiYil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_seraGider_tarihSec_gun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_seraGider_tarihSec_ay.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_seraGider_tarihSec_yil.setCurrentIndex(gecerliTarih_yil-2019)

        self.comboBox_seraGiderSonuc_baslangicTarihiGun.setCurrentIndex(1)
        self.comboBox_seraGiderSonuc_baslangicTarihiAy.setCurrentIndex(1)
        self.comboBox_seraGiderSonuc_baslangicTarihiYil.setCurrentIndex(1)

        self.comboBox_seraGiderSonuc_bitisTarihiGun.setCurrentIndex(gecerliTarih_gun)
        self.comboBox_seraGiderSonuc_bitisTarihiAy.setCurrentIndex(gecerliTarih_ay)
        self.comboBox_seraGiderSonuc_bitisTarihiYil.setCurrentIndex(gecerliTarih_yil-2019)
        # TARİHLERE BUGÜNÜN TARİHİNİ GİRME BİTTİ
        ####################
    def freshStartComboBoxFill(self):
        ################################################################################################################
        ## MÜSTAHSİLLER QComboBox'ları dolduruluyor
        self.df_mustahsilleriKisilerdenCek = pd.read_csv("datastore/kisiler.csv")
        self.df_mustahsilleriKisilerdenCek = self.df_mustahsilleriKisilerdenCek[(
                self.df_mustahsilleriKisilerdenCek["MÜŞTERİ/MÜSTAHSİL"] == "MÜSTAHSİL"
        )]
        self.mustahsiller_list = list(set(self.df_mustahsilleriKisilerdenCek["AD SOYAD"].values))
        # genel liste oluşturuldu
        self.sorted_mustahsiller_list = sorted(self.mustahsiller_list, key=str.lower)

        for i in range(len(self.mustahsiller_list)):
            self.comboBox_mustahsildenUrunAl_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
            self.comboBox_mustahsilOdemeDetaylari_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
            self.comboBox_mustahsilBilgileri_kayitliMustahsil.addItem(self.sorted_mustahsiller_list[i])
        ################################################################################################################



        ################################################################################################################
        ## MÜŞTERİLER QComboBox'ları dolduruluyor
        self.df_musterileriKisilerdenCek = pd.read_csv("datastore/kisiler.csv")
        self.df_musterileriKisilerdenCek = self.df_musterileriKisilerdenCek[(
                self.df_musterileriKisilerdenCek["MÜŞTERİ/MÜSTAHSİL"] == "MÜŞTERİ"
        )]
        self.musteriler_list = list(set(self.df_musterileriKisilerdenCek["AD SOYAD"].values))
        # genel liste oluşturuldu
        self.sorted_musteriler_list = sorted(self.musteriler_list, key=str.lower)

        for i in range(len(self.musteriler_list)):
            self.comboBox_musteriUrunSatis_KayitliMusteri.addItem(self.sorted_musteriler_list[i])
            self.comboBox_musteriUrunSatis_AlinanOdeme_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
            self.comboBox_musteriAldigiMalzemeler_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
            self.comboBox_musteriBilgileri_kayitliMusteri.addItem(self.sorted_musteriler_list[i])
        ################################################################################################################
    def otomatikTutarLabellariniYazdirma(self):
        ####################
        # Müstahsilden Ürün Alma İşlemi Tutar Yazdırma
        self.spinBox_mustahsildenUrunAl_adet.valueChanged.connect(self.mustahsildenUrunAl_SonucTutarYaz)
        self.doubleSpinBox.valueChanged.connect(self.mustahsildenUrunAl_SonucTutarYaz)
        ####################

        ####################
        # Müşteriye Ürün Satma İşlemi Tutar Yazdırma
        self.doubleSpinBox_musteriUrunSatis_maliyet.valueChanged.connect(self.musteriyeUrunSat_SonucTutarYaz)
        self.spinBox_mustahsilOdemeDetaylari_musteriUrunSatis_adet.valueChanged.connect(self.musteriyeUrunSat_SonucTutarYaz)
        ####################

        ####################
        # Sera Gelir Bugünün Geliri Tutar Yazdırma
        self.doublespinBox_seraGelir_maliyet.valueChanged.connect(self.seraGelirBugununGeliri_SonucTutarYaz)
        self.spinBox_seraGelir_adet.valueChanged.connect(self.seraGelirBugununGeliri_SonucTutarYaz)
        ####################

        ####################
        # Sera Gider Bugünün Gideri Tutar Yazdırma
        self.doubleSpinBox_seraGider_elemanGideri.valueChanged.connect(self.seraGiderBugununGeliri_SonucTutarYaz)
        self.doubleSpinBox_seraGider_yemekGideri.valueChanged.connect(self.seraGiderBugununGeliri_SonucTutarYaz)
        self.doubleSpinBox_seraGider_mazotGideri.valueChanged.connect(self.seraGiderBugununGeliri_SonucTutarYaz)
        self.doubleSpinBox_seraGider_digerGiderler.valueChanged.connect(self.seraGiderBugununGeliri_SonucTutarYaz)
        ####################
    ####################################################################################################################






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
