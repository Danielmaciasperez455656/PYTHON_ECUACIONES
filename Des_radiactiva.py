import math
import sys

# ----------------------------------------------------------------
### PUNTO CLAVE 1: FUNCIONES DE CÁLCULO "PURAS" (EL CEREBRO) ###
# Estas funciones son el "cerebro" matemático.
# No piden datos ni imprimen nada, solo reciben números y devuelven un resultado.
# Esto hace que el código sea limpio y fácil de mantener.
# ----------------------------------------------------------------

# CÁLCULOS DE LEY DE DESCOMPOSICIÓN RADIACTIVA
# Fórmulas: N(t) = N0 * e^(-kt)
#           k = ln(2) / T_half
# ----------------------------------------------------------------

def calcular_cantidad_final(N0, k, t):
    """Calcula la Cantidad Final N(t)."""
    return N0 * math.exp(-k * t)

def calcular_cantidad_inicial(Nf, k, t):
    """Calcula la Cantidad Inicial N0."""
    return Nf * math.exp(k * t)

def calcular_tiempo_radiactivo(N0, Nf, k):
    """Calcula el Tiempo (t)."""
    ### PUNTO CLAVE 3: MANEJO AVANZADO DE ERRORES (Parte A - 'raise') ###
    # En lugar de solo imprimir un error, "lanzamos" (raise) una excepción formal.
    # Esta excepción será "atrapada" (except) por el menú más abajo.
    if k == 0: raise ZeroDivisionError("La constante 'k' no puede ser cero.")
    if N0 == 0: raise ZeroDivisionError("La cantidad inicial 'N0' no puede ser cero.")
    ratio = Nf / N0
    if ratio <= 0: raise ValueError("La cantidad final debe ser positiva para el logaritmo.")
    return (-1 / k) * math.log(ratio)

def calcular_constante_k_radiactiva(N0, Nf, t):
    """Calcula la Constante (k) a partir de N0, N(t) y t."""
    if t == 0: raise ZeroDivisionError("El tiempo 't' no puede ser cero.")
    if N0 == 0: raise ZeroDivisionError("La cantidad inicial 'N0' no puede ser cero.")
    ratio = Nf / N0
    if ratio <= 0: raise ValueError("La cantidad final debe ser positiva para el logaritmo.")
    return (-1 / t) * math.log(ratio)

### PUNTO CLAVE ESPECIAL: FUNCIONES DE VIDA MEDIA ###
# Estas dos funciones son cruciales para conectar 'k' con la Vida Media.
# Permiten resolver problemas (como el del árbol) donde no te dan 'k'
# pero sí te dan la Vida Media.

def calcular_vida_media(k):
    """Calcula la Vida Media (T_half)."""
    if k <= 0: raise ZeroDivisionError("La constante 'k' debe ser positiva.")
    return math.log(2) / k

def calcular_k_desde_vida_media(t_half):
    """Calcula la constante k a partir de la Vida Media (T_half)."""
    if t_half <= 0: raise ZeroDivisionError("La Vida Media (T_half) debe ser positiva.")
    return math.log(2) / t_half

# ----------------------------------------------------------------
# CÁLCULOS DE LEY DE ENFRIAMIENTO DE NEWTON
# Fórmulas: T(t) = Ta + (T0 - Ta) * e^(-kt)
# ----------------------------------------------------------------

def calcular_temperatura_final(Ta, T0, k, t):
    """Calcula la Temperatura Final T(t)."""
    return Ta + (T0 - Ta) * math.exp(-k * t)

def calcular_temperatura_inicial(Ta, Tf, k, t):
    """Calcula la Temperatura Inicial T0."""
    # Despeje: T0 = Ta + (Tf - Ta) * e^(kt)
    return Ta + (Tf - Ta) * math.exp(k * t)

def calcular_temperatura_ambiente(Tf, T0, k, t):
    """Calcula la Temperatura Ambiente Ta. (Fórmula Despejada)"""
    # Despeje: Ta = (Tf - T0 * e^(-kt)) / (1 - e^(-kt))
    exp_factor = math.exp(-k * t)
    denominator = 1 - exp_factor
    if denominator == 0: 
        raise ZeroDivisionError("El tiempo 't' es demasiado grande, haciendo el denominador cero.")
    return (Tf - T0 * exp_factor) / denominator

