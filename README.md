# Web-backend-PY 🌐

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![MongoDB](https://img.shields.io/badge/MongoDB-4.4-brightgreen)

## Leírás
Ez egy **Flask alapú webalkalmazás**, amit én készítettem.  
Lehetővé teszi a felhasználói regisztrációt, bejelentkezést, üzenetküldést és session-kezelést MongoDB adatbázissal.

A játékos/jelentkező felhasználók:  
- Regisztrálhatnak és bejelentkezhetnek.  
- Küldhetnek üzeneteket, amiket az adatbázisban tárol a rendszer.  
- Böngészőben láthatják az üzeneteket JSON formátumban.

---

## Fő funkciók
- ✅ **Felhasználói regisztráció**: ellenőrzi az email és felhasználónév egyediségét.  
- ✅ **Bejelentkezés**: session-kezeléssel biztosítja a belépett felhasználó azonosítását.  
- ✅ **Üzenetküldés**: POST JSON formátumban (`/kulduzenet`).  
- ✅ **Üzenetek lekérése**: GET `/uzenetek` — JSON formátum, időrend szerint.  
- ✅ **Logout**: session törlése és visszairányítás a főoldalra.

---

## Telepítés és futtatás

### 1️⃣ Klónozd a repót
```bash
git clone https://github.com/mekercs/Web-backend-PY.git
cd Web-backend-PY
2️⃣ Telepítsd a függőségeket
bash
Kód másolása
pip install flask pymongo
3️⃣ Ellenőrizd a MongoDB-t
Győződj meg róla, hogy a MongoDB fut a localhost:27017 címen.

4️⃣ Futtatás
bash
Kód másolása
python app.py
5️⃣ Böngészőben
arduino
Kód másolása
http://localhost/
Projekt felépítése
csharp
Kód másolása
Web-backend-PY/
│
├─ app.py             # Flask backend logika
├─ templates/         # HTML fájlok
│   ├─ index.html
│   ├─ index2.html
│   └─ home.html
└─ static/            # (opcionális) CSS, JS fájlok
MongoDB gyűjtemények
Log/pass → felhasználók

uzenetek → küldött üzenetek

Hogyan működik a backend
Flask app létrehozása, secret key beállítása:

python
Kód másolása
app = Flask(__name__)
app.secret_key = '123456789'
MongoDB kapcsolat létrehozása:

python
Kód másolása
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["User"]
users = db["Log/pass"]
uzenetek = db["uzenetek"]
Oldalak:

/ → Bejelentkezés (index.html)

/index2 → Regisztráció (index2.html)

/home → Bejelentkezett felhasználó (home.html)

Regisztráció:

Ellenőrzi az email és felhasználónév egyediségét.

Új felhasználót ad hozzá a users gyűjteményhez.

Bejelentkezés:

Ellenőrzi az email és jelszó párost.

Létrehoz egy session-t a felhasználóhoz.

Üzenetküldés:

/kulduzenet POST: JSON tartalmazza a uzenet mezőt.

Mentés a uzenetek gyűjteménybe, időbélyeggel.

Üzenetek lekérése:

/uzenetek GET: visszaadja a felhasználó nevét és az üzenetet JSON-ban, időrend szerint.

Logout:

Session törlése, visszairányítás a főoldalra.

Készítette
mekercs
