import model

# DATOTEKA_S_STANJEM = 'kontakti.json'
# try:
#     imenik = Imenik.nalozi_stanje(DATOTEKA_S_STANJEM)
# except FileNotFoundError:
#     imenik = Imenik()
    
moj_imenik = model.Imenik()

seznam_moznosti = [
    "Dodaj kontakt",
    "Poišči številko",
    "Izbriši kontakt",
    "Uredi kontakt",
    "Pokaži kontakte",
    "Izhod"
]

def zahtevaj_vnos():
    moznost = input("> ")
    try:
        float(moznost)
    except ValueError:
        print("Vnesite število!")
        return zahtevaj_vnos()
    else:
        if int(moznost) < 1 or int(moznost) > len(seznam_moznosti):
            print(f"Vnesite število med 1 in {len(seznam_moznosti)}!")
            return zahtevaj_vnos()
        else:
            return int(moznost)

def vnos_priimka():
    return input("Vnesite priimek: ")
def vnos_imena():
    return input("Vnesite ime: ")
def vnos_stevilke():
    return input("Vnesite telefonsko številko: ")
def vnos_el_poste():
    return input("Vnesite elektronsko pošto: ")
def vnos_roj_dneva():
    return input("Vnesite rojstni dan: ")


def izvedi_opravilo(stevilo):
    if stevilo == 1:
        print("Vnesite podatke. Priimek in telefonska številka sta obvezna.")
        print("Če ostalih podatkov ne veste, samo pritisnite 'enter'.")
        priimek = vnos_priimka()
        ime = vnos_imena()
        stevilka = vnos_stevilke()
        posta = vnos_el_poste()
        roj_dan = vnos_roj_dneva()
        moj_imenik.dodaj_kontakt(priimek, ime, stevilka, posta, roj_dan)
        print('Kontakt uspešno dodan!')
    elif stevilo == 2:
        moj_imenik.poisci_stevilko()
    elif stevilo == 3:
        moj_imenik.izbrisi_kontakt()
    elif stevilo == 4:
        moj_imenik.uredi_kontakt()
    elif stevilo == 5:
        if moj_imenik.podatki == []:
            print('V imeniku ni še nobenega kontakta.')
        else:
            print(moj_imenik.podatki)
            # for kontakt in moj_imenik.podatki:
            #     print(kontakt)





def glavni_meni():
    print("Pozdravljeni, izberite možnost:")
    while True:
        for x, y in enumerate(seznam_moznosti):
            print(x + 1, y)
        stevilo = zahtevaj_vnos() # vrne število med 1 in len(seznam_moznosti)
        if stevilo == len(seznam_moznosti):
            print('Nasvidenje!')
            break
        else:
            izvedi_opravilo(stevilo)

glavni_meni()