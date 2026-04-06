# UTN-TUPaDProgramacion1

\# PUNTO 1

while True: # Creamos un bucle infinito que se termina al entrar en break

&#x20;   nombre\_cliente = input("Ingrese su nombre (solo letras): ") # Le pedimos el nombre al cliente

&#x20;   if nombre\_cliente.isalpha(): # Validamos que el nombre ingresado contenga solo letras

&#x20;       break # En caso positivo salimos del bucle

&#x20;   else:

&#x20;       print("Error, el nombre solo debe contener letras y no debe estar vacio") # En caso negativo se repite el bucle



while True: # Creamos un bucle infinito que se termina al entrar en break

&#x20;   productos\_comprar= (input("Ingrese la cantidad de productos a comprar: ")) # Le pedimos la cantidad de productos a comprar al cliente

&#x20;   if productos\_comprar.isdigit(): # Validamos que el numero ingresado sea entero y positivo

&#x20;       productos\_comprar = int(productos\_comprar)

&#x20;       if productos\_comprar > 0:

&#x20;           break # En caso positivo salimos del bucle

&#x20;       else:

&#x20;           print("por favor, ingrese un numero positivo")

&#x20;   else:

&#x20;       print("Error, ingrese un numero entero") # En caso negativo se repite el bucle



precio\_total = 0

descuento\_producto = ""

descuento = 0

precio\_descuento = 0

promedio = 0 # Creamos las variables que vamos a utilizar



for i in range(productos\_comprar): # Iniciamos bucle con la cantidad de productos que ingreso el usuario

&#x20; while True:

&#x20;     precio\_producto = (input("Ingrese el precio del producto: ")) # Le pedimos al usuario que ingrese el precio del producto

&#x20;     if precio\_producto.isdigit(): # Analizamos si el numero ingresado es valido

&#x20;         precio\_producto = int(precio\_producto) # Convertimpos el numero ingresado en un int para que lo procese bien la maquina

&#x20;         precio\_total += precio\_producto # sumamos el valor ingresado a una variante 

&#x20;         break

&#x20;     else:

&#x20;         print("Por favor ingrese un numero valido") # Si el numero no es valido le pedimos que vuelva a ingresar el precio

&#x20; while True:

&#x20;     descuento\_producto = input("¿Contiene descuento? S/N: ").lower() # Le preguntamos al usuario si tiene descuento el producto y lo ingresado lo pasamos a minuscula para evitar errores

&#x20;     if descuento\_producto not in \["s","n"]: # Analizamos si ingreso n o s

&#x20;         print("Por favor, ingrese S/N")  # En caso de poner bien la letra le pedimos que vuelva a ingresar

&#x20;     elif descuento\_producto == "s": 

&#x20;          descuento =  descuento +((precio\_producto \* 10) / 100) # Si ingresa s realizamos el descuento

&#x20;          break     

&#x20;     else:

&#x20;         print("No se aplica descuento") # Si pone n no se aplica el descuento

&#x20;         break    



precio\_descuento = precio\_total - descuento # Sumamos el valor total a pagar con descuento

promedio = precio\_descuento / productos\_comprar # Realizamos el promedio de los productos

&#x20;         

&#x20;         

&#x20;                                  



print(f"total sin decuento: {precio\_total}") # Comunicamos el total sin descuento

print(f"Total con descuento: {precio\_descuento}") # Comunicamos el total con descuento

print(f"Ahorro: {descuento}") # Comunicamos lo que se descuenta

print(f"promedio por producto: {promedio:.2f}") # Comunicamos el promedio por producto





\# PUNTO 2

usuario\_correcto = "alumno"

clave\_correcta = "python123" # Definimos el usuario y la clave determinadas



for i in range(1,4): # Iniciamos bucle for con 3 intentos

&#x20;   usuario\_ingresado = input("Por favor, ingrese el nombre de usuario: ") # Le pedimos al usuario el nombre de usuario

&#x20;   clave\_ingresada = input("Por favor, ingrese la contraseña: ") # Le pedimos al usuario la clave

