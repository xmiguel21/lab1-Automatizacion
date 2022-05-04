import math
import matplotlib.pyplot as plt

t=0.1
sol=0
lista=list()
lista_numeros=[]
print("La función es : 5.1H(t)-6.8*math.exp(-0.5)-1.7*math.exp(-2t)")

for x in range(0,30):
  sol=((-6.8*math.exp(-0.5)-1.7*math.exp(-2*t))/5.1)
  lista.append(sol)
  t=t+0.1
  lista_numeros.append(x)

fig, ax = plt.subplots()
ax.plot(lista_numeros,lista,marker='o')
plt.title("Grafico de las weas de automatizacion")
plt.show( )

print("me chupa un huevo")