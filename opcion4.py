from hojasDeVida import CVs
import json


def list_cvc_superior_export():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return

    try:
        n = int(input("Ingrese el número de años de experiencia: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    reporte = {}

    for document, data in CVs.items():
        experiencie = data.get("profesionalExperience", [])
        total_years = 0

        for item in experiencie:
            try:
                total_years += int(item[3])
            except (ValueError, IndexError):
                continue

        if total_years > n:
            reporte[document] = data

    if reporte:
        with open("reporte_experiencia_superior.json", "w", encoding="utf-8") as file:
            json.dump(reporte, file, indent=4, default=list)
        print("Reporte exportado como 'reporte_experiencia_superior.json'")
    else:
        print(f"No se encontraron hojas de vida con más de {n} años de experiencia.")

    
def ncertif_nformation_export():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return

    f = input("Ingrese el tipo de certificación o formación: ").strip()
    if f == "":
        print("CAMPO VACÍO: Por favor ingrese caracteres")
        return

    reporte = {}

    for document, data in CVs.items():
        name = data["personalInfo"]["name"]
        
        formation = data.get("academicEducation", [])
        found_in_formation = any(f.lower() in str(item).lower() for item in formation)

        skills = data.get("skills", set())
        found_in_skills = any(f.lower() in skill.lower() for skill in skills)

        certifications = data.get("certifications", set())
        found_in_certifications = any(f.lower() in cert.lower() for cert in certifications)

        if found_in_formation or found_in_skills or found_in_certifications:
            reporte[document] = data

    if reporte:
        with open("reporte_formacion_certificacion.json", "w", encoding="utf-8") as file:
            json.dump(reporte, file, indent=4, default=list)
        print("Reporte exportado como 'reporte_formacion_certificacion.json'")
    else:
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

    