&#x20;   if usuario\_ingresado == usuario\_correcto and clave\_ingresada == clave\_correcta: # corroboramos si lo ingresado es correcto

&#x20;       print("Acceso conseguido") # Al ser correcto le damos acceso

&#x20;       break

&#x20;   else:

&#x20;       print(f"Error, credenciales invalidas, intento {i} de 3 ") # Comunicamos que lo ingresado es incorrecto y le damos otro intento

else:

&#x20;   print("Cuenta bloqueada") # Al finalizar los 3 intentos se comunica que su cuenta fue bloqueada





while usuario\_ingresado == usuario\_correcto and clave\_ingresada == clave\_correcta: # Si la clave y el usuario es correcto continuamos

&#x20;   print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir") # Le mostramos que opcion puede elegir

&#x20;   opcion = (input("opcion: ")) # Le dejamos elegir una de las opciones

&#x20;   if opcion.isdigit(): # Corroboramos que lo ingresado sea un numero

&#x20;       opcion = int(opcion) # Convertimos lo ingresado en un int

&#x20;       if opcion == 1:

&#x20;           print("Inscripto") # Si elige la opcion 1 le mostramos su estado

&#x20;       elif opcion == 2:

&#x20;           nueva\_clave = input("Ingrese una nueva clave, por favor que tenga minimo 6 caracteres: ") # Si elige la opcion 2 le pedimos que ingrese una nueva clave

&#x20;           confirmacion\_nueva\_clave = input("Confirme la nueva clave: ") # Le pedimos que reingrese la clave

&#x20;           if len(nueva\_clave) >= 6 and nueva\_clave == confirmacion\_nueva\_clave: # Corroboramos que tenga mas de 6 caracteres y sean iguales las 2 claves ingresadas

&#x20;               print("Clave cambiada correctamente") # Si es positivo comunicamos el cambio de clave

&#x20;               clave\_correcta = nueva\_clave # Guardamos en la variable fija la nueva clave

&#x20;           else:

&#x20;               print("La clave no cumple con los 6 caracteres o las contraseñas no coinciden") # Si no cumple los requisitos le decimos que vuelva a intentar

&#x20;       elif opcion == 3: 

&#x20;           print("La clave del exito es el fracaso") # Si elige 3 mostramos frase motivacional

&#x20;       elif opcion == 4:

&#x20;           break # Si elige 4 salimos

&#x20;       else:

&#x20;           print("Opcion fuera de rango") # Si elige un numero fuera del rango se lo comunicamos

&#x20;   else:   

&#x20;       print("Por favor ingrese un numero valido") # Si no ingresa un numero se lo comunicamos





\# PUNTO 3

lunes1 = lunes2 = lunes3 = lunes4 = "libre"

martes1 = martes2 = martes3 = "libre" # Creamos las variables de los dias



while True:

&#x20;   nombre\_operador = input("Por favor, ingrese el nombre del operador: ") # Le pedimos al usuario el nombre del operador

&#x20;   if nombre\_operador.isalpha(): # Analizamos que ingrese solo letras

&#x20;       print("1. Reservar turno   2. Cancelar turno   3. Ver agenda del dia   4. Ver resumen general   5. Cerrar sistema") # Mostramos el menu

&#x20;       opcion = input("opcion: ") # Le damos a elegir una opcion

&#x20;       if opcion.isdigit(): # Analizamos que haya igresado un numero valido

&#x20;           opcion = int(opcion) # Pasamos lo ingresado a un int

&#x20;           if opcion == 1:

&#x20;              dia = input("Elige un dia (Lunes: 1, Martes: 2): ") # Si el usuario ingreso 1 le pedimos un dia

&#x20;              if dia != "1" and dia != "2":

&#x20;                print("Dia invalido") # Si no ingresa 1 o 2 le decimos que es un dia invalido

&#x20;                continue

&#x20;              else:

&#x20;                nombre\_paciente = input("Ingrese el nombre del paciente: ") # Si ingresa lo correcto le decimos que ingrese su nombre

&#x20;                if nombre\_paciente.isalpha(): # Analizamos que haya ingresado solo letras

