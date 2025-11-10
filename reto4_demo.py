#!/usr/bin/env python3
"""
Reto 4 – Demo de agente: clasificador de intenciones + orquestador.
Uso:
  python reto4_demo.py "texto de solicitud"
"""
import sys, json, pickle, re
from pathlib import Path

def load_model():
    path = Path(__file__).parent / "reto4_agent_model.pkl"
    if not path.exists():
        raise FileNotFoundError("Falta reto4_agent_model.pkl en la carpeta")
    return pickle.loads(path.read_bytes())

def agent_orchestrator(text):
    clf = load_model()
    intent = clf.predict([text])[0]
    actions = []
    if intent == "abastecimiento":
        m_sku = re.search(r"SKU\s*(\d+)", text)
        m_qty = re.search(r"(\d+)\s*unidades", text)
        sku = int(m_sku.group(1)) if m_sku else 1234
        qty = int(m_qty.group(1)) if m_qty else 100
        actions.append({"action":"crear_oc","sku":sku,"cantidad":qty,"proveedor":"ACME"})
    elif intent == "atencion_cliente":
        actions.append({"action":"enviar_respuesta","plantilla":"copia_factura_y_tracking"})
    elif intent == "finanzas":
        actions.append({"action":"abrir_incidente","tipo":"arqueo_caja"})
    elif intent == "rrhh":
        actions.append({"action":"enviar_a_aprobacion","flujo":"vacaciones"})
    elif intent == "analytics":
        actions.append({"action":"crear_analisis_ventas","periodo":"7d","sede":"Laureles"})
    return {"intent": intent, "actions": actions}

def main():
    args = sys.argv[1:]
    if args:
        print(json.dumps(agent_orchestrator(" ".join(args)), ensure_ascii=False, indent=2))
    else:
        demos = [
            "El inventario del SKU 1234 está bajo. Generar compra de 150 unidades.",
            "Cliente 9987 solicita copia de la factura 456-2024 y estado de envío."
        ]
        for t in demos:
            print("Entrada:", t)
            print(json.dumps(agent_orchestrator(t), ensure_ascii=False, indent=2), "\n")

if __name__ == "__main__":
    main()
