# Reto Offcorss

Para ejecutar de forma local los archivos de este reto se necesita abrir la terminal del computador, ubicarnos en la carpeta donde tenemos los ejecutables para crear y activar un entorno virtual con los siguientes comandos:

`python -m venv .venv`

`.\.venv\Scripts\activate` o `& .\.venv\Scripts\Activate.ps1`

Posteriormente a esto y cuando estemos dentro de nuestro entorno vamos a ejecutar 3 comandos:

`pip install -r requirements.txt`: Donde vamos a realizar la instalción de lo necesario para que nuestros códigos corran de la mejor manera.

`python reto1_demo.py --samples 6`: Donde vamos a ejecutar el reto 1 que consiste en crear un sistema para la detección automática de defectos en productos mediante visión computacional y para el cual en una de nuestras pruebas recibimos como resultado la respuesta: 
```
Generando muestras sintéticas y evaluando...
Muestra 1: DEFECTO
Muestra 2: DEFECTO
Muestra 3: DEFECTO
Muestra 4: DEFECTO
Muestra 5: OK
Muestra 6: DEFECTO
```
respuesta en la cual cada “muestra” es una imagen simulada de un producto ya que no tenemos como mostrar los productos reales para este reto, el modelo de visión computacional se encarga de analizar diversos aspectos de la imagen y según lo "observado"clasifica la imagen como:
“OK” → producto sin defectos.
“DEFECTO” → detecta una irregularidad que puede ser mancha, costura anómala, color mal aplicado, etc.
Por lo cual este es un reto que ustedes pueden implementar en líneas de producción o control de calidad para que una cámara identifique automáticamente prendas defectuosas antes de empaquetarlas.

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

En la práctica, esto serviría para que un empleado escriba: “El inventario del SKU 1234 está bajo, genera compra de 150 unidades” y el agente entienda la intención, cree la orden de compra y la ingrese sin intervención humana, lo cual reduce el tiempo de trabajo y la efectividad en este ya que así como recibe este comando puede recibir otros como `.\.venv\Scripts\python.exe reto4_demo.py "Cliente 9987 solicita copia de la factura 456-2024 y estado de envío."`, entre otros.
