import xml.etree.ElementTree as ET
import json

def xml_a_json_rutas(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    rutas_list = []
    for route in root.findall('route'):
        item = {
            "destino": route.find('destination').text,
            "siguiente_salto": route.find('next_hop').text,
            "protocolo": route.find('protocol').text,
            "metrica": int(route.find('metric').text)
        }
        rutas_list.append(item)

    json_normalizado = {
        "tabla_enrutamiento": {
            "total_rutas": len(rutas_list),
            "rutas": rutas_list
        }
    }
    return json.dumps(json_normalizado, indent=4)

json_resultado = xml_a_json_rutas('routing_table.xml')
print("=== TABLA DE ENRUTAMIENTO EN JSON NORMALIZADO ===")
print(json_resultado)

with open('routing_table_normalized.json', 'w') as f:
    f.write(json_resultado)

print("\n¡Archivo 'routing_table_normalized.json' generado con éxito!")