from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def generar_pdf_cv(data, document):
    nombre_archivo = f"CV_{document}.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=LETTER)
    width, height = LETTER
    y = height - 50

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, y, "Hoja de Vida")
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, f"Documento: {document}")
    y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Información Personal:")
    y -= 20
    c.setFont("Helvetica", 12)
    for key, value in data["personalInfo"].items():
        c.drawString(70, y, f"{key.capitalize()}: {value}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Formación Académica:")
    y -= 20
    for edu in data.get("academicEducation", []):
        c.drawString(70, y, f"- {edu}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Habilidades:")
    y -= 20
    for skill in data.get("skills", []):
        c.drawString(70, y, f"- {skill}")
        y -= 20

    y -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Certificaciones:")
    y -= 20
    for cert in data.get("certifications", []):
        c.drawString(70, y, f"- {cert}")
        y -= 20

    c.save()
    print(f"PDF generado: {nombre_archivo}")

