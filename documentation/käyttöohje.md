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

Kun sovellus on asennettu ohjeita noudattaen, niin virtuaaliympäristö pitää aina aktivoida ennen sovelluksen käynnistämistä paikallisesti.  

Sovelluksessa voi rekisteröityä painamalla Luo käyttäjä-painiketta. Jos Admin-ruksi on täytetty niin luot ylläpitäjätunnuksen, muuten luot normaalin käyttäjätunnuksen.

Normaali käyttäjä voi tarkastella kursseja ja varata niitä. Listaa varaukset-välilehdessä voi tarkastella omia varauksiaan. Varaukset voi peruuttaa tai voi "maksaa" kurssimaksun.

Ylläpitäjäkäyttäjä voi lisätä, muokata tai poistaa kursseja sekä aihepiirejä. Ylläpitäjäkäyttäjä voi myös listata kaikki varaukset ja poistaa niitä mielivaltaisesti. Varauksia voi tarkastella myös kurssikohtaisesti. Ylläpitäjäkäyttäjä voi myös asettaa kurssin täydeksi tai takaisin. Täynnä olevaa kurssia ei voi varata. Ylläpitäjäkäyttäjä voi esimerkiksi huomata kurssin varausten lukumäärän ylittävän varausten maksimimäärän. Tällöin ylläpitäjäkäyttäjä voi asettaa kurssin täydeksi ja poistaa haluamiaan varauksia.
