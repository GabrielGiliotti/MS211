print("Projeto 2: Aproximacao numerica para Solucao de EDOs\n")

print("Linguagem de Programacao Utilizada: Python3\n" +
	  "Motivacao: Desejamos resolver EDOs por metodos numericos de aproximacao\n")

print("Como exemplo de funcao, vamos tomar a equacao de Pierre-Francois Verhulst que modela um cenario em que a taxa de crescimento" +  
" populacional eh proporcional a populacao existente e a quantidade de recursos disponiveis no meio\n")
      

print("			y(t) =  r * y(t) * (1 - (y(t)/K) )  , sendo r a taxa de reproducao e K a constante de capacidade do meio\n\n")

print("###############################################################################################################################\n")
#Item a) a partir daqui
print("Vamos utilizar a solucao analitica do problema para fazer as comparacoes com a aplicacao dos metodos numericos, que eh dada por:\n\n")

print("  y(t) =  ( K * y0 * e^(r*t) )/( K + y0 * ( e^(r*t) - 1 ) ) \n\n")

print("Item a) Vamos aplicar o metodo de Euler para obter a solucao aproximada no intervalo [0,4] e comparar com a solucao analitica.")
print("Utilizando r = 0.5, K = 10, h = 0.05 e y0 = 1" )

print("Repare que, se o intervalo eh entre 0 e 4, queremos determinar y(4). Para a solucao analitica temos y(4) = 4.508530604")

# ini se refere ao inicio do intervalo e fim se refere ao final do intervalo
def metodoEuler(ini,fim,r,K,h,y0):
    t = ini   # t eh o valor de tempo onde vamos comecar no intervalo. y0 dado deve ser condizente com o valor de y(t0)  
    y_de_t = y0   # y_de_t eh o valor que y(t0) recebe, isso e, o valor y0 dado em nosso PVI --> y(t0) = y0
    it = 1    
    while(t <= fim): # enquanto nao chegarmos em y(t = fim)     
        y_n_mais_um = y_de_t + (h * (r * y_de_t * (1.0 - (y_de_t/K)))) # calculando y1, y2, ... , yn iteracoes     
        print("Valor na iteracao " + str(it) + " = " + str(y_n_mais_um) + " e Valor de t = " + str(t))
        it = it + 1 # incrementa para contagem de iteracoes
        t = t + h  # aumento do tempo de acordo com h dado
        y_de_t = y_n_mais_um # para calcular o y de n+1, temos que passar o valor para a proxima iteracao
             
    return y_n_mais_um

print("Para a solucao dada pelo algoritmo vamos apresentar todas a n iteracoes ate o valor limite do intervalo: \n")        

result = metodoEuler(0,4,0.5,10.0,0.05,1.0)

print("\nComparando o resultado dado pelo algoritmo: " + str(result) + " com o resultado dado analiticamente y(4) = 4.508530604")
print("Podemos verificar que o metodo de Euler se aproximou com precisao de apenas uma casa decimal em y(4)\n")

print("###############################################################################################################################\n")

print("Item b) Utilizando outros valores para os parametros inicialmente fornecidos, podemos verificar que:\n")
print("Na alteracao do parametro h, quanto MAIOR seu valor, menor sera a precisao da equacao logistica e quanto MENOR seu valor, maior sera")
print("a precisao da equacao logistica.\n")

#Descomente para analisar os resultados com diferente parametros de h
#print("h = 0.01")
#result = metodoEuler(0,4,0.5,10.0,0.01,1.0)
#print("\nh = 0.005")
#result = metodoEuler(0,4,0.5,10.0,0.005,1.0)
#print("\nh = 0.001")
#result = metodoEuler(0,4,0.5,10.0,0.001,1.0)

print("Ja para o parametro r, temos que se a taxa de reproducao for alta (r grande), a equacao logistica aponta um aumento brusco na")
print("populacao e logo em seguida um numero baixo, indicando que a populacao 'colapsou' devido aos poucos recursos (K).\n")

#result = metodoEuler(0,4,60,10.0,0.05,1.0)
#result = metodoEuler(0,4,0.00000005,10.0,0.05,1.0)

print("Ja para o parametro K, temos que se a capacidade do meio for alta (K grande), a equacao logistica aponta a possibilidade de")
print("desenvolvimento da populacao, chegando ate mesmo em um ponto onde a populacao se reproduz em seu maximo e ainda sobram recursos.")
print("Caso contrario, o meio limita o desenvolvimento de tal forma que nao importa a variacao do tempo, sempre havera um maximo que o")
print("ambiente suporta.\n")

#result = metodoEuler(0,4,0.5,1000,0.05,1.0)
#result = metodoEuler(0,4,0.5,0.75,0.05,1.0)

print("###############################################################################################################################\n")

print("item c)")









