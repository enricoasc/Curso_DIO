nome = 'Enrico'
idade = 28
profissao = 'Programador'
linguagem = 'Python'

## style string
print('''Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s 
         e estou matriculado no curso de %s.'''%(nome,idade,profissao,linguagem))

# #  %d interios
# #  %s string 

## metodo format
print('''Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} 
         e estou matriculado no curso de {}.'''.format(nome,idade,profissao,linguagem))

print('''Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} 
         e estou matriculado no curso de {0}.'''.format(linguagem,profissao,idade,nome))

print('''Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} 
         e estou matriculado no curso de {linguagem}.'''.format(linguagem=linguagem,profissao=profissao,idade=idade,nome=nome))

# USANDO UMA BIBLIOTECA PARA TROCAR O FORMAT 
pessoa = {'snome':nome, 'sidade':idade, 'sprofissao':profissao, 'slinguagem':linguagem}

print('''Olá, me chamo {snome}. Eu tenho {sidade} anos de idade, trabalho como {sprofissao} 
           e estou matriculado no curso de {slinguagem}.'''.format(**pessoa))

print(f''' Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} 
         e estou matriculado no curso de {linguagem}.''')  


PI = 3.14159
print(f'Valor de PI:{PI:0.2f}')
print(f'Valor de PI:{PI:10.2f}')
