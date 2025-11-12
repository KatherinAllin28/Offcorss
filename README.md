# Reto Offcorss

## Reto 1

Para ejecutar de forma local los archivos de este reto se necesita abrir la terminal del computador, ubicarnos en la carpeta donde tenemos los ejecutables para crear y activar un entorno virtual con los siguientes comandos:

`python -m venv .venv`

`.\.venv\Scripts\activate` o `& .\.venv\Scripts\Activate.ps1`

Posteriormente a esto y cuando estemos dentro de nuestro entorno vamos a ejecutar los siguientes comandos:

`pip install -r requirements.txt`: Donde vamos a realizar la instalación de lo necesario para que nuestros códigos corran de la mejor manera.

`.\.venv\Scripts\python.exe .\reto1_demo.py`: Donde vamos a ejecutar el reto 1 que consiste en crear un sistema para la detección automática de defectos en productos mediante visión computacional y para el cual en una de nuestras pruebas recibimos como resultado la respuesta: 
```
Cargando modelo: reto1_model.pkl
Generando 40 muestras sintéticas...
[001] real=DEFECTO
[002] real=DEFECTO
[003] real=DEFECTO
[004] real=DEFECTO
[005] real=OK
[006] real=OK
[007] real=DEFECTO
[008] real=DEFECTO
[009] real=OK
[010] real=OK
...

Total muestras: 40
Imágenes guardadas en: C:XXXX\imagenes_generadas
CSV con resultados: C:XXXX\resultados_reto1.csv
```
Respuesta en la cual cada resultado es una imagen que fue creada por el sistema, el modelo de visión computacional se encarga de analizar la imagen y según lo "observado"clasifica la imagen como:

“OK” → producto sin defectos.

“DEFECTO” → detecta una irregularidad.

Para entender los resultados que nos otorga nuestro método es importante tener en cuenta que el modelo que está dentro del archivo llamado `reto1_model.pkl`se entrenó con imágenes sintéticas que son generadas y guardadas en la carpeta `imagenes_generadas`, donde después de ser procesadas decide si esa imagen realmente si tiene defecto o no, este modelo contienen texturas simples, ya que en fotos reales hay fondo, iluminación, arrugas, siluetas o demás y el modelo debido a que es algo básico (con potencial a ser mucho más grande) si recibe una foto real de una prenda asumirá falsos positivos porque no está entrenado con eso y arroja "defecto", ya que el modelo no "ve" colores ni estampados y las imagenes generadas son en escala de grises, donde un solo tono de gris representa una prenda perfecta y alguna mancha de otro tono gris en la imagen representa un imperfecto en la prenda.

Por lo cual este es un reto que ustedes pueden implementar en líneas de producción o control de calidad para que una cámara identifique automáticamente prendas defectuosas antes de empacarlas, que al tener cámara y un mejor desarrolle tiene potencial para ser completamente funcional .

### Nota
Por defecto al ejecutar este reto hace la prueba con 40 imagenes, si queremos una simulación con un número mayor o menor debemos ejecutar `.\.venv\Scripts\python.exe .\reto1_demo.py --samples 200` donde el 200 se debe reemplazar con el número que deseamos
## Reto 4

`python reto4_demo.py --comando "Registrar pedido del cliente 887 por 30 unidades del producto 1123."`: Este modelo es tipo un chatbot que entiende mensajes en clave administrativa o logística, al ingresar este comando en la prueba recibimos como resultado 
```
Comando recibido: Registrar pedido del cliente 887 por 30 unidades del producto 1123.

Resultado: Pedido registrado: Cliente 887, 30 unidades del producto 1123.
Área responsable: Comercial | Tipo de acción: ventas
Ejecutado el 12/11/2025 00:36:09
```
En la práctica, esto serviría para que un empleado escriba: “Registrar pedido del cliente 887 por 30 unidades del producto 1123” y el agente entienda la intención, cree la orden de compra y la ingrese sin intervención humana, lo cual reduce el tiempo de trabajo y la efectividad en este ya que así como recibe este comando puede recibir otros como "El inventario del SKU 1234 está bajo. Generar compra de 150 unidades."y "Cliente 9987 solicita copia de la factura 456-2024 y estado de envío.", entre otros.
