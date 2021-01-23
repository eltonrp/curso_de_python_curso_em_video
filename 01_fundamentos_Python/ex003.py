nome = input('Qual é o seu nome? ').capitalize()
idade = input('Qual é a sua idade? ')
local = input('Onde vc nasceu? ').capitalize()
print('Ok, vc é de(a) {}, tem {} anos e seu nome é {}.'
      ' Seja Bem vindo, {}!'.format(local, idade, nome, nome))
print(nome.isalpha())
