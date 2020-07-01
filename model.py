import json

VEC_ISTIH_PRIIMKOV = 'V'

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
    def __init__(self, podatki=None):
        if podatki is None:
            self.podatki = []
        else:
            self.podatki = podatki
    
    def priimki_v_imeniku(self):
        sez = []
        for seznam in self.podatki:
            sez.append(seznam[0])
        return sez

    def stevilko_istih_priimkov(self, priimek):
        return self.priimki_v_imeniku().count(priimek)

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

    def poisci_stevilko_po_priimku(self, priimek):
        if self.stevilko_istih_priimkov(priimek) == 0:
            return None
        elif self.stevilko_istih_priimkov(priimek) > 1:
            return VEC_ISTIH_PRIIMKOV
        else:
            for kontakt in self.podatki:
                if kontakt[0] == priimek:
                    return kontakt[2]
    
    def poisci_stevilko_po_priimku_in_imenu(self, priimek, ime):
        for kontakt in self.podatki:
            if kontakt[0] == priimek:
                if kontakt[1] == ime:
                    return kontakt[2]
        else:
            return None

    def izbrisi_kontakt_po_priimku(self, priimek):
        if self.stevilko_istih_priimkov(priimek) == 0:
            return False
        elif self.stevilko_istih_priimkov(priimek) > 1:
            return VEC_ISTIH_PRIIMKOV
        else:
            for kontakt in self.podatki:
                if kontakt[0] == priimek:
                    self.podatki.remove(kontakt)

    def izbrisi_kontakt_po_priimku_in_imenu(self, priimek, ime):
        for kontakt in self.podatki:
            if kontakt[0] == priimek:
                if kontakt[1] == ime:
                    self.podatki.remove(kontakt)
        else:
            return None
            
    def uredi_kontakt(self):
        pass

    def seznam_s_podatki(self):
        return self.podatki