&#x20;                    pass

&#x20;                else:

&#x20;                    print("Solo letras") # Si no ingresa letras le decimos que lo vuelva a poner

&#x20;                    continue

&#x20;              if dia == "1":

&#x20;                 if nombre\_paciente == lunes1 or nombre\_paciente == lunes2 or nombre\_paciente == lunes3 or nombre\_paciente == lunes4:

&#x20;                    print("Paciente repetido") # Analizamos que no sea un paciente repetido

&#x20;                 else:

&#x20;                   if lunes1 == "libre":

&#x20;                     lunes1 = nombre\_paciente

&#x20;                     print("Turno reservado")  # Analizamos si el turno esta libre

&#x20;                   elif lunes2 == "libre":

&#x20;                     lunes2 = nombre\_paciente

&#x20;                     print("Turno reservado") # Analizamos si el turno esta libre

&#x20;                   elif lunes3 == "libre":

&#x20;                     lunes3 = nombre\_paciente

&#x20;                     print("Turno reservado") # Analizamos si el turno esta libre

&#x20;                   elif lunes4 == "libre":

&#x20;                     lunes4 = nombre\_paciente

&#x20;                     print("Turno reservado")# Analizamos si el turno esta libre

&#x20;                   else:

&#x20;                     print("Sin espacio.") # Si estan todos los turnos del lunes reservados le comunicamos que no hay espacio

&#x20;              else:

&#x20;                 if nombre\_paciente == martes1 or nombre\_paciente == martes2 or nombre\_paciente == martes3:

&#x20;                   print("Paciente repetido") # Analizamos que no sea un paciente repetido

&#x20;                 else:

&#x20;                    if martes1 == "libre":

&#x20;                      martes1 = nombre\_paciente

&#x20;                      print("Turno reservado") # Analizamos si el turno esta libre

&#x20;                    elif martes2 == "libre":

&#x20;                      martes2 = nombre\_paciente

&#x20;                      print("Turno reservado") # Analizamos si el turno esta libre

&#x20;                    elif martes3 == "libre":

&#x20;                      martes3 = nombre\_paciente

&#x20;                      print("Turno reservado") # Analizamos si el turno esta libre

&#x20;                    else:

&#x20;                      print("Sin espacio") # Si estan todos los turnos del martes reservados le comunicamos que no hay espacio

&#x20;           elif opcion == 2:

&#x20;               dia\_cancelar = input("Dia del turno a cancelar (Lunes: 1, Martes: 2): ") # Si elige la opcion 2 le preguntamos que dia reservo

&#x20;               if dia\_cancelar != "1" and dia\_cancelar != "2": # Analizamos que haya ingresado un numero valido

&#x20;                  print("Dia invalido") # Si no es valido se lo comunicamos

&#x20;                  continue

&#x20;               else:

&#x20;                  nombre\_cancelar = input("Nombre del paciente a cancelar: ") # Si es valido le pedimos el nombre del paciente

&#x20;                  if nombre\_cancelar.isalpha(): # Analizamos que el nombre ingresado sea solo letras

&#x20;                      if dia\_cancelar == "1":

&#x20;                          if lunes1 == nombre\_cancelar:

&#x20;                              lunes1 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          elif lunes2 == nombre\_cancelar:

&#x20;                              lunes2 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          elif lunes3 == nombre\_cancelar:

&#x20;                              lunes3 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          elif lunes4 == nombre\_cancelar:

&#x20;                              lunes4 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          else:

&#x20;                              print("No existe el turno") # Si el turno no existe se lo comunicamos

&#x20;                      else:

&#x20;                          if martes1 == nombre\_cancelar:

&#x20;                              martes1 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          elif martes2 == nombre\_cancelar:

&#x20;                              martes2 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          elif martes3 == nombre\_cancelar:

&#x20;                              martes3 = "libre"

&#x20;                              print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos

&#x20;                          else:

&#x20;                              print("No existe el turno")  # Si el turno no existe se lo comunicamos

&#x20;                  else:

&#x20;                     print("Solo letras") # Si ingreso numeros le comunicamos que solo son validas las letras

