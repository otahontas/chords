# Demo

Demo version is [hosted on heroku](https://chordsdb-demo.herokuapp.com/).

Login with test user:
- käyttäjä: testi
- salasana: testi123

# Aihekuvaus

Projektissa laaditaan järjestelmä, jossa ylläpidetään informaatiota [soinnuista](https://fi.wikipedia.org/wiki/Sointu) ja kappaleista, joissa sointuja käytetään. Käyttäjät voivat kirjautua järjestelmään, hakea sieltä sointuja, lisätä sointuja, lisätä, muokata ja poistaa kappaleita sekä lisätä sointuja kappaleiden* yhteyteen. Vain admin-tunnuksilla voi muokata tai poistaa sointuja - tällä vältetään kappaleisiin kiinnitettyjen sointujen ilkivaltainen poistaminen. Lisäksi kappaleita voi merkityä suosikseiksi

Järjestelmä osaa käsitellä kolmiäänisiä sointuja (ns. power chordit sekä kolmisointuja laajemmat soinnut jätetään huomiotta). Alkutilanteessa tietokanta sisältää ainoastaan nuotteja, joista soinnut koostetaan. Sointupankki kehittyy käyttäjien syöttäessä tietokantaan lisää sointuja.

## Toiminnot:
- kirjautuminen ja uuden käyttäjän luominen
- soinnun lisääminen
- kaikkien sointujen listaaminen, sointujen hakeminen ja soinnuissa esiintyvien sävelien listaaminen
- kappaleiden lisääminen, listaaminen ja hakeminen sekä muokkaaminen ja poistaminen (CRUD-ominaisuudet)
- sointujen lisääminen kappaleisiin sekä sointujen listaaminen kappaleen yhteydessä
- kappaleiden merkkaaminen suosikiksi
- suosituimpien kappaleiden listaaminen
- Lisäksi ylläpitäjän toiminnot:
    - Muokkaa tai poista sointuja
    - Lisää, listaa, muokkaa tai poista käyttäjiä (CRUD)


# Dokumentaatio:
- [Käyttötapaukset](/documentation/userstories.md)
- [Tietokantarakenteen kuvaus](/documentation/databasestructure.md)
- AS

# TODO vika viikko:
- flask-security ja eri käyttäjien toiminallisuudet
- Oman profiilin hallinta
- Admin tunnukset ja roolien hallinta
- Haku
- Suosikkisoinnut per käyttäjä
- Sointujen sävelet näkyviin sointu-sivulle
- Loput statistiikat
- Pagerizer
- injektionticheckit
- Biisien ja sointujen päivittäminen ja lisääminen:
    - UI paremmaksi (checkboxit)
    - Olemassa olevien tietojen näyttäminen & validointi kuntoon
- sointujen päivittämisnäkymä adminille (CRUD)
- käyttäjätietojen hallinnointinäkymä adminille
- biisien muokkaus sallituksi vain sen lisänneelle henkilölle tai adminille
- Muu:
    - dokumentaatio
    - koodin selkeys (naming conventions, docstrings, moduulit)
    - abstrahointi + moduuleihin eristäminen
        - formien validointi omaansa?
        - kannassa olevan tiedon checkkaaminen omaansa?
    - Päivitä käyttötapauksia
    - Tee käyttötapauksien SQL-kyselyt
    - Tee asennusohjeet
    - Tee käyttöohjeet
    - ks. TODOt läpi omasta kannasta

# Myöhemmin jos ehtii:
- sointujen rankin lisääminen oikein kun sävelet on oikeesti eri järjestyksessä
- redirektaus loginin jälkeen takas osoitteeseen, josta käyttäjä tuli ks. esim [täältä](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
- 404-sivut ei löytyville queryille (esim)
- Jatkuvasti chekattavaa / erityisesti lopussa
