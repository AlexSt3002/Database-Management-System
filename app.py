from flask import Flask, render_template
from database import engine
from sqlalchemy import text
app=Flask(__name__)
def load_medici():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Medici"))
    result_all=[]
    rows = result.fetchall()  # preia toate rezultatele
    for row in rows:
      result_all.append(row)
    return result_all
      
@app.route('/')
def hello_world():
  medici=load_medici()
  return render_template('home.html',medici=medici)


if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)