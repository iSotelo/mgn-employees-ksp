# Prueba para KSP

<p align="center">
    <em> Web service para la gestion de empleados</em>
    <br />
    <em> Aplicación web ReacjJS para la gestión por GUI</em>
</p>

---
### employees_management => FRONTEND REACJS

### employees_service => BACKEND WEB SERVICES FASTAPI python

---
## Requisitos previos

- Docker desktop
- docker-compose
- node y npx
- SO Windows / Linux

--- 
## Construcción y arranque:

1. Instalar docker desktop y asegurarse de tener corriendo el daemon.

2. Configurar las variables de la base de datos, por defecto estas se ecnuentran configuradas apuntando a un RDS de Postgre en AWS, ver el archivo .env en la raiz del repositorio

3. En la carpeta donde se clono el repositorio ejecutar los siguientes comandos:

        docker-compose down
        docker-compose build
        docker-compose up -d

    Asegurese que los servicios estan corriendo con el comando: 
    
        docker ps -a

4. Ingresar a la documentación de la web api en el path: 

    http://localhost:8000/docs

5. Para acceder a la aplicación web, puede ingresar en la dirección:

    http://localhost:3000


## NOTA: la ejecución del servidor web desde docker tardara algunos minutos, puede verificarlo mostrando los logs de docker con el comando siguiente:

    docker ps -a                        => Para obtener el ID del contenedor de employees_management
    docker logs -f [CONTAINER_ID]       => Para mostrat los logs del contenedor

La aplicación estara corriendo cuando los ultimos sean com sigue:

    Starting the development server...
    Compiled successfully!
    You can now view employees_management in the browser.
    Local:            http://localhost:3000
    On Your Network:  http://172.27.0.4:3000
    Note that the development build is not optimized.
    To create a production build, use npm run build.
    webpack compiled successfully


## Alternativa para ejecutar la aplicación web por separado

> Puede acceder dentro del repositorio en la carpeta employees_management

> instale la dependencias con el comando:

    npm install
    
> inicie la aplicación con el comando:

    npm start

