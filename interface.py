import tkinter as tk
from tkinter import messagebox

# func p calcular ohm e potencia
def calcular():
    try:
        
        resistencia = entry_resistencia.get()
        corrente = entry_corrente.get()
        tensao = entry_tensao.get()

        
        label_potencia.config(text="Potência: Não calculada")
        
        
        potencia = None

        
        if not tensao and not corrente and not resistencia:
            messagebox.showwarning("Entrada inválida", "Preencha pelo menos dois campos para realizar o cálculo!")
            return

        
        if resistencia and corrente:  
            tensao = float(resistencia) * float(corrente)
            label_resultado.config(text=f"Resultado: Tensão (V) = {tensao:.2f} V")
        elif tensao and corrente:  
            resistencia = float(tensao) / float(corrente)
            label_resultado.config(text=f"Resultado: Resistência (Ω) = {resistencia:.2f} Ω")
        elif tensao and resistencia:  
            corrente = float(tensao) / float(resistencia)
            label_resultado.config(text=f"Resultado: Corrente (A) = {corrente:.2f} A")
        else:
            messagebox.showwarning("Entrada inválida", "Preencha pelo menos dois campos para a Lei de Ohm!")

        
        if tensao and corrente:
            potencia = float(tensao) * float(corrente)
            label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")
        
        elif tensao and resistencia:
            potencia = (float(tensao) ** 2) / float(resistencia)
            label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")
        
        elif corrente and resistencia:
            potencia = (float(corrente) ** 2) * float(resistencia)
            label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos nas entradas.")

# Função para resetar os campos
def resetar_opcoes():
    entry_resistencia.delete(0, tk.END)
    entry_corrente.delete(0, tk.END)
    entry_tensao.delete(0, tk.END)
    label_resultado.config(text="Resultado:")
    label_potencia.config(text="Potência: Não calculada")

# Criação da janela principal
janela = tk.Tk()
janela.title("Simulador de Circuitos Elétricos")

# Labels e campos de entrada
label_tensao = tk.Label(janela, text="Tensão (V):")
label_tensao.grid(row=0, column=0)
entry_tensao = tk.Entry(janela)
entry_tensao.grid(row=0, column=1)

label_corrente = tk.Label(janela, text="Corrente (A):")
label_corrente.grid(row=1, column=0)
entry_corrente = tk.Entry(janela)
entry_corrente.grid(row=1, column=1)

label_resistencia = tk.Label(janela, text="Resistência (Ω):")
label_resistencia.grid(row=2, column=0)
entry_resistencia = tk.Entry(janela)
entry_resistencia.grid(row=2, column=1)


botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2)


botao_resetar = tk.Button(janela, text="Resetar", command=resetar_opcoes)
botao_resetar.grid(row=4, column=0, columnspan=2)


label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2)

label_potencia = tk.Label(janela, text="Potência: Não calculada")
label_potencia.grid(row=6, column=0, columnspan=2)

# Rodando a interface gráfica
janela.mainloop()
