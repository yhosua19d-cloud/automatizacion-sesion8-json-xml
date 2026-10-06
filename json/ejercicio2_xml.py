import xml.etree.ElementTree as ET
import os

# Ruta exacta buscando dentro de la carpeta json
xml_path = os.path.join('json', 'dispositivos.xml')

tree = ET.parse(xml_path)
root = tree.getroot()
print("Root Tag:", root.tag)

for router in root.findall('router'):
    router_id = router.attrib.get('id')
    hostname = router.find('hostname').text
    location = router.find('location').text
    
    print(f"\nRouter ID: {router_id} | Hostname: {hostname} | Ubicación: {location}")
    print("Interfaces:")
    
    for iface in router.find('interfaces').findall('interface'):
        nombre = iface.attrib.get('name')
        ip = iface.find('ip').text
        estado = iface.find('status').text
        print(f" * {nombre} -> IP: {ip} | Estado: {estado}")