def division(a, b):
    try:  # Inicia um bloco 'try' para tentar executar o código que pode gerar uma exceção.
        return f"{a} / {b} = {a / b}"  # Tenta retornar uma string formatada com o resultado da divisão de 'a' por 'b'.
    except ZeroDivisionError:  # Captura a exceção específica de divisão por zero.
        return "Error: Division by zero!"  # Retorna uma mensagem de erro indicando divisão por zero.
    except TypeError:  # Captura a exceção específica de tipos incompatíveis para a operação de divisão.
        return "Error: Unsupported type(s) for division!"  # Retorna uma mensagem de erro indicando tipos incompatíveis.




print(division(10, 2))
print(division("10", 2))
print(division(10, 0))
print(division(10, "b"))
