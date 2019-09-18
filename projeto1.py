import matplotlib.pyplot as plt
import math as mt

print("\nProjeto 1 - MS211 - Professor Florindo\n\n" +
	"Linguagem de Programacao Utilizada: Python3\n" +
	"Motivacao: Desejamos realizar a aproximacao e/ou encontrar raizes de funcoes atraves de metodos numericos de aproximação.\n")

print("Como exemplo de funcao, vamos tomar a equacao de Butler-Volmer em processos eletroquimicos que relaciona a\n" +
      "densidade de corrente com o potencial em um eletrodo e pode ser escrita como:\n\n")

print("			f(x) =  e^(alpha*x) - e^((alpha-1)*x) - beta 		, sendo alpha = 0.2 e beta = 2.0 \n\n")

print("###############################################################################################################################\n")
#Item a) a partir daqui
print("Item a) Encontrando um intervalo que contenha uma raiz de f(x)\n", end="")
print("Inicialmente vamos tomar arbitrariamente a funcao no intervalo x1, x2 e analisar seu grafico visualmente")
print("(Obs:Apos o plot do grafico esta indicado se o intervalo apresenta raiz ou nao, segundo os criterios do teorema que vem a seguir)")
print("Digite os valores do intervalo no eixo x [x1,x2] em que voce deseja encontrar uma raiz:\n")
x1 = float(input("Valor de x1: "))
x2 = float(input("Valor de x2: "))
print()
print("Para analisar se o intervalo [x1,x2] contem pelo menos uma raiz da funcao, fazemos uso do seguinte teorema:\n")
print("Seja f(x) uma função contínua no intervalo [x1,x2].", end="")
print("Se f(x1)*f(x2) < 0 (ou seja, f(x1) e f(x2) tem sinais contrários), então existe pelo menos uma raiz real de f no intervalo[x1,x2]\n")

flag = 0
a = 0.2 # considere que a eh alpha 
b = 2.0 # considere que b eh beta
f1 = mt.exp(x1*a) - mt.exp((a-1)*x1) - b
f2 = mt.exp(x2*a) - mt.exp((a-1)*x2) - b
if( f1*f2 < 0 ): 
	print("O Intervalo escolhido apresenta pelo menos uma raiz segundo o teorema.\n")
	flag = 1
else:
	print("O Intervalo escolhido nao atende ao(s) criterio(s) do teorema.\n")
	flag = 2

listax = [] # Eixo x: Lista utilizada como parametro para printar grafico no pyplot
listaf = [] # Eixo y (ou f(x) se preferir): Idem
for i in range(int(x1),int(x2)+1):
	f = mt.exp(i*a) - mt.exp((a-1)*i) - b
	listaf.append(f)	
	listax.append(i)

plt.plot(listax,listaf)
plt.title('Grafico do Intervalo escolhido')
plt.xlabel('Eixo x [x1,x2]')
plt.ylabel('Eixo y [f(x1), f(x2)]')
plt.show()

print("###############################################################################################################################\n")
# Item b) a partir daqui.
print("Item b) Implementacao dos metodos numericos Bisseccao e Newton\n")
print("A funcao f(x) e o intervalo ja temos do item anterior.")
print("Insira entao a tolerancia desejada e um numero maximo de iteracoes que o algoritmo pode realizar:\n")

tol = float(input("Valor da tolerancia: "))
imaxi = 0
print()

print("Vamos estimar tambem, o numero de iteracoes necessarias para aproximar a raiz pensando no proprio metodo da Bisseccao.")
print("Sabemos que o intervalo em cada iteracao k tera metade da amplitude do intervalo de iteracao k-1.\n")
print("Temos entao x2k - x1k/2 , isto eh, valor de x2 na iteracao k menos valor de x1 na iteracao k , tudo dividido por 2, eh dado por:")
print("(x20 - x10)/2^k (x2 na iteracao 0 menos x1 na itercacao 0 , tudo dividido por 2 elevado a k)")
print("Finalmente, tal equacao deve ser menor que a tolerancia desejada.")
print("Aplicando a operacao logaritmo neperiano em ambos os lados da inequacao, conseguimos isolar k, que eh o numero de iteracoes.")
print("Finalmente o numero de iteracoes estimado eh dado por:\n")
print("k > (ln(x20 - x10) - ln(tolerancia))/ ln(2)\n")

def numIterac(x1,x2,tol):	
	k = (mt.log(mt.exp(x2-x1)) - mt.log(mt.exp(tol)))/mt.log(mt.exp(2))
	k = int(k)+1
	return k

