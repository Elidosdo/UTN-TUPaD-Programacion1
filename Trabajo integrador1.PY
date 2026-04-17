# PUNTO 1
while True: # Creamos un bucle infinito que se termina al entrar en break
    nombre_cliente = input("Ingrese su nombre (solo letras): ") # Le pedimos el nombre al cliente
    if nombre_cliente.isalpha(): # Validamos que el nombre ingresado contenga solo letras
        break # En caso positivo salimos del bucle
    else:
        print("Error, el nombre solo debe contener letras y no debe estar vacio") # En caso negativo se repite el bucle

while True: # Creamos un bucle infinito que se termina al entrar en break
    productos_comprar= (input("Ingrese la cantidad de productos a comprar: ")) # Le pedimos la cantidad de productos a comprar al cliente
    if productos_comprar.isdigit(): # Validamos que el numero ingresado sea entero y positivo
        productos_comprar = int(productos_comprar)
        if productos_comprar > 0:
            break # En caso positivo salimos del bucle
        else:
            print("por favor, ingrese un numero positivo")
    else:
        print("Error, ingrese un numero entero") # En caso negativo se repite el bucle

precio_total = 0
descuento_producto = ""
descuento = 0
precio_descuento = 0
promedio = 0 # Creamos las variables que vamos a utilizar

for i in range(productos_comprar): # Iniciamos bucle con la cantidad de productos que ingreso el usuario
  while True:
      precio_producto = (input("Ingrese el precio del producto: ")) # Le pedimos al usuario que ingrese el precio del producto
      if precio_producto.isdigit(): # Analizamos si el numero ingresado es valido
          precio_producto = int(precio_producto) # Convertimpos el numero ingresado en un int para que lo procese bien la maquina
          precio_total += precio_producto # sumamos el valor ingresado a una variante 
          break
      else:
          print("Por favor ingrese un numero valido") # Si el numero no es valido le pedimos que vuelva a ingresar el precio
  while True:
      descuento_producto = input("¿Contiene descuento? S/N: ").lower() # Le preguntamos al usuario si tiene descuento el producto y lo ingresado lo pasamos a minuscula para evitar errores
      if descuento_producto not in ["s","n"]: # Analizamos si ingreso n o s
          print("Por favor, ingrese S/N")  # En caso de poner bien la letra le pedimos que vuelva a ingresar
      elif descuento_producto == "s": 
           descuento =  descuento +((precio_producto * 10) / 100) # Si ingresa s realizamos el descuento
           break     
      else:
          print("No se aplica descuento") # Si pone n no se aplica el descuento
          break    

precio_descuento = precio_total - descuento # Sumamos el valor total a pagar con descuento
promedio = precio_descuento / productos_comprar # Realizamos el promedio de los productos
          
          
                                   

print(f"total sin decuento: {precio_total}") # Comunicamos el total sin descuento
print(f"Total con descuento: {precio_descuento}") # Comunicamos el total con descuento
print(f"Ahorro: {descuento}") # Comunicamos lo que se descuenta
print(f"promedio por producto: {promedio:.2f}") # Comunicamos el promedio por producto


# PUNTO 2
usuario_correcto = "alumno"
clave_correcta = "python123" # Definimos el usuario y la clave determinadas

for i in range(1,4): # Iniciamos bucle for con 3 intentos
    usuario_ingresado = input("Por favor, ingrese el nombre de usuario: ") # Le pedimos al usuario el nombre de usuario
    clave_ingresada = input("Por favor, ingrese la contraseña: ") # Le pedimos al usuario la clave
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta: # corroboramos si lo ingresado es correcto
        print("Acceso conseguido") # Al ser correcto le damos acceso
        break
    else:
        print(f"Error, credenciales invalidas, intento {i} de 3 ") # Comunicamos que lo ingresado es incorrecto y le damos otro intento
else:
    print("Cuenta bloqueada") # Al finalizar los 3 intentos se comunica que su cuenta fue bloqueada


while usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta: # Si la clave y el usuario es correcto continuamos
    print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir") # Le mostramos que opcion puede elegir
    opcion = (input("opcion: ")) # Le dejamos elegir una de las opciones
    if opcion.isdigit(): # Corroboramos que lo ingresado sea un numero
        opcion = int(opcion) # Convertimos lo ingresado en un int
        if opcion == 1:
            print("Inscripto") # Si elige la opcion 1 le mostramos su estado
        elif opcion == 2:
            nueva_clave = input("Ingrese una nueva clave, por favor que tenga minimo 6 caracteres: ") # Si elige la opcion 2 le pedimos que ingrese una nueva clave
            confirmacion_nueva_clave = input("Confirme la nueva clave: ") # Le pedimos que reingrese la clave
            if len(nueva_clave) >= 6 and nueva_clave == confirmacion_nueva_clave: # Corroboramos que tenga mas de 6 caracteres y sean iguales las 2 claves ingresadas
                print("Clave cambiada correctamente") # Si es positivo comunicamos el cambio de clave
                clave_correcta = nueva_clave # Guardamos en la variable fija la nueva clave
            else:
                print("La clave no cumple con los 6 caracteres o las contraseñas no coinciden") # Si no cumple los requisitos le decimos que vuelva a intentar
        elif opcion == 3: 
            print("La clave del exito es el fracaso") # Si elige 3 mostramos frase motivacional
        elif opcion == 4:
            break # Si elige 4 salimos
        else:
            print("Opcion fuera de rango") # Si elige un numero fuera del rango se lo comunicamos
    else:   
        print("Por favor ingrese un numero valido") # Si no ingresa un numero se lo comunicamos


# PUNTO 3
lunes1 = lunes2 = lunes3 = lunes4 = "libre"
martes1 = martes2 = martes3 = "libre" # Creamos las variables de los dias

