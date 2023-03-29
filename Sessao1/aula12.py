nome = 'Victor Souza'
altura = 1.92
peso = 77
imc = peso / altura ** 2


print(nome, 'tem', altura, 'de altura, pesa', peso,'kg e seu IMC é', imc)

if(imc < 18.5):
    print('BOA MAGRELO FDP.')
elif (imc > 18.5 and imc < 24.9):
    print('Voce ta normal.') 
elif (imc > 25 and imc < 29.9):
    print('PARA DE ENCHER O BUCHO, TA COM SOBREPESO FDP.')
elif (imc > 30 and imc < 39.9):
    print('OBESO ARROMBADO FDP.')            
else:
    print('JA PODE SEPARAR O CAIXÃO THAIS CARLA DO KRL.')     