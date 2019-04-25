### Tietokantarakenne

[tietokantakaavio](https://raw.githubusercontent.com/robertrantanen/Kurssitarjonta-ja-kurssipaikan-varaus/master/documentation/tietokantakaavio.jpg)

Tietokantakaavio kuvastaa sovelluksen nykyistä toiminnallisuutta. Lopullisessa versiossa on mahdollisesti myös taulut aihepiirille ja opettajalle sekä liitostaulu opettajan ja kurssin välillä. Kurssin aika on tarkoituksella merkkijonomuotoinen ,jotta siihen voi kirjoittaa esim. "kevät 2019". Kurssin täynnä-sarake pitäisi olla boolean, mutta se on sovelluksessa nyt merkkijono, jotta siihen saadaan arvot "kyllä" ja "ei". Account-taulu on nyt kömpelösti englanniksi kun muut ovat suomeksi, tämä muuttuu mahdollisesti lopullisessa versiossa.

#### Create table-lauseet:

CREATE TABLE kurssi (  
	id INTEGER NOT NULL,   
	nimi VARCHAR(144) NOT NULL,   
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
	PRIMARY KEY (account_id, kurssi_id),   
	FOREIGN KEY(account_id) REFERENCES account (id),   
	FOREIGN KEY(kurssi_id) REFERENCES kurssi (id)  
)  

#### SQL-kyselyitä

Kaikkien kurssien listaaminen tapahtuu yhteenvetokyselyllä, joka selvittää myös kurssin varausten lukumäärän:

SELECT Kurssi.id, Kurssi.nimi, Kurssi.aika, Kurssi.paikka, Kurssi.maksimikoko, COUNT(Varaus.kurssi_id) AS maara,  
Kurssi.taynna FROM Kurssi  
LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id  
GROUP BY Kurssi.id, Kurssi.nimi;  

Tietyn käyttäjän varaukset selviävät seuraavalla kyselyllä:

SELECT * FROM Kurssi  
LEFT JOIN Varaus ON Varaus.kurssi_id = Kurssi.id  
WHERE (Varaus.account_id = ?);  

Sovelluksessa parametrina annetaan nykyisen normaalikäyttäjän id.