def calcular_tiempo_newton(Ta, T0, Tf, k):
    """Calcula el Tiempo (t)."""
    if k == 0: raise ZeroDivisionError("La constante 'k' no puede ser cero.")
    Tdiff_initial = T0 - Ta
    if Tdiff_initial == 0: raise ZeroDivisionError("La temperatura inicial no puede ser igual a la ambiente.")
    
    ratio = (Tf - Ta) / Tdiff_initial
    if ratio <= 0: raise ValueError("La temperatura final debe estar entre la inicial y la ambiente.")
    
    return (-1 / k) * math.log(ratio)

def calcular_constante_k_newton(Ta, T0, Tf, t):
    """Calcula la Constante de Enfriamiento (k)."""
    if t == 0: raise ZeroDivisionError("El tiempo 't' no puede ser cero.")
    Tdiff_initial = T0 - Ta
    if Tdiff_initial == 0: raise ZeroDivisionError("La temperatura inicial no puede ser igual a la ambiente.")
    
    ratio = (Tf - Ta) / Tdiff_initial
    if ratio <= 0: raise ValueError("La temperatura final debe estar entre la inicial y la ambiente.")
    
    return (-1 / t) * math.log(ratio)

# ----------------------------------------------------------------
# ENTRADAS DE USUARIO Y MENÚS DE CONTROL
# ----------------------------------------------------------------

### PUNTO CLAVE 4: FUNCIÓN DE ENTRADA SEGURA ("safe_input") ###
# Esta es una función "ayudante" (helper) que nos ahorra mucho código.
# Su único trabajo es forzar al usuario a escribir un número válido.

def safe_input(prompt, type=float):
    """Maneja la entrada de datos, forzando números y reintentando en caso de error."""
    while True:
        try:
            # Intenta convertir la entrada del usuario al tipo (float por defecto)
            return type(input(prompt))
        except ValueError:
            # Si falla (ej. el usuario escribe "hola"), muestra un error
            # y el bucle 'while True' vuelve a empezar, pidiendo el dato de nuevo
            print("❌ Error de entrada. Por favor, introduce solo números válidos.")