# define uma funcao para que possa ser chamada posteriormente (item c))
def bisseccao(z1,z2,tole,imax):		
	funz1 = (mt.exp(z1*a) - mt.exp((a-1)*z1) - b) #funcao funz1 = f(z1)
	funz2 = (mt.exp(z2*a) - mt.exp((a-1)*z2) - b) #funcao funz1 = f(z1)
	if(funz1*funz2 < 0): 
		i = 1
		pmedio = (z1 + z2)/2 # define o ponto medio para o metodo
		while( i <= imax ):		
			funpmedio = (mt.exp(pmedio*a) - mt.exp((a-1)*pmedio) - b) #funcao func = f(pmedio)
			if( funpmedio == 0 or (z2-z1)/2 < tole ):			
				return pmedio
					
			if( funz1*funpmedio < 0 ):
				z2 = pmedio
			else:
				z1 = pmedio
			pmedio = (z1+z2)/2
			i += 1
		return pmedio
	else:
		print("Nao ha raizes no intervalo ")	
		#return None

print("METODO DA BISSECCAO")
imaxi = numIterac(x1,x2,tol)		
result = bisseccao(x1,x2,tol,imaxi)
print("Raiz encontrada = " + str(result))
print()	


#Metodo de Newton

def newton(x0, tole, imax):
	funcX = (mt.exp(x0*a) - mt.exp((a-1)*x0) - b) #funcao 
	funcXDer = ((a*mt.exp(a*x0)) + ((0.8)*mt.exp((a-1)*x0))) #derivada da funcao

	x1 = (x0 - (funcX/funcXDer))  #g(x) ou x1

	i = 0
	while(i < imax): 
		if(abs((mt.exp(x0*a) - mt.exp((a-1)*x0) - b)) < tole): #criterio de parada
			return (x0, i)	
		elif(abs(x1 - x0) > tole): #criterio de parada
			x0 = x1
			x1 = (x0 - (mt.exp(x0*a) - mt.exp((a-1)*x0) - b)/((a*mt.exp(a*x0)) - ((a-1)*mt.exp((a-1)*x0))))
			i += 1
		else:
			return None, None
	return (x1, i)

print("METODO DE NEWTON-RAPHSON\n")
print("Digite o valor de aproximacao inicial x0 para encontrar ou nao uma raiz da funcao:\n")
x0 = float(input("Valor de x0: "))
result, nInt = newton(x0,tol,imaxi)
print("Raiz encontrada = " + str(result))
print()


print("###############################################################################################################################\n")
print("Item c) Encontrar raiz da equacao dada para diferentes pontos/intervalos iniciais e tabelar: ")
print("Os intervalos passados [n1,n2], as aproximacoes das raizes e o numero de iteracoes.\n")

print("Obs: Para todas as entradas que serao tabeladas, vamos tomar a tolerancia utilizada no item b)\n")

l = int(input("Defina aqui quantas linhas voce deseja em sua tabela: "))
dTabInter = []
j = 0
while(j < l):
	print("Insira na ordem: x1 valor do intervalo e x2 valor do intervalo: ")	
	x11 = float(input("valor x1: "))
	x22 = float(input("valor x2: "))
	itera = numIterac(x11,x22,tol)
	r = bisseccao(x11,x22,tol,itera)
	liInter =[x11,x22,r,itera]
	dTabInter.append(liInter)	
	j+=1	

# Falta formatar os dados em formato tabela e corrigir alguns problemas de verificacao
print()
print(" #### Tabela da Bisseccao ####")
print("| valor x1  | valor x2  | raiz encontrada para f(x) | Numero de iteracoes |")
for i in range(0,l):
	print("|    {}    |".format(dTabInter[i][0]), end="")
	print("   {}    |".format(dTabInter[i][1]), end="")
	if( dTabInter[i][2] == None ):
		print("           None            |", end="")
	else:
		print("         {0:.7f}           |".format(dTabInter[i][2]), end="")


	print("         {}        |".format(dTabInter[i][3]))

#Metodo de Newton : Erick

dTabNewton = []
j = 0
while(j < l):
	print("Insira na ordem: x1 valor do intervalo e x2 valor do intervalo: ")	
	x0 = float(input("valor x0: "))
	x1, nInt = newton(x0,tol,itera)
	liNewton =[x0,x1,nInt]
	dTabNewton.append(liNewton)	
	j+=1	

print()
print(" #### Tabela de Newton ####")
print("| valor x0 | raiz encontrada para f(x) | Numero de iteracoes |")
for i in range(0,l):
	print("|    {}    |".format(dTabNewton[i][0]), end="")
	print("   {}    |".format(dTabNewton[i][1]), end="")
	if( dTabNewton[i][2] == None ):
		print("           None            |", end="")
	else:
		print("         {0:.7f}           |".format(dTabNewton[i][2]), end="")


#comment: github repo















