tareas = [
    "Revisar correos",
    "Preparar informe", 
    "Estudiar MCP"
]

def agregar_tarea_service(descripcion):
    tareas.append(descripcion)
    return f"Tarea agregada: {descripcion}"

def completar_tarea_service(indice):
    try:
        if indice < 1 or indice > len(tareas):
            return "Índice inválido"
        
        tarea_completada = tareas[indice - 1]
        
        del tareas[indice - 1]
        
        return f"Tarea completada: {tarea_completada}"
    except (IndexError, TypeError):
        return "Índice inválido"

def ver_tareas_service():
    if not tareas:
        return "No hay tareas pendientes"
    
    lista_numerada = []
    for i, tarea in enumerate(tareas, 1):
        lista_numerada.append(f"{i}. {tarea}")
    
    resultado = "\n".join(lista_numerada)
    return resultado

def obtener_estado_inicial():
    estado = []
    for i, tarea in enumerate(tareas, 1):
        estado.append(f"{i}. {tarea}")
    return "\n".join(estado)