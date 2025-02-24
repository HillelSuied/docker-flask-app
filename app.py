import os
import mysql.connector
import socket
from flask import Flask, jsonify, request

app = Flask(__name__)

# הגדרת החיבור ל-MySQL
db_config = {
    "host": os.getenv("DATABASE_HOST", "localhost"),
    "user": os.getenv("DATABASE_USER", "root"),
    "password": os.getenv("DATABASE_PASSWORD", "rootpassword"),
    "database": os.getenv("DATABASE_NAME", "flaskdb"),
}

def get_db_connection():
    """יוצר חיבור למסד הנתונים ומטפל בשגיאות"""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"⚠️ Error connecting to MySQL: {err}")
        return None

# פונקציה שמייצרת את הטבלה אם היא לא קיימת
def create_table():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS access_log (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ip_address VARCHAR(50),
                    access_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            cursor.close()
            print("✅ Table 'access_log' is ready!")
        except mysql.connector.Error as e:
            print(f"⚠️ Error creating table: {e}")
        finally:
            conn.close()

# הפונקציה הזו תופעל תמיד כשהשרת עולה
create_table()

@app.route('/')
def home():
    """נתיב ראשי - רושם ביקור ומחזיר את ה-IP של השרת Flask"""
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        ip = request.remote_addr
        cursor.execute("INSERT INTO access_log (ip_address) VALUES (%s)", (ip,))
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM access_log")
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        # מחזיר את כתובת ה-IP של השרת Flask המטפל בבקשה
        return jsonify({
            "server_ip": socket.gethostbyname(socket.gethostname()),
            "message": "Visit logged",
            "total_visits": count
        })
    except mysql.connector.Error as e:
        return jsonify({"error": f"MySQL Error: {e}"}), 500

@app.route('/showcount')
def show_count():
    """נתיב שמחזיר את מספר הביקורים (לא מוסיף ביקור נוסף)"""
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM access_log")
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return jsonify({"total_visits": count})
    except mysql.connector.Error as e:
        return jsonify({"error": f"MySQL Error: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)