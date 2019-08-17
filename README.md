# Demo

[Live-demo Herokussa](https://sointutietokanta.herokuapp.com/)
Testitunnukset:
- käyttäjä: testi
- salasana: testinen123

# Aihekuvaus

Projektissa laaditaan järjestelmä, jossa ylläpidetään informaatiota [soinnuista](https://fi.wikipedia.org/wiki/Sointu) ja kappaleista, joissa sointuja käytetään. Käyttäjät voivat kirjautua järjestelmään, hakea sieltä sointuja, lisätä sointuja, lisätä, muokata ja poistaa kappaleita sekä lisätä sointuja kappaleiden* yhteyteen. Vain admin-tunnuksilla voi muokata tai poistaa sointuja - tällä vältetään kappaleisiin kiinnitettyjen sointujen ilkivaltainen poistaminen. Lisäksi kappaleita voi merkityä suosikseiksi

Järjestelmä osaa käsitellä kolmiäänisiä sointuja (ns. power chordit sekä kolmisointuja laajemmat soinnut jätetään huomiotta). Alkutilanteessa tietokanta sisältää ainoastaan nuotteja, joista soinnut koostetaan. Sointupankki kehittyy käyttäjien syöttäessä tietokantaan lisää sointuja.

## Toiminnot:
- kirjautuminen ja uuden käyttäjän luominen
- soinnun lisääminen
- kaikkien sointujen listaaminen, sointujen hakeminen ja siinä esiintyvien sävelien listaaminen
- kappaleiden lisääminen, listaaminen ja hakeminen sekä muokkaaminen ja poistaminen (CRUD-ominaisuudet)
- sointujen lisääminen kappaleisiin sekä sointujen listaaminen kappaleen yhteydessä
- kappaleiden merkkaaminen suosikiksi
- suosituimpien kappaleiden listaaminen (jos kerkeää)
- Lisäksi ylläpitäjän toiminnot:
    - Muokkaa tai poista sointuja
    - Listaa, muokkaa tai poista käyttäjiä


# Dokumentaatio:
- [Käyttötapaukset](/documentation/userstories.md)
- [Tietokantarakenteen kuvaus](/documentation/databasestructure.md)

# TODO:
- Kappaleiden alle kappaleiden lisäys, kaikkien listaaminen, yksittäisen katselu muokkaaminen ja poistaminen
- Song ja chord linkitykset
- yhteenvetokyselyt etusivulle
- Haku
- passwordit salatuiksi kannassa
- admin-toolit ja sointujen päivittämisnäkymä
- Suosikkisoinnut
- sointujen rankin lisääminen oikein kun sävelet on oikeesti eri järjestyksessä
- redirektaus loginin jälkeen takas osoitteeseen, josta käyttäjä tuli ks. esim [täältä](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
- Jatkuvasti chekattavaa / erityisesti lopussa
    - dokumentaatio
    - koodin selkeys (naming conventions, docstrings, moduulit)
    - abstrahointi + moduuleihin eristäminen
    - Päivitä käyttötapauksia
    - Tee käyttötapauksien SQL-kyselyt
    - Tee asennusohjeet
    - Tee käyttöohjeet
- Siivoilu
    - poista unnecessary stuff reposta
    - .gitignore kunnossa
    - development mode pois
