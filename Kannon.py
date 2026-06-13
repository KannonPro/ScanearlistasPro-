import random
import os
import time
import sys

# Colores ANSI
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
CIAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Listado de nombres latinos
nombres_base = [
    "juan", "pedro", "maria", "jose", "carlos", "luis", "ana", "diego", 
    "sofia", "miguel", "elena", "javier", "lucia", "pablo", "laura", 
    "gabriel", "valentina", "ricardo", "fernanda", "alejandro", "marta",
    "rodrigo", "ximena", "gonzalo", "claudia", "sergio", "isabel", "ramon",
    "felipe", "hugo", "mateo", "camila", "valeria", "esteban"
]

dominios = ["@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com"]

def banner():
    print(AZUL + BOLD + """
    
▄▄▄███████████████████▄▄▄▄▄──────
────▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄────
──▄██▀████████▄─────────────▀▀████─▀██▄──
─▀██▄▄██████████████████▄▄▄─────────▄██▀─
───▀█████████████████████████▄────▄██▀───
─────▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀─────
───────▀███▄──────────────▀██████▀───────
─────────▀██████▄─────────▄████▀─────────
────────────▀█████▄▄▄▄▄▄▄███▀────────────
──────────────▀████▀▀▀████▀──────────────
────────────────▀███▄███▀────────────────
───────────────────▀█▀───────────────────
       >> GENERADOR DE COMBOS PROFESIONAL | By: KANNON <<
    """ + RESET)

def indicador_progreso(actual, total):
    porcentaje = (actual / total) * 100
    barra = "█" * int(porcentaje / 5) + "-" * (20 - int(porcentaje / 5))
    sys.stdout.write(f"\r{CIAN}Generando: |{barra}| {porcentaje:.2f}% completado 🚀{RESET}")
    sys.stdout.flush()

def guardar_archivo(nombre_archivo, lista_combos):
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"
    
    ruta = "/sdcard/" + nombre_archivo
    try:
        with open(ruta, "w") as f:
            for line in lista_combos:
                f.write(line + "\n")
        print(f"\n\n{VERDE}✅ ¡Éxito! {len(lista_combos)} combos guardados en: {ruta}{RESET}")
    except PermissionError:
        print(f"\n\n{ROJO}❌ Error de permisos en SD. Guardando localmente...{RESET}")
        with open(nombre_archivo, "w") as f:
            for line in lista_combos:
                f.write(line + "\n")
        print(f"{VERDE}✅ Guardado como: {os.getcwd()}/{nombre_archivo}{RESET}")

def generar_combos():
    os.system('clear')
    banner()
    
    print(f"{AMARILLO}--- MENÚ DE OPCIONES ---{RESET}")
    print("1. User:Pass (Nombre + 4 dígitos)")
    print("2. User:Pass (Nombre + Año aleatorio)")
    print("3. User:Pass (Nombre:Nombre)")
    print("4. User:Pass (Nombre:Nombre + 3-4 dígitos)")
    print("5. User:Mail (Nombre:Mail latino)")
    print("6. Salir ❌")
    
    opcion = input(f"\n{BOLD}Selecciona una opción: {RESET}")
    
    if opcion == '6':
        print(f"{ROJO}Saliendo...{RESET}")
        return

    try:
        cantidad = int(input(f"{BOLD}¿Cuántos combos deseas generar?: {RESET}"))
        nombre_file = input(f"{BOLD}Nombre para tu archivo (ej: mis_combos): {RESET}")
    except ValueError:
        print(f"{ROJO}Entrada no válida.{RESET}")
        return

    combos = []
    print("\n") # Espacio para el indicador

    for i in range(1, cantidad + 1):
        n1 = random.choice(nombres_base)
        n2 = random.choice(nombres_base)
        
        if opcion == '1':
            num = random.randint(1000, 9999)
            combos.append(f"{n1}:{n1}{num}")
        elif opcion == '2':
            year = random.randint(1975, 2024)
            combos.append(f"{n1}:{n1}{year}")
        elif opcion == '3':
            combos.append(f"{n1}:{n2}")
        elif opcion == '4':
            num = random.randint(100, 9999)
            combos.append(f"{n1}:{n2}{num}")
        elif opcion == '5':
            mail = f"{n1}{random.randint(1,99)}{random.choice(dominios)}"
            combos.append(f"{n1}:{mail}")
        else:
            print(f"{ROJO}Opción no válida.{RESET}")
            return
        
        # Actualizar el porcentaje cada 10 combos para no ralentizar el script
        if i % 10 == 0 or i == cantidad:
            indicador_progreso(i, cantidad)

    guardar_archivo(nombre_file, combos)

if __name__ == "__main__":
    generar_combos()
