#adivinhe o número
import os

os.system('clear')

print("Pense em um número de 1 a 10...")
input("Quando estiver pronto, aperte Enter.")

os.system('clear')
print("Estou lendo sua mente...")
input()

print("Seu número é... 7!")
input("Acertei? 😄")

#pense em uma cor
import os

os.system('clear')

print("Escolha uma cor na sua mente:")
print("🔴 Vermelho")
print("🔵 Azul")
print("🟢 Verde")
print("🟡 Amarelo")
input("Aperte Enter quando tiver escolhido...")

os.system('clear')
print("Concentre-se...")
input()

print("Você pensou na cor... 🔵 Azul!")
input("Acertei, né?")

#Criando uma história maluca
print("Vamos criar uma história maluca!")

lugar = input("Digite um lugar: ")
famoso = input("Digite o nome de uma pessoa famosa: ")
objeto = input("Digite um objeto: ")
cor = input("Digite uma cor: ")
verbo = input("Digite um verbo: ")
numero = input("Digite um número: ")

print()
print("Um dia, no(a)", lugar + ", encontrei o(a)", famoso, "segurando um", objeto, cor + ".")
print("Ele(a) começou a", verbo, "sem parar, e isso durou por", numero, "horas!")

#Meu crachá de programador(a)
print("Vamos montar seu crachá de programador!")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
linguagem = input("Digite sua linguagem favorita: ")
emoji = input("Digite um emoji que te representa: ")

print()
print("--------------------------")
print("👩‍💻 Crachá do Dev")
print("Nome:", nome)
print("Idade:", idade)
print("Linguagem favorita:", linguagem)
print("Emoji:", emoji)
print("--------------------------")

#Oráculo da sabedoria Python
print('Sou o Oráculo da Sabedoria Python. Faça sua pergunta...')

pergunta = input('Você quer saber sobre (funções, loops, variáveis, listas)? ')

match pergunta:
    case 'funções' | 'funcoes' | 'funcao':
        print('Funções são blocos de código que você pode reutilizar! def nome():')
    case 'loops':
        print('Loops permitem repetir ações. Use for ou while!')
    case 'variáveis':
        print('Variáveis guardam valores. Exemplo: idade = 18')
    case 'listas':
        print('Listas guardam vários valores. Ex: frutas = ["maçã", "banana"]')
    case _:
        print('Essa resposta está além do meu conhecimento atual.')


#Quiz de perguntas e respostas
perguntas = [
    ["Quanto é 2 + 2?", "4"],
    ["Qual linguagem estamos aprendendo?", "python"],
    ["Qual animal é famoso por rir? (dica: aparece no Rei Leão)", "hiena"],
    ["Qual fruta rima com limão e é amarela?", "mamão"],
    ["Qual o nome do robô do Star Wars que parece um latão?", "r2d2"]
]

acertos = 0

for pergunta in perguntas:
    resposta = input(pergunta[0] + " ")
    if resposta.lower() == pergunta[1]:
        acertos += 1

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")

#Número secreto
numero_secreto = 7
tentativas = 0

while True:
    chute = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente!")

#Caça ao tesouro espacial
# Tabuleiro 3x3 vazio
tabuleiro = [
    [' ', ' ', ' '],  # linha 0
    [' ', ' ', ' '],  # linha 1
    [' ', ' ', ' ']   # linha 2
]

# Posição fixa do tesouro (linha 1, coluna 2)
linha_tesouro = 1
coluna_tesouro = 2

# Função para exibir o tabuleiro
def exibe_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

tentativas = 5

print("🚀 Caça ao Tesouro Espacial")
print("Encontre o 💎 escondido no tabuleiro 3x3.")
print("Use números de 0 a 2 para linha e coluna.")
print("Exemplo: linha 1, coluna 2")

for i in range(tentativas):
    print(f"\nTentativa {i+1} de {tentativas}")
    
    linha = int(input("Digite a linha (0 a 2): "))
    coluna = int(input("Digite a coluna (0 a 2): "))

    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("❌ Posição inválida! Tente valores entre 0 e 2.")
        continue

    if linha == linha_tesouro and coluna == coluna_tesouro:
        tabuleiro[linha][coluna] = '💎'
        print("\n🎉 Parabéns! Você encontrou o tesouro!")
        exibe_tabuleiro()
        break
    else:
        if tabuleiro[linha][coluna] != ' ':
            print("⚠️ Você já tentou aqui!")
        else:
            tabuleiro[linha][coluna] = 'X'
            print("Nada aqui... continue tentando!")
        exibe_tabuleiro()

else:
    print("\n⛔ Suas tentativas acabaram!")
    tabuleiro[linha_tesouro][coluna_tesouro] = '💎'
    print("O tesouro estava aqui:")
    exibe_tabuleiro()