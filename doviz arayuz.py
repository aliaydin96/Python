import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QRadioButton, QLineEdit

class Doviz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):

        yazi_alani = QLabel("Kurlarinizi secin:",self)
        yazi_alani.move(10,10)
        yazi1 = QLabel("Birinci Doviz Birimi:",self)
        yazi1.move(10, 60 )
        yazi2 = QLabel("Ikinci Doviz Birimi:",self)
        yazi2.move(10,110)
        birinci = QLineEdit("",self)
        birinci.move(100,60)
        ikinci = QLineEdit("",self)
        ikinci.move(100,110)
        yazi3 = QLabel("Miktar:",self)
        yazi3.move(10,160)
        miktar = QLineEdit("",self)
        miktar.move(100,160)
        yazi_alani1 = QLabel("Sonuc:",self)
        yazi_alani1.move(10,210)
        sonuc = QLineEdit("",self)
        sonuc.move(100,210)
        buton = QPushButton("Hesapla", self)
        buton.move(50,300)

        self.setGeometry(300, 300, 250, 350)
        buton.clicked.connect(lambda : self.click(birinci, ikinci, miktar, sonuc))
        self.setWindowTitle("Doviz")
        self.show()

    def click(self, birinci, ikinci, miktar, sonuc):
        s=self.kurlar(birinci.text(), ikinci.text(), miktar.text())
        sonuc.setText(str(s))

    def kurlar(self,bir, iki, miktar):
        url = "http://api.fixer.io/latest?base="
        response = requests.get(url + bir )
        json_verisi = response.json()
        sonuc = json_verisi["rates"][iki] * float(miktar)
        return sonuc




app = QApplication(sys.argv)
doviz = Doviz()

sys.exit(app.exec_())

