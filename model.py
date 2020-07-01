# class Uporabnik:
#     def __init__(self, uporabnisko_ime, zasifrirano_geslo, podatki):
#         self.uporabnisko_ime = uporabnisko_ime
#         self.zasifrirano_geslo = zasifrirano_geslo
#         self.podatki = podatki
    
#     def preveri_geslo(self, zasifrirano_geslo):
#         if self.zasifrirano_geslo != zasifrirano_geslo:
#             raise ValueError('Geslo je napačno!')
    
#     def shrani_stanje(self, ime_datoteke):
#         slovar_stanja = {
#             'uporabnisko_ime': self.uporabnisko_ime,
#             'zasifrirano_geslo': self.zasifrirano_geslo,
#             'podatki': self.podatki.seznam_s_podatki(),
#         }
#         with open(ime_datoteke, 'w') as datoteka:
#             json.dump(slovar_stanja, datoteka, ensure_ascii=False, indent=4)

# imenik bo seznam seznamov

class Imenik:
    def __init__(self):
        self.podatki = []
    
    def priimki_v_imeniku(self):
        sez = []
        for seznam in self.podatki:
            sez.append(seznam[0])
        return sez

    def imena_v_imeniku(self):
        sez = []
        for seznam in self.podatki:
            sez.append(seznam[1])
        return sez

    def stevilke_v_imeniku(self):
        sez = []
        for seznam in self.podatki:
            sez.append(seznam[2])
        return sez

    def dodaj_kontakt(self, priimek, ime, stevilka, posta, roj_dan):
        self.podatki.append([priimek, ime, stevilka, posta, roj_dan])

    def poisci_stevilko(self):
        pass

    def izbrisi_kontakt(self):
        pass

    def uredi_kontakt(self):
        pass


    def seznam_s_podatki(self):
        return self.podatki