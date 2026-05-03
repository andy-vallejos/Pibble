# libreria-python

## Instalacion

git clone <https://github.com/andy-vallejos/libreria-python.git>

## Cambiar rama

Recuerden cambiar su rama de trabajo

```
    git switch -c "aqui-ponen-el-nombre-de-su-rama"
```

## Entorno virtual

Recuerden crear su entorno virtual

```
    python -m venv .venv
```

## Instalar dependencias

Recuerden instalar dependencias:

```
    pip install -r requirements.txt
```

Recuerden agregar las librerias que usen en el requirements.txt para poder ejecutar el comando anterior.

## Ejecutar pruebas

Para ejecutar las pruebas deben estar en el repositorio raiz y ejecutar lo siguiente:

```
     pytest
     python -m pytest  #por si les da un error (aveces pasa porque el pytest lo instalan en sus sistema y trata de usar ese en lugar del de .venv)
```

## API_KEY

<https://aistudio.google.com/app/api-keys?hl=es-419&project=gen-lang-client-0705034784>
De este url se crean una API_KEY para el tema de la ia

Recuerden crearse un archivo .env y ahi colocar esa key de la manera que se muestra en el .env.example
