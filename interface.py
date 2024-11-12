import tkinter as tk
from tkinter import messagebox

# Função para calcular os valores usando a Lei de Ohm, resistores em série/paralelo e potência
def calcular():
    try:
        # Coletar os valores inseridos pelo usuário
        resistencia = entry_resistencia.get()
        corrente = entry_corrente.get()
        tensao = entry_tensao.get()
        resistores = entry_resistor.get()

        # Limpar resultados de potência e corrente total
        label_potencia.config(text="Potência: Não calculada")
        label_correntes.config(text="Corrente Total (Paralelo): Não calculada")
        
        # Inicializar a variável de potência
        potencia = None

        # Verificar se a opção "Série" ou "Paralelo" foi escolhida
        tipo_circuito = tipo_circuito_var.get()

        # Cálculos básicos (Lei de Ohm)
        if tipo_circuito == "Nenhum":  # Caso o tipo de circuito não tenha sido selecionado
            if resistencia and corrente:  # Se resistência e corrente estão preenchidos
                tensao = float(resistencia) * float(corrente)
                label_resultado.config(text=f"Resultado: Tensão (V) = {tensao:.2f} V")
            elif tensao and corrente:  # Se tensão e corrente estão preenchidos
                resistencia = float(tensao) / float(corrente)
                label_resultado.config(text=f"Resultado: Resistência (Ω) = {resistencia:.2f} Ω")
            elif tensao and resistencia:  # Se tensão e resistência estão preenchidos
                corrente = float(tensao) / float(resistencia)
                label_resultado.config(text=f"Resultado: Corrente (A) = {corrente:.2f} A")
            else:
                messagebox.showwarning("Entrada inválida", "Preencha pelo menos dois campos para a Lei de Ohm!")

            # Cálculo da potência (P = V * I) se ambos os campos forem preenchidos
            if tensao and corrente:
                potencia = float(tensao) * float(corrente)
                label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")
            # Cálculo da potência (P = V² / R) se ambos os campos forem preenchidos
            elif tensao and resistencia:
                potencia = (float(tensao) ** 2) / float(resistencia)
                label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")
            # Cálculo da potência (P = I² * R) se ambos os campos forem preenchidos
            elif corrente and resistencia:
                potencia = (float(corrente) ** 2) * float(resistencia)
                label_potencia.config(text=f"Potência (P) = {potencia:.2f} W")

        # Cálculo para resistores em série
        if tipo_circuito == "Série":
            if resistores:
                resistores_list = [float(r) for r in resistores.split(",")]
                resistencia_eq = sum(resistores_list)
                label_resultado.config(text=f"Resultado: Resistência Equivalente (Série) = {resistencia_eq:.2f} Ω")
            else:
                messagebox.showwarning("Entrada inválida", "Por favor, insira os valores dos resistores em série.")

        # Cálculo para resistores em paralelo
        elif tipo_circuito == "Paralelo":
            if resistores:
                resistores_list = [float(r) for r in resistores.split(",")]
                resistencia_eq = 1 / sum([1 / r for r in resistores_list])
                label_resultado.config(text=f"Resultado: Resistência Equivalente (Paralelo) = {resistencia_eq:.2f} Ω")

                # Calcular a corrente total dividida nos resistores (tensão constante)
                if tensao:
                    correntes = [float(tensao) / r for r in resistores_list]
                    corrente_total = sum(correntes)
                    label_correntes.config(text=f"Corrente Total (Paralelo) = {corrente_total:.2f} A")
                else:
                    label_correntes.config(text="Corrente total não calculada, insira a tensão")

            else:
                messagebox.showwarning("Entrada inválida", "Por favor, insira os valores dos resistores em paralelo.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos nas entradas.")

# Função para resetar as opções
def resetar_opcoes():
    tipo_circuito_var.set("Nenhum")  # Reseta o tipo de circuito para "Nenhum"
    entry_resistor.delete(0, tk.END)  # Limpa o campo de resistores
    label_resultado.config(text="Resultado:")  # Limpa os resultados
    label_potencia.config(text="Potência: Não calculada")  # Limpa a potência
    label_correntes.config(text="Corrente Total (Paralelo): Não calculada")  # Limpa a corrente total

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

label_resistor = tk.Label(janela, text="Resistores (Série/Paralelo):")
label_resistor.grid(row=3, column=0)
entry_resistor = tk.Entry(janela)
entry_resistor.grid(row=3, column=1)

# Botões de seleção do tipo de circuito
tipo_circuito_var = tk.StringVar(value="Nenhum")
botao_série = tk.Radiobutton(janela, text="Série", variable=tipo_circuito_var, value="Série")
botao_série.grid(row=4, column=0)

botao_paralelo = tk.Radiobutton(janela, text="Paralelo", variable=tipo_circuito_var, value="Paralelo")
botao_paralelo.grid(row=4, column=1)

# Botão para calcular os resultados
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=5, column=0, columnspan=2)

# Botão para resetar os campos
botao_resetar = tk.Button(janela, text="Resetar", command=resetar_opcoes)
botao_resetar.grid(row=6, column=0, columnspan=2)

# Labels para exibir os resultados
label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.grid(row=7, column=0, columnspan=2)

label_potencia = tk.Label(janela, text="Potência: Não calculada")
label_potencia.grid(row=8, column=0, columnspan=2)

label_correntes = tk.Label(janela, text="Corrente Total (Paralelo): Não calculada")
label_correntes.grid(row=9, column=0, columnspan=2)

# Rodando a interface gráfica
janela.mainloop()
