import json
import random

VEC_ISTIH_PRIIMKOV = 'V'
KONTAKT_NE_OBSTAJA = 'N'

DATOTEKA_STANJE = 'stanje.json'

class Kontakt:
    def __init__(self):
        self.podatki = {}
    
    def priimki_v_imeniku(self):
        sez = []
        for slovar in self.podatki.keys():
            sez.append(self.podatki[slovar]['priimek'])
        return sez

    def stevilo_istih_priimkov(self, priimek):
        return self.priimki_v_imeniku().count(priimek)

    def obstoj_in_enolicnost_kontakta(self, priimek):
        if self.stevilo_istih_priimkov(priimek) == 0:
            return KONTAKT_NE_OBSTAJA
        elif self.stevilo_istih_priimkov(priimek) > 1:
            return VEC_ISTIH_PRIIMKOV
        else:
            return True        

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
        x = self.obstoj_in_enolicnost_kontakta(priimek)
        if x == True:
            for slovar in self.podatki.keys():
                if self.podatki[slovar]['priimek'] == priimek:
                    return self.podatki[slovar]['stevilka']            
        else:
            return x
    
    def poisci_stevilko_po_priimku_in_imenu(self, priimek, ime):
        for slovar in self.podatki.keys():
            if self.podatki[slovar]['priimek'] == priimek:
                if self.podatki[slovar]['ime'] == ime:
                    return self.podatki[slovar]['stevilka']
        else:
            return KONTAKT_NE_OBSTAJA

    def izbrisi_kontakt_po_priimku(self, priimek):
        x = self.obstoj_in_enolicnost_kontakta(priimek)
        if x == True:
            for slovar in self.podatki.keys():
                if self.podatki[slovar]['priimek'] == priimek:
                    self.podatki.pop(slovar)
                    return True
        else:
            return x

    def izbrisi_kontakt_po_priimku_in_imenu(self, priimek, ime):
        for slovar in self.podatki.keys():
            if self.podatki[slovar]['priimek'] == priimek:
                if self.podatki[slovar]['ime'] == ime:
                    self.podatki.pop(slovar)
                    return True
        else:
            return KONTAKT_NE_OBSTAJA