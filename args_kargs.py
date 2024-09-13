def exibir_poema(data_extenso,*args,**kwargs):
    texto = '\n'.join(args)
    meta_dados='\n'.join( [f'{chave.title()} : {valor}' for chave, valor in kwargs.items()] )
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('10 de setembro de 2024', 
            'poema1',
            'poema2',
            'poema3',
            'poema4',
            'poema5',
            'poema6',
            'poema7',
            autor='Enc Asc',ano=2024)


