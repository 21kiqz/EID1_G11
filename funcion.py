import sympy as sp
import math

x = sp.symbols('x')

def evaluar_funcion(func_str, valor_x, paso_a_paso=False):
    """
    Evalúa la función en un punto y devuelve el resultado.
    Si paso_a_paso=True, devuelve el desarrollo paso a paso más detallado.
    """
    try:
        expr = sp.sympify(func_str)
    except Exception as e:
        raise ValueError(f"Error al interpretar la función: {e}")

    try:
        sustitucion = expr.subs(x, valor_x)
        valor = float(sp.N(sustitucion))
    except Exception as e:
        raise ValueError(f"No se puede evaluar la función en x={valor_x}: {e}")

    if paso_a_paso:
        paso_texto = f"1. Función original: f(x) = {expr}\n"
        paso_texto += f"2. Sustituimos x={valor_x}: f({valor_x}) = {sustitucion}\n"
        paso_texto += f"3. Evaluamos numéricamente: {valor}"
        return valor, paso_texto

    return valor


def analizar_funcion(func_str):
    """
    Devuelve:
        - Dominio
        - Rango aproximado
        - Intersección con eje y
        - Intersecciones con eje x
    """
    try:
        expr = sp.sympify(func_str)
    except Exception:
        raise ValueError("Función inválida")

    # Dominio: evitar divisiones por cero
    try:
        denominadores = sp.denom(expr)
        puntos_no_validos = sp.solveset(denominadores, x, domain=sp.S.Reals)
        dominio = sp.S.Reals - puntos_no_validos
    except:
        dominio = sp.S.Reals

    # Rango aproximado
    try:
        xs_test = [i/100 for i in range(-1000, 1001)]
        ys = []
        f_lambd = sp.lambdify(x, expr, "math")
        for xi in xs_test:
            try:
                y = f_lambd(xi)
                if math.isfinite(y):
                    ys.append(y)
            except:
                continue
        if ys:
            rango = (min(ys), max(ys))
        else:
            rango = "No se pudo calcular"
    except:
        rango = "No se pudo calcular"

    # Intersección con eje y
    try:
        y_inter = float(expr.subs(x, 0))
    except:
        y_inter = "No se puede calcular"

    # Intersecciones con eje x
    x_inters = []
    try:
        raices = sp.solve(sp.Eq(expr, 0), x)
        for r in raices:
            if r.is_real:
                x_inters.append(float(r))
    except:
        pass

    return {
        "dominio": dominio,
        "rango": rango,
        "y_interseccion": y_inter,
        "x_intersecciones": x_inters
    }