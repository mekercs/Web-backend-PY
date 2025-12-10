# Web-backend-PY 🌐

## Rövid leírás  
Ez a projekt egy **Python Flask alapú webalkalmazás**, amit én készítettem.  
A célja egy **felhasználói rendszer** létrehozása MongoDB adatbázissal, ami lehetővé teszi a regisztrációt, bejelentkezést, üzenetküldést és a session-kezelést.  

## ⚙️ Fő funkciók
- **Regisztráció**: új felhasználók hozzáadása az adatbázishoz, ellenőrizve az email és felhasználónév egyediségét.  
- **Bejelentkezés**: session-alapú autentikáció.  
- **Üzenetküldés**: felhasználók üzeneteket küldhetnek, amiket a MongoDB tárol.  
- **Üzenetek lekérése**: JSON formátumban, időrendi sorrendben.  
- **Logout**: session törlése és visszairányítás a főoldalra.  

## 🛠️ Hogyan működik
1. **Flask app létrehozása** és MongoDB kapcsolat:  
   ```python
   app = Flask(__name__)
   app.secret_key = '123456789'
   client = pymongo.MongoClient("mongodb://localhost:27017")
   db = client["User"]
   users = db["Log/pass"]
   uzenetek = db["uzenetek"]
Oldalak:

/ → index.html (bejelentkezés)

/index2 → index2.html (regisztráció)

/home → home.html (bejelentkezett felhasználó)

Regisztráció: ellenőrzi, hogy az email vagy felhasználónév már létezik-e, majd új felhasználót ad az adatbázishoz.

Bejelentkezés: session-t hoz létre, ha a felhasználó és a jelszó helyes.

Üzenetküldés: POST /kulduzenet, a JSON-ban érkező üzenetet menti a MongoDB-be nev, uzenet, ido mezőkkel.

Üzenetek lekérése: GET /uzenetek, visszaadja a felhasználó nevét és az üzenetet időrendben JSON-ban.

Logout: session törlése és visszairányítás a főoldalra.

🚀 Telepítés és futtatás
Klónozd a repót:

bash
Kód másolása
git clone https://github.com/mekercs/Web-backend-PY.git
Telepítsd a függőségeket:

bash
Kód másolása
pip install flask pymongo
Győződj meg róla, hogy a MongoDB fut a localhost:27017 címen.

Futtasd a Flask alkalmazást:

bash
Kód másolása
python app.py
Nyisd meg a böngészőt:

arduino
Kód másolása
http://localhost/
📦 Projekt felépítése
app.py – a teljes backend logika (Flask + MongoDB + session).

templates/ – HTML fájlok (index.html, index2.html, home.html).

static/ (opcionális) – CSS, JS fájlok.

MongoDB gyűjtemények:

Log/pass → felhasználók

uzenetek → küldött üzenetek

👤 Készítette
mekercs
