# Sistema de Gestión de Nómina con Api y Prolog

Este proyecto es una aplicación de gestión de nómina que permite registrar docentes y calcular sus salarios netos. La aplicación utiliza **FastAPI** como framework para la creación de endpoints y **Prolog** para realizar cálculos y consultas sobre los datos de los docentes.

## Participantes
- Luis Miguel Viuche Madroñero (20212020082)
- Daniel Alejandro Chave Bustos (20212020109)
- Dilan Stive Arboleda Zambrano (20212020105)


## Características

- **Registrar Docentes:** Agregar nuevos docentes con su nombre, categoría y salario base.
- **Consultar Nómina:** Calcular el salario neto de los docentes considerando deducciones y bonificaciones según su categoría.
- **Validación de Datos:** Verifica que las categorías de los docentes sean válidas para evitar errores en los cálculos.

## Requisitos

### Software
- **Python 3.9+**
- **SWI-Prolog**
- Bibliotecas de Python:
  - `fastapi`
  - `uvicorn`
  - `pydantic`
  - `pyswip`

### Instalación de Dependencias
Ejecuta el siguiente comando para instalar las dependencias necesarias:
```bash
pip install fastapi uvicorn pyswip pydantic 
```


## Configuracion

1. Asegúrate de tener SWI-Prolog instalado y configurado en tu sistema.
2. Coloca el archivo nomina.pl en el mismo directorio que el archivo main.py.
3. Ejecuta la aplicación FastAPI utilizando el siguiente comando:

```bash
python main.py

```

## Comprobación de conexion con el servidor


## POST para registrar profesor y consultar nomina usando FastAPI









