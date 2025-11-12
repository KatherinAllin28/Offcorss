# Reto Offcorss

## Reto 1

Para ejecutar de forma local los archivos de este reto se necesita abrir la terminal del computador, ubicarnos en la carpeta donde tenemos los ejecutables para crear y activar un entorno virtual con los siguientes comandos:

`python -m venv .venv`

`.\.venv\Scripts\activate` o `& .\.venv\Scripts\Activate.ps1`

Posteriormente a esto y cuando estemos dentro de nuestro entorno vamos a ejecutar 3 comandos:

`pip install -r requirements.txt`: Donde vamos a realizar la instalción de lo necesario para que nuestros códigos corran de la mejor manera.

`.\.venv\Scripts\python.exe .\reto1_export_synthetics.py --n 40 --out_dir ".\imagenes" --pred_dir ".\imagenes_pred"` : Donde vamos a ejecutar el reto 1 que consiste en crear un sistema para la detección automática de defectos en productos mediante visión computacional y para el cual en una de nuestras pruebas recibimos como resultado la respuesta: 
```
Generando 20 OK y 20 DEFECTO…
[0001] real=OK  pred=DEFECTO  (prob_def=0.5069)
[0002] real=OK  pred=DEFECTO  (prob_def=0.5065)
[0003] real=OK  pred=DEFECTO  (prob_def=0.5066)
[0004] real=OK  pred=DEFECTO  (prob_def=0.5071)
...
[0021] real=DEFECTO  pred=DEFECTO  (prob_def=0.5058)
[0022] real=DEFECTO  pred=DEFECTO  (prob_def=0.5068)
[0023] real=DEFECTO  pred=DEFECTO  (prob_def=0.5074)
[0024] real=DEFECTO  pred=DEFECTO  (prob_def=0.5073)
...
```
Respuesta en la cual cada resultado es una imagen simulada, el modelo de visión computacional se encarga de analizar diversos aspectos de la imagen y según lo "observado"clasifica la imagen como:

“OK” → producto sin defectos.

“DEFECTO” → detecta una irregularidad.

Para entender los resultados que nos otorga nuestro método es importante tener en cuenta que el modelo que está dentro del archivo llamado `reto1_model.pkl`se entrenó con imágenes sintéticas que son generadas y guardadas en la carpeta `imagenes` y en las subcarpetas `ok` y `defectos`, donde después de ser procesadas decide si esa imagen sin importar de que subcarpeta provenga realmente si tiene defecto o no y las agrega en una nueva carpeta llamada `imagenes_pred`, este modelo contienen texturas simples, ya que en fotos reales hay fondo, iluminación, arrugas y el modelo debido a que es algo básico (con potencial a ser mucho más grande) si recibe una foto real asume falsos positivos y arroja "defecto", ya que el modelo no "ve" colores ni estampados y las imagenes generadas son en escala de grises.

Por lo cual este es un reto que ustedes pueden implementar en líneas de producción o control de calidad para que una cámara identifique automáticamente prendas defectuosas antes de empacarlas, que al tener cámara y un mejor desarrolle tiene potencial para ser completamente funcional .

## Reto 4

`python reto4_demo.py "El inventario del SKU 1234 está bajo. Generar compra de 150 unidades."`: Este modelo es tipo un chatbot que entiende mensajes en clave administrativa o logística, al ingresar este comando en la prueba recibimos como resultado 
```
{
  "intent": "abastecimiento",
  "actions": [
    {
      "action": "crear_oc",
      "sku": 1234,
      "cantidad": 150,
      "proveedor": "ACME"
    }
  ]
}

```
donde podemos traducir o interpretar que:

"intent": "abastecimiento" → el sistema entendió que el mensaje habla de reponer inventario.

"action": "crear_oc" → decidió que debe crear una orden de compra.

"sku": 1234 → identificó el código del producto.

"cantidad": 150" → interpretó cuántas unidades reponer.

"proveedor": "ACME" → ejemplo de proveedor que el sistema asociaría automáticamente.

En la práctica, esto serviría para que un empleado escriba: “El inventario del SKU 1234 está bajo, genera compra de 150 unidades” y el agente entienda la intención, cree la orden de compra y la ingrese sin intervención humana, lo cual reduce el tiempo de trabajo y la efectividad en este ya que así como recibe este comando puede recibir otros como "Cliente 9987 solicita copia de la factura 456-2024 y estado de envío.", "Registrar pedido del cliente 887 por 30 unidades del producto 1123.", "Cliente 221 reporta prenda defectuosa en pedido 441." y "Generar reporte semanal de devoluciones y ventas online.", entre otros.
