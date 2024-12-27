from flask import Flask, render_template, request, redirect, url_for
from database import engine
from sqlalchemy import text
app=Flask(__name__)
def load_medici():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Medici"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_medicamente():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Medicamente"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_pacienti():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Pacienti"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_studii():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Studii_Clinice"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all

def load_locatie():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Locatie"))
    result_all=[]
    rows = result.fetchall()  
    for row in rows:
      result_all.append(row)
    return result_all
      
@app.route('/')
def hello_world():
  return render_template('home.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/medici')
def medici():
  medici=load_medici()
  return render_template('medici.html',medici=medici)
@app.route('/medicamente')
def medicamente():
  medicamente=load_medicamente()
  return render_template('medicamente.html',medicamente=medicamente)

@app.route('/pacienti')
def pacienti():
  pacienti=load_pacienti()
  return render_template('pacienti.html',pacienti=pacienti)

@app.route('/studii')
def studii():
  studii=load_studii()
  return render_template('studii.html',studii=studii)

@app.route('/locatie')
def locatie():
  locatie=load_locatie()
  return render_template('locatie.html',locatie=locatie)

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
            """),
            {"nume": nume, "prenume": prenume, "specializare": specializare, "email": email, "telefon": telefon, "spital": spital}
        )
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
            text("""UPDATE Medici SET Nume=:nume, Prenume=:prenume, Specializare=:specializare, Email=:email, Telefon=:telefon, Spital=:spital WHERE Id_medic=:id"""),
            {"nume": nume, "prenume": prenume, "specializare": specializare, "email": email, "telefon": telefon, "spital": spital, "id": id}
        )
        conn.commit()
    return redirect(url_for('medici'))

@app.route('/medici/delete/<int:id>', methods=['POST'])
def delete_medic(id):
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Medici WHERE Id_medic=:id"""), {"id": id})
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
            """),
            {"nume_medicament": nume_medicament, "efecte_adverse": efecte_adverse, "doza": doza, "producator": producator}
        )
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
            """),
            {"nume_medicament": nume_medicament, "efecte_adverse": efecte_adverse, "doza": doza, "producator": producator, "id": id}
        )
        conn.commit()
    return redirect(url_for('medicamente'))

@app.route('/medicamente/delete/<int:id>', methods=['POST'])
def delete_medicament(id):
    with engine.connect() as conn:
        conn.execute(
            text("""DELETE FROM Medicamente WHERE Id_medicament=:id"""),
            {"id": id}
        )
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
            """),
            {"nume": nume, "prenume": prenume, "cnp": cnp, "data_nasterii": data_nasterii, "sex": sex, "adresa": adresa, "telefon": telefon, "id_medic": id_medic}
        )
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
            """),
            {"nume": nume, "prenume": prenume, "cnp": cnp, "data_nasterii": data_nasterii, "sex": sex, "adresa": adresa, "telefon": telefon, "id_medic": id_medic, "id": id}
        )
        conn.commit()
    return redirect(url_for('pacienti'))


@app.route('/pacienti/delete/<int:id>', methods=['POST'])
def delete_pacient(id):
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM Pacienti WHERE Id_pacient=:id"), {"id": id})
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
            """),
            {"nume_locatie": nume_locatie, "adresa": adresa, "oras": oras, "judet": judet, "cod_postal": cod_postal, "telefon_contact": telefon_contact, "email": email}
        )
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
            text("""UPDATE Locatie SET Nume_locatie=:nume_locatie, Adresa=:adresa, Oras=:oras, Judet=:judet, Cod_postal=:cod_postal, Telefon_contact=:telefon_contact, Email=:email WHERE Id_locatie=:id"""),
            {"nume_locatie": nume_locatie, "adresa": adresa, "oras": oras, "judet": judet, "cod_postal": cod_postal, "telefon_contact": telefon_contact, "email": email, "id": id}
        )
        conn.commit()
    return redirect(url_for('locatie'))

@app.route('/locatie/delete/<int:id>', methods=['POST'])
def delete_locatie(id):
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Locatie WHERE Id_locatie=:id"""), {"id": id})
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
            """),
            {"nume_studiu": nume_studiu, "data_incepere": data_incepere, "data_finalizare": data_finalizare, "stadiu": stadiu, "descriere": descriere, "id_medicament": id_medicament, "id_locatie": id_locatie}
        )
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
            text("""UPDATE Studii_Clinice SET Nume_studiu=:nume_studiu, Data_incepere=:data_incepere, Data_finalizare=:data_finalizare, Stadiu=:stadiu, Descriere=:descriere, Id_medicament=:id_medicament, Id_locatie=:id_locatie WHERE Id_studiu=:id"""),
            {"nume_studiu": nume_studiu, "data_incepere": data_incepere, "data_finalizare": data_finalizare, "stadiu": stadiu, "descriere": descriere, "id_medicament": id_medicament, "id_locatie": id_locatie, "id": id}
        )
        conn.commit()
    return redirect(url_for('studii'))


@app.route('/studii/delete/<int:id>', methods=['POST'])
def delete_studiu(id):
    with engine.connect() as conn:
        conn.execute(text("""DELETE FROM Studii_Clinice WHERE Id_studiu=:id"""), {"id": id})
        conn.commit()
    return redirect(url_for('studii'))

if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)