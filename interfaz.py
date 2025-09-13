import tkinter as tk
from tkinter import ttk, messagebox
from funcion import analizar_funcion, evaluar_funcion
from graficos import graficar_funcion

def main_gui():
    ventana = tk.Tk()
    ventana.title("Analizador de Funciones")
    ventana.geometry("750x550")

    tk.Label(ventana, text="Función f(x) (ej: x**2 - 4*x + 3, sin(x)):", font=("Arial", 11)).pack(pady=5)
    entrada_funcion = tk.Entry(ventana, width=50, font=("Arial", 11))
    entrada_funcion.pack()

    tk.Label(ventana, text="Valor de x (opcional):", font=("Arial", 11)).pack(pady=5)
    entrada_x = tk.Entry(ventana, width=20, font=("Arial", 11))
    entrada_x.pack()

    texto_resultados = tk.Text(ventana, height=15, width=85, font=("Consolas", 10))
    texto_resultados.pack(pady=10)

    def analizar():
        func_str = entrada_funcion.get()
        if not func_str:
            messagebox.showerror("Error", "Ingrese una función")
            return
        try:
            resultado = analizar_funcion(func_str)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        texto_resultados.delete(1.0, tk.END)
        texto_resultados.insert(tk.END, f"Función: {func_str}\n\n")
        texto_resultados.insert(tk.END, f"Dominio: {resultado['dominio']}\n")
        texto_resultados.insert(tk.END, f"Recorrido aproximado: {resultado['rango']}\n")
        texto_resultados.insert(tk.END, f"Intersección con eje y: {resultado['y_interseccion']}\n")
        texto_resultados.insert(tk.END, f"Intersecciones con eje x: {resultado['x_intersecciones']}\n")

        graficar_funcion(func_str, intersecciones=resultado["x_intersecciones"])

    def evaluar():
        func_str = entrada_funcion.get()
        x_val = entrada_x.get()
        if not func_str or not x_val:
            messagebox.showerror("Error", "Ingrese la función y el valor de x")
            return
        try:
            valor_x = float(x_val)
        except:
            messagebox.showerror("Error", "Valor de x inválido")
            return
        try:
            valor_f, paso_texto = evaluar_funcion(func_str, valor_x, paso_a_paso=True)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        texto_resultados.insert(tk.END, f"\nEvaluando f({valor_x}):\n")
        texto_resultados.insert(tk.END, paso_texto + "\n")
        graficar_funcion(func_str, punto=(valor_x, valor_f))

    ttk.Button(ventana, text="Analizar función", command=analizar).pack(pady=10)
    ttk.Button(ventana, text="Evaluar punto", command=evaluar).pack(pady=10)

    ventana.mainloop()
