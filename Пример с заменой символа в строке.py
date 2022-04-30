def filter_string(text, char):
    index = 0 # начальное значение для счетчика
    result = '' # нулевое значение для строки
    while index < len(text): # цикл "ОТ И ДО"     
      current_char = text[index] # переменная
      index = index + 1 # счетчик должен увеличиваться
      if current_char != char: # если индекс не равен заданному, тогда выполняется формула ниже: result = result + current_char 
        result = result + current_char      
    return result # в противном случае возврат пустой строки, т.е замена заданного сивола на пустую строку.
print(filter_string('If I look back I am lost', 'o'))