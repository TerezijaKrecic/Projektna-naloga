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

Poleg spletnega vmesnika je na voljo tudi tekstovni vmesnik skupaj z modelom, ki se
za tekstovni vmesnik razlikuje od tistega kot za spletni vmesnik, saj je tekstovni vmesnik
precej osnoven in ne shranjuje stanja, ko odideš iz njega. Razlog za to je osredotočenost
na spletni vmesnik - tekstovni vmesnik je bil le opora pri izbiri funkcij.  
V njem ima uporabnik na voljo:
* vpisati podatke za kontakt (priimek in številka obvezna)
* izpisati slovar kontaktov
* izbrisati kontakt
* poiskati kontakt
* urediti kontakt (ta funkcija ni dodelana)