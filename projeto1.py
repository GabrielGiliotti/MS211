import matplotlib.pyplot as plt
import math as mt

print("\nProjeto 1 - MS211 - Professor Florindo\n\n" +
	"Linguagem de Programacao Utilizada: Python3\n" +
	"Motivacao: Desejamos realizar a aproximacao e/ou encontrar raizes de funcoes atraves de metodos numericos de aproximação.\n")

print("Como exemplo de funcao, vamos tomar a equacao de Butler-Volmer em processos eletroquimicos que relaciona a\n" +
      "densidade de corrente com o potencial em um eletrodo e pode ser escrita como:\n\n")

print("			f(x) =  e^(alpha*x) - e^((alpha-1)*x) - beta 		, sendo alpha = 0.2 e beta = 2.0 \n\n")

#Item a) a partir daqui
print("Item a) Encontrando um intervalo que contenha uma raiz de f(x)\n", end="")
print("Inicialmente vamos tomar arbitrariamente a funcao no intervalo x1, x2 e analisar seu grafico visualmente")
print("(Obs:Apos o plot do grafico esta indicado se o intervalo apresenta raiz ou nao, segundo os criterios do teorema que vem a seguir)")
print("Digite os valores do intervalo no eixo x [x1,x2] em que voce deseja encontrar uma raiz:\n")
x1 = float(input("Valor de x1: "))
x2 = float(input("Valor de x2: "))
print("Para analisar se o intervalo [x1,x2] contem pelo menos uma raiz da funcao, fazemos uso do seguinte teorema:\n")
print("Seja f(x) uma função contínua no intervalo [x1,x2].", end="")
print("Se f(x1)*f(x2) < 0 (ou seja, f(x1) e f(x2) tem sinais contrários), então existe pelo menos uma raiz real de f no intervalo[x1,x2]\n")

a = 0.2 # considere que a eh alpha 
b = 2.0 # considere que b eh beta
f1 = mt.exp(x1*a) - mt.exp((a-1)*x1) - b
f2 = mt.exp(x2*a) - mt.exp((a-1)*x2) - b
if( f1*f2 < 0 ): 
	print("O Intervalo escolhido apresenta pelo menos uma raiz segundo o teorema.")
else:
	print("O Intervalo escolhido nao atende ao(s) criterio(s) do teorema.")

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

# Item b) a partir daqui.
print("Item b) Implementacao dos metodos numericos Bisseccao --> (Metodo1) e Newton --> (Metodo2)")














