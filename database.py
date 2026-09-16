import sqlite3
conexion = sqlite3.connect("transferencias.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transferencias (
    cliente TEXT,
    valor REAL,
    fecha TEXT,
    hora TEXT,
    banco TEXT,
    id_pago TEXT PRIMARY KEY,
    estado TEXT
)
""")
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

def obtener_transferencias():
    conexion = sqlite3.connect("transferencias.db")
    cursor = conexion.cursor()
    cursor.execute("""  
        SELECT cliente, valor, fecha, hora, banco, id_pago, estado
        FROM transferencias
      """)
    registros = cursor.fetchall()
    conexion.close()
    transferencias = []

    for registro in registros:
        transferencias.append({
            "cliente": registro[0],
            "valor": registro[1],
            "fecha": registro[2],
            "hora": registro[3],
            "banco": registro[4],
            "id_pago": registro[5],
            "estado": registro[6]
        })
    return transferencias
def obtener_transferencia(id_pago):
    conexion = sqlite3.connect("transferencias.db")
    cursor = conexion.cursor()
    cursor.execute("""  
        SELECT cliente, valor, fecha, hora, banco, id_pago, estado
        FROM transferencias
        WHERE id_pago = ?
      """, (id_pago,))

    registro = cursor.fetchone()
    conexion.close()
    if registro is None:
        return None
    return {
        "cliente": registro[0],
        "valor": registro[1],
        "fecha": registro[2],
        "hora": registro[3],
        "banco": registro[4],
        "id_pago": registro[5],
        "estado": registro[6]

    }

def actualizar_transferencia(id_pago, transferencia):
    conexion = sqlite3.connect("transferencias.db")
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE transferencias
        SET cliente = ?, valor = ?, fecha = ?, hora = ?, banco = ?, estado = ?
        WHERE id_pago = ?
    """, (
        transferencia.cliente,
        transferencia.valor,
        transferencia.fecha,
        transferencia.hora,
        transferencia.banco,
        transferencia.estado,
        id_pago
    ))

    conexion.commit()
    filas_actualizadas = cursor.rowcount
    conexion.close()

    return filas_actualizadas
