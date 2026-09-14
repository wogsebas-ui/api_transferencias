import sqlite3
conexion = sqlite3.connect("transferencias.db")
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS transferencias (
    cliente TEXT,
    vaolor REAL,
    fecha TEXT,
    hora TEXT,
    banco TEXT,
    id_pago TEXT PRIMARY KEY,
    estado TEXT
)
''')
conexion.commit()
conexion.close()

def guardar_transferencia(transferencia):
    conexion = sqlite3.connect("transferencias.db")
    cursor = conexion.cursor()
    cursor.execute(''' 
         INSERT INTO transferencias
         (cliente, valor, fecha, hora, banco, id_pago, estado)
         VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        transferencia.cliente,
        transferencia.valor,
        transferencia.fecha,
        transferencia.hora,
        transferencia.banco,
        transferencia.id_pago,
        transferencia.estado
     
    ))
    conexion.commit()
    conexion.close()
    
