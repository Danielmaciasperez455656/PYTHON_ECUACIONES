import math

# --- Fórmulas de la Ley de Enfriamiento de Newton ---
# T(t) = Ta + (T0 - Ta) * e^(-kt)
#
# Donde:
# T(t) = Temperatura final en el tiempo t
# Ta   = Temperatura ambiente
# T0   = Temperatura inicial del objeto
# k    = Constante de enfriamiento/calentamiento
# t    = Tiempo

def calcular_temperatura_final():
    """Pide los datos para hallar la Temperatura Final T(t)."""
    print("\n--- Hallar Temperatura Final T(t) ---")
    print("Fórmula: T(t) = Ta + (T0 - Ta) * e^(-kt)")
    try:
        # Pide los datos necesarios
        Ta = float(input("Introduce la temperatura ambiente (Ta): "))
        T0 = float(input("Introduce la temperatura inicial (T0): "))
        k = float(input("Introduce la constante de enfriamiento (k): "))
        t = float(input("Introduce el tiempo transcurrido (t): "))
        
        # Calcula T(t)
        Tf = Ta + (T0 - Ta) * math.exp(-k * t)
        
        print(f"\nResultado: La temperatura final T(t) es: {Tf:.4f}")
        
    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def calcular_tiempo():
    """Pide los datos para hallar el Tiempo (t)."""
    print("\n--- Hallar el Tiempo (t) ---")
    print("Fórmula: t = (-1/k) * ln((T(t) - Ta) / (T0 - Ta))")
    try:
        # Pide los datos necesarios
        Ta = float(input("Introduce la temperatura ambiente (Ta): "))
        T0 = float(input("Introduce la temperatura inicial (T0): "))
        Tf = float(input("Introduce la temperatura final (T(t)): "))
        k = float(input("Introduce la constante de enfriamiento (k): "))
        
        # Validaciones
        if k == 0:
            print("Error: La constante 'k' no puede ser cero.")
            return
        if T0 == Ta:
             print("Error: La temperatura inicial no puede ser igual a la ambiente.")
             return
            
        # Comprobación para el logaritmo
        ratio = (Tf - Ta) / (T0 - Ta)
        if ratio <= 0:
            print("Error: La temperatura final (T(t)) debe estar entre la inicial (T0) y la ambiente (Ta).")
            print("Esto causa un logaritmo de un número no positivo.")
        else:
            # Calcula t
            t = (-1 / k) * math.log(ratio)
            print(f"\nResultado: El tiempo (t) transcurrido es: {t:.4f}")
            
    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def calcular_constante_k():
    """Pide los datos para hallar la Constante (k)."""
    print("\n--- Hallar la Constante de Enfriamiento (k) ---")
    print("Fórmula: k = (-1/t) * ln((T(t) - Ta) / (T0 - Ta))")
    try:
        # Pide los datos necesarios
        Ta = float(input("Introduce la temperatura ambiente (Ta): "))
        T0 = float(input("Introduce la temperatura inicial (T0): "))
        Tf = float(input("Introduce la temperatura final (T(t)): "))
        t = float(input("Introduce el tiempo transcurrido (t): "))
        
        # Validaciones
        if t == 0:
            print("Error: El tiempo 't' no puede ser cero.")
            return
        if T0 == Ta:
             print("Error: La temperatura inicial no puede ser igual a la ambiente.")
             return

        # Comprobación para el logaritmo
        ratio = (Tf - Ta) / (T0 - Ta)
        if ratio <= 0:
            print("Error: La temperatura final (T(t)) debe estar entre la inicial (T0) y la ambiente (Ta).")
            print("Esto causa un logaritmo de un número no positivo.")
        else:
            # Calcula k
            k = (-1 / t) * math.log(ratio)
            print(f"\nResultado: La constante de enfriamiento (k) es: {k:.4f}")

    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- ¡NUEVA FUNCIÓN! ---
def calcular_temperatura_inicial():
    """Pide los datos para hallar la Temperatura Inicial (T0)."""
    print("\n--- Hallar Temperatura Inicial (T0) ---")
    print("Fórmula: T0 = Ta + (T(t) - Ta) * e^(kt)")
    try:
        # Pide los datos necesarios
        Ta = float(input("Introduce la temperatura ambiente (Ta): "))
        Tf = float(input("Introduce la temperatura final (T(t)): "))
        k = float(input("Introduce la constante de enfriamiento (k): "))
        t = float(input("Introduce el tiempo transcurrido (t): "))

        # Calcula T0
        # Usamos math.exp(k * t) que es lo mismo que 1 / math.exp(-k * t)
        T0 = Ta + (Tf - Ta) * math.exp(k * t)
        
        print(f"\nResultado: La temperatura inicial (T0) es: {T0:.4f}")

    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
# --- FIN DE LA NUEVA FUNCIÓN ---

def main():
    """Función principal que muestra el menú."""
    while True:
        print("\n--- Calculadora de la Ley de Enfriamiento de Newton ---")
        # Esta es la pregunta clave que pediste
        print("¿Qué deseas hallar en el ejercicio?")
        print("1. La temperatura final (T(t))")
        print("2. El tiempo (t)")
        print("3. La constante de enfriamiento (k)")
        print("4. La temperatura inicial (T0)") # <--- NUEVA OPCIÓN
        print("5. Salir")                      # <--- ACTUALIZADO
        
        choice = input("Selecciona una opción (1, 2, 3, 4 o 5): ") # <--- ACTUALIZADO
        
        if choice == '1':
            calcular_temperatura_final()
        elif choice == '2':
            calcular_tiempo()
        elif choice == '3':
            calcular_constante_k()
        elif choice == '4':                   # <--- NUEVA OPCIÓN
            calcular_temperatura_inicial()
        elif choice == '5':                   # <--- ACTUALIZADO
            print("Adiós.")
            break # Termina el bucle y sale del programa
        else:
            print("Opción no válida. Por favor, elige 1, 2, 3, 4 o 5.")
        
        print("-" * 50) # Separador para la siguiente iteración

# Ejecutar el programa
if __name__ == "__main__":
    main()