&#x20;                     continue  

&#x20;           elif opcion == 3:

&#x20;              dia\_agenda = int(input("Ingresa el dia (Lunes: 1, Martes: 2): ")) # Le pedimos que eliga el dia de los turnos a mostrar

&#x20;              if dia\_agenda == 1:

&#x20;                 print(f"lunes: {lunes1},{lunes2},{lunes3},{lunes4}") # Mostramos la agenda del lunes

&#x20;              elif dia\_agenda == 2:

&#x20;                 print(f"Martes: {martes1}, {martes2},{martes3}") # Mostramos la agenda del martes

&#x20;              else:

&#x20;                 print("Dia invalido") # Si ingresa un numero invalido se lo comunicamos

&#x20;           elif opcion == 4:

&#x20;              print(f"Lunes: {lunes1}, {lunes2}, {lunes3}, {lunes4}") 

&#x20;              print(f"Martes: {martes1}, {martes2}, {martes3}") # Mostramos la agenda de los 2 dias juntos

&#x20;           elif opcion == 5:

&#x20;              print("Sistema cerrado") # Le comunicamos que cerro el sistema y lo cerramos

&#x20;              break

&#x20;           else:

&#x20;              print("Numero invalido") # Comunicamos que ingreso un numero invalido

&#x20;       else: 

&#x20;            print("Por favor, ingrese un numero valido") # Le pedimos que ingrese un numero valido

&#x20;            continue    

&#x20;   else:

&#x20;       print("Solo letras") # Le comunicamos que son validas solo las letras

&#x20;       continue







\# PUNTO 4

energia = 100

tiempo = 12

cerraduras\_abiertas = 0

alarma = False

codigo\_parcial = "" 

forzar\_seguidas = 0  # Ingresamos las variables iniciales



while True:

&#x20;   nombre\_agente = input("Ingrese el nombre del agente(Solo letras): ") # Le pedimos al usuario que ingrese un nombre para el agente

&#x20;   if nombre\_agente.isalpha(): # Analizamos que el nombre solo contenga letras

&#x20;       print(f"Bienvenido {nombre\_agente}") # Si es correcto le damos la bienvenida

&#x20;       break

&#x20;   else:

&#x20;       print("Solo letras") # Si es incorrecto le pedimos que lo vuelva a ingresar

&#x20;       continue



while True:

&#x20;       if alarma == True and tiempo <= 3:

&#x20;           print("Haz perdido") # Si se cumple esta condicion el usuario perdio

&#x20;           break

&#x20;       elif energia <= 0 or tiempo <= 0:

&#x20;           print("Haz perdido") # Si se cumple esta condicion el usuario perdio

&#x20;           break

&#x20;       elif cerraduras\_abiertas == 3:

&#x20;           print("Haz ganado, felicitaciones") # Si se cumple esta condicion el usuario gano

&#x20;           break

&#x20;       print(f"energia: {energia}, tiempo: {tiempo}, cerraduras abiertas: {cerraduras\_abiertas}, alarma: {alarma}, codigo parcial: {codigo\_parcial} ") # Informamos en que condicion se encuentra

&#x20;       print ("1) Forjar cerradura (costo: -20 energía, -2 tiempo)   2) Hackear panel (costo: -10 energía, -3 tiempo)   3) Descansar(costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)") # Le damos a elegir opciones

&#x20;       opcion = input("Opcion: ") # Le decimos al usuario que eliga una opcion

&#x20;       if opcion.isdigit(): # Analizamos que haya ingresado numeros

&#x20;           opcion = int(opcion) # Convertimos lo ingresado en un int

&#x20;           if opcion == 1: # Si elige la opcion 1

&#x20;               print("Haz perdido 20 de energia y 2 de tiempo") # Le comunicamos que perdio 20 de energia y 2 de tiempo

&#x20;               forzar\_seguidas += 1

&#x20;               energia -= 20

&#x20;               tiempo -= 2 # Sumamos los valores correspondientes

&#x20;               if alarma == False:

