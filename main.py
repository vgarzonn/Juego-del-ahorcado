# Preguntas y respuestas del primer nivelsirio
nivel1 = {
    "¿Qué es un objeto celeste que orbita al rededor de una estrella?": {"respuesta": "planeta", "pista": "7 letras"},
    "¿Cuál es la estrella más cercana a la Tierra?": {"respuesta": "sol", "pista": "3 letras"},
    "¿Cómo se llama el satélite natural de la Tierra?": {"respuesta": "luna", "pista": "4 letras"},
    "¿Cuál es el nombre del planeta rojo?": {"respuesta": "marte", "pista": "5 letras"},
    "¿Cuál es el nombre del cometa que visita la Tierra cada 76 años?": {"respuesta": "halley", "pista": "6 letras"}
}

vidas = 3  # Vidas del usuario

# Función para verificar si la respuesta del usuario es correcta
def verificar_respuesta(respuesta_correcta, respuesta_usuario):
    if respuesta_correcta == respuesta_usuario:
        print("¡Respuesta correcta!")
        return True
    else:
        print("Respuesta incorrecta.")
        for i in range(len(respuesta_correcta)):
            if i < len(respuesta_usuario):
                if respuesta_correcta[i] != respuesta_usuario[i]:
                    print(f"La letra {i+1} es incorrecta.")
            else:
                print(f"Faltó la letra {i+1}.")
        return False

# Función para jugar el primer nivel
def jugar_nivel1():
    global vidas
    for pregunta, datos in nivel1.items():
        print(f"\nPregunta: {pregunta}\nPista: {datos['pista']}")
        respuesta_correcta = datos["respuesta"]
        respuesta_usuario = ""
        while respuesta_correcta != respuesta_usuario:
            respuesta_usuario = input("Ingrese la respuesta letra por letra: ").lower()
            if verificar_respuesta(respuesta_correcta, respuesta_usuario):
                break
            else:
                vidas -= 1
                print(f"Te quedan {vidas} vidas.")
                if vidas == 0:
                    print("Perdiste. Comenzarás de nuevo desde el primer nivel.")
                    return False
    print("¡Felicitaciones! Pasas al siguiente nivel.")
    return True

import time

# Preguntas y respuestas del segundo nivel
nivel2 = {
    "¿Cuál es el nombre de la estrella más brillante en el cielo nocturno?": {"respuesta": "sirio", "pista": "5 letras"},
    "¿Cuál es el proceso mediante el cual las estrellas convierten el hidrógeno en helio?": {"respuesta": "fusion", "pista": "6 letras"},
    "¿Cómo se llaman las rocas espaciales que orbitan alrededor del espacio?": {"respuesta": "asteroides", "pista": "10 letras"},
    "¿Qué es la fuerza que mantienen a los planetas orbitando alrededor del Sol?": {"respuesta": "gravedad", "pista": "8 letras"},
    "¿Qué planeta es más grande, Júpiter o Marte?": {"respuesta": "jupiter", "pista": "7 letras"}
}

vidas = 3  # Vidas del usuario

# Función para verificar si la respuesta del usuario es correcta
def verificar_respuestaa(respuesta_correcta,respuesta_usuario):
    if respuesta_correcta == respuesta_usuario:
        print("¡Respuesta correcta!")
        return True
    else:
        print("Respuesta incorrecta.")
        for i in range(len(respuesta_correcta)):
            if i < len(respuesta_usuario):
                if respuesta_correcta[i] != respuesta_usuario[i]:
                    print(f"La letra {i+1} es incorrecta.")
            else:
                print(f"Faltó la letra {i+1}.")
        return False

# Función para jugar el segundo nivel
def jugar_nivel2():
    global vidas
    for pregunta, datos in nivel2.items():
        print(f"\nPregunta: {pregunta}\nPista: {datos['pista']}")
        respuesta_correcta = datos["respuesta"]
        respuesta_usuario = ""
        start_time = time.time()  # Tiempo de inicio
        while True:
            respuesta_usuario = input("Ingrese la respuesta letra por letra: ").lower()
            elapsed_time = time.time() - start_time  # Tiempo transcurrido
            if elapsed_time > 20:  # Si el tiempo límite se ha pasado
                print("¡Se acabó el tiempo! Comenzarás de nuevo desde el primer nivel.")
                return False
            if verificar_respuestaa(respuesta_correcta, respuesta_usuario):
                break
            else:
                vidas -= 1
                print(f"Te quedan {vidas} vidas.")
                if vidas == 0:
                    print("Perdiste. Comenzarás de nuevo desde el primer nivel.")
                    return False
    print("¡Felicitaciones! Pasas al siguiente nivel.")
    return True




# Preguntas y respuestas del tercer nivel
nivel3 = {
    "¿Cuál es la medida de la cantidad de materia de un objeto celeste?": {"respuesta": "masa"},
    "¿Cómo se llama la agrupación de estrellas, gas y polvo que se mantiene unida por la gravedad?": {"respuesta": "galaxia"},
    "¿Cuál es la teroria que sugiere que hay múltiples universos?": {"respuesta": "multiverso"},
    "¿Cómo se llama el planeta que en 2006 comenzó a ser considerado como un planeta enano?": {"respuesta": "pluton"},
    "Cuántos planetas tiene. uestro sistema solar?": {"respuesta": "Ocho"}
}

vidas = 3  # Vidas del usuario

# Función para verificar si la respuesta del usuario es correcta
def verificar_respuestaaa(respuesta_correcta, respuesta_usuario):
    if respuesta_correcta == respuesta_usuario:
        print("¡Respuesta correcta!")
        return True
    else:
        print("Respuesta incorrecta.")
        for i in range(len(respuesta_correcta)):
            if i < len(respuesta_usuario):
                if respuesta_correcta[i] != respuesta_usuario[i]:
                    print(f"La letra {i+1} es incorrecta.")
            else:
                print(f"Faltó la letra {i+1}.")
        return False

# Función para jugar el tercer nivel
def jugar_nivel3():
    global vidas
    for pregunta, datos in nivel3.items():
  
        respuesta_correcta = datos["respuesta"]
        respuesta_usuario = ""
        tiempo_inicio = time.time()
        while time.time() - tiempo_inicio < 10:
            respuesta_usuario = input("Ingrese la respuesta letra por letra: ").lower()
            if verificar_respuestaaa(respuesta_correcta, respuesta_usuario):
                break
            else:
                vidas -= 1
                print(f"Te quedan {vidas} vidas.")
                if vidas == 0:
                    print("Perdiste. Comenzarás de nuevo desde el primer nivel.")
                    return False
        else:
            print("Se acabó el tiempo. Comenzarás de nuevo desde el primer nivel.")
            return False
    print("¡Felicitaciones! Completaste el juego.")
    return True

# Loop del juego completo
while True:
    print("\n¡Bienvenido al juego de pregunta-respuesta!")
    print("Nivel 1: contesta correctamente.")
    print("Tienes 3 vidas para responder 5 preguntas.")
    input("Presiona enter para comenzar.")
    vidas = 3
    if not jugar_nivel1():
        continue
    print("Nivel 2: contesta correctamente en el tiempo establecido.")
    print("Tienes 3 vidas y límite de tiempo de 20 segundos.")
    input("Presiona enter para comenzar.")
    vidas = 3
    if not jugar_nivel2():
        continue
    print("Nivel 3: contesta correctamente en el tiempo establecido.")
    print("Tienes 3 vidas y límite de tiempo de 10 segundos.")
    input("Presiona enter para comenzar.")
    vidas = 3
    break