def put(word, result):
    current = result.get(word)
    result[word] = (current if current is not None else 0) + 1
    return

def count_words(sentence):
    replaced_letters = ',.:!&@$%^_\n\t'
    for r in replaced_letters:
        sentence = sentence.replace(r, ' ')
    result = {}
    for word in sentence.split():
        word = word.strip('\'')
        put(word.lower(), result)
    return result