&#x20;                   cerraduras\_abiertas +=1

&#x20;                   print("Haz abierto una cerradura") # Si la alarma esta apagada abre una cerradura

&#x20;               if forzar\_seguidas == 3:

&#x20;                   alarma = True

&#x20;                   print("Se activo la alarma, haz perdido") # Regla anti spam

&#x20;                   break

&#x20;               if energia < 40:

&#x20;                   print("Hay riesgo de alarma, elige un numero del 1 al 3") # Si tiene menos de 40 de energia tiene que elegir un numero del 1 al 3

&#x20;                   numero\_alarma = int(input("Numero elegido: ")) # Le dejamos elegir

&#x20;                   if numero\_alarma == 3:

&#x20;                       alarma = True

&#x20;                       print("Se activo la alarma, haz perdido") # Si elige el 3 se prende la alarma y pierde

&#x20;                       break

&#x20;                   elif numero\_alarma == 1 or numero\_alarma == 2:

&#x20;                       cerraduras\_abiertas += 1 # Si elige el 1 o el 2 se abre la cerradura

&#x20;                   else:

&#x20;                       print("Numero invalido") # Si no ingresa un valor correcto se lo comunicamos

&#x20;                       continue

&#x20;           elif opcion == 2:

&#x20;               print("Haz perdido 10 de energia y 3 de tiempo") # Si elige la opcion 2 pierde 10 de energia y 3 de tiempo

&#x20;               energia -= 10

&#x20;               tiempo -= 3

&#x20;               forzar\_seguidas = 0 # Modificamos los valores correspondientes

&#x20;               for i in range(1,5): # Creamos bucle for

&#x20;                   print(f"Paso {i}, haz sumado una A") # Informamos los pasos

&#x20;                   codigo\_parcial += "A" # Sumamos una A por paso

&#x20;               print(f"Tu codigo parcial es: {codigo\_parcial}") # Le mostramos el codigo

&#x20;               if len(codigo\_parcial) >=8:

&#x20;                   cerraduras\_abiertas +=1

&#x20;                   print("Haz abierto una cerradura") # Si llega a las 8 A abre una cerradura

&#x20;                   codigo\_parcial = "" # Reiniciamos el contador

&#x20;           elif opcion == 3: # Si elige la opcion 3

&#x20;               energia += 15

&#x20;               tiempo -= 1

&#x20;               forzar\_seguidas = 0 # Modificamos las variables correspondientes

&#x20;               print("Recuperaste 15 de energia y perdiste 1 de tiempo") # Informamos que recupero 15 de energia y perdio 1 de tiempo

&#x20;               if energia > 100:

&#x20;                   energia = 100 # No permitimos que tenga mas de 100 de energia

&#x20;               if alarma == True:

&#x20;                   energia -= 10 # Modificamos la variable correspondiente

&#x20;                   print("Haz descansado con la alarma prendida, pierdes 10 de energia") # Si descansa con la alarma prendida pierde 10 de energia

&#x20;           else:

&#x20;               print("opcion invalida") # Informamos que la opcion no es valida

&#x20;               continue

&#x20;       else:

&#x20;           print("Opcion invalida") # Informamos que la opcion no es valida

&#x20;           continue





\# PUNTO 5

while True: # Creamos bucle while

&#x20;   print("Bienvenido a la arena") # Le damos la bienvenida al usuario

&#x20;   nombre\_gladiador = input("Nombre del gladiador: ") # Le pedimos el nombre del gladiador al usuario

&#x20;   if nombre\_gladiador.isalpha(): # Analizamos si el nombre contiene solo letras

&#x20;       print("Inicio del combate") # En caso positivo arrancamos el combate

&#x20;       break

&#x20;   else:

&#x20;       print("Error: solo se permiten letras") # En caso negativo le decimos que solo se permiten letras

&#x20;       continue



Vida\_del\_Gladiador = 100 

Vida\_Enemigo = 100 

Pociones\_de\_Vida = 3 

Dano\_base\_Ataque\_Pesado = 15 

Dano\_base\_enemigo = 12 

Turno\_Gladiador = True  # Ingresamos las variables iniciales