while True:
    nombre_operador = input("Por favor, ingrese el nombre del operador: ") # Le pedimos al usuario el nombre del operador
    if nombre_operador.isalpha(): # Analizamos que ingrese solo letras
        print("1. Reservar turno   2. Cancelar turno   3. Ver agenda del dia   4. Ver resumen general   5. Cerrar sistema") # Mostramos el menu
        opcion = input("opcion: ") # Le damos a elegir una opcion
        if opcion.isdigit(): # Analizamos que haya igresado un numero valido
            opcion = int(opcion) # Pasamos lo ingresado a un int
            if opcion == 1:
               dia = input("Elige un dia (Lunes: 1, Martes: 2): ") # Si el usuario ingreso 1 le pedimos un dia
               if dia != "1" and dia != "2":
                 print("Dia invalido") # Si no ingresa 1 o 2 le decimos que es un dia invalido
                 continue
               else:
                 nombre_paciente = input("Ingrese el nombre del paciente: ") # Si ingresa lo correcto le decimos que ingrese su nombre
                 if nombre_paciente.isalpha(): # Analizamos que haya ingresado solo letras
                     pass
                 else:
                     print("Solo letras") # Si no ingresa letras le decimos que lo vuelva a poner
                     continue
               if dia == "1":
                  if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                     print("Paciente repetido") # Analizamos que no sea un paciente repetido
                  else:
                    if lunes1 == "libre":
                      lunes1 = nombre_paciente
                      print("Turno reservado")  # Analizamos si el turno esta libre
                    elif lunes2 == "libre":
                      lunes2 = nombre_paciente
                      print("Turno reservado") # Analizamos si el turno esta libre
                    elif lunes3 == "libre":
                      lunes3 = nombre_paciente
                      print("Turno reservado") # Analizamos si el turno esta libre
                    elif lunes4 == "libre":
                      lunes4 = nombre_paciente
                      print("Turno reservado")# Analizamos si el turno esta libre
                    else:
                      print("Sin espacio.") # Si estan todos los turnos del lunes reservados le comunicamos que no hay espacio
               else:
                  if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                    print("Paciente repetido") # Analizamos que no sea un paciente repetido
                  else:
                     if martes1 == "libre":
                       martes1 = nombre_paciente
                       print("Turno reservado") # Analizamos si el turno esta libre
                     elif martes2 == "libre":
                       martes2 = nombre_paciente
                       print("Turno reservado") # Analizamos si el turno esta libre
                     elif martes3 == "libre":
                       martes3 = nombre_paciente
                       print("Turno reservado") # Analizamos si el turno esta libre
                     else:
                       print("Sin espacio") # Si estan todos los turnos del martes reservados le comunicamos que no hay espacio
            elif opcion == 2:
                dia_cancelar = input("Dia del turno a cancelar (Lunes: 1, Martes: 2): ") # Si elige la opcion 2 le preguntamos que dia reservo
                if dia_cancelar != "1" and dia_cancelar != "2": # Analizamos que haya ingresado un numero valido
                   print("Dia invalido") # Si no es valido se lo comunicamos
                   continue
                else:
                   nombre_cancelar = input("Nombre del paciente a cancelar: ") # Si es valido le pedimos el nombre del paciente
                   if nombre_cancelar.isalpha(): # Analizamos que el nombre ingresado sea solo letras
                       if dia_cancelar == "1":
                           if lunes1 == nombre_cancelar:
                               lunes1 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           elif lunes2 == nombre_cancelar:
                               lunes2 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           elif lunes3 == nombre_cancelar:
                               lunes3 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           elif lunes4 == nombre_cancelar:
                               lunes4 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           else:
                               print("No existe el turno") # Si el turno no existe se lo comunicamos
                       else:
                           if martes1 == nombre_cancelar:
                               martes1 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           elif martes2 == nombre_cancelar:
                               martes2 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           elif martes3 == nombre_cancelar:
                               martes3 = "libre"
                               print("Turno cancelado") # Analizamos si el turno esta ocupado y lo cancelamos
                           else:
                               print("No existe el turno")  # Si el turno no existe se lo comunicamos
                   else:
                      print("Solo letras") # Si ingreso numeros le comunicamos que solo son validas las letras
                      continue  
            elif opcion == 3:
               dia_agenda = int(input("Ingresa el dia (Lunes: 1, Martes: 2): ")) # Le pedimos que eliga el dia de los turnos a mostrar
               if dia_agenda == 1:
                  print(f"lunes: {lunes1},{lunes2},{lunes3},{lunes4}") # Mostramos la agenda del lunes
               elif dia_agenda == 2:
                  print(f"Martes: {martes1}, {martes2},{martes3}") # Mostramos la agenda del martes
               else:
                  print("Dia invalido") # Si ingresa un numero invalido se lo comunicamos
            elif opcion == 4:
               print(f"Lunes: {lunes1}, {lunes2}, {lunes3}, {lunes4}") 
               print(f"Martes: {martes1}, {martes2}, {martes3}") # Mostramos la agenda de los 2 dias juntos
            elif opcion == 5:
               print("Sistema cerrado") # Le comunicamos que cerro el sistema y lo cerramos
               break
            else:
               print("Numero invalido") # Comunicamos que ingreso un numero invalido
        else: 
             print("Por favor, ingrese un numero valido") # Le pedimos que ingrese un numero valido
             continue    
    else:
        print("Solo letras") # Le comunicamos que son validas solo las letras
        continue



# PUNTO 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = "" 
forzar_seguidas = 0  # Ingresamos las variables iniciales

while True:
    nombre_agente = input("Ingrese el nombre del agente(Solo letras): ") # Le pedimos al usuario que ingrese un nombre para el agente
    if nombre_agente.isalpha(): # Analizamos que el nombre solo contenga letras
        print(f"Bienvenido {nombre_agente}") # Si es correcto le damos la bienvenida
        break
    else:
        print("Solo letras") # Si es incorrecto le pedimos que lo vuelva a ingresar
        continue

