import json
import random

VEC_ISTIH_PRIIMKOV = 'V'
KONTAKT_NE_OBSTAJA = 'N'

DATOTEKA_STANJE = 'stanje.json'

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, podatki):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.podatki = podatki
    
    def preveri_geslo(self, zasifrirano_geslo):
        if self.zasifrirano_geslo != zasifrirano_geslo:
            raise ValueError('Geslo je napačno!')
    
    def shrani_stanje(self, ime_datoteke):
        slovar_stanja = {
            'uporabnisko_ime': self.uporabnisko_ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'podatki': self.kontakt.slovar_s_podatki()
        }
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(slovar_stanja, datoteka, ensure_ascii=False, indent=4)

    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
        uporabnisko_ime = slovar_stanja['uporabnisko_ime']
        zasifrirano_geslo = slovar_stanja['zasifrirano_geslo']
        podatki = slovar_stanja['podatki']
        return cls(uporabnisko_ime, zasifrirano_geslo, podatki)

# slovar_stanja bo slovar, katerega ključi so imena podatkov, vrednosti pa tistih 5 podatkov
#
# {
    # '1':
    #     {
    #         'priimek': 'NOVAK',
    #         'ime': 'JANEZ',
    #         'številka': '040100100',
    #         'elektronski naslov': 'janez.novak@hotmail.com',
    #         'rojstni dan': '1. 1. 1990'
    #     }
# }

class Kontakt:
    def __init__(self):
        self.podatki = {}
    
    # def priimki_v_imeniku(self):
    #     sez = []
    #     for slovar in self.podatki.keys():
    #         sez.append(self.podatki[slovar]['priimek'])
    #     return sez

    # def stevilo_istih_priimkov(self, priimek):
    #     return self.priimki_v_imeniku().count(priimek)

    # def obstoj_in_enolicnost_kontakta(self, priimek):  # po priimku
    #     if self.stevilo_istih_priimkov(priimek) == 0:
    #         return KONTAKT_NE_OBSTAJA
    #     elif self.stevilo_istih_priimkov(priimek) > 1:
    #         return VEC_ISTIH_PRIIMKOV
    #     else:
    #         return True        

    # def imena_v_imeniku(self):
    #     sez = []
    #     for slovar in self.podatki.keys():
    #         sez.append(self.podatki[slovar]['ime'])
    #     return sez

    # def stevilke_v_imeniku(self):
    #     sez = []
    #     for slovar in self.podatki.keys():
    #         sez.append(self.podatki[slovar]['stevilka'])
    #     return sez

    def nov_indeks(self):
        if self.podatki == {}:
            return 0
        else:
            vsota = 0
            for slovar in self.podatki:
                vsota += 1
            return vsota + 1

    def dodaj_kontakt(self, priimek, ime, stevilka, posta, roj_dan):
        self.podatki[self.nov_indeks()] = {
            'priimek': priimek,
            'ime': ime,
            'stevilka': stevilka,
            'mail': posta,
            'rojdan': roj_dan
        }

    # def poisci_stevilko_po_priimku(self, priimek):
    #     x = self.obstoj_in_enolicnost_kontakta(priimek)
    #     if x == True:
    #         for slovar in self.podatki.keys():
    #             if self.podatki[slovar]['priimek'] == priimek:
    #                 return self.podatki[slovar]['stevilka']            
    #     else:
    #         return x
    
    # def poisci_stevilko_po_priimku_in_imenu(self, priimek, ime):
    #     for slovar in self.podatki.keys():
    #         if self.podatki[slovar]['priimek'] == priimek:
    #             if self.podatki[slovar]['ime'] == ime:
    #                 return self.podatki[slovar]['stevilka']
    #     else:
    #         return KONTAKT_NE_OBSTAJA

    # def izbrisi_kontakt_po_priimku(self, priimek):
    #     x = self.obstoj_in_enolicnost_kontakta(priimek)
    #     if x == True:
    #         for slovar in self.podatki.keys():
    #             if self.podatki[slovar]['priimek'] == priimek:
    #                 self.podatki.pop(slovar)
    #                 return True
    #     else:
    #         return x

    # def izbrisi_kontakt_po_priimku_in_imenu(self, priimek, ime):
    #     for slovar in self.podatki.keys():
    #         if self.podatki[slovar]['priimek'] == priimek:
    #             if self.podatki[slovar]['ime'] == ime:
    #                 self.podatki.pop(slovar)
    #                 return True
    #     else:
    #         return KONTAKT_NE_OBSTAJA
            
    # def uredi_kontakt(self):
    #     pass

    def slovar_s_podatki(self):
        return self.podatki

    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.slovar_s_podatki(), datoteka, ensure_ascii=False, indent=4)

    def nalozi_stanje(self, ime_datoteke):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            self.podatki = json.load(f)