# ============================================
# TRABALHO AV1 - ENGENHARIA DE SOFTWARE
# Aluno: Levi Neves
# Aplicação: Gerenciador de Tarefas (Com Status)
# ============================================

def menu():
    print("\n--- GERENCIADOR DE TAREFAS (V2.0) ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir/Remover tarefa")
    print("4 - Sair")

def main():
    tarefas = []
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nova_tarefa = input("Digite a descrição da tarefa: ")
            tarefas.append({"texto": nova_tarefa, "concluida": False})
            print("-> Tarefa adicionada com sucesso!")
            
        elif opcao == "2":
            print("\n--- SUAS TAREFAS ---")
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, t in enumerate(tarefas, 1):
                    status = "[X]" if t["concluida"] else "[ ]"
                    print(f"{i}. {status} {t['texto']}")
                    
        elif opcao == "3":
            if not tarefas:
                print("Nenhuma tarefa para concluir.")
            else:
                print("\n--- CONCLUIR TAREFA ---")
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t['texto']}")
                
                num = int(input("Digite o número da tarefa concluída: ")) - 1
                if 0 <= num < len(tarefas):
                    tarefas[num]["concluida"] = True
                    print("-> Tarefa marcada como concluída!")
                else:
                    print("Número de tarefa inválido.")
                    
        elif opcao == "4":
            print("Encerrando o programa. Bons estudos!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()