while True:
        if alarma == True and tiempo <= 3:
            print("Haz perdido") # Si se cumple esta condicion el usuario perdio
            break
        elif energia <= 0 or tiempo <= 0:
            print("Haz perdido") # Si se cumple esta condicion el usuario perdio
            break
        elif cerraduras_abiertas == 3:
            print("Haz ganado, felicitaciones") # Si se cumple esta condicion el usuario gano
            break
        print(f"energia: {energia}, tiempo: {tiempo}, cerraduras abiertas: {cerraduras_abiertas}, alarma: {alarma}, codigo parcial: {codigo_parcial} ") # Informamos en que condicion se encuentra
        print ("1) Forjar cerradura (costo: -20 energía, -2 tiempo)   2) Hackear panel (costo: -10 energía, -3 tiempo)   3) Descansar(costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)") # Le damos a elegir opciones
        opcion = input("Opcion: ") # Le decimos al usuario que eliga una opcion
        if opcion.isdigit(): # Analizamos que haya ingresado numeros
            opcion = int(opcion) # Convertimos lo ingresado en un int
            if opcion == 1: # Si elige la opcion 1
                print("Haz perdido 20 de energia y 2 de tiempo") # Le comunicamos que perdio 20 de energia y 2 de tiempo
                forzar_seguidas += 1
                energia -= 20
                tiempo -= 2 # Sumamos los valores correspondientes
                if alarma == False:
                    cerraduras_abiertas +=1
                    print("Haz abierto una cerradura") # Si la alarma esta apagada abre una cerradura
                if forzar_seguidas == 3:
                    alarma = True
                    print("Se activo la alarma, haz perdido") # Regla anti spam
                    break
                if energia < 40:
                    print("Hay riesgo de alarma, elige un numero del 1 al 3") # Si tiene menos de 40 de energia tiene que elegir un numero del 1 al 3
                    numero_alarma = int(input("Numero elegido: ")) # Le dejamos elegir
                    if numero_alarma == 3:
                        alarma = True
                        print("Se activo la alarma, haz perdido") # Si elige el 3 se prende la alarma y pierde
                        break
                    elif numero_alarma == 1 or numero_alarma == 2:
                        cerraduras_abiertas += 1 # Si elige el 1 o el 2 se abre la cerradura
                    else:
                        print("Numero invalido") # Si no ingresa un valor correcto se lo comunicamos
                        continue
            elif opcion == 2:
                print("Haz perdido 10 de energia y 3 de tiempo") # Si elige la opcion 2 pierde 10 de energia y 3 de tiempo
                energia -= 10
                tiempo -= 3
                forzar_seguidas = 0 # Modificamos los valores correspondientes
                for i in range(1,5): # Creamos bucle for
                    print(f"Paso {i}, haz sumado una A") # Informamos los pasos
                    codigo_parcial += "A" # Sumamos una A por paso
                print(f"Tu codigo parcial es: {codigo_parcial}") # Le mostramos el codigo
                if len(codigo_parcial) >=8:
                    cerraduras_abiertas +=1
                    print("Haz abierto una cerradura") # Si llega a las 8 A abre una cerradura
                    codigo_parcial = "" # Reiniciamos el contador
            elif opcion == 3: # Si elige la opcion 3
                energia += 15
                tiempo -= 1
                forzar_seguidas = 0 # Modificamos las variables correspondientes
                print("Recuperaste 15 de energia y perdiste 1 de tiempo") # Informamos que recupero 15 de energia y perdio 1 de tiempo
                if energia > 100:
                    energia = 100 # No permitimos que tenga mas de 100 de energia
                if alarma == True:
                    energia -= 10 # Modificamos la variable correspondiente
                    print("Haz descansado con la alarma prendida, pierdes 10 de energia") # Si descansa con la alarma prendida pierde 10 de energia
            else:
                print("opcion invalida") # Informamos que la opcion no es valida
                continue
        else:
            print("Opcion invalida") # Informamos que la opcion no es valida
            continue


