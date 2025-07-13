from simple_term_menu import TerminalMenu
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from os import system, name
from time import sleep
from random import choices

# ========================#
#  OPÇÕES MENU PRINCIPAL  #
#=========================#
opções = ['Classificado de peso', 'Loja Cat Pro - Tec', 'Game ⪼ Pedra papel tesoura', 'Créditos', 'Sair']

#===============================
# OPÇÕES PAGAMENTO - CAT STORE - SIMPLE-TERM-MENU
#=================================
pagamentos = ['A vista dinheiro/cheque', 'A vista no cartão', 'A vista no cartão 2x', '3x ou mais no cartão']
cat = Console() # Rich libs

#======================
# Função título grande
#=======================
def title(title_name, color):
  print(f'[{color}]'+figlet_format(title_name, font="slant")) # Exibir título vermelho

#===========================
#  Limpar terminal função  
#===========================
def clear():
  system('cls' if name == 'nt' else 'clear')

#==========================
# Função exibição processo 
#==========================
def processa(sleep_time, motivo, cor, estado):
  if estado:
    clear()
    title('Cat Pro', 'red')
    cat.print(Panel(Align.center(f'Finalizado com sucesso ⪼ {motivo}'), title=f'Sucesso', border_style=cor))
    sleep(sleep_time)
  else:
    i = 3
    while i >= 0:
      clear()
      title('Cat Pro', 'red')
      cat.print(Panel(Align.center(f'⊂⊃ ⪼ {motivo}'), title=f'Processando por {i}s', border_style=cor))
      sleep(1)
      i-=1

def imprimir_result_option_1(text):
  clear()
  processa(3, 'Calculando..', 'yellow', False)
  processa(1, 'Calculando', 'green', True)
  clear()
  title('Resultado', 'green')
  print(f'\nResultado ⪼ [green]{text}\n')
  input('Enter ⪼ Início ⪼⪼')


#================#
#  JOGO JOKENPÔ  #
#================#
#==============================
def jogar(nivel, jogador):
  # Tesoura: 1
  # Pedra: 2
  # Papel: 3
  if jogador == 1:
    matar = 2
  elif jogador == 2:
    matar = 3
  else:
    matar = 1

  if nivel == 1:
    # fácil
    maquina_jogadas = [1,1,2,2,3,3]
  elif nível == 2:
    maquina_jogadas = [1, 2, 3]
  else:
    maquina_jogadas = [1, 2, 3]
    for i in range(50000):
      maquina_jogadas.append(matar)
  
  máquina = choices(maquina_jogadas, k=1)[0] # Tesoura, papel, Pedra
  def animation_game(ti, co):
    for i in range(3):
       print(f'JOGADOR ⪼⪼⪼ {choices(["🗿", "📄", "✂"], k=1)[0]}')
       print(f'\nMÁQUINA ⪼⪼⪼ {choices(["🗿", "📄", "✂"], k=1)[0]}')
       sleep(0.3)
       clear()
       title(ti, co)
       
  clear()
  animation_game('JOOO', 'blue')
  animation_game('KENN', 'purple')
  animation_game('POOK', 'red')
  clear()
  title('JOKENPOK', 'blue')
  print(f'JOGADOR ⪼⪼⪼ {["Tesoura", "Pedra", "Papel"][jogador-1]}\nMÁQUINA ⪼⪼⪼ {["Tesoura", "Pedra", "Papel"][máquina-1]}\n')
  if máquina == jogador:
    print('Empate 😞')
  elif jogador == 1 and máquina == 2:
    print('MÁQUINA GANHOU!')
  elif jogador == 2 and máquina == 3:
    print('MÁQUINA GANHOU!')
  else:
    print('JOGADOR GANHOU!')
  input('Enter ⪼ início ⪼⪼')
#=========Jogo poken fim===========


#===================================
# FUNÇÃO DE IMPRIMIR COMPROVANTE & PROCESSO PAGAMENTO!
#===================================


#============= Cat Store ============#
#==============================#
#  FUNÇÃO CENTRAL DO CAT PRO!  #
#==============================#
def configura_comprov(tipo, valor, parc):
  
  tipo_pag = ['Dinheiro', 'A vista no cartão', 'A vista no cartão 2x', '3x ou mais no cartão'][tipo - 1]
  if tipo == 3:
    parc = 2
  desconto = str(valor * 0.10).replace('.', ',') if tipo == 1 else '0,00'
  total = (
      str(valor / parc).replace('.', ',') if tipo == 4 or tipo == 3
      else str(valor + valor * 0.10).replace('.', ',') if tipo == 1
      else str(valor).replace('.', ',')
  )

  return f'Comprovante ⬇︎\n\nRecebedo: Cat Store\nPagamento: {tipo_pag if parc == 0 else f"Cartão em {parc}"}\nGeral: {str(valor).replace(".", ",")}\nDesconto: {desconto}\nParcelas: {parc}\nTotal: {total}'

