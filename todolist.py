import sqlite3


conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    concluida BOOLEAN NOT NULL DEFAULT 0
)
''')
conn.commit()

# Funções principais
def adicionar_tarefa(titulo):
    cursor.execute('INSERT INTO tarefas (titulo) VALUES (?)', (titulo,))
    conn.commit()

def listar_tarefas():
    cursor.execute('SELECT id, titulo, concluida FROM tarefas')
    tarefas = cursor.fetchall()
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    for id, titulo, concluida in tarefas:
        status = "✅" if concluida else "❌"
        print(f"[{id}] {titulo} - {status}")

def concluir_tarefa(id):
    cursor.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (id,))
    conn.commit()

def excluir_tarefa(id):
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()


def menu():
    while True:
        print("\n=== To-Do List ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ")
            adicionar_tarefa(titulo)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            id = int(input("Digite o ID da tarefa a concluir: "))
            concluir_tarefa(id)
        elif opcao == "4":
            id = int(input("Digite o ID da tarefa a excluir: "))
            excluir_tarefa(id)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    menu()
