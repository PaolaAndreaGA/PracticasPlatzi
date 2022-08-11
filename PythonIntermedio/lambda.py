palindrome = lambda string: string == string[::-1]
print(palindrome('lateleletal'))
print(palindrome('racecar'))
print(palindrome('radar'))
print(palindrome('evan'))
#estructura lambda para crear funciones anonimas: identificador = argumeto : expresion
#se imprime llamando la varianble que contiene la funcion anonima y se le pasa un argumento