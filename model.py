class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, podatki):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        self.podatki = podatki
    
    def preveri_geslo(self, zasifrirano_geslo):
        if self.zasifrirano_geslo != zasifrirano_geslo:
            raise ValueError('Geslo je napačno!')
    

# imenik bo slovar, katerega ključi bodo priimki (ti so v naboru)

class Imenik:
    def __init__(self):
        self.podatki = {}

    def prestej_stevilo_priimkov(self, priimek):
        if (priimek, 1) not in self.podatki:
            return 0
        vsota = 0
        for nabor in self.podatki.keys:
            if nabor[0] == priimek:
                vsota += 1
        return vsota

    # def dodaj_priimek(self, priimek):
    #     n = prestej_stevilo_priimkov(priimek)
    #     self.podatki[(priimek, n + 1)] = []

    # def dodaj_ime(self, ime):
    #     self.podatki

    # def dodaj_podatke(self, priimek, ime, telefonska_stevilka, el_posta, rojstni_dan, dodatno):
    #     self.podatki[priimek] = [ime, telefonska_stevilka, el_posta, rojstni_dan, dodatno]

    def dodaj_podadtke(self, priimek, ime, telefonska_stevilka, el_posta, rojstni_dan, dodatno):
        n = prestej_stevilo_priimkov(priimek)
        self.podatki[(priimek, n + 1)] = [ime, telefonska_stevilka, el_posta, rojstni_dan, dodatno]    