# Aihekuvaus

Projektissa laaditaan järjestelmä, jossa ylläpidetään informaatiota [soinnuista](https://fi.wikipedia.org/wiki/Sointu) sekä kappaleista, joissa sointuja käytetään. Käyttäjät voivat kirjautua järjestelmään, hakea sieltä sointuja, lisätä, muokata ja poistaa kappaleita sekä lisätä sointuja kappaleiden yhteyteen. Järjestelmä osaa käsitellä kolmi- ja neliäänisiä sointuja (ns. power chordit ja neliäänisiä useammat soinnut jätetään huomiotta).

## Toiminnot:
- kirjautuminen
- soinnun hakeminen ja siinä esiintyvien sävelien listaaminen
- kaikkien sointujen listaaminen
- kappaleiden syöttö, poisto ja muokkaus

# Tietokantakaavio:
- Account((pk) id:Integer, date_created:Date, date_mofidied:Date, name:String, username:String, password:String)
- AccountFavouriteChord((fk) account_id -> Account, (fk) chord_id -> Chord)
- Chord((pk) id:Integer, name:String, chordtype:String)
- ChordNote((fk) chord_id -> Chord, (fk) note_id -> Note, rank:Integer)
- Note((pk) id:Integer, name:String)
