# Sistema de Gestión de Envíos con Flask y Base de Datos Access

Este proyecto es un Sistema de Gestión de Envíos desarrollado con Flask, un framework web de Python, y utiliza una base de datos Microsoft Access para almacenar la información relacionada con los envíos. La aplicación permite agregar, eliminar y visualizar los detalles de los envíos, brindando una interfaz simple y eficiente para la gestión logística. Además, incluye un diseño atractivo y funcionalidades básicas para el manejo de tareas comunes asociadas con el proceso de envío y entrega.

## Configuración

### Clona el Proyecto desde el Repositorio

```bash
git clone https://github.com/luchopan/GestionDeEnvios.git
cd GestionDeEnvios
```

### Crea y Activa tu Entorno Virtual

Asegúrate de tener Python y pip instalados en tu sistema. Luego, crea un entorno virtual y actívalo:

```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
```

### Instala las Dependencias

Dentro de tu entorno virtual, instala las dependencias utilizando el archivo 'requirements.txt':

```bash
pip install -r requirements.txt
```

### Configura las Variables de Entorno

Si tu aplicación utiliza variables de entorno (por ejemplo, para la configuración de la base de datos), crea un archivo .env en el directorio principal del proyecto y define tus variables allí.

### Ejecuta la Aplicación

Asegúrate de estar dentro de tu entorno virtual y luego ejecuta la aplicación:

```bash
python init.py
```

### Desactiva el Entorno Virtual

Cuando hayas terminado de trabajar en tu proyecto, puedes desactivar el entorno virtual:

```bash
deactivate
```
