'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    def counter(word, count):
        if word.find('th') == -1:
            return count
        if word.find('th') != -1:
            count = count + 1
            position = word.find('th') + 2
            newString = word[position:]
            return counter(newString, count)
    return counter(word, 0)

