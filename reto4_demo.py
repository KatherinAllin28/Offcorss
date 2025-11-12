import argparse
import re
import datetime
import warnings
warnings.filterwarnings("ignore")

def ejecutar_modelo_original():
    print("Ejecutando lógica base del Reto 4...")
    pass


def interpretar_comando(texto):
    texto = texto.lower()

    if "inventario" in texto and ("compra" in texto or "reabastecer" in texto):
        return {
            "intencion": "inventario",
            "area": "Logística",
            "accion": "generar_orden_compra"
        }
    elif "registrar pedido" in texto or "nuevo pedido" in texto:
        return {
            "intencion": "ventas",
            "area": "Comercial",
            "accion": "registrar_pedido"
        }
    elif "factura" in texto or "estado de envío" in texto:
        return {
            "intencion": "facturacion",
            "area": "Finanzas",
            "accion": "consultar_factura"
        }
    elif "defectuosa" in texto or "devolución" in texto:
        return {
            "intencion": "postventa",
            "area": "Atención al Cliente",
            "accion": "registrar_devolucion"
        }
    elif "reporte" in texto:
        return {
            "intencion": "reportes",
            "area": "Dirección General",
            "accion": "generar_reporte"
        }
    else:
        return {
            "intencion": "desconocida",
            "area": "No definida",
            "accion": "No identificada"
        }


def procesar_comando(texto):
    info = interpretar_comando(texto)
    tipo = info["accion"]
    area = info["area"]
    intencion = info["intencion"]

    if tipo == "generar_orden_compra":
        sku = re.search(r"sku\s*(\d+)", texto)
        cantidad = re.search(r"(\d+)\s*unidades", texto)
        sku = sku.group(1) if sku else "N/A"
        cantidad = int(cantidad.group(1)) if cantidad else 0
        respuesta = f"Orden de compra generada: SKU {sku} por {cantidad} unidades."
        dependencia = f"Área responsable: {area} | Tipo de acción: {intencion}"

    elif tipo == "registrar_pedido":
        cliente = re.search(r"cliente\s*(\d+)", texto)
        producto = re.search(r"producto\s*(\d+)", texto)
        cantidad = re.search(r"(\d+)\s*unidades", texto)
        cliente = cliente.group(1) if cliente else "N/A"
        producto = producto.group(1) if producto else "N/A"
        cantidad = int(cantidad.group(1)) if cantidad else 0
        respuesta = f"Pedido registrado: Cliente {cliente}, {cantidad} unidades del producto {producto}."
        dependencia = f"Área responsable: {area} | Tipo de acción: {intencion}"

    elif tipo == "consultar_factura":
        cliente = re.search(r"cliente\s*(\d+)", texto)
        factura = re.search(r"factura\s*([0-9\-]+)", texto)
        cliente = cliente.group(1) if cliente else "N/A"
        factura = factura.group(1) if factura else "N/A"
        respuesta = f"Factura {factura} del cliente {cliente}: enviada y en tránsito."
        dependencia = f"Área responsable: {area} | Tipo de acción: {intencion}"

    elif tipo == "registrar_devolucion":
        cliente = re.search(r"cliente\s*(\d+)", texto)
        pedido = re.search(r"pedido\s*(\d+)", texto)
        cliente = cliente.group(1) if cliente else "N/A"
        pedido = pedido.group(1) if pedido else "N/A"
        respuesta = f"Devolución registrada para el pedido {pedido} del cliente {cliente}."
        dependencia = f"Área responsable: {area} | Tipo de acción: {intencion}"

    elif tipo == "generar_reporte":
        periodo = "semanal" if "semanal" in texto else "mensual"
        respuesta = f"Reporte {periodo} de devoluciones y ventas online generado exitosamente."
        dependencia = f"Área responsable: {area} | Tipo de acción: {intencion}"

    else:
        respuesta = "No se pudo interpretar el comando."
        dependencia = f"Área responsable: {area} | Tipo de acción: {intencion}"

    return respuesta, dependencia


def main():
    parser = argparse.ArgumentParser(description="Reto 4 - Agente inteligente con áreas responsables")
    parser.add_argument("--comando", type=str, help="Texto del comando natural a procesar")
    args = parser.parse_args()

    if args.comando:
        print(f"\nComando recibido: {args.comando}")
        resultado, dependencia = procesar_comando(args.comando)
        print(f"\nResultado: {resultado}")
        print(f"{dependencia}")
        print(f"Ejecutado el {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Modo normal del Reto 4 (sin comando natural)\n")
        ejecutar_modelo_original()


if __name__ == "__main__":
    main()
