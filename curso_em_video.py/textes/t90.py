import tkinter as tk
from tkinter import messagebox

def calcular_deslocamento():
    try:
        v0 = float(entrada_velocidade.get())
        a  = float(entrada_aceleracao.get())
        t  = float(entrada_tempo.get())

        deslocamento = v0 * t + 0.5 * a * t ** 2
        messagebox.showinfo("Resultado",f"O deslocamento é {deslocamento:.2f}.metros")
    except ValueError:
        messagebox.showinfo("Erro","Por favor, insira apenas números válidos.")

janela = tk.Tk()
janela.title(calcular_deslocamento)

tk.Label(janela,text = "Velocidade inicial (m/s):").grid(row=0,column=0, sticky="e")
entrada_velocidade = tk.Entry(janela)
entrada_velocidade.grid(row=0,column=1)

tk.Label(janela, text="Aceleração (m/s):").grid(row=1,column=0, sticky="e")
entrada_aceleracao = tk.Entry(janela)
entrada_aceleracao.grid(row=1,column=1)

tk.Label(janela, text="Tempo(s):").grid(row=2,column=0, sticky="e")
entrada_tempo = tk.Entry(janela)
entrada_tempo.grid(row=2, column=1)

tk.Button(janela, text="calculadora", command=calcular_deslocamento).grid(row=3,columnspan=2, pady=10)

janela.mainloop()