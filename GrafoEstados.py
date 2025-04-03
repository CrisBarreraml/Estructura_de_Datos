def resolver_problema_estados_sin_librerias():
    """Resuelve el problema de recorrido de estados mexicanos usando grafos, sin librerías externas."""

    estados = ["CDMX", "Morelos", "Puebla", "Veracruz", "Oaxaca", "Guerrero", "Michoacán"]
    relaciones = {
        ("CDMX", "Morelos"): 80,
        ("CDMX", "Puebla"): 130,
        ("Morelos", "Puebla"): 90,
        ("Morelos", "Guerrero"): 250,
        ("Puebla", "Veracruz"): 280,
        ("Puebla", "Oaxaca"): 350,
        ("Veracruz", "Oaxaca"): 200,
        ("Oaxaca", "Guerrero"): 400,
        ("Guerrero", "Michoacán"): 380,
        ("Michoacán", "CDMX"): 300,
    }

    print("Estados:")
    print(estados)
    print("\nRelaciones (Estado1, Estado2, Costo):")
    for (u, v), peso in relaciones.items():
        print(f"{u} - {v}: {peso}")

    print("\nRecorrido sin repeticiones (aproximación):")
    camino_sin_repeticiones = buscar_camino_hamiltoniano(estados, relaciones)
    if camino_sin_repeticiones:
        costo_sin_repeticiones = calcular_costo_camino(camino_sin_repeticiones, relaciones)
        print(" -> ".join(camino_sin_repeticiones))
        print(f"Costo total: {costo_sin_repeticiones}")
    else:
        print("No se encontró un camino sin repeticiones (aproximación simple).")

    print("\nRecorrido con repeticiones (aproximación):")
    camino_con_repeticiones = buscar_ciclo_euleriano_aproximado(estados, relaciones)
    if camino_con_repeticiones:
        costo_con_repeticiones = calcular_costo_camino(camino_con_repeticiones, relaciones, ciclo=True)
        print(" -> ".join(camino_con_repeticiones))
        print(f"Costo total: {costo_con_repeticiones}")
    else:
        print("No se encontró un camino con repeticiones (aproximación simple).")

def buscar_camino_hamiltoniano(estados, relaciones):
    """Busca un camino hamiltoniano aproximado."""
    camino = [estados[0]]
    estados_restantes = estados[1:]
    while estados_restantes:
        ultimo_estado = camino[-1]
        mejor_estado_siguiente = None
        mejor_costo = float('inf')
        for estado_siguiente in estados_restantes:
            if (ultimo_estado, estado_siguiente) in relaciones:
                costo = relaciones[(ultimo_estado, estado_siguiente)]
                if costo < mejor_costo:
                    mejor_costo = costo
                    mejor_estado_siguiente = estado_siguiente
        if mejor_estado_siguiente:
            camino.append(mejor_estado_siguiente)
            estados_restantes.remove(mejor_estado_siguiente)
        else:
            return None  
    return camino

def buscar_ciclo_euleriano_aproximado(estados, relaciones):
    """Busca un ciclo euleriano aproximado."""
    camino = buscar_camino_hamiltoniano(estados, relaciones)
    if camino:
        camino.append(camino[0])  
        return camino
    else:
        return None

def calcular_costo_camino(camino, relaciones, ciclo=False):
    """Calcula el costo total de un camino."""
    costo_total = 0
    for i in range(len(camino) - 1):
        u, v = camino[i], camino[i + 1]
        if (u, v) in relaciones:
            costo_total += relaciones[(u, v)]
        elif (v,u) in relaciones:
          costo_total += relaciones[(v,u)]
        else:
            return float('inf')  
    if ciclo and camino:
      u, v = camino[-1], camino[0]
      if (u,v) in relaciones:
        costo_total += relaciones[(u,v)]
      elif (v,u) in relaciones:
        costo_total += relaciones[(v,u)]
      else:
        return float('inf')

    return costo_total

resolver_problema_estados_sin_librerias()