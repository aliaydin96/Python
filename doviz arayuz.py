import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication,QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QRadioButton, QLineEdit

class Doviz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QLabel("Kurlarinizi secin")
        self.yazi1 = QLabel("Birinci Doviz Birimi:")
        self.yazi2 = QLabel("Ikinci Doviz Birimi:")
        self.yazi3 = QLabel("*******************")
        self.birinci = QLineEdit("")
        self.ikinci = QLineEdit("")
        self.yazi4 = QLabel("Miktar:")
        self.miktar = QLineEdit("")
        self.yazi_alani1 = QLabel("Sonuc:")
        self.sonuc = QLineEdit("")
        self.buton = QPushButton("Hesapla")
        vbox = QVBoxLayout()
        vbox.addWidget(self.yazi_alani)
        hbox = QHBoxLayout()
        hbox.addWidget(self.yazi1)
        hbox.addWidget(self.birinci)
        vbox.addWidget(self.yazi3)
        vbox.addStretch()
        hbox.addStretch()
        hbox.addWidget(self.yazi2)
        hbox.addWidget(self.ikinci)
        hbox.addWidget(self.yazi4)
        hbox.addWidget(self.miktar)
        vbox.addStretch()
        hbox.addWidget(self.yazi_alani1)
        hbox.addWidget(self.sonuc)
        hbox.addWidget(self.buton)

        vbox.addLayout(hbox)
        #hbox.addLayout(vbox)
        self.setLayout(vbox)
        #self.setLayout(hbox)
        self.buton.clicked.connect(lambda : self.click(self.birinci, self.ikinci, self.miktar, self.sonuc))
        self.setWindowTitle("Doviz")
        self.show()

    def click(self, birinci, ikinci, miktar, sonuc):
        try:
            s=self.kurlar(birinci.text(), ikinci.text(), miktar.text())
            sonuc.setText(str(s))
        except:
            sys.stderr.write("Bir sorun olustu")
            sys.stderr.flush()

    def kurlar(self,bir, iki, miktar):
        url = "http://api.fixer.io/latest?base="
        response = requests.get(url + bir )
        json_verisi = response.json()
        sonuc = json_verisi["rates"][iki] * float(miktar)
        return sonuc




app = QApplication(sys.argv)
doviz = Doviz()
sys.exit(app.exec_())
