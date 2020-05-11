import tkinter as tk


def interfazgrafica():
    global texto
    texto = "texto"
    res = "sexo"
    ventana = tk.Tk()
    ventana.title("Aerodinámica")
    ventana.geometry("700x100")
    lbl0 = tk.Label(ventana,text = "Programa para el cálculo de los coeficientes de la Teoría Potencial Linealizada")
    lbl1 = tk.Label(ventana,text="Introduce tu DNI")
    lbl2 = tk.Label(ventana)
    txt = tk.Entry(ventana,width=10)
    lbl0.grid(column=0, row=0)
    lbl1.grid(column=0, row=1)
    lbl2.grid(column=1, row=2)
    txt.grid(column=0, row=2)


    def pulsar():
        global res
        res = "h"
        res = txt.get()
        lbl0.destroy()
        lbl1.destroy()
        txt.destroy()
        btn.destroy()
        lbl2.configure(text = "DNI Obtenido")


    btn = tk.Button(ventana , text="Enter", command = pulsar )
    btn.grid(column=1, row=2)
    ventana.mainloop()
    texto = res


