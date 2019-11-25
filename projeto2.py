import matplotlib.pyplot as plt
import math as mt

print("Projeto 2: Aproximacao numerica para Solucao de EDOs\n")

print("Linguagem de Programacao Utilizada: Python3\n" +
	  "Motivacao: Desejamos resolver EDOs por metodos numericos de aproximacao\n")

print("Como exemplo de funcao, vamos tomar a equacao de Pierre-Francois Verhulst que modela um cenario em que a taxa de crescimento" +  
" populacional eh proporcional a populacao existente e a quantidade de recursos disponiveis no meio\n")
      

print("			y(t) =  r * y(t) * (1 - (y(t)/K) )  , sendo r a taxa de reproducao e K a constante de capacidade do meio\n\n")

print("##############################################################################################################################################################################\n")
#Item a) a partir daqui
print("Vamos utilizar a solucao analitica do problema para fazer as comparacoes com a aplicacao dos metodos numericos, que eh dada por:\n\n")

print("  y(t) =  ( K * y0 * e^(r*t) )/( K + y0 * ( e^(r*t) - 1 ) ) \n\n")

print("Item a) Vamos aplicar o metodo de Euler para obter a solucao aproximada no intervalo [0,4] e comparar com a solucao analitica.")
print("Utilizando r = 0.5, K = 10, h = 0.05 e y0 = 1" )

print("Repare que, se o intervalo eh entre 0 e 4, queremos determinar y(4). Para a solucao analitica temos y(4) = 4.508530604")

# ini se refere ao inicio do intervalo e fim se refere ao final do intervalo
def metodoEuler(ini,fim,r,K,h,y0): #para a equacao logistica dada
    t = ini   # t eh o valor de tempo onde vamos comecar no intervalo. y0 dado deve ser condizente com o valor de y(t0)  
    y_de_t = y0   # y_de_t eh o valor que y(t0) recebe, isso e, o valor y0 dado em nosso PVI --> y(t0) = y0
    it = 1    
    lista = []
    while(t < fim): # enquanto nao chegarmos em y(t = fim)     
        y_n_mais_um = y_de_t + (h * (r * y_de_t * (1.0 - (y_de_t/K)))) # calculando y1, y2, ... , yn iteracoes     
        print("Valor na iteracao " + str(it) + " = " + str(y_n_mais_um) + " e Valor de t = " + str(t))
        it = it + 1 # incrementa para contagem de iteracoes
        t = t + h  # aumento do tempo de acordo com h dado
        y_de_t = y_n_mais_um # para calcular o y de n+1, temos que passar o valor para a proxima iteracao
        #lista.append(y_n_mais_um)

    return y_n_mais_um
    #return lista

print("Para a solucao dada pelo algoritmo vamos apresentar todas a n iteracoes ate o valor limite do intervalo: \n")        

result = metodoEuler(0,4,0.5,10.0,0.05,1.0)

print("\nComparando o resultado dado pelo algoritmo: " + str(result) + " com o resultado dado analiticamente y(4) = 4.508530604")
print("Podemos verificar que o metodo de Euler se aproximou com precisao de apenas uma casa decimal em y(4)\n")

print("############################################################################################################################################################################\n")

print("Item b) Utilizando outros valores para os parametros inicialmente fornecidos, podemos verificar que:\n")
print("Na alteracao do parametro h, quanto MAIOR seu valor, menor sera a precisao da equacao logistica e quanto MENOR seu valor, maior sera")
print("a precisao da equacao logistica.\n")

#Descomente para analisar os resultados com diferente parametros de h
'''
print("h = 0.01")
result = metodoEuler(0,4,0.5,10.0,0.01,1.0)
print("Resultado = %.8f" % result)

print("\nh = 0.005")
result = metodoEuler(0,4,0.5,10.0,0.005,1.0)
print("Resultado = %.8f" % result)

print("\nh = 0.001")
result = metodoEuler(0,4,0.5,10.0,0.001,1.0)
print("Resultado = %.8f" % result)

print("\nh = 0.0005")
result = metodoEuler(0,4,0.5,10.0,0.0005,1.0)
print("Resultado = %.8f" % result)

print("\nh = 0.0001")
result = metodoEuler(0,4,0.5,10.0,0.0001,1.0)
print("Resultado = %.8f\n" % result)
'''

print("Ja para o parametro r, temos que se a taxa de reproducao for alta (r grande), a equacao logistica aponta um aumento brusco na")
print("populacao e logo em seguida um numero baixo, indicando que a populacao 'colapsou' devido aos poucos recursos (K).\n")


#Descomente o trecho de codigo para analise de valores diferentes para r
'''
print("r = 60")
result = metodoEuler(0,4,60.0,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 50")
result = metodoEuler(0,4,50.0,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 40")
result = metodoEuler(0,4,40.0,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 10")
result = metodoEuler(0,4,10.0,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 5")
result = metodoEuler(0,4,5.0,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 2")
result = metodoEuler(0,4,2.0,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 1")
result = metodoEuler(0,4,1,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 0.5")
result = metodoEuler(0,4,0.5,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 0.05")
result = metodoEuler(0,4,0.05,10.0,0.05,1.0)
print("Resultado = %.8f" % result)

print("\nr = 0.00000005")
result = metodoEuler(0,4,0.00000005,10.0,0.05,1.0)
print("Resultado = %.8f\n" % result)'''

