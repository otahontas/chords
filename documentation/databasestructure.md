# Tietokantarakenteen kuvaus

## Tietokantakaavio


## Create TABLE -lauseet
**Status 9.8.**

```
CREATE TABLE note (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
);

CREATE TABLE chord (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        "key" VARCHAR(144) NOT NULL,
        name VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE chord_note (
        id INTEGER NOT NULL,
        chord_id INTEGER NOT NULL,
        note_id INTEGER NOT NULL,
        rank INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(chord_id) REFERENCES chord (id),
        FOREIGN KEY(note_id) REFERENCES note (id)
);
```
