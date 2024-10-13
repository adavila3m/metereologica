import requests

url = "http://192.168.0.89:8081/api/datos/"
url2 = "http://192.168.0.89:8081/api/sensor-data/"
headers = {'Content-Type': 'application/json'}
#headers = {'Content-Type': 'application/json'}
datos1 = {  'temperatura': 35.5,
            'humedad': 50,
            'presion': 1010,
            'nivel_sonido': 30.5,

}

datos2 ={   'temperature': 25.3,
            'humidity': 1012,
            
}
# Realizar solicitud POST
respuesta = requests.post(url, json=datos1, headers=headers)

# Imprimir la respuesta del servidor
print(respuesta.text)

# Cerrar conexión HTTP
respuesta.close()

print(datos2)