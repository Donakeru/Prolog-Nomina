from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyswip import Prolog

app = FastAPI()

# Inicializar Prolog y cargar el archivo
prolog_engine = Prolog()
prolog_engine.consult("nomina.pl")

# Modelo para agregar un nuevo profesor
class Profesor(BaseModel):
    nombre: str
    categoria: str
    salario: int

# Endpoint para registrar un nuevo profesor
@app.post("/registrar_profesor/")
def registrar_profesor(profesor: Profesor):
    profesor_nombre = profesor.nombre.lower()
    profesor_categoria = profesor.categoria.lower()
    salario_inicial = profesor.salario

    # Validar que la categoría sea correcta
    categorias_validas = ["auxiliar", "asociado", "titular"]
    if profesor_categoria not in categorias_validas:
        raise HTTPException(
            status_code=400, 
            detail=f"Categoría inválida. Debe ser una de {categorias_validas}."
        )

    # Intentar agregar al profesor en Prolog
    try:
        # Verificar si ya existe en la base
        consulta_existe = f"docente({profesor_nombre}, _, _)"
        resultado = list(prolog_engine.query(consulta_existe))

        if resultado:
            raise HTTPException(status_code=400, detail="El profesor ya está registrado.")

        # Insertar el nuevo profesor
        insertar_comando = f"assertz(docente({profesor_nombre}, {profesor_categoria}, {salario_inicial}))"
        list(prolog_engine.query(insertar_comando))

        return {"message": f"Profesor {profesor_nombre} registrado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Modelo para consultar el salario neto de un profesor
class ConsultaProfesor(BaseModel):
    nombre: str

# Endpoint para calcular el salario neto
@app.post("/consultar_nomina/")
def consultar_nomina(profesor: ConsultaProfesor):
    profesor_nombre = profesor.nombre.lower()  # Convertir a minúsculas

    try:
        # Realizar la consulta al predicado Prolog
        consulta_nomina = f"salario_neto({profesor_nombre}, SalarioNeto)"
        resultado = list(prolog_engine.query(consulta_nomina))

        if resultado:
            salario_final = resultado[0]["SalarioNeto"]
            return {"nombre": profesor_nombre, "salario_neto": salario_final}
        else:
            raise HTTPException(status_code=404, detail="Profesor no encontrado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
