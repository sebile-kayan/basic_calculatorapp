
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5.QtGui import  QIcon,QPalette,QColor     #BUnları da import ettiğimizi özellikle belirtmek istedik
from PyQt5.QtGui import *   # pyqt5.qtqui 'den tüm özellikleri import ettirir.
from PyQt5.QtWidgets import *
 

class Color(QWidget):     #Arka plan renklendirme için sınıf oluşturuyoruz.
    def __init__(self, color):
        super(Color,self).__init__()      #sınıfını ve nesnesini fonksiyon parametresi veriyoruz.
        self.setAutoFillBackground(True)    #Arka planı otomatikman boyasın.

        palette=self.palette()
        palette.setColor(QPalette.Window , QColor(color))
        self.setPalette(palette)



class mywindow(QMainWindow):             
    def __init__(self):      #Pencereyi oluşturuyoruz.
        super(mywindow,self).__init__()   ##class adını ve nesneyi içine yazıp init'i çağırdık.
        self.setWindowTitle("4 İŞLEM UYGULAMASI")    #Pencereye başlık atadık.
        self.setWindowIcon(QIcon("matt.jpg"))       #Pencerenin başlığının yanında icon simge olur.

        layout=QtWidgets.QVBoxLayout()       # ARKAPLAN RENK AYARLAMASI VLayout ile yatay şekilde birden çok renk oluşturur.
        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('yellow'))
        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        self.inita()  #fonksiyonu çağırdık.



    def inita(self):
       self.lbl_sayi1=QtWidgets.QLabel(self) #Oluşturduğumuz pencere içine label ekleyerek pencerenin iç kısmını oluşturmaya başladık. lbl_name'e widget ve labeller atandı onların özellikleri de kullanıma açık hale getirildi.
       self.lbl_sayi1.setText(" Sayı 1: ")   #setText labeli ekrana metin yazdırır.
       self.lbl_sayi1.setFont(QFont("Arial", 10))
       self.lbl_sayi1.move(700,350)    # lbl_sayi1 soldan 50 içeri,yukardan 30 içeri taşındı.
       self.lbl_sayi2=QtWidgets.QLabel(self)    #sayi2 için de pencerenin içinde metin oluşturalım.
       self.lbl_sayi2.setText(" Sayı 2: ")
       self.lbl_sayi2.move(700,400)
       self.lbl_sayi2.setFont(QFont("Arial", 10))     #Yazı boyut ve tipi değişimi
     

       self.txt_sayi1=QtWidgets.QLineEdit(self)     #Pencere içine metin kutusu ekledik QLineEdit ile.
       self.txt_sayi1.move(800,350)     #sayi1'in yanına metin kutusu ekledik. Soldan içeriliği farklı yukardan içeriliği aynı olmalı lbl_sayi1 ile.
       self.txt_sayi1.resize(200,32)   #Buton boyutunu ayarladık.
       self.txt_sayi2=QtWidgets.QLineEdit(self)     #Sayı2 için de metin kutusu ekledik.
       self.txt_sayi2.move(800,400) 
       self.txt_sayi2.resize(200,32)


       self.btn_topla=QtWidgets.QPushButton(self)     #Buton oluşturduk.
       self.btn_topla.setText(" Toplama:")
       self.btn_topla.move(800,505) 
       self.btn_topla.resize(200,50)
       self.btn_topla.clicked.connect(self.hesap)         # Butonların işlemlerin hepsini bir metoda hesap'a çağırdık.Ayrı ayrı yapmamak için.


       self.btn_cikar=QtWidgets.QPushButton(self)     #Buton oluşturduk.
       self.btn_cikar.setText(" Çıkarma:")
       self.btn_cikar.move(800,555)
       self.btn_cikar.resize(200,50)
       self.btn_cikar.clicked.connect(self.hesap)
     
       self.btn_carp=QtWidgets.QPushButton(self)     #Buton oluşturduk.
       self.btn_carp.setText(" Çarpma:")
       self.btn_carp.move(800,605)
       self.btn_carp.resize(200,50)
       self.btn_carp.clicked.connect(self.hesap)


       self.btn_bol=QtWidgets.QPushButton(self)     #Buton oluşturduk.
       self.btn_bol.setText(" Bölme:")
       self.btn_bol.move(800,655)
       self.btn_bol.resize(200,50)
       self.btn_bol.clicked.connect(self.hesap)

       
       self.lbl_resut=QtWidgets.QLabel(self)    #Yeni bir yer daha açıp boyut ayarladık top,cik,car,bo metodlarının içindekileri yazacak.
       self.lbl_resut.setText(" İşlem Sonucunuz:")
       
       self.lbl_resut.resize(300,150)
       self.lbl_resut.move(770,700)

       self.showMaximized()     #Pencereyi tam ekran yaptık.
       

       

    def hesap(self):     
        sender=self.sender().text()   #sender, hangi işlemi seçtiğimizi algılayan bir yapı.Yani çarp butonuna basınca sender text'i çarpma olur ona gider.
        result=0

        if sender==" Toplama:":
             result=int(self.txt_sayi1.text())+int(self.txt_sayi2.text()) 
        elif sender==" Çıkarma:":
             result=int(self.txt_sayi1.text())-int(self.txt_sayi2.text())     
        elif sender==" Çarpma:":
             result=int(self.txt_sayi1.text())*int(self.txt_sayi2.text())     
        elif sender==" Bölme:":
            result=int(self.txt_sayi1.text())/int(self.txt_sayi2.text())  
        
        self.lbl_resut.setText("İşlem Sonucunuz:"+str(result))    #result neye eşitlendiyse o işlemi yapacak.

        
        


             
  

def window():
      app=QApplication(sys.argv)         #sys.argv komut satırındakileri uygulamaya aktarır.
      win=mywindow()                  # Bir pencere açtık.
    
    #EKRANA YANSITMA.
      win.show()            #Pencereyi ekrana yansıttık
      sys.exit(app.exec_())  #Çarpıya basınca pencere kapansın diye.


window()     #Fonksiyonu çağırdık.
    