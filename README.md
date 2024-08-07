# Resolución de Ecuaciones e Integrales en Python

Esta aplicación, desarrollada en Python utilizando Tkinter y SymPy, permite resolver sistemas de ecuaciones lineales con dos o tres incógnitas, así como calcular integrales definidas e indefinidas.

## Requisitos

- Python 3.6 o superior
- Paquetes Python: `tkinter`, `sympy`

## Instalación

1. **Clonar el repositorio** o descargar el archivo Python.
2. **Instalar las dependencias** si es necesario. Puedes instalar el paquete `sympy` usando pip:

    ```bash
    pip install sympy
    ```

## Uso

1. **Ejecuta la aplicación**. Puedes hacerlo ejecutando el archivo Python en tu terminal o desde un entorno de desarrollo:

    ```bash
    python main.py
    ```

2. **Selecciona el tipo de cálculo** en la interfaz gráfica:
   - **Dos incógnitas**: Para resolver un sistema de dos ecuaciones lineales con dos incógnitas.
   - **Tres incógnitas**: Para resolver un sistema de tres ecuaciones lineales con tres incógnitas.
   - **Integrales**: Para calcular la integral de una función respecto a una variable.

3. **Introduce las ecuaciones o función**:
   - Para **dos incógnitas** o **tres incógnitas**, ingresa las ecuaciones en los campos proporcionados.
   - Para **integrales**, ingresa la función y la variable de integración.

4. **Haz clic en "Calcular"** para obtener el resultado de la operación.

## Funcionalidades

- **Sistema de Dos Incógnitas**:
  - Introduce dos ecuaciones lineales con dos incógnitas (`x` y `y`).
  - La solución es calculada usando el método de sustitución o eliminación.

- **Sistema de Tres Incógnitas**:
  - Introduce tres ecuaciones lineales con tres incógnitas (`x`, `y` y `z`).
  - La solución es calculada utilizando métodos algebraicos para resolver el sistema.

- **Integrales**:
  - Introduce una función matemática y la variable de integración.
  - Calcula la integral indefinida de la función respecto a la variable.

## Código

### Archivo Python (`tu_archivo.py`)

- **Funciones**:
  - `resolver_sistema_dos_incognitas(ecuacion1, ecuacion2)`: Resuelve un sistema de dos ecuaciones con dos incógnitas.
  - `resolver_sistema_tres_incognitas(ecuacion1, ecuacion2, ecuacion3)`: Resuelve un sistema de tres ecuaciones con tres incógnitas.
  - `calcular_integrales(funcion, variable)`: Calcula la integral indefinida de una función respecto a una variable.

- **Interfaz gráfica**:
  - Utiliza Tkinter para crear una interfaz gráfica que permite al usuario seleccionar el tipo de cálculo y proporcionar los datos necesarios.
  - Los resultados se muestran en la interfaz después de hacer clic en el botón "Calcular".

## Ejemplo de Uso

1. **Resolver un sistema de dos incógnitas**:
   - Selecciona "Dos incógnitas".
   - Introduce las ecuaciones, por ejemplo:
     - Ecuación 1: `x + y = 10`
     - Ecuación 2: `2x - y = 5`
   - Haz clic en "Calcular" para ver la solución.

2. **Calcular una integral**:
   - Selecciona "Integrales".
   - Introduce la función, por ejemplo: `x**2 + 3*x`
   - Introduce la variable de integración: `x`
   - Haz clic en "Calcular" para obtener la integral.
