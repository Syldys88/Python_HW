# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def Polynomial(k):
  s = ''
  r = 0
  for i in range(k, 0, -1):
    r = random.randint(0, 100)
    if r == 0:
      s += ''
    elif r == 1:
      s += str(f'x^{i} + ')
    elif i != 1:
      s += str(f'{r}x^{i} + ')
    else:
      s += str(f'{r}x ')
  r = random.randint(0, 100)
  if r != 0:
    s += str(f'+ {r} = 0')
  else:
    s += str(f'= 0')
  return s


k = int(input("Введите: "))
while k <= 0:
  k = int(input("Введите больше 0: "))
print(Polynomial(k))