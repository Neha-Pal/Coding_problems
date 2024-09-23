# Input: Ram is a good boy
# Output: R i a g b

def output (sentence):
    #split the sentence into words
    words = sentence.split()

    #extract the 1st letter of each word
    i = [word[0] for word in words]
    result = ' '.join(i)

    return result

sentence = 'Ram is a good boy'
print(output(sentence))
