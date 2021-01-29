
#esto es la creacion del archivo con el mensaje a cifrar
mensaje = '''8
HOLA CHICOS Y CHICAS
ESTE MENSAJE ES SECRETO
Y LO ESTAMOS CIFRANDO CON
CODIGO CESAR'''
with open("mensaje.txt", "w+") as f: 
  f.write(mensaje)  
  f.close() 

from string import ascii_uppercase #aqui empieza mi programa

def cifrador(mensaje): #creo una funcion que va recibir el nombre de un archivo a leer
  abecedario = ascii_uppercase #creo una variable con las letras del abecedario
  mensajeCifrado = " " #creo una variable vacia donde se va a guardar mi mensaje cifrado

  print("Nombre del programa: Cifrador Cesar")
  print("Hecho por Leonel Benjamin Mercau")

  print(f"Nombre del archivo a cifrar: {mensaje} ")
  print("Nombre del archivo cifrado: mensajeCifrado.txt.cifrado ")

  with open(mensaje, "r") as f: #leo el archivo con la clave y el mensaje que quiero cifrar dentro de el
    f.seek(0)#pongo el cursor al comienzo del archivo
    primeraLineaMensaje = int(f.readline()) #leo la primera linea del archivo para sacar la clave y la convierto en integer
    mensajeLeido = f.read() #guardo la lectura del archivo en una variable para usarlo despues
    f.close() #cierro el archivo para evitar errores luego

  for letra in mensajeLeido.upper(): #recorro el mensaje letra por letra y lo convierto todo en mayuscula

    if letra in abecedario: #esto va a preguntar si la letra esta en el abecedario y si es asi, la remplaza sino la conserva
      numeroDeLaLetra = abecedario.index(letra) #saco la posicion (int) que ocupa la letra dentro de mi variable abecedario
                                                                  
      numeroDeLaLetra = (numeroDeLaLetra + primeraLineaMensaje) % 26 #aqui hago el desplazamiento, tomo la posicion de la letra y le sumo la clave
                                                                 #aqui arriba puse el % 26 porque hace que el numero no salga del rango de la cantidad de letras de mi abecedario, pongo un limite
      mensajeCifrado += abecedario[numeroDeLaLetra] #aqui genero el nuevo mensaje letra por letra y la guardo en la variable mensajeCifrado
    else:
      mensajeCifrado += letra #si la que hay en el mensaje no esta en el abecedario se conserva igual

  with open("mensajeCifrado.txt.cifrado", "w+") as ff:#aqui creo un archivo con los datos del mensaje cifrado
    ff.write(mensajeCifrado)#escribo el mensaje cifrado en mi nuevo archivo
    ff.seek(0)# pongo el cursor al principio
    codigoCifradoLectura = ff.read()#guardo la lectura del archivo en una variable para mostrar el texto cifrado despues
    ff.close() #cierro el archivo


  #print(f"Texto cifrado:\n{codigoCifradoLectura}")

cifrador("mensaje.txt")