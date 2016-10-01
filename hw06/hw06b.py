sequence = range(100,1000)
palindromes = []

for x1 in sequence:
  for x2 in sequence:
    number = x1 * x2
    number = str(number)
    if number == number[::-1]:
      palindromes.append(int(number))

print max(palindromes)
