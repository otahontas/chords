# Demo

[Live-demo Herokussa](https://sointutietokanta.herokuapp.com/)

# Aihekuvaus

Projektissa laaditaan järjestelmä, jossa ylläpidetään informaatiota [soinnuista](https://fi.wikipedia.org/wiki/Sointu) ja jos aikaa riittää, työtä laajennetaan listalla kappaleista, joissa sointuja käytetään. Käyttäjät voivat kirjautua järjestelmään, hakea sieltä sointuja, lisätä sointuja, lisätä, muokata ja poistaa kappaleita* sekä lisätä sointuja kappaleiden* yhteyteen. Vain admin-tunnuksilla voi muokata tai poistaa sointuja - tällä vältetään kappaleisiin kiinnitettyjen sointujen ilkivaltainen poistaminen. Lisäksi sointuja sekä kappaleita* voi merkityä suosikseiksi

Järjestelmä osaa käsitellä kolmi- ja neliäänisiä sointuja (ns. power chordit ja neliäänisiä useammat soinnut jätetään huomiotta). Alkutilanteessa tietokanta sisältää ainoastaan nuotteja, joista soinnut koostetaan. Sointupankki kehittyy käyttäjien syöttäessä tietokantaan lisää sointuja.

## Toiminnot:
- kirjautuminen
- soinnun hakeminen ja siinä esiintyvien sävelien listaaminen
- soinnun lisääminen
- sointujen ja kappaleiden* merkkaaminen suosikiksi
- kaikkien sointujen tai kappaleiden* listaaminen sekä filtteröinti suosituimmuuden mukaan
- kappaleiden* syöttö, poisto ja muokkaus sekä sointujen lisääminen kappaleiden yhteyteen
- sointujen listaaminen kappaleen yhteydessä
- Lisäksi ylläpitäjän toiminnot:
    - Muokkaa tai poista sointuja
    - Listaa, muokkaa tai poista käyttäjiä

# Tietokantakaavio:
- Account((pk) id:Integer, (fk) role -> Role, name:String, username:String, password:String)
- Role((pk) id:Integer, name:String)
- Chord((pk) id:Integer, key:String, name:String)
- ChordNote((fk) chord_id -> Chord, (fk) note_id -> Note, rank:Integer)
- Note((pk) id:Integer, name:String)
- Song((pk) id:Integer, name:String, favourite:Boolean)*
- SongChord((fk) chord_id -> Chord, (fk) song_id -> Song)*
- AccountFavouriteChord((fk) account_id -> Account, (fk) chord_id -> Chord)
- AccountFavouriteSong((fk) account_id -> Account, (fk) song_id -> Song)*

tähdellä(*) merkityt ominaisuudet toteutetaan vain, jos kurssin aikana ehditään. Sointuominaisuuksien toteuttaminen on ensisijainen prioriteetti.

# Dokumentaatio:
- [Käyttötapaukset](/documentation/userstories.md)

# TODO:
- Tee tietokantakaavio ja siirrä se dokumentaatioon
- Luo sopivat taulut, joissa crud
- docstringit metodeihin?
- kommentoi koodia selkeämmäksi
- check, että koodi noudattaa python nimeämiskäytänteitä
