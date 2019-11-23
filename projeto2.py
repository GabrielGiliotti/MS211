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
print("Utilizando r = 0.5, K = 10, h = 0,05 e y0 = 1" )

def metodoEuler (r,K,h,y0):
    print("Escrever algoritmo de Euler aqui")
    print(r,K,y0,h)



metodoEuler(0.5,10,0.05,1)




