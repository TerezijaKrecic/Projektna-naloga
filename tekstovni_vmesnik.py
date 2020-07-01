import model
napaka = 'Kontakt s temi podatki ne obstaja!\n'

# DATOTEKA_S_STANJEM = 'stanje.json'

# try:
#     moj_imenik = Imenik(DATOTEKA_S_STANJEM)
# except FileNotFoundError:
#     moj_imenik = Imenik()
    
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
    n = input("Vnesite priimek: ")
    if n == '':
        print('Priimek je obvezen!')
        return vnos_priimka()
    else:
        return n

def vnos_imena():
    return input("Vnesite ime: ")

def vnos_stevilke():
    n = input("Vnesite telefonsko številko: ")
    if n == '':
        print('Številka je obvezna!')
        return vnos_stevilke()
    try:
        float(n)
    except ValueError:
        print("Vnesite število!")
        return vnos_stevilke()
    else:
        return n

def vnos_el_poste():
    return input("Vnesite elektronsko pošto: ")

def vnos_roj_dneva():
    return input("Vnesite rojstni dan: ")

def izvedi_opravilo(stevilo):
    if stevilo == 1:
        return dodaj_kontakt_v_imenik()
    elif stevilo == 2:
        return poisci_stevilko()
    elif stevilo == 3:
        return izbrisi_kontakt()
    elif stevilo == 4:
        return uredi_kontakt()
    elif stevilo == 5:
        return izpisi_imenik()

def dodaj_kontakt_v_imenik():
    print("Vnesite podatke. Priimek in telefonska številka sta obvezna.")
    print("Če ostalih podatkov ne veste, samo pritisnite 'enter'.")
    priimek = vnos_priimka().upper()
    ime = vnos_imena().upper()
    stevilka = vnos_stevilke()
    posta = vnos_el_poste()
    roj_dan = vnos_roj_dneva()
    moj_imenik.dodaj_kontakt(priimek, ime, stevilka, posta, roj_dan)
    print('Kontakt uspešno dodan!\n')
    
def poisci_stevilko():
    priimek = vnos_priimka().upper()
    stevilka = moj_imenik.poisci_stevilko_po_priimku(priimek)
    if stevilka is None:
        print(napaka)
    elif stevilka == model.VEC_ISTIH_PRIIMKOV:
        ime = vnos_imena().upper()
        stevilka = moj_imenik.poisci_stevilko_po_priimku_in_imenu(priimek, ime)
        if stevilka is None:
            print(napaka)
        else:
            print(f'Številka:{stevilka}.\n')
    else:
        print(f'Številka:{stevilka}.\n')

def izbrisi_kontakt():
    priimek = vnos_priimka().upper()
    uspeh = moj_imenik.izbrisi_kontakt_po_priimku(priimek)
    if uspeh == False:
        print(napaka)
    elif uspeh == model.VEC_ISTIH_PRIIMKOV:
        ime = vnos_imena().upper()
        uspeh = moj_imenik.izbrisi_kontakt_po_priimku_in_imenu(priimek, ime)
        if uspeh is None:
            print(napaka)
        else:
            print('Kontakt uspešno izbrisan!\n')
    else:
        print('Kontakt uspešno izbrisan!\n')


def uredi_kontakt():
        print('Ta možnost trenutno ni mogoča.\n')

def izpisi_imenik():
        if moj_imenik.podatki == []:
            print('V imeniku ni še nobenega kontakta.\n')
        else:
            print(moj_imenik.podatki)

def glavni_meni():
    print("Pozdravljeni, izberite možnost:\n")
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