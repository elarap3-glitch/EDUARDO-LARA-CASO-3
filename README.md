# EDUARDO-LARA-CASO-3
TEST 1
Introducción

En este trabajo se desarrolló un sistema de inventario en Python aplicando programación orientada a objetos.  
El objetivo principal fue organizar correctamente la lógica del programa separando cada responsabilidad en archivos distintos: una clase para representar productos, otra para gestionar el inventario y un archivo principal para ejecutar el flujo del sistema.  
Además, se incluyó un diagrama UML para mostrar de manera visual la estructura del caso.

Objetivos

- Implementar un modelo de inventario funcional en Python.
- Aplicar conceptos de clases, atributos y métodos.
- Organizar el proyecto por módulos para mejorar la claridad del código.
- Permitir la gestión básica de productos dentro del inventario.
- Representar la estructura del sistema mediante un diagrama UML.

Desarrollo

1. Organización del proyecto

El código se estructuró en los siguientes archivos:

- `modelo/producto.py`: contiene la clase **Producto**.
- `modelo/inventario.py`: contiene la clase **Inventario**.
- `main.py`: archivo principal para ejecutar y probar el sistema.
- `uml/caso_06_inventario.puml`: diagrama UML del caso.

Esta organización ayuda a mantener el proyecto limpio, entendible y fácil de mantener.
 

2. Clase Producto (`modelo/producto.py`)

En este archivo se definió la clase que representa cada producto del inventario.  
Aquí se modelan los datos de cada artículo (por ejemplo, código, nombre, precio, cantidad, según la implementación del archivo).  
La clase Producto encapsula la información de cada elemento que será administrado por el inventario.
 

3. Clase Inventario (`modelo/inventario.py`)

En este archivo se implementó la lógica central del sistema.  
La clase Inventario se encarga de administrar la colección de productos y de ejecutar las operaciones necesarias, como registrar, buscar, actualizar o eliminar productos (según lo desarrollado en el código).  
De esta forma, toda la gestión del inventario queda centralizada y ordenada.
 

4. Archivo principal (`main.py`)

Este archivo integra las clases y ejecuta el flujo de uso del sistema.  
Desde aquí se crean objetos, se llaman métodos del inventario y se muestran resultados en consola para verificar el funcionamiento general.
 

5. Diagrama UML (`uml/caso_06_inventario.puml`)

Se elaboró un diagrama UML para representar visualmente las clases y su relación.  
Esto permite explicar mejor la arquitectura del proyecto y entender cómo interactúan los componentes antes y después de ejecutar el código.
 

Conclusiones

El resultado es un sistema de inventario modular, claro y funcional, construido con buenas prácticas de organización básica en Python.  
La separación por archivos permitió una mejor estructura del código y facilitó la comprensión de cada parte del programa.  
El uso del diagrama UML complementa la implementación al mostrar de forma visual el diseño del sistema.  
En conjunto, el trabajo cumple con el propósito académico del caso y deja una base sólida para ampliaciones futuras.
