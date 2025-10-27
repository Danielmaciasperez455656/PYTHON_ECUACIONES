import math
import sys

# --- Fórmulas de la Ley de Enfriamiento de Newton ---
# T(t) = Ta + (T0 - Ta) * e^(-kt)
# 
# Donde:
# T(t) = Temperatura final en el tiempo t
# Ta   = Temperatura ambiente
# T0   = Temperatura inicial del objeto
# k    = Constante de enfriamiento/calentamiento
# t    = Tiempo

def safe_input(prompt, type=float):
    """Maneja la entrada de datos, forzando números y reintentando en caso de error."""
    while True:
        try:
            return type(input(prompt))
        except ValueError:
            print("❌ Error de entrada. Por favor, introduce solo números válidos.")

def calcular_temperatura_final(Ta, T0, k, t):
    """Calcula la Temperatura Final T(t)."""
    return Ta + (T0 - Ta) * math.exp(-k * t)

def calcular_temperatura_inicial(Ta, Tf, k, t):
    """Calcula la Temperatura Inicial T0. Despeje: T0 = Ta + (Tf - Ta) * e^(kt)"""
    return Ta + (Tf - Ta) * math.exp(k * t)

def calcular_temperatura_ambiente(Tf, T0, k, t):
    """Calcula la Temperatura Ambiente Ta. Despeje: Ta = (Tf - T0 * e^(-kt)) / (1 - e^(-kt))"""
    exp_factor = math.exp(-k * t)
    denominator = 1 - exp_factor
    if abs(denominator) < 1e-9: # Evita división por cero si t es muy grande o k muy pequeño
        raise ZeroDivisionError("No se puede resolver: la temperatura final es casi igual a la inicial (t es demasiado grande).")
    return (Tf - T0 * exp_factor) / denominator

def calcular_tiempo(Ta, T0, Tf, k):
    """Calcula el Tiempo (t). Fórmula: t = (-1/k) * ln((T(t) - Ta) / (T0 - Ta))"""
    if k == 0: raise ZeroDivisionError("La constante 'k' no puede ser cero.")
    Tdiff_initial = T0 - Ta
    if Tdiff_initial == 0: raise ZeroDivisionError("La temperatura inicial no puede ser igual a la ambiente.")
    
    ratio = (Tf - Ta) / Tdiff_initial
    if ratio <= 0: raise ValueError("La temperatura final (T(t)) debe estar entre la inicial (T0) y la ambiente (Ta) o viceversa para un enfriamiento/calentamiento lógico.")
    
    return (-1 / k) * math.log(ratio)

def calcular_constante_k(Ta, T0, Tf, t):
    """Calcula la Constante de Enfriamiento (k). Fórmula: k = (-1/t) * ln((T(t) - Ta) / (T0 - Ta))"""
    if t == 0: raise ZeroDivisionError("El tiempo 't' no puede ser cero.")
    Tdiff_initial = T0 - Ta
    if Tdiff_initial == 0: raise ZeroDivisionError("La temperatura inicial no puede ser igual a la ambiente.")
    
    ratio = (Tf - Ta) / Tdiff_initial
    if ratio <= 0: raise ValueError("La temperatura final (T(t)) debe estar entre la inicial (T0) y la ambiente (Ta) o viceversa para un enfriamiento/calentamiento lógico.")
    
    return (-1 / t) * math.log(ratio)

def menu_newton():
    """Función principal que muestra el menú."""
    while True:
        print("\n--- Calculadora de la Ley de Enfriamiento de Newton ---")
        print("¿Qué deseas hallar en el ejercicio?")
        print("1. La temperatura final (T(t))")
        print("2. El tiempo (t)")
        print("3. La constante de enfriamiento (k)")
        print("4. La temperatura inicial (T0)")
        print("5. La temperatura ambiente (Ta) [NUEVO]") # Opción añadida
        print("6. Salir")
        
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
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = calcular_tiempo(Ta, T0, Tf, k)
                print(f"\n✅ Resultado: El tiempo (t) transcurrido es: {t:.4f}")
            elif choice == '3':
                Ta = safe_input("Introduce la temperatura ambiente (Ta): ")
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                k = calcular_constante_k(Ta, T0, Tf, t)
                print(f"\n✅ Resultado: La constante de enfriamiento (k) es: {k:.4f}")
            elif choice == '4':
                Ta = safe_input("Introduce la temperatura ambiente (Ta): ")
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                T0 = calcular_temperatura_inicial(Ta, Tf, k, t)
                print(f"\n✅ Resultado: La temperatura inicial T0 es: {T0:.4f} °C")
            elif choice == '5': # <--- NUEVA OPCIÓN
                Tf = safe_input("Introduce la temperatura final (T(t)): ")
                T0 = safe_input("Introduce la temperatura inicial (T0): ")
                k = safe_input("Introduce la constante de enfriamiento (k): ")
                t = safe_input("Introduce el tiempo transcurrido (t): ")
                Ta = calcular_temperatura_ambiente(Tf, T0, k, t)
                print(f"\n✅ Resultado: La temperatura ambiente Ta es: {Ta:.4f} °C")
            elif choice == '6':
                print("Adiós.")
                sys.exit(0)
            else:
                print("Opción no válida. Por favor, elige 1, 2, 3, 4, 5 o 6.")
        
        except (ValueError, ZeroDivisionError) as e:
            print(f"❌ Error en el cálculo: {e}")
            
        print("-" * 50)

if __name__ == "__main__":
    menu_newton()
