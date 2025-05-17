from hojasDeVida import CVs
import json


def list_cvc_superior():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return

    try:
        n = int(input("Ingrese el número de años de experiencia: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    found = 0

    for document, data in CVs.items():
        experiencie = data.get("profesionalExperience", [])
        total_years = 0

        for experiencie_item in experiencie:
            try:
                # El valor del tiempo (años) está en la posición 3
                total_years += int(experiencie_item[3])
            except (ValueError, IndexError):
                continue  # Saltar si algo está mal con ese dato

        if total_years > n:
            found += 1
            print("\n--- Hoja de Vida ---")
            print(f"Documento: {document}")
            print(f"Nombre: {data['personalInfo']['name']}")
            print(f"Total años de experiencia: {total_years}")

    if found == 0:
        print(f"\nNo se encontraron hojas de vida con más de {n} años de experiencia.")
    
def ncertif_nformation():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return
    
    f = input("Ingrese el tipo de certificación o formación: ").strip()
    if f == "":
        print("CAMPO VACÍO: Por favor ingrese caracteres")
        return

    
    found = 0

    for document, data in CVs.items():
        name = data["personalInfo"]["name"]
        
        # Verificar en formación académica
        formation = data.get("academicEducation", [])
        found_in_formation = any(f.lower() in str(item).lower() for item in formation)

        # Verificar en skills 
        skills = data.get("skills", set())
        found_in_skills = any(f.lower() in skill.lower() for skill in skills)

        # Verificar en certifications 
        certifications = data.get("certifications", set())
        found_in_certifications = any(f.lower() in cert.lower() for cert in certifications)

        if found_in_formation or found_in_skills or found_in_certifications:
            found += 1
            print("\n--- Candidato encontrado ---")
            print(f"Nombre: {name}")
            print(f"Documento: {document}")
            if found_in_formation:
                print("Formación relacionada")
            if found_in_skills:
                print("Formación relacionada")
            if found_in_certifications:
                print("Formación relacionada")

    if found == 0:
        print(f"No se encontraron hojas de vida relacionadas con '{f}'.")
        
def export_single_cv_json(filename, document_id, cvs_data):
    def convert_sets(obj):
        if isinstance(obj, set):
            return list(obj)
        return obj

    if document_id in cvs_data:
        single_cv = {document_id: cvs_data[document_id]}
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(single_cv, file, indent=4, default=convert_sets)
        print("Archivo exportado exitosamente como: ", filename)
    else:
        print("Documento no encontrado")

    

ncertif_nformation()
