import sqlite3

# Cria e conecta ao banco de dados
def create_connection():
    conn = sqlite3.connect('luna.db')
    return conn

# Cria a tabela de logs de conversas (se não existir)
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT NOT NULL,
            luna_response TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Loga a conversa no banco de dados
def log_conversation(user_input, luna_response):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO conversation_log (user_input, luna_response)
        VALUES (?, ?)
    ''', (user_input, luna_response))
    conn.commit()
    conn.close()

# Inicializa o banco de dados e cria a tabela
create_table()
