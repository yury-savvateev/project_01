# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace('!', '')

print(remove_exclamation_marks("Hi! Hello!"))  # "Hi Hello"
print(remove_exclamation_marks(""))  # ""
print(remove_exclamation_marks("Oh, no!!!"))  # "Oh, no"

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    # обрежем строку до предпоследнего символа, вырежем из строки поседний символ 
    # и если это "!" заменим его на пустую строку, затем сложим обе части вырезки
    return s[:-1] + s[-1:].replace('!', '')  

print(remove_last_em("Hi!"))  # "Hi"
print(remove_last_em("Hi!!!"))  # "Hi!!"
print(remove_last_em("!Hi"))  # "!Hi"


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass
