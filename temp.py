import matplotlib.pyplot as plt
plt.plot([0,0,1,1,2,2,2,2,3,3,5,5,5,6,6,6,6,7,7])
#Con esta isntruccion colocamos un titulo al eje de la grafica. 
plt.ylabel('Numero de hermanos y primos')
plt.xlabel('Anios')
plt.title('Numero de hermanos y primos por anio de vida')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()

