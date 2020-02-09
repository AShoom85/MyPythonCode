# Предложение разбивается на список слов, затем создается список который
# содержит длину каждого слова.

# sentence = 'It is raining cats and dogs'
# ...
# print(list(lengths)) # [2, 2, 7, 4, 3, 4]

# Записать одной строкой



print(list(map(lambda word: len(word), str.split('It is raining cats and dogs')))) 

