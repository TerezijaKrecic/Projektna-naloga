import bottle
from model import Uporabnik, Kontakt, NAPACNO_GESLO
import os
import hashlib

uporabniki = {}
skrivnost = 'Secret'


for ime_datoteke in os.listdir('uporabniki'):
    uporabnik = Uporabnik.nalozi_stanje(os.path.join('uporabniki', ime_datoteke))
    uporabniki[uporabnik.uporabnisko_ime] = uporabnik

def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret=skrivnost)
    return uporabniki[uporabnisko_ime] # dobimo razred Uporabnik, ki vsebuje ime in geslo in (na začetku prazen) Kontakt()

def imenik_uporabnika():
    return trenutni_uporabnik().kontakti # dobimo razred Kontakt, ki lahko že vsebuje podatke

def shrani_trenutnega_uporabnika():
    uporabnik = trenutni_uporabnik()
    uporabnik.shrani_stanje(os.path.join('uporabniki', f'{uporabnik.uporabnisko_ime}.json'))



@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/prijava/')

@bottle.get('/prijava/')
def prijava_get():
    pozdrav = 'Pozdravljeni! Za nadaljevanje se vpišite:'
    return bottle.template('prijava.html', obvestilo=pozdrav)

@bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    if uporabnisko_ime not in uporabniki:
        napaka = 'Uporabniško ime ne obstaja. Poskusite še enkrat:'
        return bottle.template('prijava.html', obvestilo=napaka)
    geslo = bottle.request.forms.getunicode('geslo')
    h = hashlib.blake2b()
    h.update(geslo.encode(encoding='utf-8'))
    zasifrirano_geslo = h.hexdigest()
    uporabnik = uporabniki[uporabnisko_ime]
    if uporabnik.preveri_geslo(zasifrirano_geslo) == NAPACNO_GESLO:
        napaka = 'Geslo je napačno. Poskusite znova:'
        return bottle.template('prijava.html', obvestilo=napaka)
    bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=skrivnost)
    bottle.redirect('/imenik/')

@bottle.get('/registracija/')
def registracija_get():
    pozdrav = 'Pozdravljeni! Za nadaljevanje se registrirajte:'
    return bottle.template('registracija.html', obvestilo=pozdrav)

@bottle.post('/registracija/')
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    if uporabnisko_ime in uporabniki:
        napaka = 'To uporabniško ime že obstaja. Uporabite drugo ime.'
        return bottle.template('registracija.html', obvestilo=napaka)
    geslo = bottle.request.forms.getunicode('geslo')
    h = hashlib.blake2b()
    h.update(geslo.encode(encoding='utf-8'))
    zasifrirano_geslo = h.hexdigest()
    uporabnik = Uporabnik(
        uporabnisko_ime,
        zasifrirano_geslo,
        Kontakt()
        )
    uporabniki[uporabnisko_ime] = uporabnik
    bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=skrivnost)
    bottle.redirect('/imenik/')

@bottle.get('/imenik/')
def nacrtovanje_imenika():
    slovar_podatkov = imenik_uporabnika().podatki
    return bottle.template('imenik.html', imenik=slovar_podatkov)

@bottle.post('/odjava/')
def odjava():
    shrani_trenutnega_uporabnika()
    bottle.response.delete_cookie('uporabnisko_ime', path='/')
    bottle.redirect('/')

@bottle.post('/dodaj-kontakt/')
def dodaj_kontakt():
    priimek = bottle.request.forms.getunicode('priimek')
    ime = bottle.request.forms.getunicode('ime')
    stevilka = str(bottle.request.forms.getunicode('stevilka'))
    mail = bottle.request.forms.getunicode('mail')
    rojdan = bottle.request.forms.getunicode('rojdan')
    opomba = bottle.request.forms.getunicode('opombe')
    imenik_uporabnika().dodaj_kontakt(priimek, ime, stevilka, mail, rojdan, opomba)
    shrani_trenutnega_uporabnika()
    bottle.redirect('/imenik/')

@bottle.post('/izbrisi-kontakt<indeks>/')
def izbrisi_kontakt(indeks):
    imenik_uporabnika().izbrisi_kontakt(int(indeks))
    imenik_uporabnika().uredi_indekse()
    bottle.redirect('/imenik/')

@bottle.get('/uredi-kontakt<indeks>/')
def uredi_kontakt(indeks):
    slovar_podatkov = imenik_uporabnika().podatki
    shrani_trenutnega_uporabnika()
    return bottle.template('uredi_kontakt.html', imenik=slovar_podatkov, indeks=int(indeks))

@bottle.post('/uredi-kontakt<indeks>/')
def uredi_kontakt(indeks):
    priimek = bottle.request.forms.getunicode('priimek')
    ime = bottle.request.forms.getunicode('ime')
    stevilka = str(bottle.request.forms.getunicode('stevilka'))
    mail = bottle.request.forms.getunicode('mail')
    rojdan = bottle.request.forms.getunicode('rojdan')
    opombe = bottle.request.forms.getunicode('opombe')
    stevilo = int(indeks)
    imenik_uporabnika().uredi_kontakt(stevilo, priimek, ime, stevilka, mail, rojdan, opombe)
    shrani_trenutnega_uporabnika()
    bottle.redirect('/imenik/')

@bottle.post('/poisci-kontakt/')
def poisci_kontakt():
    priimek = bottle.request.forms.getunicode('iskanje-priimek')
    ime = bottle.request.forms.getunicode('iskanje-ime')
    stevilka = str(bottle.request.forms.getunicode('iskanje-stevilka'))
    rezultat = imenik_uporabnika().poisci_kontakt(priimek, ime, stevilka)
    return bottle.template('iskanje.html', rezultat=rezultat)  # rezultat je lahko slovar ali pa obvestilo, da kontakta ni

@bottle.post("/uredi-kontakte-po-priimkih/")
def uredi_po_priimkih():
    imenik_uporabnika().uredi_po_priimkih()
    bottle.redirect('/imenik/')

@bottle.post("/uredi-kontakte-po-imenih/")
def uredi_po_imenih():
    imenik_uporabnika().uredi_po_imenih()
    bottle.redirect('/imenik/')

bottle.run(debug=True, reloader=True)