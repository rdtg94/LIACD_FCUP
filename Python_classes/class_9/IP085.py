def sum_integers(data):
  """
  Calcula a soma de todos os inteiros presentes em uma estrutura de dados,
  que pode ser uma lista ou tupla com aninhamentos de profundidade arbitrária.

  Args:
    data: Uma lista, tupla ou um inteiro.

  Returns:
    A soma total dos inteiros encontrados na estrutura.
  """
  total_sum = 0

  if isinstance(data, (list, tuple)):
    # Se 'data' é uma lista ou tupla, iteramos sobre cada elemento.
    for element in data:
      # Chamada recursiva para processar cada elemento, que pode ser
      # outro inteiro, lista ou tupla.
      total_sum += sum_integers(element)
  elif isinstance(data, int):
    # Se 'data' é um inteiro, adicionamos diretamente à soma total.
    total_sum += data

  return total_sum




print(sum_integers([[(4,3)],(((45,[9]))),[(42)],[1,6,8]]))
print(sum_integers(["a",([[2]],[["b"]]),40,[[2.2]]]))
print(sum_integers((1,2,[3],[[4]])))
print(sum_integers(["hello","world"]))