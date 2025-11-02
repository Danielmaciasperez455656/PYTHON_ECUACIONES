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

# --- SE ELIMINÓ safe_input() ---
# (Esta función se moverá a app.py para ser el controlador principal)

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

# --- SE ELIMINÓ menu_newton() ---
# (Esta lógica se moverá a app.py)

# --- SE ELIMINÓ if __name__ == "__main__": ---
# (app.py será el punto de entrada)