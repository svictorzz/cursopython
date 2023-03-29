nome = 'Victor Souza'
altura = 1.92
peso = 77
imc = peso / altura ** 2


print(nome, 'tem', altura, 'de altura, pesa', peso,'kg e seu IMC é', imc)

if(imc < 18.5):
    print('Abaixo da média.')
elif (imc > 18.5 and imc < 24.9):
    print('Voce ta normal.') 
elif (imc > 25 and imc < 29.9):
    print('Sobrepeso.')
elif (imc > 30 and imc < 39.9):
    print('OBESO.')            
else:
    print('Meus pêsames.')     