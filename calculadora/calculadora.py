from fractions import Fraction
import re

def transformar_fracoes(expr: str) -> str:

    return re.sub(r"(\d+/\d+)", r"Fraction('\1')", expr)

def calcular_expressao (expressao: str):
 
    try:
        expr_modificada = transformar_fracoes(expressao)
        return eval(expr_modificada, {"Fraction": Fraction})
    except ZeroDivisionError:
        raise
    except Exception:
        raise ValueError("Expressão inválida")
