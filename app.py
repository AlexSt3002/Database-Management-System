from flask import Flask, render_template, request, redirect, url_for
from database import engine
from sqlalchemy import text
# Cod pentru afisarea elementelor fiecarui tabel
app = Flask(__name__)


def load_medici():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Medici"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all


def load_medicamente():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Medicamente"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all


def load_pacienti():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Pacienti"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all


def load_studii():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Studii_Clinice"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all


def load_locatie():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Locatie"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all
def load_medicistudiu():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Medici_studiu"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all
def load_participantistudiu():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Participanti_studiu"))
        result_all = []
        rows = result.fetchall()
        for row in rows:
            result_all.append(row)
        return result_all
def search_pacienti1(search_by, search_value):
    with engine.connect() as conn:
        # Asigură-te că search_by și search_value sunt corect sanitizate
        query = text(f"SELECT * FROM Pacienti WHERE {search_by} LIKE :search_value")
        result = conn.execute(query, {'search_value': f"%{search_value}%"})
        rows = result.fetchall()
        result_all = []
        for row in rows:
            result_all.append(row)
        return result_all
@app.route('/pacienti/search', methods=['GET'])
def search_pacienti():
    search_by = request.args.get('search_by')
    search_value = request.args.get('search_value')

    if search_by and search_value:
        # Apelăm funcția de căutare cu câmpul și valoarea de căutare
        pacienti_gasiti = search_pacienti1(search_by, search_value)
    else:
        pacienti_gasiti = []

    return render_template('pacienti.html', pacienti=pacienti_gasiti)
def search_medici1(search_by, search_value):
    with engine.connect() as conn:
        # Asigură-te că search_by și search_value sunt corect sanitizate
        query = text(f"SELECT * FROM Medici WHERE {search_by} LIKE :search_value")
        result = conn.execute(query, {'search_value': f"%{search_value}%"})
        rows = result.fetchall()
        result_all = []
        for row in rows:
            result_all.append(row)
        return result_all
@app.route('/medici/search', methods=['GET'])
def search_medici():
    search_by = request.args.get('search_by')
    search_value = request.args.get('search_value')

    if search_by and search_value:
        # Apelăm funcția de căutare cu câmpul și valoarea de căutare
        pacienti_gasiti = search_medici1(search_by, search_value)
    else:
        pacienti_gasiti = []

    return render_template('medici.html', medici=pacienti_gasiti)
def search_medicamente1(search_by, search_value):
    with engine.connect() as conn:
        # Asigură-te că search_by și search_value sunt corect sanitizate
        query = text(f"SELECT * FROM Medicamente WHERE {search_by} LIKE :search_value")
        result = conn.execute(query, {'search_value': f"%{search_value}%"})
        rows = result.fetchall()
        result_all = []
        for row in rows:
            result_all.append(row)
        return result_all
@app.route('/medicamente/search', methods=['GET'])
def search_medicamente():
    search_by = request.args.get('search_by')
    search_value = request.args.get('search_value')

    if search_by and search_value:
        # Apelăm funcția de căutare cu câmpul și valoarea de căutare
        pacienti_gasiti = search_medicamente1(search_by, search_value)
    else:
        pacienti_gasiti = []

    return render_template('medicamente.html', medicamente=pacienti_gasiti)
def search_studii1(search_by, search_value):
    with engine.connect() as conn:
        # Asigură-te că search_by și search_value sunt corect sanitizate
        query = text(f"SELECT * FROM Studii_Clinice WHERE {search_by} LIKE :search_value")
        result = conn.execute(query, {'search_value': f"%{search_value}%"})
        rows = result.fetchall()
        result_all = []
        for row in rows:
            result_all.append(row)
        return result_all
@app.route('/studii/search', methods=['GET'])
def search_studii():
    search_by = request.args.get('search_by')
    search_value = request.args.get('search_value')

    if search_by and search_value:
        # Apelăm funcția de căutare cu câmpul și valoarea de căutare
        pacienti_gasiti = search_studii1(search_by, search_value)
    else:
        pacienti_gasiti = []

    return render_template('studii.html', studii=pacienti_gasiti)
