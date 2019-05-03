### Käyttötapauksia
-Kaikki käyttäjät voivat listata kaikki kurssit ja kaikki aihepiirit. Kurssit voidaan myös listata aihepiirikohtaisesti.   
-Rekisteröitymätön käyttäjä voi luoda uuden käyttäjätunnuksen. Rekisteröinnissä voi valita tekeekö normaalin vai admin-käyttäjän.  
-Rekisteröitymätön käyttäjä voi kirjautua.  
-Admin-käyttäjä voi lisätä uuden aihepiirin, muokata sen nimeä tai poistaa sen.  
-Admin-käyttäjä voi lisätä uuden kurssin parametreilla nimi, aihepiiri, aika, paikka ja ilmoittautuneiden maksimimäärä.  
-Admin-käyttäjä voi muokata kurssin parametreja tai poistaa kurssin.  
-Admin-käyttäjä voi tarkastella kaikkia varauksia. Varauksia voi myös tarkastella kurssikohtaisesti.  
-Admin-käyttäjä voi poistaa varauksen.  
-Admin käyttäjä voi muokata kurssin täydeksi tai takaisin. Täynnä olevaa kurssia ei voi varata.  
-Tavallinen käyttäjä voi varata kurssin.    
-Tavallinen Käyttäjä voi tarkastella varauksiaan.  
-Tavallinen käyttäjä voi "maksaa" kurssimaksun.  
-Tavallinen Käyttäjä voi poistaa varauksensa.  
-Kirjautunut käyttäjä voi kirjautua ulos.  

### Puutteita
-Aihepiirejä ja kursseja voi olla duplikaatteja samoilla parametreilla.  
-Aihepiirin poistaminen ei toimi herokussa jos siihen liittyy kursseja. Kurssit voi kuitenkin poistaa ensin, minkä jälkeen aihepiirin saa myös poistettua.   
-Kurssit voi listata aihepiirikohtaisesti, mutta jonkin kurssin toiminnon tekeminen vie "kaikki kurssit"-välilehdelle.   
-Varaukset voi listata kurssikohtaisesti, mutta varauksen poistaminen vie "kaikki varaukset"-välilehdelle.   
-Puuttuu paljon virheviestejä, kuten "kurssi on täynnä"-viesti kun yritetään varata täynnä olevaa kurssia. En saanut selville miten html-sivulle saa välitettyä viestejä, jos se ei ole form-muotoinen.   
-Käyttäjänimet ja salasanat voivat olla yhden merkin pituisia, mikä on varmaankin epämieluista.   
-Kurssin muokkaamisessa aihepiirivalikko valittaa "not a valid choise" vaikka sen voi jättää ennalleen. En myöskään keksinyt miten kyseisen viestin voisi muuttaa suomenkieliseksi niin kuin muut viestit.   

### Toteuttamatta jääneitä toiminnallisuuksia 
-Tietoa opettajista.  
-Kurssiesitteet.



