pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print "Your word in english: " + original
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)] + first + pyg
    print "Your word in pig latin: " + new_word

else:
    print 'empty'