def search_locatie1(search_by, search_value):
    with engine.connect() as conn:
        # Asigură-te că search_by și search_value sunt corect sanitizate
        query = text(f"SELECT * FROM Locatie WHERE {search_by} LIKE :search_value")
        result = conn.execute(query, {'search_value': f"%{search_value}%"})
        rows = result.fetchall()
        result_all = []
        for row in rows:
            result_all.append(row)
        return result_all
@app.route('/locatie/search', methods=['GET'])
def search_locatie():
    search_by = request.args.get('search_by')
    search_value = request.args.get('search_value')

    if search_by and search_value:
        # Apelăm funcția de căutare cu câmpul și valoarea de căutare
        pacienti_gasiti = search_locatie1(search_by, search_value)
    else:
        pacienti_gasiti = []

    return render_template('locatie.html', locatie=pacienti_gasiti)
@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/medici')
def medici():
    medici = load_medici()
    return render_template('medici.html', medici=medici)


@app.route('/medicamente')
def medicamente():
    medicamente = load_medicamente()
    return render_template('medicamente.html', medicamente=medicamente)


@app.route('/pacienti')
def pacienti():
    pacienti = load_pacienti()
    return render_template('pacienti.html', pacienti=pacienti)


@app.route('/studii')
def studii():
    studii = load_studii()
    return render_template('studii.html', studii=studii)


@app.route('/locatie')
def locatie():
    locatie = load_locatie()
    return render_template('locatie.html', locatie=locatie)

@app.route('/medici_studiu')
def medici_studiu():
    studii = load_medicistudiu()
    return render_template('medici_studiu.html', studii=studii)

@app.route('/participanti_studiu')
def participanti_studiu():
    studii = load_participantistudiu()
    return render_template('participanti_studiu.html', studii=studii)

# Cod pentru adaugare/stergere/editare elemente din fiecare tabel
@app.route('/studiu/add', methods=['POST'])
def add_medic_studiu():
    id_studiu = request.form['id_studiu']
    id_medic = request.form['id_medic']
    nr_pacienti = request.form['nr_pacienti']
    nr_ore = request.form['nr_ore']

    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Medici_studiu (Id_studiu1, Id_medic1, Nr_pacienti, Nr_ore) 
                VALUES (:id_studiu, :id_medic, :nr_pacienti, :nr_ore)
            """), {
                "id_studiu": id_studiu,
                "id_medic": id_medic,
                "nr_pacienti": nr_pacienti,
                "nr_ore": nr_ore
            })
        conn.commit()
    return redirect(url_for('medici_studiu'))  

@app.route('/medici_studiu/delete/<int:id_medic>/<int:id_studiu>', methods=['POST'])
def delete_medic_studiu(id_medic, id_studiu):
    
    with engine.connect() as conn:
        
        conn.execute(
            text("""Delete FROM Medici_studiu WHERE Id_medic1 = :id_medic AND Id_studiu1 = :id_studiu"""), 
            {"id_medic": id_medic, "id_studiu": id_studiu}
        )
        conn.commit()
    return redirect(url_for('medici_studiu'))
@app.route('/participanti_studiu/add', methods=['POST'])
def add_participanti_studiu():
    id_pacient = request.form['id_pacient']
    id_studiu = request.form['id_studiu']
    data_inrolare = request.form['data_inrolare']
    stare_participare = request.form['stare_participare']

    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Participanti_studiu (Id_pacient, Id_studiu, Data_inrolare, Stare_participare) 
                VALUES (:id_pacient, :id_studiu, :data_inrolare, :stare_participare)
            """), {
                "id_pacient": id_pacient,
                "id_studiu": id_studiu,
                "data_inrolare": data_inrolare,
                "stare_participare": stare_participare
            })
        conn.commit()
    return redirect(url_for('participanti_studiu'))  