print("Ja para o parametro K, temos que se a capacidade do meio for alta (K grande), a equacao logistica aponta a possibilidade de")
print("desenvolvimento da populacao, chegando ate mesmo em um ponto onde a populacao se reproduz em seu maximo e ainda sobram recursos.")
print("Caso contrario, o meio limita o desenvolvimento de tal forma que nao importa a variacao do tempo, sempre havera um maximo que o")
print("ambiente suporta.\n")

#Descomente o trecho de codigo para analise de valores diferentes para K
'''print("K = 10000000")
result = metodoEuler(0,4,0.5,10000000,0.05,1.0)
print("Resultado = %.8f\n" % result)

#variando o tempo para capacidade do meio alta
print("K = 10000000")
result = metodoEuler(0,3000,0.5,10000000,0.05,1.0)
print("Resultado = %.8f\n" % result)


print("K = 0.75")
result = metodoEuler(0,4,0.5,0.75,0.05,1.0)
print("Resultado = %.8f\n" % result)

#variando o tempo para Capacidade do meio pequena
print("K = 0.75")
result = metodoEuler(0,10,0.5,0.75,0.05,1.0)
print("Resultado = %.8f\n" % result)'''

print("############################################################################################################################################################################\n")

print("item c) Para o intervalo [0,4], com os dados do item a) temos uma aproximacao com certeza de 5 casas decimais, enquanto Euler obteve apenas uma casa decimal.")
print("Ja para o intervalo [0,10], temos uma aproximacao com ate 8 casas decimais, o que diz que o metodo eh bastante preciso em comparacao com Euler.\n")


def RungeKuttaOrdem4(ini, fim , r, K, h, y0): #para a equacao logistica dada
	tk = ini
	yk = y0
	it = 1
	lista = []
	while( tk < fim ):
		# k1 recebe os parametros tk e yk iniciais, ou seja, t0 = 0 e y(t0) = y0 = 1 
		
		k1 = h*(r * yk *(1.0 - (yk/K)))   
        # tkparak2 e ykparak2 sao os parametros que devemos passar para k2, que utilizam tk inicial, h, yk inicial e k1
		tkparak2 = tk + (h/2.0)
		ykparak2 = yk + (k1/2.0)
		k2 = h*(r * ykparak2 * (1.0 - (ykparak2/K)))
		
        # tkparak3 e ykparak3 sao os parametros que devemos passar para k3, que utilizam tk inicial, h, yk inicial e k2
		tkparak3 = tk + (h/2.0)
		ykparak3 = yk + (k2/2.0)
		k3 = h*(r * ykparak3 * (1.0 - (ykparak3/K)))
		
        # tkparak4 e ykparak4 sao os parametros que devemos passar para k4, que utilizam tk inicial, h, yk inicial e k3
		tkparak4 = tk + h
		ykparak4 = yk + k3
		k4 = h*(r * ykparak4 * (1.0 - (ykparak4/K)))
		 	
		yk_mais_um = yk + ((1.0/6.0)*(k1+(2.0*k2)+(2.0*k3)+k4))
		tk = tk + h
		yk = yk_mais_um
		print("Valor na iteracao " + str(it) + " = " + str(yk_mais_um) + " e Valor de t = " + str(tk) + "\n")
		it = it + 1
 
		lista.append(yk_mais_um)

	return lista
	


# Teste com dados iniciais
#RungeKuttaOrdem4(0,4,0.5,10.0,0.05,1)
# Teste com intervalo [0,10]
#listaResult = RungeKuttaOrdem4(0,10,0.5,10.0,0.05,1)

print("#################################################################################################################################################################\n")
 
print("item d) Analisando os dados (descomente as chamadas do algoritmo no script), temos que Runge Kutta, pela sua precisao, eh mais condizente com a solucao analitica que o metodo de Euler.")
print("Relatorio ira melhor apresentar as explicacoes.\n") 

print("PARA CONSEGUIR TESTAR OS RESULTADOS OBTIDOS NESSE ARQUIVO, VOCE DEVERA ANALISAR O CODIGO E ENCONTRAR ONDE COMENTAR E DESCOMENTAR\n")

#print("#################################################################################################################################################################\n")

#print("Secao para plot de graficos: ignore a partir daqui")

#listax = []
#listay = []

#for i in range(0,401,5):
#	listax.append(float(i/100.0))

#print(listax)
#listay = metodoEuler(0,4,0.5,10.0,0.05,1)
#listay = RungeKuttaOrdem4(0,4,0.5,10.0,0.05,1)

#plt.plot(listax,listay) # A biblioteca plot estou usando para gerar o grafico, apesar de nao o ter usado no relatorio
#plt.plot([0,1,2,3,4],[1.00000,1.54828099,2.319693167,3.324278617,4.508530604]) 
#plt.title('Grafico Analitico x Metodo Runge Kutta Ordem 4') # Define um titulo para o grafico
#plt.xlabel('Eixo t') # Define um rotulo para o eixo x
#plt.ylabel('Eixo y(t)') # Idem para o eixo y
#plt.show() # Faz o plot do Grafico com as devidas definicoes