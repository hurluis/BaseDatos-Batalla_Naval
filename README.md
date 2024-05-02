# Documentación del Juego de Batalla Naval

## Descripción
Este proyecto consiste en la implementación de un juego de batalla naval en Python. El juego permite a un jugador intentar hundir todos los barcos en un tablero de tamaño NxM utilizando coordenadas de disparo. O por medio de click a botones si usamos la interfaz grafica de kivy.

## Requisitos del Sistema
- Tener Python Instalado
- Tener Kivy instalado

## Instrucciones de Instalación
1. Copie el enlace HTTPS del github: "https://github.com/hurluis/tabrajoavaznce.git".
2. Abre una terminal (preferiblemente git bash) y clona el repositorio usando: `git clone https://github.com/hurluis/tabrajoavaznce.git` .
3. Cambia/parate al repositorio usando: `cd tabrajoavaznce`.
4. Cambia/parate a la carpeta src usando: `cd src`.

### Interfaz grafica

1. Cambia al directorio de interfaz usando: `cd GUI` .
2. Ejectuta el archivo usando: `py interfaz.py` .
3. Si deseas devolverte usa: `cd ..`

### Consola

1. Cambia al directorio de consola usando: `cd consoleTTY` .
2. Ejectuta el archivo usando: `py jugar_consola.py` .
3. Si deseas devolverte usa: `cd ..`

## Estructura del Código
El código está organizado en cuatro archivos principales:
- `crear_tablero_logica.py`: Contiene la lógica para crear el tablero de juego.
- `disparar_logica.py`: Contiene la lógica para realizar disparos en el juego.
- `jugar_consola.py`: El punto de entrada del juego que gestiona la interacción con el usuario.
- `interfaz.py`: El punto de entrada del juego que gestiona la interfaz grafica.

## Descripción de las Funciones Principales
### Funcion crear tablero
Esta es la funcionalidad que recibe los datos del tablero y los crea haciendo uso de la clase "TableroBarcos".

### Funcion disparar
Esta es la funcionalidad que recibe las Coordenadas del disparo y nos confirma si disparamos a un barco o si fallamos, usando la clase "Disparar".


## Ejemplos de Uso
1. Sigue las instrucciones de instalacion
2. Una vez ejecutado entregas los datos que te pide el juego
3. Entregas las coordenadas donde crees que hay un barco o seleccionas el lugar donde crees que hay un barco y asi sucesivamente hasta que logres hallar y destruir todos los barcos.
4. Puedes volver a ejecutar el archivo para volver a jugar! :D