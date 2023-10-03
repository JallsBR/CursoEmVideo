#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = ('Arroz 5kg', 9.75, 'Feijão', 5.20 ,'Óleo de soja', 2.80, 'Sal', 1.25, 'Açúcar', 1.13, 'Café', 60.0, 'Molho de tomate', 2.18, 'Macarrão', 4.70, 'Milho', 1.20)
pos=0
print(f'{"Lista de compras":-^40}')
for item in itens[::2]:
    pos+=1
    print(f'{item:.<15}................. R$ {itens[pos]:>5.2f}')
    pos += 1
print('-'* 40)