@app.route('/participanti_studiu/delete/<int:id_pacient>/<int:id_studiu>', methods=['POST'])
def delete_participanti_studiu(id_pacient, id_studiu):
    
    with engine.connect() as conn:
       
        conn.execute(
            text("""Delete FROM Participanti_studiu WHERE Id_pacient = :id_pacient AND Id_studiu = :id_studiu"""), 
            {"id_pacient": id_pacient, "id_studiu": id_studiu}
        )
        conn.commit()
    return redirect(url_for('participanti_studiu'))
    
@app.route('/medici/add', methods=['POST'])
def add_medic():
    nume = request.form['nume']
    prenume = request.form['prenume']
    specializare = request.form['specializare']
    email = request.form['email']
    telefon = request.form['telefon']
    spital = request.form['spital']
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Medici (Nume, Prenume, Specializare, Email, Telefon, Spital) 
                VALUES (:nume, :prenume, :specializare, :email, :telefon, :spital)
            """), {
                "nume": nume,
                "prenume": prenume,
                "specializare": specializare,
                "email": email,
                "telefon": telefon,
                "spital": spital
            })
        conn.commit()
    return redirect(url_for('medici'))


@app.route('/medici/edit/<int:id>', methods=['POST'])
def edit_medic(id):
    nume = request.form['nume']
    prenume = request.form['prenume']
    specializare = request.form['specializare']
    email = request.form['email']
    telefon = request.form['telefon']
    spital = request.form['spital']
    with engine.connect() as conn:
        conn.execute(
            text(
                """UPDATE Medici SET Nume=:nume, Prenume=:prenume, Specializare=:specializare, Email=:email, Telefon=:telefon, Spital=:spital WHERE Id_medic=:id"""
            ), {
                "nume": nume,
                "prenume": prenume,
                "specializare": specializare,
                "email": email,
                "telefon": telefon,
                "spital": spital,
                "id": id
            })
        conn.commit()
    return redirect(url_for('medici'))


@app.route('/medici/delete/<int:id>', methods=['POST'])
def delete_medic(id):
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Participanti_studiu 
WHERE Id_pacient IN (
    SELECT p.Id_pacient
    FROM Pacienti p
    WHERE p.Id_medic = :id
);"""),
                     {"id": id})
        conn.commit()
        with engine.connect() as conn:
            conn.execute(text("""DELETE FROM Pacienti WHERE Id_medic=:id"""),
                         {"id": id})
            conn.commit()
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Medici_studiu WHERE Id_medic1=:id"""),
                     {"id": id})
        conn.commit()
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Medici WHERE Id_medic=:id"""),
                     {"id": id})
        conn.commit()
        
    return redirect(url_for('medici'))


@app.route('/medicamente/add', methods=['POST'])
def add_medicament():
    nume_medicament = request.form['nume_medicament']
    efecte_adverse = request.form['efecte_adverse']
    doza = request.form['doza']
    producator = request.form['producator']
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Medicamente (Nume_medicament, Efecte_adverse, Doza, Producator) 
                VALUES (:nume_medicament, :efecte_adverse, :doza, :producator)
            """), {
                "nume_medicament": nume_medicament,
                "efecte_adverse": efecte_adverse,
                "doza": doza,
                "producator": producator
            })
        conn.commit()
    return redirect(url_for('medicamente'))


@app.route('/medicamente/edit/<int:id>', methods=['POST'])
def edit_medicament(id):
    nume_medicament = request.form['nume_medicament']
    efecte_adverse = request.form['efecte_adverse']
    doza = request.form['doza']
    producator = request.form['producator']
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE Medicamente 
                SET Nume_medicament=:nume_medicament, Efecte_adverse=:efecte_adverse, Doza=:doza, Producator=:producator 
                WHERE Id_medicament=:id
            """), {
                "nume_medicament": nume_medicament,
                "efecte_adverse": efecte_adverse,
                "doza": doza,
                "producator": producator,
                "id": id
            })
        conn.commit()
    return redirect(url_for('medicamente'))


