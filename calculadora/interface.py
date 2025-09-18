import tkinter as tk
from calculadora import calcular_expressao
from fractions import Fraction

def calcular():
    try:
        expressao = entrada_var.get()
        resultado = calcular_expressao(expressao)
        if isinstance(resultado, Fraction):
            entrada_var.set(f"{resultado}  (≈ {float(resultado)})")
        else:
            entrada_var.set(str(resultado))
    except Exception as e:
        entrada_var.set(f"Erro: {e}")

def adicionar(valor):
    entrada_var.set(entrada_var.get() + valor)

def limpar():
    entrada_var.set("")


janela = tk.Tk()
janela.title("Calculadora Frações")
janela.resizable(True, True)  


entrada_var = tk.StringVar()
entrada = tk.Entry(
    janela,
    textvariable=entrada_var,
    font=("Arial", 24),  
    justify="right",
    width=20 
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


botoes = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(
            janela,
            text=texto,
            width=8,  
            height=3,  
            font=("Arial", 20),
            command=calcular
        ).grid(row=linha, column=coluna, padx=8, pady=8)
    else:
        tk.Button(
            janela,
            text=texto,
            width=8,
            height=3,
            font=("Arial", 20),
            command=lambda t=texto: adicionar(t)
        ).grid(row=linha, column=coluna, padx=8, pady=8)

tk.Button(
    janela,
    text="C",
    width=8,
    height=3,
    font=("Arial", 20),
    command=limpar
).grid(row=5, column=0, columnspan=4, padx=8, pady=8, sticky="we")

janela.mainloop()
