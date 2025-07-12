from simple_term_menu import TerminalMenu
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from os import system, name
from time import sleep

# Opções menh
opções = ['Classificado de peso', 'Loja Cat Pro - Tec', 'Créditos', 'Sair']

# OOpções pag
pagamentos = ['A vista dinheiro/cheque', 'A vista no cartão', 'A vista no cartão 2x', '3x ou mais no cartão']
cat = Console() # Rich libs

def title(title_name, color):
  print(f'[{color}]'+figlet_format(title_name, font="slant")) # Exibir título vermelho

def clear():
  system('cls' if name == 'nt' else 'clear')

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

def result(text):
  clear()
  processa(3, 'Calculando..', 'yellow', False)
  processa(1, 'Calculando', 'green', True)
  clear()
  title('Resultado', 'green')
  print(f'\nResultado ⪼ [green]{text}\n')
  input('Enter ⪼ Início ⪼⪼')
  main()

def imprimir_comprov(valor, tipo, parcS):
  if parcS == 1:
    clear()
    title('Cat Store', 'blue')
    parc = int(input('Quantas parcelas desejar pagar no cartão? [3/12] ⪼ '))
    
  if valor <= 2000:
    processa(3, 'Pagamento..', 'yellow', False)
    processa(1, 'Pagamento', 'green', True)
    clear()
    title('Cat Store', 'purple')
    if tipo == 1:
      # Dinheiro
      print(f'Comprovante ⬇︎\n\nRecebedo: Cat Store\nPagamento: Dinheiro ou Cheque\nGeral: {str(valor).replace(".", ",")}\nDesconto: {str(valor*10/100).replace(".", ",")}\nTotal: {str(valor-(valor*10/100)).replace(".", ",")}')
    elif tipo == 2:
      print(f'Comprovante ⬇︎\n\nRecebedo: Cat Store\nPagamento: Cartão a vista\nGeral: {str(valor).replace(".", ",")}\nDesconto: 0,00\nParcelas: 0x\nTotal: {str(valor).replace(".", ",")}')
      print()
    elif tipo == 3:
      # A vista no cartão 2x
      print(f'Comprovante ⬇︎\n\nRecebedo: Cat Store\nPagamento: Cartão parcelado 2x\nGeral: {str(valor).replace(".", ",")}\nDesconto: 0,00\nParcelas: 2x\nTotal: {str(valor/2).replace(".", ",")}')
      print()
    else:
      print(f'Comprovante ⬇︎\n\nRecebedo: Cat Store\nPagamento: Cartão parcelado {parc}x\nGeral: {str(valor).replace(".", ",")}\nDesconto: 0,00\nParcelas: {parc}x\nTotal: {str(valor/parc).replace(".", ",")}')
      print()
  else:
    # Dinheiro insuficiente! 
    processa(3, 'Pagamento..', 'yellow', False)
    clear()
    title('Cat Store', 'blue')
    print(Panel(Align.center("Sem saldo disponível!!"), title='Saldo inválido!', border_style='red'))

  input('\n\nEnter ⪼ Início ⪼⪼')
  main()

def main(): # Função start
  global opções, pagamentos# exporta valor
  clear() # Limpar terminal
  title('Cat Pro', 'red')
  # Exibir lista:
  match TerminalMenu(opções, menu_highlight_style=('fg_blue', 'bold')).show()+1:
    case 1:
      # Função peso
      clear()
      title('Cat Pro', 'red')
      peso = float(input('Seu peso [kg] ⪼ ').strip().replace(',', '.'))
      altura = float(input('Sua altura [m] ⪼ ').strip().replace(',', '.').lower().replace('m', ''))
      imc = peso / (altura * altura)
      if imc < 18.5:
        result(f'Seu imc e {imc:.2f}, e esta abaixo do peso!')
      elif imc >= 18.5 and imc <= 25:
        result(f'Seu imc e {imc:.2f}, e está no peso ideal!')
      elif imc >= 25 and imc <= 30:
        result(f'Seu imc e {imc:.2f}, e está sobrepeso')
      elif imc >= 30 and imc <= 40:
        result(f'Seu imc e {imc:.2f}, e está Obeso (a)')
      else:
        result(f'Seu imc e {imc:.2f}, e está em obesidade mórbida')
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

    case 3:
      # função crédito:
      processa(3, '******', 'yellow', False)
      processa(1, '******', 'green', True)
      clear()
      title('Créditos', 'green')
      print('\nCreditos ⪼ 『 Luks Code - Cat Pro』\nCriador ⪼ Lucas - 12/07/2025 - 8:50 AM')
      input('\nEnter ⪼ início ⪼⪼')
      main()
      # Término creditos
    
    case 4:
      processa(1, 'Close Cat Pro', 'green', True)
      exit()
main()