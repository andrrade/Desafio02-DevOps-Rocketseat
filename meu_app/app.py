from flask import Flask
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=3306
        )
        cursor = db.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return f"✅ Conectado ao MySQL com sucesso! Hora atual: {result[0]}"
    except mysql.connector.Error as err:
        return f"❌ Erro na conexão: {err}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
