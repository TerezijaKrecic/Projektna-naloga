Projektna naloga
==========

Osebni imenik
---------

Osnovni cilj naloge je bil napisati program, ki več uporabnikom omogoča
dostop do osebne kontaktne knjige z uporabo uporabniškega imena in gesla.

Ob prvi prijavi se mora uporabnik registrirati, pri čemer ne sme vpisati
uporabniškega imena, ki je že uporabljeno.

Pri vsakem vpisu se ustvari nova _json_ datoteka, v kateri so shranjeni uporabnikovi
podatki - uporabniško ime, zašifrirano geslo ter slovar kontaktov.

Po vpisu ima uporabnik na voljo:
* vpisati podatke za nov kontakt (pri tem je obvezen vpis telefonske številke)
* urejanje kontakta
* brisanje kontakta
* urejanje seznama kontaktov po priimkih in po imenih
* iskanje kontakta (s ključi 'ime', 'priimek' in 'telefonska številka')

Ko uporabnik konča z opravili, se lahko odjavi in zapre program.