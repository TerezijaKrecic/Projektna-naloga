import json
import random

VEC_ISTIH_PRIIMKOV = 'V'
KONTAKT_NE_OBSTAJA = 'N'

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

# imenik bo slovar, katerega ključi so imena podatkov, vrednosti pa tistih 5 podatkov
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



class Imenik:
    def __init__(self):
        self.podatki = {}
    
    def priimki_v_imeniku(self):
        sez = []
        for slovar in self.podatki.keys():
            sez.append(self.podatki[slovar]['priimek'])
        return sez

    def stevilo_istih_priimkov(self, priimek):
        return self.priimki_v_imeniku().count(priimek)

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
        x = random.choice([0, 1000])
        if str(x) in self.podatki:
            return self.nov_indeks()
        else:
            return str(x)

    def dodaj_kontakt(self, priimek, ime, stevilka, posta, roj_dan):
        self.podatki[self.nov_indeks()] = {
            'priimek': priimek,
            'ime': ime,
            'stevilka': stevilka,
            'mail': posta,
            'rojdan': roj_dan
        }

    def poisci_stevilko_po_priimku(self, priimek):
        if self.stevilo_istih_priimkov(priimek) == 0:
            return KONTAKT_NE_OBSTAJA
        elif self.stevilo_istih_priimkov(priimek) > 1:
            return VEC_ISTIH_PRIIMKOV
        else:
            for slovar in self.podatki.keys():
                if self.podatki[slovar]['priimek'] == priimek:
                    return self.podatki[slovar]['stevilka']
    
    def poisci_stevilko_po_priimku_in_imenu(self, priimek, ime):
        for slovar in self.podatki.keys():
            if self.podatki[slovar]['priimek'] == priimek:
                if self.podatki[slovar]['ime'] == ime:
                    return self.podatki[slovar]['stevilka']
        else:
            return KONTAKT_NE_OBSTAJA

    def izbrisi_kontakt_po_priimku(self, priimek):
        if self.stevilo_istih_priimkov(priimek) == 0:
            return KONTAKT_NE_OBSTAJA
        elif self.stevilo_istih_priimkov(priimek) > 1:
            return VEC_ISTIH_PRIIMKOV
        else:
            for slovar in self.podatki.keys():
                if self.podatki[slovar]['priimek'] == priimek:
                    self.podatki.pop(slovar)
                    return True

    def izbrisi_kontakt_po_priimku_in_imenu(self, priimek, ime):
        for slovar in self.podatki.keys():
            if self.podatki[slovar]['priimek'] == priimek:
                if self.podatki[slovar]['ime'] == ime:
                    self.podatki.pop(slovar)
                    return True
        else:
            return KONTAKT_NE_OBSTAJA
            
    # def uredi_kontakt(self):
    #     pass

    def seznam_s_podatki(self):
        return self.podatki