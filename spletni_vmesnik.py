import bottle
from model import Uporabnik, Kontakt
import os
import hashlib
import random

uporabniki = {}
skrivnost = 'Secret'

nov_imenik = Kontakt()

# for ime_datoteke in os.listdir('uporabniki'):
#     uporabnik = Uporabnik.nalozi_stanje(os.path.join('uporabniki', ime_datoteke))
#     uporabniki[uporabnik.uporabnisko_ime] = uporabnik

# def trenutni_uporabnik():
#     uporabnisko_ime = bottle.request.get_cookie('uporabnisko_ime', secret=skrivnost)
#     if uporabnisko_ime is None:
#         bottle.redirect('/prijava/')
#     return uporabniki[uporabnisko_ime]

# def imenik_uporabnika():
#     return trenutni_uporabnik().podatki

# def shrani_trenutnega_uporabnika():
#     uporabnik = trenutni_uporabnik()
#     uporabnik.shrani_stanje(os.path.join('uporabniki', f'{uporabnik.uporabnisko_ime}.json'))

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/imenik/')

@bottle.get('/imenik/')
def nacrtovanje_imenika():
    slovar_podatkov = nov_imenik.slovar_s_podatki()
    return bottle.template('imenik.html', imenik=slovar_podatkov)

# @bottle.get('/imenik/')
# def nacrtovanje_imenika():
#     imenik = imenik_uporabnika()
#     return bottle.template('imenik.html', imenik=imenik)

# @bottle.get('/prijava/')
# def prijava_get():
#     return bottle.template('prijava.html')

# @bottle.post('/prijava/')
# def prijava_post():
#     uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
#     geslo = bottle.request.forms.getunicode('geslo')
#     h = hashlib.blake2b()
#     h.update(geslo.encode(encoding='utf-8'))
#     zasifrirano_geslo = h.hexdigest()
#     if 'dodaj_kontakt' in bottle.request.forms and uporabnisko_ime not in uporabniki:
#         uporabnik = Uporabnik(
#             uporabnisko_ime,
#             zasifrirano_geslo,
#             Kontakt()
#         )
#         uporabniki[uporabnisko_ime] = uporabnik
#     else:
#         uporabnik = uporabniki[uporabnisko_ime]
#         uporabnik.preveri_geslo(zasifrirano_geslo)
#     bottle.response.set_cookie('uporabnisko_ime', uporabnik.uporabnisko_ime, path='/', secret=skrivnost)
#     bottle.redirect('/')

# @bottle.post('/odjava/')
# def odjava():
#     bottle.response.delete_cookie('uporabnisko_ime', path='/')
#     bottle.redirect('/')

# @bottle.post('/dodaj-kontakt/')
# def dodaj_kontakt():
#     imenik = imenik_uporabnika()
#     Kontakt.dodaj_kontakt(bottle.request.forms.getunicode('ime'))
#     shrani_trenutnega_uporabnika()
#     bottle.redirect('/')

@bottle.post('/dodaj-kontakt/')
def dodaj_kontakt():
    priimek = bottle.request.forms.getunicode('priimek')
    ime = bottle.request.forms.getunicode('ime')
    stevilka = bottle.request.forms.getunicode('stevilka')
    mail = bottle.request.forms.getunicode('mail')
    rojdan = bottle.request.forms.getunicode('rojdan')
    nov_imenik.dodaj_kontakt(priimek, ime, stevilka, mail, rojdan)
    bottle.redirect('/')




bottle.run(debug=True, reloader=True)