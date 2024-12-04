import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk  # Importando a biblioteca Pillow

# Função para calcular a tensão, corrente e resistência e exibir a potência
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

        # Cálculos baseados na Lei de Ohm
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

        # Cálculo da potência
        if tensao and corrente:
            potencia = float(tensao) * float(corrente)
            label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")
        
        elif tensao and resistencia:
            potencia = (float(tensao) ** 2) / float(resistencia)
            label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")
        
        elif corrente and resistencia:
            potencia = (float(corrente) ** 2) * float(resistencia)
            label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")

        # Gerar o gráfico
        plotar_grafico(resistencia, tensao, corrente)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos nas entradas.")

# Função para resetar os campos
def resetar_opcoes():
    entry_resistencia.delete(0, tk.END)
    entry_corrente.delete(0, tk.END)
    entry_tensao.delete(0, tk.END)
    label_resultado.config(text="Resultado:")
    label_potencia.config(text="Potência: Não calculada")
    canvas.get_tk_widget().destroy()  # Remover o gráfico anterior
    canvas.draw()

# Função para criar o gráfico
def plotar_grafico(resistencia, tensao, corrente):
    try:
        if resistencia:
            resistencia = float(resistencia)
        else:
            resistencia = 1  # Definir valor padrão para resistência se não for informado

        if tensao and corrente:
            # Gerar gráfico baseado na Lei de Ohm
            correntes = np.linspace(0, 10, 100)  # Correntes de 0 a 10 A
            tensoes = resistencia * correntes  # Tensão = Resistência * Corrente

            fig, ax = plt.subplots(figsize=(5.5, 4))  # Reduzido um pouco o tamanho do gráfico
            ax.plot(correntes, tensoes, label=f'R = {resistencia} Ω', color='blue')
            ax.set_xlabel('Corrente (A)')
            ax.set_ylabel('Tensão (V)')
            ax.set_title('Gráfico Ôhmico')
            ax.legend()

            # Inserir o gráfico na interface do Tkinter
            global canvas
            canvas = FigureCanvasTkAgg(fig, master=janela)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7, column=0, padx=10, pady=10)

    except ValueError:
        messagebox.showerror("Erro", "Erro ao gerar gráfico! Verifique os valores de entrada.")

# Função para carregar e exibir a imagem
def exibir_imagem():
    # Carregar a imagem com Pillow
    imagem = Image.open("dimensfio.webp")  # Substitua pelo caminho da sua imagem
    imagem = imagem.resize((350, 500), Image.Resampling.LANCZOS)  # Reduzir um pouco o tamanho da imagem
    imagem_tk = ImageTk.PhotoImage(imagem)  # Converter para formato Tkinter

    # Exibir a imagem em um Label
    label_imagem.config(image=imagem_tk)
    label_imagem.image = imagem_tk  # Guardar uma referência à imagem

# Criação da janela principal
janela = tk.Tk()
janela.title("Simulador de Circuitos Elétricos")

# Labels e campos de entrada
label_tensao = tk.Label(janela, text="Tensão (V):")
label_tensao.grid(row=0, column=0, padx=5, pady=5)
entry_tensao = tk.Entry(janela)
entry_tensao.grid(row=0, column=1, padx=5, pady=5)

label_corrente = tk.Label(janela, text="Corrente (A):")
label_corrente.grid(row=1, column=0, padx=5, pady=5)
entry_corrente = tk.Entry(janela)
entry_corrente.grid(row=1, column=1, padx=5, pady=5)

label_resistencia = tk.Label(janela, text="Resistência (Ω):")
label_resistencia.grid(row=2, column=0, padx=5, pady=5)
entry_resistencia = tk.Entry(janela)
entry_resistencia.grid(row=2, column=1, padx=5, pady=5)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

botao_resetar = tk.Button(janela, text="Resetar", command=resetar_opcoes)
botao_resetar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

label_potencia = tk.Label(janela, text="Potência: Não calculada")
label_potencia.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Label para exibir o gráfico e a imagem
label_imagem = tk.Label(janela)
label_imagem.grid(row=7, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

# Chamar a função para exibir a imagem
exibir_imagem()

# Rodando a interface gráfica
janela.mainloop()
