# ── Base de conocimientos: leyes ──
leyes = {
    "Ley de Protección Animal": {
        "descripcion": "La mascota es considerada un ser vivo con derechos básicos.",
        "obligaciones": ["proporcionar alimento", "proporcionar agua", "proporcionar refugio",
                         "atención veterinaria", "protección contra maltrato"],
        "hechos": ["mascota_tiene_derechos", "dueño_debe_cuidar"]
    },
    "Ley de Registro de Mascotas": {
        "descripcion": "Toda mascota doméstica debe registrarse en los primeros 30 días.",
        "obligaciones": ["registrar mascota en municipio", "renovar registro anualmente"],
        "hechos": ["mascota_debe_registrarse", "registro_anual"]
    },
    "Ley de Vacunación Obligatoria": {
        "descripcion": "Perros y gatos deben tener vacuna antirrábica y esquema básico.",
        "obligaciones": ["vacuna antirrábica vigente", "esquema básico de vacunación"],
        "hechos": ["vacunacion_obligatoria", "sancion_sin_vacuna"]
    },
    "Ley de Responsabilidad del Propietario": {
        "descripcion": "El propietario responde por daños que su mascota cause a terceros.",
        "obligaciones": ["responder por daños a terceros", "evitar negligencia en vigilancia"],
        "hechos": ["dueño_es_responsable", "daños_por_negligencia"]
    },
    "Ley de Tenencia de Perros Potencialmente Peligrosos": {
        "descripcion": "Razas peligrosas requieren seguro, licencia especial, bozal y correa.",
        "obligaciones": ["seguro de responsabilidad civil", "licencia especial", "bozal en público", "correa reforzada"],
        "hechos": ["raza_peligrosa_requiere_licencia", "bozal_obligatorio_en_publico"]
    },
    "Ley de Prohibición de Maltrato Animal": {
        "descripcion": "Se prohíbe tortura, abuso, abandono extremo o mutilaciones injustificadas.",
        "obligaciones": ["no maltratar animales", "no abandonar extremadamente"],
        "hechos": ["maltrato_es_ilegal", "sancion_penal_por_maltrato"]
    },
    "Ley de Transporte de Mascotas": {
        "descripcion": "La mascota debe ir asegurada en el vehículo, con ventilación adecuada.",
        "obligaciones": ["asegurar mascota en vehículo", "garantizar ventilación", "no obstruir visibilidad"],
        "hechos": ["transporte_seguro_obligatorio", "ventilacion_en_transporte"]
    },
    "Ley de Tenencia en Espacios Públicos": {
        "descripcion": "Las mascotas deben estar bajo control y usar correa en espacios públicos.",
        "obligaciones": ["controlar mascota en público", "usar correa si la norma lo exige"],
        "hechos": ["correa_en_espacios_publicos", "control_en_via_publica"]
    },
    "Ley de Deposición de Residuos": {
        "descripcion": "El dueño debe recoger los residuos de su mascota en vía pública.",
        "obligaciones": ["recoger heces en vía pública", "disponer residuos adecuadamente"],
        "hechos": ["recoger_heces_obligatorio", "sancion_por_no_recoger"]
    },
    "Ley de Esterilización y Control de Población": {
        "descripcion": "Se promueve la esterilización para evitar sobre"
        "oblación y abandono.",
        "obligaciones": ["considerar esterilización", "aprovechar campañas municipales"],
        "hechos": ["esterilizacion_promovida", "campañas_municipales_disponibles"]
    },
}

# ── Consultas predefinidas y qué leyes las responden ──
consultas = {
    "¿Qué necesito para tener un perro de raza peligrosa?":
        ["Ley de Tenencia de Perros Potencialmente Peligrosos"],

    "¿Qué pasa si mi mascota muerde a alguien?":
        ["Ley de Responsabilidad del Propietario"],

    "¿Debo registrar a mi mascota?":
        ["Ley de Registro de Mascotas"],

    "¿Cuáles son las vacunas obligatorias?":
        ["Ley de Vacunación Obligatoria"],

    "¿Puedo llevar a mi mascota en el carro?":
        ["Ley de Transporte de Mascotas"],

    "¿Qué pasa si alguien maltrata a un animal?":
        ["Ley de Prohibición de Maltrato Animal"],

    "¿Tengo que limpiar lo que ensucia mi mascota en la calle?":
        ["Ley de Deposición de Residuos"],

    "¿Qué derechos tiene mi mascota?":
        ["Ley de Protección Animal"],

    "¿Puedo sacar a mi perro sin correa?":
        ["Ley de Tenencia en Espacios Públicos"],

    "¿Hay apoyo para esterilizar a mi mascota?":
        ["Ley de Esterilización y Control de Población"],

    "¿Cuáles son todas mis obligaciones como dueño?":
        list(leyes.keys()),  # Aplican todas las leyes
}

# ── Motor de consulta ──
def responder_consulta(consulta):
    leyes_aplicables = consultas.get(consulta, [])
    if not leyes_aplicables:
        return

    print(f"\n Consulta: {consulta}")
    print("─" * 55)
    for nombre_ley in leyes_aplicables:
        ley = leyes[nombre_ley]
        print(f"\n  {nombre_ley}")
        print(f"   {ley['descripcion']}")
        print(f"    Obligaciones:")
        for ob in ley["obligaciones"]:
            print(f"      • {ob}")
        print(f"    Hechos: {', '.join(ley['hechos'])}")

# ── Menú interactivo ──
def menu():
    print("=" * 55)
    print("    SISTEMA DE CONSULTA - LEYES DE MASCOTAS")
    print("=" * 55)

    lista = list(consultas.keys())
    for i, consulta in enumerate(lista, 1):
        print(f"  {i:2}. {consulta}")
    print(f"  {len(lista)+1:2}. Mostrar todos los hechos del sistema")
    print(f"   0. Salir")
    print("─" * 55)

def mostrar_hechos():
    print("\n📋 TODOS LOS HECHOS DEL SISTEMA:")
    print("─" * 55)
    for nombre_ley, ley in leyes.items():
        print(f"\n    {nombre_ley}")
        for hecho in ley["hechos"]:
            print(f"     → {hecho}")

# ── Programa principal ──
def main():
    lista = list(consultas.keys())
    while True:
        menu()
        try:
            opcion = int(input("  Elige una opción: "))
        except ValueError:
            print("    Ingresa un número válido.\n")
            continue

        if opcion == 0:
            print("\n  ¡Hasta luego!\n")
            break
        elif opcion == len(lista) + 1:
            mostrar_hechos()
        elif 1 <= opcion <= len(lista):
            responder_consulta(lista[opcion - 1])
        else:
            print("   Opción fuera de rango.\n")

        input("\n  Presiona Enter para continuar...")
        print()

if __name__ == "__main__":
    main()
