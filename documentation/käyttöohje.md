### Asennusohje

Sovellus ladataan Githubista zip-pakettina ja puretaan. Vaihtoehtoisesti voi käyttää git clone-komentoa. Sitten pitää luoda virtuaaliympäristö venv komennolla

```
python3 -m venv venv
```

Sitten virtuaaliympäristö aktivoidaan komennolla

```
source venv/bin/activate
```

Sitten sovelluksen riippuvuudet ladataan komennolla

```
pip install -r requirements.txt
```

Nyt sovelluksen voi käynnistää paikallisesti komennolla

```
python3 run.py
```

Jos sovelluksen haluaa ajaa herokussa niin voi painaa herokulinkkiä joka löytyy readme-tiedostosta.

### Käyttöohje

Kun sovellus on asennettu ohjeita noudattaen, niin virtuaaliympäristö pitää aina aktivoida ennen sovelluksen käynnistämistä.  

Sovelluksessa voi rekisteröityä painamalla Luo käyttäjä-painiketta. Jos Admin-ruksi on täytetty niin luot ylläpitäjätunnuksen, muuten luot normaalin käyttäjätunnuksen.
