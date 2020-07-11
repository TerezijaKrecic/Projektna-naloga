Projektna naloga
==========

Osebni imenik
---------

Osnovni cilj naloge je bil napisati program, ki več uporabnikom omogoča
dostop do osebne kontaktne knjige z uporabo uporabniškega imena in gesla.

Po vpisu ima uporabnik na voljo:
* vpisati podatke za nov kontakt (pri tem je obvezen vpis telefonske številke)
* urejanje kontakta
* brisanje kontakta
* urejanje seznama kontaktov po priimkih in po imenih
* iskanje kontakta (s ključi 'ime', 'priimek' in 'telefonska številka')

Poleg spletnega vmesnika je na voljo tudi tekstovni vmesnik skupaj z modelom, ki se
za tekstovni vmesnik razlikuje od tistega kot za spletni vmesnik, saj je tekstovni vmesnik
precej osnoven in ne shranjuje stanja, ko odideš iz njega. V njem ima uporabnik na voljo:
* vpisati podatke za kontakt (priimek in številka obvezna)
* izpisati slovar kontaktov
* izbrisati kontakt
* poiskati kontakt
* urediti kontakt (ta funkcija ni dodelana)

Shranjevanje kontaktov
----------

Za vsakega uporabnika se ustvari svoja datoteka z imenom <i>uporabnisko_ime</i>.json,
ki izgleda nekako takole:
<i>
'
{
    "uporabnisko_ime": "uporabnisko_ime",
    "zasifrirano_geslo": "zasifriran_niz",
    "podatki": {
        "1": {
            "priimek": "priimek1",
            "ime": "ime1",
            "stevilka": "stevilka1",
            "mail": "elektronski_naslov1",
            "rojdan": "datum_rojstva1",
            "opombe": "opombe1"
        },
        "2": {
            "priimek": "priimek2",
            "ime": "ime2",
            "stevilka": "stevilka2",
            "mail": "elektronski_naslov2",
            "rojdan": "datum_rojstva2",
            "opombe": "opombe2"
        }
    }
}
'
</i>