@app.route('/medicamente/delete/<int:id>', methods=['POST'])
def delete_medicament(id):
    with engine.connect() as conn:
        conn.execute(
            text("""DELETE FROM Studii_Clinice WHERE Id_medicament=:id"""),
            {"id": id})
        conn.commit()
    with engine.connect() as conn:
        conn.execute(
            text("""DELETE FROM Medicamente WHERE Id_medicament=:id"""),
            {"id": id})
        conn.commit()
    return redirect(url_for('medicamente'))


@app.route('/pacienti/add', methods=['POST'])
def add_pacient():
    nume = request.form['nume']
    prenume = request.form['prenume']
    cnp = request.form['cnp']
    data_nasterii = request.form['data_nasterii']
    sex = request.form['sex']
    adresa = request.form['adresa']
    telefon = request.form['telefon']
    id_medic = request.form['id_medic']
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Pacienti (Nume, Prenume, CNP, Data_nasterii, Sex, Adresa, Telefon, Id_medic) 
                VALUES (:nume, :prenume, :cnp, :data_nasterii, :sex, :adresa, :telefon, :id_medic)
            """), {
                "nume": nume,
                "prenume": prenume,
                "cnp": cnp,
                "data_nasterii": data_nasterii,
                "sex": sex,
                "adresa": adresa,
                "telefon": telefon,
                "id_medic": id_medic
            })
        conn.commit()
    return redirect(url_for('pacienti'))


@app.route('/pacienti/edit/<int:id>', methods=['POST'])
def edit_pacient(id):
    nume = request.form['nume']
    prenume = request.form['prenume']
    cnp = request.form['cnp']
    data_nasterii = request.form['data_nasterii']
    sex = request.form['sex']
    adresa = request.form['adresa']
    telefon = request.form['telefon']
    id_medic = request.form['id_medic']
    with engine.connect() as conn:
        conn.execute(
            text("""
                UPDATE Pacienti 
                SET Nume=:nume, Prenume=:prenume, CNP=:cnp, Data_nasterii=:data_nasterii, 
                    Sex=:sex, Adresa=:adresa, Telefon=:telefon, Id_medic=:id_medic
                WHERE Id_pacient=:id
            """), {
                "nume": nume,
                "prenume": prenume,
                "cnp": cnp,
                "data_nasterii": data_nasterii,
                "sex": sex,
                "adresa": adresa,
                "telefon": telefon,
                "id_medic": id_medic,
                "id": id
            })
        conn.commit()
    return redirect(url_for('pacienti'))


@app.route('/pacienti/delete/<int:id>', methods=['POST'])
def delete_pacient(id):
    with engine.connect() as conn:
        conn.execute(text(""" DELETE FROM Participanti_studiu WHERE Id_pacient =:id;
        """
        ),
                     {"id": id})
        conn.commit()
        with engine.connect() as conn:
            conn.execute(text(""" DELETE FROM Pacienti WHERE Id_pacient=:id"""
            ),
                         {"id": id})
            conn.commit()
    return redirect(url_for('pacienti'))


@app.route('/locatie/add', methods=['POST'])
def add_locatie():
    nume_locatie = request.form['nume_locatie']
    adresa = request.form['adresa']
    oras = request.form['oras']
    judet = request.form['judet']
    cod_postal = request.form['cod_postal']
    telefon_contact = request.form['telefon_contact']
    email = request.form['email']
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Locatie (Nume_locatie, Adresa, Oras, Judet, Cod_postal, Telefon_contact, Email) 
                VALUES (:nume_locatie, :adresa, :oras, :judet, :cod_postal, :telefon_contact, :email)
            """), {
                "nume_locatie": nume_locatie,
                "adresa": adresa,
                "oras": oras,
                "judet": judet,
                "cod_postal": cod_postal,
                "telefon_contact": telefon_contact,
                "email": email
            })
        conn.commit()
    return redirect(url_for('locatie'))