### PUNTO CLAVE 2: EL MENÚ "CONTROLADOR" DE RADIACTIVIDAD ###
# Esta función maneja toda la interacción con el usuario para este módulo.
# Llama a las funciones de cálculo (PUNTO 1) y maneja los errores (PUNTO 3).
def menu_radiactiva():
    """Menú para el modelo de Decaimiento Radiactivo."""
    # El bucle mantiene al usuario en este menú hasta que elija '7' para salir.
    while True:
        print("\n--- Modelos: Decaimiento Radiactivo ---")
        print("¿Qué variable deseas calcular?")
        print(" 1. Cantidad Final (N(t))")
        print(" 2. Cantidad Inicial (N0)")
        print(" 3. Tiempo Transcurrido (t)")
        print(" 4. Constante de Desintegración (k)")
        print(" 5. Vida Media / Semivida (T_half)")
        print(" 6. Constante (k) a partir de la Vida Media")
        print(" 7. Volver al Menú Principal")
        
        choice = safe_input("Selecciona una opción (1-7): ", type=str)
        print("-" * 50)
        ### PUNTO CLAVE 3: MANEJO AVANZADO DE ERRORES (Parte B - 'try/except') ###
        # "Intentamos" (try) hacer toda la operación (pedir datos y calcular).
        
        try:
            if choice == '1':
                # 1. Recolecta datos usando la entrada segura
                N0 = safe_input("Introduce la cantidad inicial (N0): ")
                k = safe_input("Introduce la constante de desintegración (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                # 2. Llama a la función de cálculo "pura"
                Nf = calcular_cantidad_final(N0, k, t)
                # 3. Imprime el resultado
                print(f"\n✅ Resultado: La cantidad final N(t) es: {Nf:.4f}")
            elif choice == '2':
                Nf = safe_input("Introduce la cantidad final (N(t)): ")
                k = safe_input("Introduce la constante de desintegración (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                N0 = calcular_cantidad_inicial(Nf, k, t)
                print(f"\n✅ Resultado: La cantidad inicial N0 es: {N0:.4f}")
            elif choice == '3':
                N0 = safe_input("Introduce la cantidad inicial (N0): ")
                Nf = safe_input("Introduce la cantidad final (N(t)): ")
                k = safe_input("Introduce la constante de desintegración (k): ")
                t = calcular_tiempo_radiactivo(N0, Nf, k)
                print(f"\n✅ Resultado: El tiempo (t) transcurrido es: {t:.4f}")
            elif choice == '4':
                N0 = safe_input("Introduce la cantidad inicial (N0): ")
                Nf = safe_input("Introduce la cantidad final (N(t)): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                k = calcular_constante_k_radiactiva(N0, Nf, t)
                print(f"\n✅ Resultado: La constante de desintegración (k) es: {k:.6f}")
            elif choice == '5':
                # (Llamada a la función de Vida Media)
                k = safe_input("Introduce la constante de desintegración (k): ")
                t_half = calcular_vida_media(k)
                print(f"\n✅ Resultado: La Vida Media (T_half) es: {t_half:.6f}")
            elif choice == '6':
                # (Llamada a la función de Vida Media - usada para el Carbono-14)
                t_half = safe_input("Introduce la Vida Media (T_half): ")
                k = calcular_k_desde_vida_media(t_half)
                print(f"\n✅ Resultado: La constante de desintegración (k) es: {k:.6f}")
            elif choice == '7':
                break # Rompe el bucle 'while True' y vuelve al menú principal
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 7.")
        # Si el bloque 'try' falla (porque una función de cálculo 'raise' un error),
        # este bloque 'except' lo "atrapa" y maneja elegantemente.
        # El programa no se cierra, solo muestra el error y vuelve al menú.
        except (ValueError, ZeroDivisionError) as e:
            print(f"❌ Error en el cálculo: {e}")
            
        print("-" * 50)


def menu_newton():
    """Menú para el modelo de Ley de Enfriamiento de Newton."""
    while True:
        print("\n--- Modelos: Ley de Enfriamiento de Newton ---")
        print("¿Qué variable deseas calcular?")
        print(" 1. Temperatura Final (T(t))")
        print(" 2. Temperatura Inicial (T0)")
        print(" 3. Temperatura Ambiente (Ta)") # Nuevo despeje
        print(" 4. Tiempo Transcurrido (t)")
        print(" 5. Constante de Enfriamiento (k)")
        print(" 6. Volver al Menú Principal")
        
        choice = safe_input("Selecciona una opción (1-6): ", type=str)
        print("-" * 50)

        try:
            if choice == '1':
                Ta = safe_input("Introduce la temperatura ambiente (Ta): ")
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                Tf = calcular_temperatura_final(Ta, T0, k, t)
                print(f"\n✅ Resultado: La temperatura final T(t) es: {Tf:.4f} °C")
            elif choice == '2':
                Ta = safe_input("Introduce la temperatura ambiente (Ta): ")
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                T0 = calcular_temperatura_inicial(Ta, Tf, k, t)
                print(f"\n✅ Resultado: La temperatura inicial T0 es: {T0:.4f} °C")
            elif choice == '3':
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                Ta = calcular_temperatura_ambiente(Tf, T0, k, t)
                print(f"\n✅ Resultado: La temperatura ambiente Ta es: {Ta:.4f} °C")
            elif choice == '4':
                Ta = safe_input("Introduce la temperatura ambiente (Ta): ")
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = calcular_tiempo_newton(Ta, T0, Tf, k)
                print(f"\n✅ Resultado: El tiempo (t) transcurrido es: {t:.4f}")
            elif choice == '5':
                Ta = safe_input("Introduce la temperatura ambiente (Ta): ")
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                k = calcular_constante_k_newton(Ta, T0, Tf, t)
                print(f"\n✅ Resultado: La constante de enfriamiento (k) es: {k:.6f}")
            elif choice == '6':
                break
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 6.")

        except (ValueError, ZeroDivisionError) as e:
            print(f"❌ Error en el cálculo: {e}")
            
        print("-" * 50)


def main():
    """Función principal que muestra el menú de selección de modelo."""
    while True:
        print("\n" + "=" * 50)
        print("  CALCULADORA CIENTÍFICA: MODELOS EXPONENCIALES")
        print("=" * 50)
        print("Selecciona el modelo a simular:")
        print(" 1. Decaimiento Radiactivo (N(t))")
        print(" 2. Ley de Enfriamiento de Newton (T(t))")
        print(" 3. Salir del Programa")
        
        choice = safe_input("Selecciona una opción (1-3): ", type=str)
        print("-" * 50)
        
        if choice == '1':
            # Llama al menú de radiactividad
            menu_radiactiva()
        elif choice == '2':
            # Llama al menú de enfriamiento
            menu_newton()
        elif choice == '3':
            print("Programa finalizado. ¡Adiós!")
            sys.exit(0)# Cierra el programa de forma limpia
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
# Esta línea estándar de Python asegura que la función main()
# solo se ejecute cuando corres el archivo directamente.
if __name__ == "__main__":
    main()
