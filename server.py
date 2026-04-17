from jsonrpcserver import method, serve, Success, Error

@method
def agregar_tarea(description):
    return Success(f"Tarea '{description}' agregada exitosamente.")

@method
def completar_tarea(task_id):
    return Success(f"Tarea con ID {task_id} marcada como completada.")

@method
def ver_tareas():
    return Success("Lista de tareas devuelta exitosamente.")

if __name__ == "__main__":
    print("RPC Server listening on http://localhost:8000")
    serve(port=8000)