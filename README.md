# br securityheaders

### Resumen 

- **brsecurityheaders.py** Simple script to analyzed headers from a BurpSuite text-file request and based on shcheck.py code.

### Instalación

Para iniciar, siga los siguientes pasos:

1. **Clone el repositorio de GitHub :** use el siguiente comando:
   ```
   git clone https://github.com/brprodriguez/brsecurityheaders.git && cd brsecurityheaders
   ``` 
2. **Seleccion "Copy to file" en las opciones que ofrece BurpSuite:** 
   
   
   ![Seleccione "Copy to file"](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/1.png)


2. **Guarda el Request en un archivo en la misma carpeta que el script brsecurityheaders.py :**    
 
   ![Guarde el Request en la misma carpeta que el script](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/2.png)
   
3. **Comando:** python brsecurityheaders.py <BurpSuite_Requestfile_name>
   
4. **Ejpmplo:** 
   ```
   python brsecurityheaders.py requestToBeSaved.file 
	```
5. **Resultado :**    
 
   ![Resultado de ejemplo](https://raw.githubusercontent.com/brprodriguez/brsecurityheaders/main/Steps/3.png)
	
### Actualizaciones 

* 20 de Octubre del 2023: brsecurityheaders.py v1.0 

### Nuevas actualizaciones, mejoras o nuevas funcionalidades son bienvenidas

Licencia
---------------
Copyright (C) brprodriguez 

Licencia Publica GNU, version 2