# DESCRIPCIÓN GENERAL DE "ADOGCIÓN"

Aplicativo web cuyo objetivo es facilitar y agilizar el reconocimiento de centros de adopción a su vez de facilitar tareas internas de estos, uniendo a la comunidad con los centros de adopción. 

## ¿COMO DESPLEGAR? (LOCAL)

Para bajar el proyecto de manera local en su maquína, debe seguir estos pasos:

1. **Clonar el repositorio**
   ```
   git clone https://github.com/WILLY192002/adogcionweb.git
   ```

2. **Configurar MySQL Workbench**

   - Abre MySQL Workbench y ejecuta los comandos que se encuentran en `Database_SQL.txt`.
     > **Nota:** Estos están divididos en 3 pasos para realizar de manera secuencial.
   - Edita la conexión a MySQL Workbench en el archivo `src/database/mysql_db.py`, actualiza el usuario y la contraseña según tu configuración. Si cambiaste el nombre de la base de datos, asegurate de cambiar en esta sección también.

3. **Crear el entorno virtual e instalar las dependencias**

   ```
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

4. **Ejecutar el proyecto**
Debes situarte en la carpeta src, posteriormente, ejecutar el archivo "index.py"
   ```
   cd src
   python index.py
   ```

¡Listo! Ahora deberías tener el proyecto corriendo en tu máquina local.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de carpetas:

- `src/`: Esta carpeta contiene el código fuente del proyecto.
    - `database/`: Contiene los archivos relacionados con la base de datos. El archivo `mysql_db.py` se utiliza para establecer la conexión con MySQL Workbench.
    - `models/`: Contiene el reflejo de las tablas en la base de datos, representadas como objetos para realizar acciones correspondientes a ese modelo y la base de datos.
    - `routes/`: Aquí se encuentran todos los endpoints del proyecto.
    - `services/`: Contiene todas las consultas a la base de datos.
    - `statics/`: Aquí se encuentran los archivos CSS y JS del proyecto.
    - `templates/`: Contiene los archivos HTML del proyecto.
    - `utils/`: Contiene funciones auxiliares que se utilizan en todo el proyecto.

## Autores

- [William Gil Clavijo](https://www.github.com/WILLY192002)
- [Jhoan Andres Diaz Castaño](https://www.github.com/JDiazc0)

---


# DESCRIPTION

Web application whose objective is to facilitate and expedite the recognition of adoption centers as well as to facilitate their internal tasks, linking the community with the adoption centers. 
 

 
# HOW TO DEPLOY (LOCAL)
To download the project locally on your machine, follow these steps:
1. **Clone the repository**
   ```
   git clone https://github.com/WILLY192002/adogcionweb.git
   ```
2. **ConfigureMySQL Workbench** **Setup MySQLWorkbench**
   - Open MySQL Workbench and execute the commands found in `Database_SQL.txt`. Note: These are divided into 3 steps to be performed sequentially.
   - Edit the MySQL Workbench connection in the `src/database/mysql_db.py` file, update the username and password according to your configuration. If you changed the database name, be sure to change it in this section as well.
3. **Createthe virtual environment and install the dependencies**.
   ```
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
4. **Runthe project**
You must go to the src folder, then run the file "index.py".
   ```
   cd src
   python index.py
   ```
That's it! You should now have the project running on your local machine.

## Project Structure

The project has the following folder structure:

- `src/`: This folder contains the source code of the project.
    - `database/`: Contains files related to the database. The `mysql_db.py` file is used to establish the connection with MySQL Workbench.
    - `models/`: Contains the reflection of the tables in the database, represented as objects to perform actions corresponding to that model and the database.
    - `routes/`: Here you can find all the endpoints of the project.
    - `services/`: Contains all the database queries.
    - `statics/`: Here you can find the CSS and JS files of the project.
    - `templates/`: Contains the HTML files of the project.
    - `utils/`: Contains auxiliary functions that are used throughout the project.


## Authors

- [William Gil Clavijo](https://www.github.com/WILLY192002)
- [Jhoan Andres Diaz Castaño](https://www.github.com/JDiazc0)
