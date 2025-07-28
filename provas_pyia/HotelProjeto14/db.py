import mysql.connector
import pymysql


conexao = pymysql.connect(
    host="localhost",
    user="admin",
    password="admin1234",
    database="hotel",
    cursorclass=pymysql.cursors.DictCursor
)



def obter_clientes():
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

def adicionar_cliente(nome, telefone, email):
    cursor = conexao.cursor()
    sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()
    cursor.close()


def deletar_cliente(id):
    with conexao.cursor() as cursor:
        cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id,))
        conexao.commit()

def obter_quartos():
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM quartos")
        return cursor.fetchall()

def adicionar_quarto(numero, tipo, preco):
    with conexao.cursor() as cursor:
        cursor.execute("INSERT INTO quartos (numero, tipo, preco_diaria) VALUES (%s, %s, %s)", (numero, tipo, preco))
        conexao.commit()

def deletar_quarto(numero):
    with conexao.cursor() as cursor:
        cursor.execute("DELETE FROM quartos WHERE numero=%s", (numero,))
        conexao.commit()

def obter_reservas():
    with conexao.cursor() as cursor:
        cursor.execute("""
            SELECT r.id, c.nome AS nome_cliente, q.numero AS numero_quarto, q.tipo, r.checkin, r.checkout
            FROM reservas r
            JOIN clientes c ON r.id_cliente = c.id_cliente
            JOIN quartos q ON r.numero_quarto = q.numero
            WHERE r.ativa = TRUE
        """)
        return cursor.fetchall()

def criar_reserva(id_cliente, numero_quarto, checkin, checkout):
    with conexao.cursor() as cursor:
        cursor.execute("INSERT INTO reservas (id_cliente, numero_quarto, checkin, checkout) VALUES (%s, %s, %s, %s)", (id_cliente, numero_quarto, checkin, checkout))
        cursor.execute("UPDATE quartos SET disponivel=FALSE WHERE numero=%s", (numero_quarto,))
        conexao.commit()

def cancelar_reserva(id_reserva):
    with conexao.cursor() as cursor:
        cursor.execute("SELECT numero_quarto FROM reservas WHERE id=%s", (id_reserva,))
        quarto = cursor.fetchone()
        if quarto:
            cursor.execute("UPDATE quartos SET disponivel=TRUE WHERE numero=%s", (quarto['numero_quarto'],))
        cursor.execute("UPDATE reservas SET ativa=FALSE WHERE id=%s", (id_reserva,))
        conexao.commit()
