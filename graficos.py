import matplotlib.pyplot as plt
import sympy as sp
import math

x = sp.symbols('x')

def graficar_funcion(func_str, punto=None, intersecciones=None):
    try:
        expr = sp.sympify(func_str)
        f = sp.lambdify(x, expr, "math")
    except Exception as e:
        print("No se puede graficar:", e)
        return

    xs = [i/100 for i in range(-1000, 1001)]
    ys = []
    for xi in xs:
        try:
            yi = f(xi)
            if not math.isfinite(yi):
                ys.append(None)
            else:
                ys.append(yi)
        except:
            ys.append(None)

    plt.figure(figsize=(8,6))
    seg_x, seg_y = [], []
    for xi, yi in zip(xs, ys):
        if yi is None:
            if seg_x:
                plt.plot(seg_x, seg_y, color="orange")
                seg_x, seg_y = [], []
        else:
            seg_x.append(xi)
            seg_y.append(yi)
    if seg_x:
        plt.plot(seg_x, seg_y, color="orange")

    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

    if intersecciones:
        plt.scatter(intersecciones, [0]*len(intersecciones), color="green", marker="x", s=80, label="Intersecciones eje x")
    try:
        y0 = f(0)
        if math.isfinite(y0):
            plt.scatter([0], [y0], color="blue", marker="o", s=80, label="Intersección eje y")
    except:
        pass

    if punto:
        plt.scatter([punto[0]], [punto[1]], color="red", s=100, label=f"Punto ({punto[0]}, {punto[1]})")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Gráfica de la función")
    plt.legend()
    plt.grid(True)
    plt.show()

