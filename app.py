# importalom a flasket abból azokat a részeket amik kellenek a pymongo-t ami az adatbázis miatt van és a datetime az idő miatt
from flask import Flask, request, render_template, jsonify, flash, session, redirect, url_for
import pymongo
from datetime import datetime



# Flask alkalmazás létrehozása és a MongoDB kapcsolat
app = Flask(__name__)
app.secret_key = '123456789'

# MongoDB kapcsolat
client = pymongo.MongoClient("mongodb://localhost:27017")  # Lokális MongoDB
#létrehoz egy user izét azon beül pedig majd létrehoz egy users-t meg a másikat 
db = client["User"]
users = db["Log/pass"] 
uzenetek=db["uzenetek"]


#itt betölti az alap oldalt a fő oldalt a login oldalt
@app.route('/')
def index():
    return render_template('index.html')
#betölti a másik oldalt az index2 oldalt register oldalt
@app.route('/index2')
def index2():
    return render_template('index2.html')

# regisztráció
@app.route('/register', methods=['POST'])
def register():
    #itt lekéri igazából a email users pass szart szóval elmenti őket ebben a valtozoban hogy majd ellenőrizni tudja hogy van e már
    email = request.form['email']
    user = request.form['user']
    password = request.form['pass']
    
    #elenőrzi hogy a users kolekcióban van e már egyező izék
    if users.find_one({'email': email}):
        return render_template('index2.html', email_error="Ez az email/felhasználónév már regisztrálva van!")
    elif users.find_one({'user': user}):
        return render_template('index2.html', email_error="Ez az email/felhasználónév már regisztrálva van!")
    
    # felhasznáó hozzáadása az adatbázishoz
    users.insert_one({'email': email, 'user': user, 'password': password, })
    
    return render_template('index.html', email_jo="Sikeres regisztráció")


# Bejelentkezés
@app.route('/login', methods=['POST'])
def login():
    #itt megint mint előtte legéri és elmenti ideiglenesen azokat az izéket
    email = request.form['email']
    password = request.form['pass']


    #megkeresi a felhasználót hogy van e az email és a password alapján
    user = users.find_one({'email': email, 'password': password})
    if user: 
        session['user'] = user['user'] #ha van mind a kettő és jó akkor átvisz a home.html-re szóval yes session ez ilyen alap python izé ami publikus izét csinál
        return redirect(url_for("home"))
    else:
        return render_template('index.html', hiba="Hibás jelszó")#itt kidobja azt a valamit a fő oldalon ami nem jó 
    
#elvisz a home oldalra aztán a sessionból betölti a felhasználonevet aztán igen   
@app.route('/home', methods=['GET', 'POST'])
def home():
    if "user" not in session: #elenőrzi ha a session üres szóval nincs akkor oda visz a index.html oldalra
        return redirect(url_for("index"))
    return render_template("home.html", user=session['user']) #ha meg igen akkor ki írja a felhasznáónavet mer érted

#üzeten küldés 
@app.route('/kulduzenet', methods=['POST'])
def kulduzenet():
    szoveg = request.json.get('uzenet')

    uzenetek.insert_one({
        'nev': session['user'],
        'uzenet': szoveg,
        'ido': datetime.utcnow()
    })
    return jsonify({'status': 'ok'})

@app.route('/uzenetek')
def uzenetek_lekerese():
    #sorba rendezi az üzeneteket az ido szerint
    lista = list(uzenetek.find().sort('ido'))
    #ez vissza adja a nevet és az üzenetet egy for ciklus segítségével ami betölti az adabazisbol a nevet meg az üzenetet
    return jsonify([
        {'nev': u['nev'], 'uzenet': u['uzenet']} for u in lista
    ])
    
#kijelentkezés    
@app.route('/logout')
def logout():
    #törli a session-t és vissza visz az index.html oldalra ami a bejelentkezős izé 
    session.clear()
    return redirect(url_for("index"))

# Futtatás
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
