def verificar_correo(correos_registrados, nuevo_correo):
    return nuevo_correo in correos_registrados

def main():
    print("📧 Verificador de correos registrados (usa set/hash)")

    entrada = input("Ingresa correos registrados, separados por comas: ")
    correos = set(map(str.strip, entrada.split(",")))

    nuevo = input("Ingresa el correo a verificar: ").strip()

    if verificar_correo(correos, nuevo):
        print("⚠️ El correo ya está registrado.")
    else:
        print("✅ El correo está disponible.")

if __name__ == "__main__":
    main()
