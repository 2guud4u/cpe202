def indexOf(word, index, count):
    num = len(index)
    if len(word) == 0:
        return -1
    if index != word[0:num]:
        word = word[1:]
        count = count + 1
        return indexOf(word, index, count)
    return count



