from src.ia import inicializar, generar_respuesta
from src.audio import run

[cliente, modelo] = inicializar()

print(generar_respuesta(cliente, modelo, "Hola"))
