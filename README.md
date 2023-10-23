# br securityheaders

### Resumen 

- **brsecurityheaders.py** 
Es un script simple que permite analizar las cabeceras HTTP configuradas en la aplicación. Recibe como imput un archivo de texto de BurpSuite (Burpsuite Text-File Request) 

### Pre-Requisitos

Es necesario obtener el request text file de BurpSuite

### Instalación

Para iniciar, siga los siguientes pasos:

1. **Clone el repositorio de GitHub :** use el siguiente comando:
   ```
   git clone https://github.com/brprodriguez/brsecurityheaders.git && cd brsecurityheaders
   ``` 
2. **En Burp Suite seleccione la opción "Copy to file":** 
      
   ![Seleccione "Copy to file"](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/1.png)

2. **Guarde el Request en un archivo en la misma carpeta que el script brsecurityheaders.py :**    
 
   ![Guarde el Request en la misma carpeta que el script](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/2.png)
   
3. **Ejecute el comando:** python brsecurityheaders.py <BurpSuite_Requestfile_name>
   
4. **Ejemplo:** 
   ```
   python brsecurityheaders.py requestToBeSaved.file 
	```
5. **Resultado :**    
 
   ![Resultado de ejemplo](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/3.png)
	
### Actualizaciones 

* 20 de Octubre del 2023: brsecurityheaders.py v1.0 

### Mejoras o nuevas funcionalidades son bienvenidas

Licencia
---------------
Copyright (C) brprodriguez 

Licencia Publica GNU, version 2