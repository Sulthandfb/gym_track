import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="gymtrack",
            user="sulthan",
            password="raihan2004"
        )
        return conn
    except psycopg2.Error as e:
        print("Gagal terkoneksi ke database:", e)
        return None
