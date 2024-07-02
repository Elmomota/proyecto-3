# Zapacity

Zapacity es una aplicación web de gestión de tareas. Este proyecto está construido con Django y utiliza Bootstrap para el diseño. 

## Requisitos

- Python 3.x
- Pip
- Virtualenv

## Instalación

1. Clona el repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/zapacity.git
    cd zapacity
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv myvenv
    ```

3. Activa el entorno virtual:

    - En Windows:

      ```bash
      myvenv\Scripts\activate
      ```

    - En macOS y Linux:

      ```bash
      source myvenv/bin/activate
      ```

4. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones para crear las tablas en la base de datos:

    ```bash
    python manage.py migrate
    ```

6. Crea un superusuario para acceder al panel de administración de Django (opcional):

    ```bash
    python manage.py createsuperuser
    ```

7. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

8. Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Uso

- Usuario de prueba: `elmo`
- Contraseña: `elmo123`

## Estructura del Proyecto

- `main/`: La aplicación principal.
  - `static/`: Archivos estáticos como CSS, JS, imágenes.
    - `main/`
      - `css/`
        - `styles.css`: Archivo de estilos.
      - `js/`
        - `map.js`: Archivo JavaScript.
  - `templates/`: Plantillas HTML.
    - `main/`
      - `base.html`: Plantilla base.

- `myproject/`: Configuración del proyecto Django.
  - `settings.py`: Configuración principal del proyecto.
  - `urls.py`: URLs principales del proyecto.

- `manage.py`: Herramienta de línea de comandos de Django.

## Contribución

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
