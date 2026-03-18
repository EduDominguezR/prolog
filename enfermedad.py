# Base de conocimientos
enfermedades = {
    "Gripe":     ["Tos", "Dolor de Cabeza"],
    "Alergia":   ["Congestion Nasal", "Dolor de Cabeza"],
    "Resfriado": ["Congestion Nasal", "Tos", "Fiebre"],
    "Covid":     ["Perdida de Olfato", "Tos", "Fiebre"],
    "Migraña":   ["Dolor de Cabeza", "Nauseas"],
}

# Preguntar síntomas al usuario
print("=== Diagnóstico de Enfermedades ===\n")
sintomas_usuario = []

todos = ["Tos", "Dolor de Cabeza", "Congestion Nasal", "Fiebre",
         "Perdida de Olfato", "Nauseas"]

for sintoma in todos:
    resp = input(f"¿Tienes {sintoma}? (s/n): ")
    if resp.lower() == "s":
        sintomas_usuario.append(sintoma)

# Diagnóstico
print("\n--- Resultados ---")
encontrado = False

for enfermedad, sintomas in enfermedades.items():
    if all(s in sintomas_usuario for s in sintomas):
        print(f" Posible diagnóstico: {enfermedad}")
        encontrado = True

if not encontrado:
    print(" No se encontró un diagnóstico exacto.")
    # Mostrar coincidencias parciales
    for enfermedad, sintomas in enfermedades.items():
        coinciden = [s for s in sintomas if s in sintomas_usuario]
        if coinciden:
            print(f"  {enfermedad} (parcial): {', '.join(coinciden)}")
set