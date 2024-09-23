def reverse(sentence):
    # split the words from the sentence
    words = sentence.split()
    #reverse the list of words
    r = words[::-1]

    reverse_sentence = ' '.join(r)

    return reverse_sentence

sentence = 'Ram is a good boy'
print(reverse(sentence))