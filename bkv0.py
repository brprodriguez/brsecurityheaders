import sys
import requests
import urllib3
from colorama import Fore, Style

urllib3.disable_warnings()

if len(sys.argv) != 2:
    print("Uso: python brsecurityheader.py <nombre_de_archivo>")
else:
    nombre_de_archivo = sys.argv[1]


# Nombre del archivo que contiene la solicitud HTTP en formato de texto
archivo_solicitud = nombre_de_archivo

# Leer el archivo línea por línea
with open(archivo_solicitud, 'r') as archivo:
    solicitud = archivo.read()

# Dividir la solicitud en las partes necesarias
partes = solicitud.split('\n\n')  # Separa la solicitud en el encabezado y el cuerpo
#print(partes)
#print("===")
lineas_encabezado = partes[0].split('\n')  # Divide el encabezado en líneas
#print(lineas_encabezado)
#print("===")
lineas_cuerpo = partes[1]
#print(lineas_cuerpo)
#print("===")

# Parsear el método, la ruta y la versión HTTP
primera_linea = lineas_encabezado[0]
metodo, ruta, version_http = primera_linea.split()

# Parsear los encabezados
encabezados = {}
for linea in lineas_encabezado[1:]:
    dupla = linea.split(': ', 1)
    if (len(dupla)==2):
        key, value = dupla[0],dupla[1]
        encabezados[key] = value
    else:
        key = dupla[0]
        value = None
        encabezados[key] = value
    

# Construir la URL completa
url = "https://" + encabezados['Host'] + ruta

# Imprimir la solicitud HTTP
print(f"Request:\n\n{metodo} {ruta} HTTP/{version_http}")
for clave, valor in encabezados.items():
    print(f"{clave}: {valor}")
# Realizar la solicitud HTTP
print(lineas_cuerpo)
    
if (metodo == "GET"):
    response = requests.get(url, headers=encabezados, verify=False)
if (metodo == "POST"): 
    response = requests.post(url, headers=encabezados, data = lineas_cuerpo.encode('utf-8'), verify=False)

# Verificar si la solicitud fue exitosa
if response.status_code >= 200:
    print("\nResponse Headers:\n")
    print(f"HTTP Code: {response.status_code}")
    #print(response.headers)
    for k,v in response.headers.items():
    	print(f'{k} : {v}')
else:
    print(f"La solicitud falló con el código de estado: {response.status_code}")
    exit(0)

#
security_headers = [
    "X-XSS-Protection",
    "X-Frame-Options", 
    "X-Content-Type-Options", 
    "Strict-Transport-Security", 
    "Content-Security-Policy", 
    "Referrer-Policy", 
    "Permissions-Policy",
    "Cross-Origin-Resource-Policy", 
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Embedder-Policy"
]


def search_header(header,response_headers):
    for key,value in response_headers:
        if header.upper() == key.upper():
            return key,value
    return None, None 

print("\nHeaders analyzed for: ",end="")
print(Fore.BLUE + url + Style.RESET_ALL)
for security_header in security_headers:
    key,value = search_header(security_header,response.headers.items()) 
    if key is not None:
        print("Header: ",end="")
        print(Fore.LIGHTGREEN_EX + key + Style.RESET_ALL, end="")
        print( " is present! Value: " + value)
    else:
        print("Missing security header: ",end="")
        print(Fore.YELLOW + security_header + Style.RESET_ALL)
exit(0)

