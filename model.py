import json
import random

VEC_ISTIH_PRIIMKOV = 'V'
KONTAKT_NE_OBSTAJA = 'N'
PRAZNO = 'Vpišite nekaj!'

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
    # 1:
    #     {
    #         'priimek': 'NOVAK',
    #         'ime': 'JANEZ',
    #         'številka': '040100100',
    #         'elektronski naslov': 'janez.novak@hotmail.com',
    #         'rojstni dan': '1. 1. 1990',
    #         'opombe': 'Ta blond guy'
    #     }
# }

class Kontakt:
    def __init__(self):
        self.podatki = {}

    def nov_indeks(self):
        if self.podatki == {}:
            return 1
        else:
            vsota = 0
            for slovar in self.podatki:
                vsota += 1
            return vsota + 1

    def dodaj_kontakt(self, priimek, ime, stevilka, posta, roj_dan, opombe):
        self.podatki[self.nov_indeks()] = {
            'priimek': priimek,
            'ime': ime,
            'stevilka': stevilka,
            'mail': posta,
            'rojdan': roj_dan,
            'opombe': opombe
        }

    def uredi_indekse(self):
        '''Uredi indekse po vrsti z VSEMI nar. števili od 1 do dolžine slovarja'''
        if self.podatki == {}:
            pass
        else:
            nov_slovar = {}
            seznam_indeksov = [kljuc for kljuc in self.podatki]
            for n in range(1, len(seznam_indeksov) + 1):
                kontakt = self.podatki[seznam_indeksov[n - 1]]
                self.podatki.pop(seznam_indeksov[n - 1])
                self.podatki[n] = kontakt

    def uredi_kontakt(self, indeks, priimek, ime, stevilka, mail, rojdan, opombe):
        self.podatki[indeks]['priimek'] = priimek
        self.podatki[indeks]['ime'] = ime
        self.podatki[indeks]['stevilka'] = stevilka
        self.podatki[indeks]['mail'] = mail
        self.podatki[indeks]['rojdan'] = rojdan
        self.podatki[indeks]['opombe'] = opombe

    def uredi_po_priimkih(self):
        pass

    def stevilke_v_imeniku(self):
        return [self.podatki[i]['stevilka'] for i in self.podatki.keys()]

    def priimki_v_imeniku(self):
        return [self.podatki[i]['priimek'] for i in self.podatki.keys()]

    def imena_v_imeniku(self):
        return [self.podatki[i]['ime'] for i in self.podatki.keys()]

    def kontakti_priimek(self, priimek):
        '''Vrne slovar vseh kontaktov, ki imajo tak priimek'''
        if priimek == '':
            return self.podatki
        else:
            slovar = {}
            for i in self.podatki:
                if self.podatki[i]['priimek'] == priimek:
                    slovar[i] = self.podatki[i]
            return slovar

    def kontakti_ime(self, ime, slovar):
        '''Vrne slovar vseh kontaktov, ki imajo tako ime (in priimek od prej)'''
        if ime == '':
            return slovar
        else:
            slovarcek = {}
            for i in slovar:
                if slovar[i]['ime'] == ime:
                    slovarcek[i] = slovar[i]
            return slovarcek

    def poisci_kontakt(self, priimek, ime, stevilka):
        if priimek + ime + stevilka == '':
            return PRAZNO
        kontakti_s_tem_priimkom = self.kontakti_priimek(priimek)
        kontakti_s_tem_priimkom_in_imenom = self.kontakti_ime(ime, kontakti_s_tem_priimkom)
        if stevilka == '':
            return kontakti_s_tem_priimkom_in_imenom
        else:
            slovar = {}
            for i in kontakti_s_tem_priimkom_in_imenom:
                if kontakti_s_tem_priimkom_in_imenom[i]['stevilka'] == stevilka:
                    slovar[i] = kontakti_s_tem_priimkom_in_imenom[i]
            if slovar == {}:
                return KONTAKT_NE_OBSTAJA
            else:
                return slovar

    def slovar_s_podatki(self):
        return self.podatki

    # def shrani_stanje(self, ime_datoteke):
    #     with open(ime_datoteke, 'w') as datoteka:
    #         json.dump(self.slovar_s_podatki(), datoteka, ensure_ascii=False, indent=4)

    # def nalozi_stanje(self, ime_datoteke):
    #     with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
    #         self.podatki = json.load(f)