# 1 
# Read obama_speech.txt file and count number of lines and words
def count_lines_and_words(path):
    
    with open(path) as f:
        text = f.read()
    number_of_lines = len(text.splitlines())
    number_of_words = len(text.split())
    return number_of_lines, number_of_words

lines, words = count_lines_and_words('./data/obama_speech.txt')
print('Obama speech')
print('number of lines : ', lines)
print('number of words : ', words)

# Read michelle_obama_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('./data/michelle_obama_speech.txt')
print('Michelle obama speech')
print('lines : ', lines)
print('words : ', words)

