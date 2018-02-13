
import time
import random
class Kumanda():
    def __init__(self,tv_durum="kapali",tv_ses=0,kanal_list=["fox"],kanal='fox'):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_list=kanal_list
        self.kanal=kanal
    def tv_ac(self):
        if (self.tv_durum =="acik"):
            print('zaten acik')
        else:
            print('tv aciliyor')
            self.tv_durum="acik"
    def tv_kapa(self):
        if self.tv_durum=="kapali":
            print('tv zaten kapali aq')
        else:
            print('tv kapaniyor')
            self.tv_durum="kapali"
    def ses(self):
        while True:
            cevap=input("sesi azalt: '<'\nsesi arttir: '>'\ncikis: cikis")
            if cevap=='<':
                if self.tv_ses!=0:   
                
                    self.tv_ses-=1
                    print('ses=',self.tv_ses)
            elif cevap=='>': 
                   
                if self.tv_ses!=31:
                    self.tv_ses+=1
                    print('ses=',self.tv_ses)
                    
            else:
                    print('ses guncellendi',self.tv_ses)
                    break
    def kanal_ek(self,kanal_ismi):
        print('kanal ekleniyor...')
        time.sleep(0.5)
        self.kanal_list.append(kanal_ismi)
        print('kanal eklendi...')
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_list)-1)
        self.kanal=self.kanal_list[rastgele]
        print('su anki kanal',self.kanal)
    def __len__(self):
        return len(self.kanal_list)
    def __str__(self):
        return 'tv_durum={}, tv_ses={}, su anki kanal={} '.format(self.tv_durum,self.tv_ses,self.kanal)
kumanda=Kumanda()
 
print("""
            1.tv ac
            2.tv kapat
            3.ses ayarlari
            4.kanal ekle
            5.kanal sayisi ogrenme
            6.rastgele secme 
            7.tv bilgileri
            cikmak icin aq yaz
      """)  
while True:
    islem=input("islem seciniz:")
    if islem=='aq':
        print('program sonlandiriliyor')
        break
    elif islem=="1":
        kumanda.tv_ac()
    elif islem=="2":
        kumanda.tv_kapa()
    elif islem=="3":
        kumanda.ses()
    elif islem=="4":
        kanal_ismi=input("kanallari ',' ile ayir")
        kanal_list=kanal_ismi.split(",")
        for ekle in kanal_list:
            kumanda.kanal_ek(ekle)
    elif islem=="5":
        print(len(kumanda))
    elif islem=="6":
        kumanda.rastgele_kanal()
    elif islem=="7":
        print(kumanda)
    else:
        print('gecersiz islem')