@app.route('/locatie/edit/<int:id>', methods=['POST'])
def edit_locatie(id):
    nume_locatie = request.form['nume_locatie']
    adresa = request.form['adresa']
    oras = request.form['oras']
    judet = request.form['judet']
    cod_postal = request.form['cod_postal']
    telefon_contact = request.form['telefon_contact']
    email = request.form['email']
    with engine.connect() as conn:
        conn.execute(
            text(
                """UPDATE Locatie SET Nume_locatie=:nume_locatie, Adresa=:adresa, Oras=:oras, Judet=:judet, Cod_postal=:cod_postal, Telefon_contact=:telefon_contact, Email=:email WHERE Id_locatie=:id"""
            ), {
                "nume_locatie": nume_locatie,
                "adresa": adresa,
                "oras": oras,
                "judet": judet,
                "cod_postal": cod_postal,
                "telefon_contact": telefon_contact,
                "email": email,
                "id": id
            })
        conn.commit()
    return redirect(url_for('locatie'))


@app.route('/locatie/delete/<int:id>', methods=['POST'])
def delete_locatie(id):
    with engine.connect() as conn:
        conn.execute(
            text("""DELETE FROM Studii_Clinice WHERE Id_locatie=:id"""),
            {"id": id})
        conn.commit()
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Locatie WHERE Id_locatie=:id"""),
                     {"id": id})
        conn.commit()
    return redirect(url_for('locatie'))


@app.route('/studii/add', methods=['POST'])
def add_studiu():
    nume_studiu = request.form['nume_studiu']
    data_incepere = request.form['data_incepere']
    data_finalizare = request.form['data_finalizare']
    stadiu = request.form['stadiu']
    descriere = request.form['descriere']
    id_medicament = request.form['id_medicament']
    id_locatie = request.form['id_locatie']
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO Studii_Clinice (Nume_studiu, Data_incepere, Data_finalizare, Stadiu, Descriere, Id_medicament, Id_locatie) 
                VALUES (:nume_studiu, :data_incepere, :data_finalizare, :stadiu, :descriere, :id_medicament, :id_locatie)
            """), {
                "nume_studiu": nume_studiu,
                "data_incepere": data_incepere,
                "data_finalizare": data_finalizare,
                "stadiu": stadiu,
                "descriere": descriere,
                "id_medicament": id_medicament,
                "id_locatie": id_locatie
            })
        conn.commit()
    return redirect(url_for('studii'))


@app.route('/studii/edit/<int:id>', methods=['POST'])
def edit_studiu(id):
    nume_studiu = request.form['nume_studiu']
    data_incepere = request.form['data_incepere']
    data_finalizare = request.form['data_finalizare']
    stadiu = request.form['stadiu']
    descriere = request.form['descriere']
    id_medicament = request.form['id_medicament']
    id_locatie = request.form['id_locatie']
    with engine.connect() as conn:
        conn.execute(
            text(
                """UPDATE Studii_Clinice SET Nume_studiu=:nume_studiu, Data_incepere=:data_incepere, Data_finalizare=:data_finalizare, Stadiu=:stadiu, Descriere=:descriere, Id_medicament=:id_medicament, Id_locatie=:id_locatie WHERE Id_studiu=:id"""
            ), {
                "nume_studiu": nume_studiu,
                "data_incepere": data_incepere,
                "data_finalizare": data_finalizare,
                "stadiu": stadiu,
                "descriere": descriere,
                "id_medicament": id_medicament,
                "id_locatie": id_locatie,
                "id": id
            })
        conn.commit()
    return redirect(url_for('studii'))


@app.route('/studii/delete/<int:id>', methods=['POST'])
def delete_studiu(id):
    with engine.connect() as conn:
        conn.execute(
            text("""DELETE FROM Medici_studiu WHERE Id_studiu1=:id"""),
            {"id": id})
        conn.commit()
        with engine.connect() as conn:
            conn.execute(
                text("""DELETE FROM Participanti_studiu WHERE Id_studiu=:id"""),
                {"id": id})
            conn.commit()
    with engine.connect() as conn:
        conn.execute(
            text("""DELETE FROM Studii_Clinice WHERE Id_studiu=:id"""),
            {"id": id})
        conn.commit()
    return redirect(url_for('studii'))


