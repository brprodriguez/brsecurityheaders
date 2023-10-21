# br securityheaders

### Resumen 

- **brsecurityheaders.py** Simple script to analyzed headers from a text-file request from BurpSuite and based on shcheck.py code.

### Instalación

Para iniciar, siga los siguientes pasos:

1. **Clone el repositorio de GitHub :** use el siguiente comando:
   ```
   git clone https://github.com/brprodriguez/brsecurityheaders.git
   ``` 
2. **Guarda el Request en un archivo de texto :** 
   
   
   ![uarde el Request de BurpSuite en un archivo de texto](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/1.png)


   
 
 
   
2. **Comando de ejemplo :**: python brsecurityheaders.py <requestfile>
   ```
   python brsecurityheaders.py
	```

### Opciones

```
Comando: gencard.py [-m MODO] [-c CANT] [Opciones]

Opciones:  
  -h, --help            Muestra un mensaje de ayuda 

  Obligatorio:
    -m           (Obligatorio) MODO : AT -> Aleatorio Full Mutiples BIN, S -> Secuencial, A1 -> Aleatorio Simple 1 BIN 
    -c           (Obligatorio) CANT : Cantidad de tarjetas a generar 
    -b           (Opcional)    BIN : Identificador del Banco 
    -f           (Opcional)    FILE PATH BANK : Ruta del archivo con información 
	                        pública de Bancos. Por defecto se usa 
				el archivo ./binfiles/binar.csv
```
