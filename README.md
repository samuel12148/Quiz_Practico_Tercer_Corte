# Quiz_Practico_Tercer_Corte
## Autor: Samuel Parra
## Descripción
Desarrollo del quiz propuesto en el cual se usa **MediaPipe** y **Streamlit** para detectar si una persona está **parada** o **sentada**.\
Se implementan **hilos**, **mutex**, **sección crítica** y **semaforización** para procesar video en tiempo real.

## Procedimiento
Primero creo una carpeta, en este caso la nombré Quiz_Practico\
En la consola, uso el comando:
```
cd %USERPROFILE%\Desktop\Quiz_Practico
```
Luego creo el entorno virtual
```
python -m venv venv
venv\Scripts\activate
```
Después instalo las dependencias necesarias
```
pip install streamlit mediapipe opencv-python
```
El siguiente paso es crear dentro de la carpeta el archivo de python, el cual adjunto en el repositorio\
Por último, ejecutamos
```
streamlit run quiz.py
```
Y obtengo los siguientes resultados donde se evidencia la detección de si estoy parado o sentado. :)

<img width="1437" height="971" alt="Captura de pantalla 2025-11-02 221937" src="https://github.com/user-attachments/assets/452c6a02-6bd3-44b6-862c-799f019d160c" />

<img width="1481" height="910" alt="image" src="https://github.com/user-attachments/assets/dd9ef3c5-edf8-4f23-b25e-9c87a823b5d9" />