#Cod pentru interogarile simple si complexe
@app.route('/join1')
def join1():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
            SELECT 
            med.Nume, 
            stud.Nume_studiu,
            ms.Nr_ore,
            ms.Nr_pacienti
        FROM 
            Medici med
        JOIN 
            Medici_studiu ms ON med.Id_medic = ms.Id_medic1
        JOIN
            Studii_Clinice stud ON ms.Id_studiu1 = stud.Id_studiu
        """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Medici Studii")



@app.route('/join2')
def join2():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT 
              paci.Nume, 
              stud.Nume_studiu,
              ps.Data_inrolare,
              ps.Stare_participare
          FROM 
              Pacienti paci
          JOIN 
              Participanti_studiu ps ON paci.Id_pacient = ps.Id_pacient
          JOIN
              Studii_Clinice stud ON ps.Id_studiu = stud.Id_studiu
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Pacienti Studii")



@app.route('/join3')
def join3():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT 
              paci.Nume, 
              med.Nume
              
          FROM 
              Pacienti paci
          JOIN 
              Medici med ON paci.Id_medic = med.Id_medic
          
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Pacienti Medici")



@app.route('/join4')
def join4():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              
          SELECT 
              stud.Nume_studiu, 
              med.Nume_medicament

          FROM 
              Studii_Clinice stud
          JOIN 
              Medicamente med ON stud.Id_medicament = med.Id_medicament
          ORDER BY  stud.Nume_studiu DESC;
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Studiu Medicament")



@app.route('/join5')
def join5():
    with engine.connect() as conn:
        result = conn.execute(
            text("""

        SELECT 
            loc.Nume_locatie,
            stud.Nume_studiu
            
        FROM 
            Studii_Clinice stud
        JOIN 
            Locatie loc ON stud.Id_locatie = loc.Id_locatie
        Where loc.Nume_locatie Like 'C%';
        """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Locatie C Studii")



@app.route('/join6')
def join6():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT 
              med.Nume, 
              ms.Nr_ore              
          FROM 
              Medici med
          JOIN 
              Medici_studiu ms ON med.Id_medic = ms.Id_medic1
          ORDER BY ms.Nr_ore DESC
          Limit 3
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Medici Ore")


@app.route('/complex1')
def complex1():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT md.nume_medicament, md.producator
FROM Medicamente md
WHERE md.Id_medicament IN (
    SELECT sc.Id_medicament
    FROM Studii_Clinice sc
    WHERE sc.Id_locatie IN (
        SELECT l.Id_locatie
        FROM Locatie l
        WHERE l.Oras = 'București'))
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Medici Ore")


@app.route('/complex2')
def complex2():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT md.nume_medicament, md.producator
FROM Medicamente md
WHERE md.Id_medicament NOT IN (
    SELECT sc.Id_medicament
    FROM Studii_Clinice sc
);
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Medici Ore")


@app.route('/complex3')
def complex3():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT m.nume, m.specializare
FROM Medici m
WHERE m.Id_medic IN (
    SELECT ms.Id_medic1
    FROM Medici_studiu ms
    WHERE ms.Id_studiu1 = (
        SELECT ps.Id_studiu
        FROM Participanti_studiu ps
        GROUP BY ps.Id_studiu
        ORDER BY COUNT(ps.Id_pacient) DESC
        LIMIT 1
    )
);
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Medici Ore")


@app.route('/complex4')
def complex4():
    with engine.connect() as conn:
        result = conn.execute(
            text("""
              SELECT sc.nume_studiu
FROM Studii_Clinice sc
WHERE sc.Id_studiu IN (
    SELECT ps.Id_studiu
    FROM Participanti_studiu ps
    JOIN Pacienti p ON ps.Id_pacient = p.Id_pacient
    GROUP BY ps.Id_studiu
    HAVING SUM(CASE WHEN p.sex = 'F' THEN 1 ELSE 0 END) > 
           SUM(CASE WHEN p.sex = 'M' THEN 1 ELSE 0 END)
);
          """))
        rows = result.fetchall()
        columns = result.keys()
    return render_template('join_results.html',
                           rows=rows,
                           columns=columns,
                           query=" Medici Ore")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
