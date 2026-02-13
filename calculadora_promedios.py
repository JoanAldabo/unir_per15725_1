SUSPENDIDAS = 0
APROBADAS = 1

VALOR_NOTA = 0
INDICE_NOTA = 1


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def ingresar_calificaciones():
    ingresar_nombre = True
    ingresar_calificacion = True
    seguir_pidiendo = 's'
    materias = []
    calificaciones = []
    while seguir_pidiendo == 's':
        error_pidiendo = True
        while ingresar_nombre:
            nombre = input("Ingrese el nombre de la materia: ").strip()
            ingresar_nombre = nombre == ""
            if ingresar_nombre:
                print("El nombre no puede estar vacío")
        while ingresar_calificacion:
            calificacion = input("Ingrese la calificación (0 a 10)").strip()
            ingresar_calificacion = True  # asumimos inválida hasta validar
            if not isFloat(calificacion):
                print("La calificación debe ser un número decimal entre 0 y 10")
            else:
                valor = float(calificacion)
                ingresar_calificacion = valor < 0 or valor > 10
                if ingresar_calificacion:
                    print("La calificación debe ser un número decimal "
                          "entre 0 y 10")
        materias.append(nombre)
        calificaciones.append(float(calificacion))
        while error_pidiendo:
            seguir_pidiendo = \
                input("¿Desea ingresar otra materia? (S/n): ").lower().strip()
            seguir_pidiendo = seguir_pidiendo if seguir_pidiendo != '' else 's'
            error_pidiendo = seguir_pidiendo not in ['s', 'n']
            if error_pidiendo:
                print("La respuesta debe ser S o N")
        ingresar_nombre = True
        ingresar_calificacion = True
    return materias, calificaciones

def calcular_promedio(calificaciones):
    try:
        return sum(calificaciones) / len(calificaciones)
    except ZeroDivisionError:
        return None

def determinar_estado(calificaciones, umbral=5.0):
    estado = [[], []]
    for index, calificacion in enumerate(calificaciones):
        estado[calificacion >= umbral].append(index)
    return estado[APROBADAS], estado[SUSPENDIDAS]

def encontrar_extremos(calificaciones):
    if len(calificaciones) == 0:
        return None, None

    max_value = (calificaciones[0], 0)
    min_value = (calificaciones[0], 0)

    for index, calificacion in enumerate(calificaciones):
        if calificacion > max_value[VALOR_NOTA]:
            max_value = (calificacion, index)
        if calificacion < min_value[VALOR_NOTA]:
            min_value = (calificacion, index)

    return max_value[INDICE_NOTA], min_value[INDICE_NOTA]

def main():
    materias, calificaciones = ingresar_calificaciones()

    print("\n=== Resumen Final ===")

    if len(materias) == 0:
        print("No se ingresó ninguna materia. No hay datos para procesar.")
    else:
        print("\n- Materias y calificaciones:")
        for nombre, nota in zip(materias, calificaciones):
            print("\t- {}: {:.2f}".format(nombre, nota))
        promedio = calcular_promedio(calificaciones)
        if promedio is None:
            print("\n- Promedio general: No hay datos")
        else:
            print("\n- Promedio general: {:.2f}".format(promedio))
        aprobadas_idx, suspendidas_idx = determinar_estado(calificaciones, 5.0)
        print("\n- Materias aprobadas (>= 5.0):")
        if len(aprobadas_idx) == 0:
            print("\t- Ninguna")
        else:
            for i in aprobadas_idx:
                print("\t- {}: {:.2f}".format(materias[i],
                                              calificaciones[i]))
        print("\n- Materias suspendidas (< 5.0):")
        if len(suspendidas_idx) == 0:
            print("\t- Ninguna")
        else:
            for i in suspendidas_idx:
                print("\t- {}: {:.2f}".format(materias[i],
                                              calificaciones[i]))
        idx_max, idx_min = encontrar_extremos(calificaciones)
        if idx_max is not None and idx_min is not None:
            print("\n- Mejor calificación: {} ({:.2f})".format(
                materias[idx_max], calificaciones[idx_max]
            ))
            print("\n- Peor calificación: {} ({:.2f})".format(
                materias[idx_min], calificaciones[idx_min]
            ))
    print("\n\n¡Gracias por usar la calculadora de promedios! ¡Hasta luego!")


if __name__ == "__main__":
    main()