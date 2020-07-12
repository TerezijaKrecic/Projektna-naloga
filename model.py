import json

VEC_ISTIH_PRIIMKOV = 'V'
KONTAKT_NE_OBSTAJA = 'N'
PRAZNO = 'Vpišite nekaj!'
NAPACNO_GESLO = 'Geslo je napačno. Poskusite znova:'
UPORABNISKO_IME_NE_OBSTAJA = 'Uporabniško ime ne obstaja. Poskusite še enkrat:'
UPORABNISKO_IME_ZE_OBSTAJA = 'To uporabniško ime že obstaja. Uporabite drugo ime.'

class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, kontakti):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.kontakti = kontakti # to je razred Kontakt()
    
    def preveri_geslo(self, zasifrirano_geslo):
        if self.zasifrirano_geslo != zasifrirano_geslo:
            return NAPACNO_GESLO
    
    def shrani_stanje(self, ime_datoteke): #ime datoteke je uporabniško_ime.json
        slovar_stanja = {
            'uporabnisko_ime': self.uporabnisko_ime,
            'zasifrirano_geslo': self.zasifrirano_geslo,
            'podatki': self.kontakti.podatki
        }
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            json.dump(slovar_stanja, datoteka, ensure_ascii=False, indent=4)

    def nalozi_stanje(ime_datoteke):
        with open(ime_datoteke, encoding='utf-8') as datoteka:
            slovar_stanja = json.load(datoteka)
        uporabnisko_ime = slovar_stanja['uporabnisko_ime']
        zasifrirano_geslo = slovar_stanja['zasifrirano_geslo']
        kontakti = Kontakt(slovar_stanja['podatki']) # tu mora biti Kontakt(), če ne dobimo seznam in ne razreda
        return Uporabnik(uporabnisko_ime, zasifrirano_geslo, kontakti)

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
    def __init__(self, podatki=None):
        self.podatki = {} if podatki is None else podatki

    def nov_indeks(self):
        if self.podatki == {}:
            return 1
        else:
            vsota = 0
            for slovar in self.podatki:
                vsota += 1
            indeks = vsota + 1
            return str(indeks)

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

    def izbrisi_kontakt(self, indeks):
        self.podatki.pop(indeks)

    def uredi_po_priimkih(self):
        if self.podatki == {}:
            pass
        seznam_parov = [] # seznam parov [('novak', 1), ('lokar', 2), ('', 3), ('48', 4)]
        for i in self.podatki:
            priimek = self.podatki[i]['priimek']
            seznam_parov.append((priimek.upper(), i))
        pari = sorted(seznam_parov) # seznam uredimo po abecedi [('', 3), ('48', 4), ('lokar', 2), ('novak', 1)]
        slovar = {}
        for  n, (priimek, indeks) in enumerate(pari):
            slovar[str(n + 1)] = self.podatki[indeks]
            self.podatki.pop(indeks)
        self.podatki = slovar
        
    def uredi_po_imenih(self):
        if self.podatki == {}:
            pass
        seznam_parov = []
        for i in self.podatki:
            ime = self.podatki[i]['ime']
            seznam_parov.append((ime.upper(), i))
        pari = sorted(seznam_parov)
        slovar = {}
        for  n, (ime, indeks) in enumerate(pari):
            slovar[str(n + 1)] = self.podatki[indeks]
            self.podatki.pop(indeks)
        self.podatki = slovar

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
                if self.podatki[i]['priimek'].upper() == priimek:
                    slovar[i] = self.podatki[i]
            return slovar

    def kontakti_ime(self, ime, slovar):
        '''Vrne slovar vseh kontaktov, ki imajo tako ime (in priimek od prej)'''
        if ime == '':
            return slovar
        else:
            slovarcek = {}
            for i in slovar:
                if slovar[i]['ime'].upper() == ime:
                    slovarcek[i] = slovar[i]
            return slovarcek

    def ali_je_prazen(self, slovar):
        if slovar == {}:
            return KONTAKT_NE_OBSTAJA
        else:
            return slovar

    def poisci_kontakt(self, priimek, ime, stevilka):
        if priimek + ime + stevilka == '':
            return PRAZNO
        ime = ime.upper()
        priimek = priimek.upper()
        kontakti_s_tem_priimkom = self.kontakti_priimek(priimek)
        kontakti_s_tem_priimkom_in_imenom = self.kontakti_ime(ime, kontakti_s_tem_priimkom)
        if stevilka == '':
            return self.ali_je_prazen(kontakti_s_tem_priimkom_in_imenom)
        else:
            slovar = {}
            for i in kontakti_s_tem_priimkom_in_imenom:
                if kontakti_s_tem_priimkom_in_imenom[i]['stevilka'] == stevilka:
                    slovar[i] = kontakti_s_tem_priimkom_in_imenom[i]
            return self.ali_je_prazen(slovar)