#=================#
# FUNÇÃO IMPRIMIR #
#=================#
def imprimir_comprov(valor, tipo, parcS):
  parc = 0
  if parcS == 1:
    clear()
    title('Cat Store', 'blue')
    parc = int(input('Quantas parcelas desejar pagar no cartão? [3/12] ⪼ '))
  if valor <= 2000:
    processa(3, 'Pagamento..', 'yellow', False)
    processa(1, 'Pagamento', 'green', True)
    clear()
    title('Cat Store', 'purple')
    print(configura_comprov(tipo, valor, parc)) 
  else:
    # Dinheiro insuficiente! 
    processa(3, 'Pagamento..', 'yellow', False)
    clear()
    title('Cat Store', 'blue')
    print(Panel(Align.center("Sem saldo disponível!!"), title='Saldo inválido!', border_style='red'))
  input('\n\nEnter ⪼ Início ⪼⪼')
#==========FIM CAT STORE===========#


#===========MENU CENTRAL===========#

main = True # Em quando for true continuar executado! 
while main: # Função start
  clear() # Limpar terminal
  title('Cat Pro', 'red')
  # Exibir lista:
  match TerminalMenu(opções, menu_highlight_style=('fg_blue', 'bold')).show()+1:
    #========================#
    #   FUNÇÕES DAS OPÇÕES   #
    #========================#
    
    # Imc, peso, classificado
    case 1:
      clear()
      title('Cat Pro', 'red')
      peso = float(input('Seu peso [kg] ⪼ ').strip().replace(',', '.'))
      altura = float(input('Sua altura [m] ⪼ ').strip().replace(',', '.').lower().replace('m', ''))
      imc = peso / (altura * altura)
      # FUNÇÃO OTIMIZADO ADPTADO!
      def definir_option_1(imc, catg):
        return f'Seu imc e {imc:.2f}, e está na categoria {catg}!'
        
      if imc < 18.5:
        imprimir_result_option_1(definir_option_1(imc, 'abaixo do peso'))
      elif imc >= 18.5 and imc <= 25:
        imprimir_result_option_1(definir_option_1(imc, 'peso ideal'))
      elif imc >= 25 and imc <= 30:
        imprimir_result_option_1(definir_option_1(imc, 'sobrepeso'))
      elif imc >= 30 and imc <= 40:
        imprimir_result_option_1(definir_option_1(imc, 'obeso'))
      else:
        imprimir_result_option_1(definir_option_1('obesidade mórbida'))
    # Terminando função peso
    case 2:
      # Função loja:
      clear()
      title('Cat Store', 'blue')
      print('\nSaldo disponível ⪼ R$2000')
      valor_reais = float(input('Qual valor da sua comprar? ⪼ R$').strip().replace(',', '.'))
      clear()
      title('Cat Store', 'blue')
      match TerminalMenu(pagamentos, menu_highlight_style=('fg_blue', 'bold'), title='Escolha sua forma de pagamento!\n[Dinheiro/Cheque] 10% promoção!\n').show():
        case 0:
          imprimir_comprov(valor_reais, 1, 0)
        case 1:
          imprimir_comprov(valor_reais, 2, 0)
        case 2:
          imprimir_comprov(valor_reais, 3, 0)
        case 3:
          imprimir_comprov(valor_reais, 4, 1)
    # Pedra papel tesoura
    case 3:
      clear()
      title('GAME', 'red')
      nível = TerminalMenu(['Modo fácil', 'Modo normal', 'Modo Hard'], title='ESCOLHA DIFICULDADE!\n', menu_highlight_style=('fg_red', 'bold')).show()
      objeto = TerminalMenu(['Pedra', 'Papel', 'Tesoura'], title='Escolha sua jogada!\n', menu_highlight_style=('fg_blue', 'bold')).show()
      jogar(nível+1, objeto+1) 
    # Término de pedra papel tesoura
    
    # Créditos
    case 4:
      processa(3, '******', 'yellow', False)
      processa(1, '******', 'green', True)
      clear()
      title('Créditos', 'green')
      print('\nCreditos ⪼ 『 Luks Code - Cat Pro』\nCriador ⪼ Lucas - 12/07/2025 - 8:50 AM')
      input('\nEnter ⪼ início ⪼⪼')
    # Término creditos
    
    # Sair
    case 5:
      processa(1, 'Close Cat Pro', 'green', True)
      exit()
    # Término sair

#===========MENU CENTRAL FIM===========#