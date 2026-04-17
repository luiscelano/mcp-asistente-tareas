from jsonrpcserver import method, serve, Success, Error
from services import agregar_tarea_service, completar_tarea_service, ver_tareas_service, obtener_estado_inicial

@method
def agregar_tarea(descripcion):
    resultado = agregar_tarea_service(descripcion)
    return Success(resultado)

@method
def completar_tarea(indice):
    resultado = completar_tarea_service(indice)
    return Success(resultado)

@method
def tareas_pendientes():
    resultado = ver_tareas_service()
    return Success(resultado)

if __name__ == "__main__":
    print("JSON-RPC server listening on http://localhost:8000")
    print("Initial state:")
    print(obtener_estado_inicial())
    serve(port=8000)