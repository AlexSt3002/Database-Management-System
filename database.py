from sqlalchemy import create_engine, text

  # Configurația pentru conexiune
conf = {
      'host': "mysql-37218507-proiect.h.aivencloud.com",
      'port': '16871',
      'user': "avnadmin",
      'password': "AVNS_G86nntv5hQTv7VIITFG",
      'database': "PROIECT"  # Specifică numele bazei de date
  }

  # Creează engine-ul pentru MySQL folosind pymysql
engine = create_engine(
      "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**conf)
  )

  # Execută interogarea și afișează rezultatele
with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM Medici"))
      rows = result.fetchall()  # preia toate rezultatele
      for row in rows:
          print(row)
