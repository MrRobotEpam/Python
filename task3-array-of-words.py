def letter_in_words(words):
    
    result = ""  #iniciar el resultado de forma vacia

    for index, word in enumerate(words):

        #Checa si la palabra tiene suficientes caracteres
        if index < len(word):
            result += word[index]
    return result

print(letter_in_words(['Air', 'end', 'aggitated', 'green', 'lllll']))  #output: Angel