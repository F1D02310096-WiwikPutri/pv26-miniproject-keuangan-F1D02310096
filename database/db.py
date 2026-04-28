import sqlite3

def koneksi():
    return sqlite3.connect("keuangan.db")

def buat_tabel():
    conn = koneksi()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal TEXT,
        kategori TEXT,
        jenis TEXT,
        nominal INTEGER,
        catatan TEXT
    )
    """)
    conn.commit()
    conn.close()

def tambah_data(data):
    conn = koneksi()
    c = conn.cursor()
    c.execute("""
    INSERT INTO transaksi (tanggal, kategori, jenis, nominal, catatan)
    VALUES (?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

def ambil_data():
    conn = koneksi()
    c = conn.cursor()
    c.execute("SELECT * FROM transaksi")
    data = c.fetchall()
    conn.close()
    return data

def hapus_data(id):
    conn = koneksi()
    c = conn.cursor()
    c.execute("DELETE FROM transaksi WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
def update_data(id, data):
    conn = koneksi()
    c = conn.cursor()
    c.execute("""
    UPDATE transaksi 
    SET tanggal=?, kategori=?, jenis=?, nominal=?, catatan=?
    WHERE id=?
    """, (*data, id))
    conn.commit()
    conn.close()