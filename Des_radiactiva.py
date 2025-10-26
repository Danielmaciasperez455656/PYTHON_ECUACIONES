import math

# --- Fórmulas de Descomposición Radiactiva ---
# N(t) = N0 * e^(-kt)
#
# Relación con Vida Media (T_half):
# k = ln(2) / T_half
# T_half = ln(2) / k
#
# Donde:
# N(t) = Cantidad final
# N0   = Cantidad inicial
# k    = Constante de desintegración
# t    = Tiempo
# T_half = Vida Media (Tiempo para que se desintegre la mitad)

def calcular_cantidad_final():
    """Pide los datos para hallar la Cantidad Final N(t)."""
    print("\n--- Hallar Cantidad Final N(t) ---")
    print("Fórmula: N(t) = N0 * e^(-kt)")
    try:
        # Pide los datos necesarios
        N0 = float(input("Introduce la cantidad inicial (N0): "))
        k = float(input("Introduce la constante de desintegración (k): "))
        t = float(input("Introduce el tiempo transcurrido (t): "))
        
        # Calcula N(t)
        Nf = N0 * math.exp(-k * t)
        
        print(f"\nResultado: La cantidad final N(t) es: {Nf:.4f}")
        
    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def calcular_cantidad_inicial():
    """Pide los datos para hallar la Cantidad Inicial (N0)."""
    print("\n--- Hallar Cantidad Inicial (N0) ---")
    print("Fórmula: N0 = N(t) * e^(kt)")
    try:
        # Pide los datos necesarios
        Nf = float(input("Introduce la cantidad final (N(t)): "))
        k = float(input("Introduce la constante de desintegración (k): "))
        t = float(input("Introduce el tiempo transcurrido (t): "))
        
        # Calcula N0
        N0 = Nf * math.exp(k * t)
        
        print(f"\nResultado: La cantidad inicial (N0) es: {N0:.4f}")

    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def calcular_tiempo():
    """Pide los datos para hallar el Tiempo (t)."""
    print("\n--- Hallar el Tiempo (t) ---")
    print("Fórmula: t = (-1/k) * ln(N(t) / N0)")
    try:
        # Pide los datos necesarios
        N0 = float(input("Introduce la cantidad inicial (N0): "))
        Nf = float(input("Introduce la cantidad final (N(t)): "))
        k = float(input("Introduce la constante de desintegración (k): "))
        
        # Validaciones
        if k == 0:
            print("Error: La constante 'k' no puede ser cero.")
            return
        if N0 == 0:
             print("Error: La cantidad inicial 'N0' no puede ser cero.")
             return
            
        # Comprobación para el logaritmo
        ratio = Nf / N0
        if ratio <= 0:
            print("Error: La cantidad final debe ser un número positivo.")
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
    """Pide los datos para hallar la Constante (k) a partir de N0, N(t) y t."""
    print("\n--- Hallar la Constante de Desintegración (k) ---")
    print("Fórmula: k = (-1/t) * ln(N(t) / N0)")
    try:
        # Pide los datos necesarios
        N0 = float(input("Introduce la cantidad inicial (N0): "))
        Nf = float(input("Introduce la cantidad final (N(t)): "))
        t = float(input("Introduce el tiempo transcurrido (t): "))
        
        # Validaciones
        if t == 0:
            print("Error: El tiempo 't' no puede ser cero.")
            return
        if N0 == 0:
             print("Error: La cantidad inicial 'N0' no puede ser cero.")
             return

        # Comprobación para el logaritmo
        ratio = Nf / N0
        if ratio <= 0:
            print("Error: La cantidad final debe ser un número positivo.")
            print("Esto causa un logaritmo de un número no positivo.")
        else:
            # Calcula k
            k = (-1 / t) * math.log(ratio)
            print(f"\nResultado: La constante de desintegración (k) es: {k:.6f}")

    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def calcular_vida_media():
    """Calcula la Vida Media (T_half) a partir de k."""
    print("\n--- Hallar la Vida Media / Semivida (T_half) ---")
    print("Fórmula: T_half = ln(2) / k")
    try:
        k = float(input("Introduce la constante de desintegración (k): "))
        
        if k <= 0:
            print("Error: La constante 'k' debe ser un número positivo.")
            return
            
        # Calcula T_half (ln(2) es math.log(2))
        t_half = math.log(2) / k
        print(f"\nResultado: La Vida Media (T_half) es: {t_half:.6f}")
        
    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def convertir_vida_media_a_k():
    """Calcula la constante k a partir de la Vida Media (T_half)."""
    print("\n--- Hallar Constante (k) a partir de la Vida Media ---")
    print("Fórmula: k = ln(2) / T_half")
    try:
        t_half = float(input("Introduce la Vida Media (T_half): "))
        
        if t_half <= 0:
            print("Error: La Vida Media (T_half) debe ser un número positivo.")
            return
            
        # Calcula k
        k = math.log(2) / t_half
        print(f"\nResultado: La constante de desintegración (k) es: {k:.6f}")
        
    except ValueError:
        print("Error: Asegúrate de introducir solo números válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main():
    """Función principal que muestra el menú."""
    while True:
        print("\n--- Calculadora de Descomposición Radiactiva ---")
        # Esta es la pregunta clave que pediste
        print("¿Qué deseas hallar en el ejercicio?")
        print("1. La cantidad final (N(t))")
        print("2. La cantidad inicial (N0)")
        print("3. El tiempo (t)")
        print("4. La constante de desintegración (k) (con N0, N(t) y t)")
        print("5. La Vida Media / Semivida (T_half) (a partir de k)")
        print("6. La constante (k) (a partir de la Vida Media)")
        print("7. Salir")
        
        choice = input("Selecciona una opción (1-7): ")
        
        if choice == '1':
            calcular_cantidad_final()
        elif choice == '2':
            calcular_cantidad_inicial()
        elif choice == '3':
            calcular_tiempo()
        elif choice == '4':
            calcular_constante_k()
        elif choice == '5':
            calcular_vida_media()
        elif choice == '6':
            convertir_vida_media_a_k()
        elif choice == '7':
            print("Adiós.")
            break # Termina el bucle y sale del programa
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 7.")
        
        print("-" * 50) # Separador para la siguiente iteración


if __name__ == "__main__":
    main()