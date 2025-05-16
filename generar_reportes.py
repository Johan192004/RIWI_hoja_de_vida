from hojasDeVida import CVs
def list_cvc_superior():
    if not CVs:
        print("Aun no hay hojas de vida registradas")
        return

    try:
        n = int(input("Ingrese el número mínimo de años de experiencia: "))
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
    
    