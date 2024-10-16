def single_root_words(root_word, *other_words):
    same_words = []
    right_words = list(other_words)

    for i in right_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('wood', 'Woodman', 'Greasewood', 'wod', 'woody', 'Hollywood')
result4 = single_root_words('Disablement', 'Mentol', 'Ment', 'Overdisablement', 'dicent')

print(result1)
print(result2)
print(result3)
print(result4)
