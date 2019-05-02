### Tietokantarakenne

![tietokantakaavio](https://raw.githubusercontent.com/robertrantanen/Kurssitarjonta-ja-kurssipaikan-varaus/master/documentation/tietokantakaavio.png)

Tietokantakaavio kuvastaa sovelluksen nykyistä toiminnallisuutta. Kurssin aika on tarkoituksella merkkijonomuotoinen, jotta siihen voi kirjoittaa esim. "kevät 2019". Kurssin täynnä-sarake sekä varauksen maksettu-sarake pitäisivät olla boolean, mutta ne ovat sovelluksessa nyt merkkijonoja, jotta niihin saadaan arvot "kyllä" ja "ei". Account-taulu on nyt kömpelösti englanniksi kun muut ovat suomeksi, en jaksanut korjata sitä sillä pelkäsin sovelluksen rikkoutuvan.

#### Create table-lauseet:

CREATE TABLE aihepiiri (  
	id INTEGER NOT NULL,   
	nimi VARCHAR(144) NOT NULL,   
	PRIMARY KEY (id)  
)  


CREATE TABLE kurssi (  
	id INTEGER NOT NULL,   
	nimi VARCHAR(144) NOT NULL,   
	aihepiiri_id INTEGER NOT NULL,  
	aika VARCHAR(144),   
	paikka VARCHAR(144),   
	maksimikoko INTEGER,   
	taynna VARCHAR(144),    
	PRIMARY KEY (id)  
)  

CREATE TABLE account (  
	id INTEGER NOT NULL,   
	username VARCHAR(144) NOT NULL,   
	password VARCHAR(144) NOT NULL,   
	admin BOOLEAN NOT NULL,   
	PRIMARY KEY (id),   
)  

CREATE TABLE varaus (  
	account_id INTEGER NOT NULL,   
	kurssi_id INTEGER NOT NULL,   
	maksettu VARCHAR(144),   
	PRIMARY KEY (account_id, kurssi_id),   
	FOREIGN KEY(account_id) REFERENCES account (id),   
	FOREIGN KEY(kurssi_id) REFERENCES kurssi (id)   
)  

#### SQL-kyselyitä

Kaikkien kurssien listaaminen tapahtuu yhteenvetokyselyllä, joka selvittää myös kurssin varausten lukumäärän:

SELECT Kurssi.id, Kurssi.nimi, Aihepiiri.nimi AS aihepiiri, Kurssi.aika, Kurssi.paikka, Kurssi.maksimikoko, COUNT(Varaus.kurssi_id) AS maara, Kurssi.taynna FROM Kurssi  
LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id  
LEFT JOIN Aihepiiri ON Kurssi.aihepiiri_id = Aihepiiri.id  
GROUP BY Kurssi.id, Kurssi.nimi, Aihepiiri.id;  

Seuraava yhteenvetokysely selvittää kaikki aihepiirit ja niiden kurssien lukumäärät:

SELECT Aihepiiri.id, Aihepiiri.nimi, COUNT(Kurssi.id) AS kurssit FROM Aihepiiri  
LEFT JOIN Kurssi ON Kurssi.aihepiiri_id = Aihepiiri.id   
GROUP BY Aihepiiri.id;  

Uuden käyttäjän, kurssin, aihepiirin tai varauksen luominen tapahtuu suoraviivaisesti INSERT INTO-kyselyillä:

INSERT INTO account (username, password, admin) VALUES (?, ?, ?)  
INSERT INTO aihepiiri (nimi) VALUES (?)  
INSERT INTO kurssi (nimi, aihepiiri_id, aika, paikka, maksimikoko, taynna) VALUES (?, ?, ?, ?, ?, ?)  
INSERT INTO varaus (account_id, kurssi_id, maksettu) VALUES (?, ?, ?)  

Tiedon poistaminen ja muokkaaminen on myös niin ikään suoraviivaista:

DELETE FROM varaus WHERE varaus.account_id = ? AND varaus.kurssi_id = ?  
DELETE FROM kurssi WHERE kurssi.id = ?  
DELETE FROM aihepiiri WHERE aihepiiri.id = ?  

UPDATE kurssi SET nimi=?, aihepiiri_id=?, aika=?, paikka=?, maksimikoko=? WHERE kurssi.id = ?  
UPDATE aihepiiri SET nimi=? WHERE aihepiiri.id = ?  

Kurssin täynnä-sarakkeen ja varauksen maksettu-sarakkeen muokkaaminen tapahtuu myös UPDATE-kyselyillä:

UPDATE kurssi SET taynna=? WHERE kurssi.id = ?  
UPDATE varaus SET maksettu=? WHERE varaus.account_id = ? AND varaus.kurssi_id = ?  

Tietyn käyttäjän varatut kurssit selviävät seuraavalla kyselyllä:

SELECT * Kurssi.id, Kurssi.nimi, Kurssi.aika, Kurssi.paikka, Varaus.maksettu FROM Kurssi    
LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id  
WHERE (Varaus.account_id = ?);  

Sovelluksessa parametrina annetaan nykyisen normaalikäyttäjän id. 
