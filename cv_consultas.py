import json
from verifies import * 

with open("cv_data.json", "r", encoding="utf-8") as f:
    CVs = json.load(f)

def search_cvs(query = "", experiencia_min = None, formacion = None, habilidad = None):
    resultados = []

    for cv in CVs:
        if (query.lower() in cv["name"].lower() or query in cv["document"] or query.lower() in cv["email"].lower()):

            if experiencia_min and cv["experiencia"] < experiencia_min:
                continue

            if formacion and cv["formacion"].lower() != formacion.lower():
                continue   

            if habilidad and habilidad not in cv["habilidades"]:
                continue

            resultados.append(cv)
    return resultados
SUCCESS = "\033[92m"    
RESET = "\033[0m"
DANGER = "\033[91m"
def show_cv(cv):
    print(f"Nombre: {cv['name']}")
    print(f"Documento: {cv['document']}")
    print(f"Correo: {cv['email']}")
    print(f"Experiencia: {cv['experiencia']} años")
    print(f"Formación: {cv['formacion']}")
    print(f"Habilidades: {', '.join(cv['habilidades'])}")
    print(DANGER + "-" * 44 + RESET)

def menu():
    print("=== CONSULTA DE HOJAS DE VIDA ===")
    query = input("Buscar por nombre, documento o correo: ").strip()
    exp = input("Experiencia mínima (dejar en blanco si no aplica): ").strip()
    formacion = input("Formación requerida (Técnico / Profesional / Posgrado): ").strip()
    #formacion = verifyName(formacion)
    habilidad = input("Habilidad específica (ej. Python): ").strip()

    experiencia_min = int(exp) if exp.isdigit() else None
    resultados = search_cvs(query, experiencia_min, formacion, habilidad)

    print(f"\nSe encontraron {len(resultados)} resultados:\n")
    for cv in resultados:
        show_cv(cv)

if __name__ == '__main__':
    while True:
        menu()
        continuar = input("¿Deseas hacer otra búsqueda? (s/n): ").strip().lower()
        if continuar != 's':
            break