# PUNTO 5
while True: # Creamos bucle while
    print("Bienvenido a la arena") # Le damos la bienvenida al usuario
    nombre_gladiador = input("Nombre del gladiador: ") # Le pedimos el nombre del gladiador al usuario
    if nombre_gladiador.isalpha(): # Analizamos si el nombre contiene solo letras
        print("Inicio del combate") # En caso positivo arrancamos el combate
        break
    else:
        print("Error: solo se permiten letras") # En caso negativo le decimos que solo se permiten letras
        continue

Vida_del_Gladiador = 100 
Vida_Enemigo = 100 
Pociones_de_Vida = 3 
Dano_base_Ataque_Pesado = 15 
Dano_base_enemigo = 12 
Turno_Gladiador = True  # Ingresamos las variables iniciales

while Vida_del_Gladiador > 0 and Vida_Enemigo > 0: # Si los 2 tienen mas de 0 puntos de vida la partida sigue
    if Turno_Gladiador == True: # Se ejecuta si es turno del usuario
        print(f"Leonidas: (HP {Vida_Enemigo}) VS {nombre_gladiador}: (HP {Vida_del_Gladiador}) | {Pociones_de_Vida} pociones de vida") # Informamos al usuario la vida de los 2 y cuantas pociones de vida tiene
        print("Elige una opcion.  1. Ataque Pesado   2. Ráfaga Veloz   3. Curar") # Le mostramos las opciones a elegir
        opcion = input("Opcion: ") # Le dejamos elegir
        if opcion.isdigit(): # Analizamos si ingreso un valor correcto
            opcion = int(opcion) # En caso positivo convertimos lo ingresado en int
            if opcion == 1: # Si elige la opcion 1
                if Vida_Enemigo < 20: # Si el enemigo tiene menos de 20 puntos de vida
                    Vida_Enemigo -= Dano_base_Ataque_Pesado * 1.5 # Se le resta el valor indicado a la vida del enemigo
                    print(f"Atacaste al enemigo por {Dano_base_Ataque_Pesado * 1.5} puntos de daño") # Se comunica el daño causado
                    Turno_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo
                else:
                    Vida_Enemigo -= Dano_base_Ataque_Pesado # Si el enemigo tiene mas de 20 puntos de vida se resta el ataque normal
                    print(f"Atacaste al enemigo por {Dano_base_Ataque_Pesado} puntos de daño") # Se comunica el daño causado
                    Turno_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo
            elif opcion == 2: # Si elige la opcion 2
                for i in range(3): # Se crea bucle for
                    print("Golpe conectado por 5 de daño") # Se comunica el daño causado
                    Vida_Enemigo -= 5 # Se resta la vida del enemigo
                Turno_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo
            elif opcion == 3: # Si elige la opcion 3
                if Pociones_de_Vida > 0: # Si tiene pociones de vida
                    Vida_del_Gladiador += 30 # Se cura 30 puntos de vida
                    Pociones_de_Vida -= 1 # Pierde una pocion de vida
                    print("Te has curado 30 puntos de vida") # Se comunica que se curo 30 puntos de vida
                    Turno_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo
                else:
                    print("¡No quedan pociones!, pierdes el turno") # Se comunica que no tiene pociones de vida y pierde el turno
                    Turno_Gladiador = False # Se cambia el valor booleano para que sea turno del enemigo
            else:
                print("Numero invalido") # Comunicamos que lo ingresado es invalido
                continue
        else:
            print("Error: ingrese un numero valido") # Comunicamos que lo ingresado es invalido
            continue
    else:
        Vida_del_Gladiador -= Dano_base_enemigo # Le restamos vida al usuario por cada turno del rival
        print(f"¡El enemigo te atacó por {Dano_base_enemigo} puntos de daño!") # Comunicamos el daño del enemigo
        Turno_Gladiador = True # Se cambia el valor booleano para que sea turno del usuario


if Vida_del_Gladiador <= 0:
    print("DERROTA. Has caído en combate.") # Se comunica que si el usuario llega a 0 puntos de vida perdio

if Vida_Enemigo <= 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla!.") # Se comunica que si el enemigo llego a 0 puntos de vida gano 



   
       

    
   

