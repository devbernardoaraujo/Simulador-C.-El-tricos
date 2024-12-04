import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importando a biblioteca Pillow

# Função para calcular ohm, potência e circuito
def calcular_circuito():
    try:
        tipo_circuito = circuito_var.get()
        resistores = entry_resistores.get()
        
        if not resistores:
            messagebox.showwarning("Entrada inválida", "Preencha os resistores!")
            return

        resistores = list(map(float, resistores.split(',')))

        if tipo_circuito == "Série":
            # Cálculo para circuito em Série
            Req = sum(resistores)  # Resistência equivalente para série
            corrente_total = float(entry_tensao.get()) / Req
            tensao_resistores = [corrente_total * r for r in resistores]
            potencia_total = float(entry_tensao.get()) * corrente_total  # Correção da fórmula de potência total
            potencia_resistores = [(corrente_total ** 2) * r for r in resistores]
        
        elif tipo_circuito == "Paralelo":
            # Cálculo para circuito em Paralelo
            Req = 1 / sum([1 / r for r in resistores])  # Resistência equivalente para paralelo
            corrente_total = float(entry_tensao.get()) / Req
            tensao_resistores = [float(entry_tensao.get()) for _ in resistores]
            potencia_total = sum([(tensao_resistor ** 2) / r for tensao_resistor, r in zip(tensao_resistores, resistores)])
            potencia_resistores = [(tensao_resistor ** 2) / r for tensao_resistor, r in zip(tensao_resistores, resistores)]

        # Exibição dos resultados
        label_resultado.config(text=f"Resistência Equivalente (R_eq): {Req:.2f} Ω")
        label_potencia.config(text=f"Potência Total (P): {potencia_total:.2f} W")

        # Mostrando a tensão em cada resistor
        label_tensao_resistores.config(text=f"Tensão em cada resistor: {', '.join([f'{tensao:.2f} V' for tensao in tensao_resistores])}")

        # Mostrando a potência em cada resistor
        label_potencia_resistores.config(text=f"Potência em cada resistor: {', '.join([f'{potencia:.2f} W' for potencia in potencia_resistores])}")

        # Corrente total
        label_corrente_total.config(text=f"Corrente Total (I): {corrente_total:.2f} A")

        # Cálculo do disjuntor (corrente total * 1,1)
        disjuntor = corrente_total * 1.1
        label_disjuntor.config(text=f"Disjuntor: {disjuntor:.2f} A")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos nas entradas.")

# Função para resetar os campos
def resetar_opcoes():
    entry_resistores.delete(0, tk.END)
    entry_tensao.delete(0, tk.END)
    label_resultado.config(text="Resultado:")
    label_potencia.config(text="Potência: Não calculada")
    label_tensao_resistores.config(text="Tensão em cada resistor:")
    label_potencia_resistores.config(text="Potência em cada resistor:")
    label_corrente_total.config(text="Corrente Total:")
    label_disjuntor.config(text="Disjuntor:")

# Função para carregar e exibir a imagem
def exibir_imagem():
    # Carregar a imagem com Pillow
    imagem = Image.open("dimensfio.webp")  # Substitua pelo caminho da sua imagem
    imagem = imagem.resize((350, 500), Image.Resampling.LANCZOS)  # Reduzir o tamanho da imagem
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

label_resistores = tk.Label(janela, text="Resistores (Ω) separados por vírgula:")
label_resistores.grid(row=1, column=0, padx=5, pady=5)
entry_resistores = tk.Entry(janela)
entry_resistores.grid(row=1, column=1, padx=5, pady=5)

# Opções de tipo de circuito
circuito_var = tk.StringVar(value="Série")
radio_serie = tk.Radiobutton(janela, text="Série", variable=circuito_var, value="Série")
radio_serie.grid(row=2, column=0, padx=5, pady=5)
radio_paralelo = tk.Radiobutton(janela, text="Paralelo", variable=circuito_var, value="Paralelo")
radio_paralelo.grid(row=2, column=1, padx=5, pady=5)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_circuito)
botao_calcular.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

botao_resetar = tk.Button(janela, text="Resetar", command=resetar_opcoes)
botao_resetar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

label_potencia = tk.Label(janela, text="Potência Total: Não calculada")
label_potencia.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

label_tensao_resistores = tk.Label(janela, text="Tensão em cada resistor:")
label_tensao_resistores.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

label_potencia_resistores = tk.Label(janela, text="Potência em cada resistor:")
label_potencia_resistores.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

label_corrente_total = tk.Label(janela, text="Corrente Total:")
label_corrente_total.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

label_disjuntor = tk.Label(janela, text="Disjuntor:")
label_disjuntor.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

# Label para exibir a imagem
label_imagem = tk.Label(janela)
label_imagem.grid(row=0, column=2, rowspan=11, padx=10, pady=10)

# Chamar a função para exibir a imagem
exibir_imagem()

# Rodando a interface gráfica
janela.mainloop()