while Vida\_del\_Gladiador > 0 and Vida\_Enemigo > 0: # Si los 2 tienen mas de 0 puntos de vida la partida sigue

&#x20;   if Turno\_Gladiador == True: # Se ejecuta si es turno del usuario

&#x20;       print(f"Leonidas: (HP {Vida\_Enemigo}) VS {nombre\_gladiador}: (HP {Vida\_del\_Gladiador}) | {Pociones\_de\_Vida} pociones de vida") # Informamos al usuario la vida de los 2 y cuantas pociones de vida tiene

&#x20;       print("Elige una opcion.  1. Ataque Pesado   2. Ráfaga Veloz   3. Curar") # Le mostramos las opciones a elegir

&#x20;       opcion = input("Opcion: ") # Le dejamos elegir

&#x20;       if opcion.isdigit(): # Analizamos si ingreso un valor correcto

&#x20;           opcion = int(opcion) # En caso positivo convertimos lo ingresado en int

&#x20;           if opcion == 1: # Si elige la opcion 1

&#x20;               if Vida\_Enemigo < 20: # Si el enemigo tiene menos de 20 puntos de vida

&#x20;                   Vida\_Enemigo -= Dano\_base\_Ataque\_Pesado \* 1.5 # Se le resta el valor indicado a la vida del enemigo

&#x20;                   print(f"Atacaste al enemigo por {Dano\_base\_Ataque\_Pesado \* 1.5} puntos de daño") # Se comunica el daño causado

&#x20;                   Turno\_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo

&#x20;               else:

&#x20;                   Vida\_Enemigo -= Dano\_base\_Ataque\_Pesado # Si el enemigo tiene mas de 20 puntos de vida se resta el ataque normal

&#x20;                   print(f"Atacaste al enemigo por {Dano\_base\_Ataque\_Pesado} puntos de daño") # Se comunica el daño causado

&#x20;                   Turno\_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo

&#x20;           elif opcion == 2: # Si elige la opcion 2

&#x20;               for i in range(3): # Se crea bucle for

&#x20;                   print("Golpe conectado por 5 de daño") # Se comunica el daño causado

&#x20;                   Vida\_Enemigo -= 5 # Se resta la vida del enemigo

&#x20;               Turno\_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo

&#x20;           elif opcion == 3: # Si elige la opcion 3

&#x20;               if Pociones\_de\_Vida > 0: # Si tiene pociones de vida

&#x20;                   Vida\_del\_Gladiador += 30 # Se cura 30 puntos de vida

&#x20;                   Pociones\_de\_Vida -= 1 # Pierde una pocion de vida

&#x20;                   print("Te has curado 30 puntos de vida") # Se comunica que se curo 30 puntos de vida

&#x20;                   Turno\_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo

&#x20;               else:

&#x20;                   print("¡No quedan pociones!, pierdes el turno") # Se comunica que no tiene pociones de vida y pierde el turno

&#x20;                   Turno\_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo

&#x20;           else:

&#x20;               print("Numero invalido") # Comunicamos que lo ingresado es invalido

&#x20;               continue

&#x20;       else:

&#x20;           print("Error: ingrese un numero valido") # Comunicamos que lo ingresado es invalido

&#x20;           continue

&#x20;   else:

&#x20;       Vida\_del\_Gladiador -= Dano\_base\_enemigo # Le restamos vida al usuario por cada turno del rival

&#x20;       print(f"¡El enemigo te atacó por {Dano\_base\_enemigo} puntos de daño!") # Comunicamos el daño del enemigo

&#x20;       Turno\_Gladiador = True # Se cambia el valor booleano para que sea turno del usuario





if Vida\_del\_Gladiador <= 0:

&#x20;   print("DERROTA. Has caído en combate.") # Se comunica que si el usuario llega a 0 puntos de vida perdio



if Vida\_Enemigo <= 0:

&#x20;   print(f"¡VICTORIA! {nombre\_gladiador} ha ganado la batalla!.") # Se comunica que si el enemigo llego a 0 puntos de vida gano 



