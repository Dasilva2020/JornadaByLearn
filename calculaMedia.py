n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))


def calcular_media(notas):
  quantidade = len(notas)
  soma = sum(notas)
  media = soma / quantidade
  print('O aluno tirou', media)
  verificar_aprovacao(media)

def verificar_aprovacao(media):
    print('Aluno Aprovado **PARABÉNS**' if media >=6 else 'Aluno Reprovado **ESTUDE MAIS**')

calcular_media([n1, n2, n3, n4])

