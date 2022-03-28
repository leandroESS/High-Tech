# Fazer um programa que imprima a tabuada do 0 até o 10
# no (Console)
# 1-) Entender o problema
# Gerar as tabuadas do 0 até o 10 no console
# 2-) Planejar a solução (Console)
# Criar um sistema que tenha os seguinte:
# -Um login/boas vindas
# -Menu
#   -Multiplicar
#   -Sair
# 3-) Dividir/Planejar Tarefas
# -Criação tela login
# -Criação Menu principal
# -Criação funcionalidade Sair
# -Criação Tela "Multiplicar"
#   -Preparar loops
# 4-) Estimar tempo de desenvolvimento (Até a metade da aula)

def opcao1():
     print("Iniciando a multiplicação")
     # 4 x 4 = 16
     for i in range(11):
        for j in range(11):
            print(f"{i} x {j} = {i*j}")
        print("\n")
     print("Sucesso!")

def opcao2():
    print("Saindo do sistema...")
    exit()



usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")
lista = []
while True:
    print("Selecione uma opção:")
    print("1 - Multiplicar")
    print("2 - Sair")
    opcao = int(input(""))
    if opcao in [1,2]:
      if opcao == 1: #Multiplicar
          opcao1()
      elif opcao == 2:#Sair
          opcao2()
            
    else:
        print("Opção Inválida!")
