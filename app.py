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


if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)