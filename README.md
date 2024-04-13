# DESCRIPCIÓN GENERAL DE "ADOGCIÓN"

Aplicativo web cuyo objetivo es facilitar y agilizar el reconocimiento de centros de adopción a su vez de facilitar tareas internas de estos, uniendo a la comunidad con los centros de adopción. 

## ¿COMO DESPLEGAR? (LOCAL)

Para bajar el proyecto de manera local en su maquína, debe seguir estos pasos:

1. **Clonar el repositorio**
   ```
   git clone https://github.com/WILLY192002/adogcionweb.git
   ```

2. **Configurar MySQL Workbench**

   - Abre MySQL Workbench y ejecuta los comandos que se encuentran en `Database_SQL.txt`. Nota: Estos están divididos en 3 pasos para realizar de manera secuencial.
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

## Autores

- [William Gil Clavijo](https://www.github.com/WILLY192002)
- [Jhoan Andres Diaz Castaño](https://www.github.com/JDiazc0)




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
 

## Authors

- [William Gil Clavijo](https://www.github.com/WILLY192002)
- [Jhoan Andres Diaz Castaño](https://www.github.com/JDiazc0)
