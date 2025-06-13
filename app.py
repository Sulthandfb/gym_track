# app.py (Flask API)
from flask import Flask, jsonify, request
from db_config import get_db_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Agar bisa menerima request dari origin berbeda (React app)

@app.route('/members', methods=['GET'])
def get_members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM member;')
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    members = [dict(zip(columns, row)) for row in data]
    cursor.close()
    conn.close()
    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()  # Mendapatkan data JSON dari request
    
    # Mengambil data yang sesuai dengan struktur Anda
    nama_lengkap = data.get('nama_lengkap')
    email = data.get('email')
    
    # Validasi data
    if not nama_lengkap or not email:
        return jsonify({"error": "Nama lengkap dan email diperlukan"}), 400

    # Koneksi ke database dan menyimpan data
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO member (nama_lengkap, email) 
        VALUES (%s, %s)
    """, (nama_lengkap, email))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Member added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
