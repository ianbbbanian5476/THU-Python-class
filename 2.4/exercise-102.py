sentence = input('Enter a sentence:')
print(f'First word: {sentence.split(" ")[0]}')
print(f'Last word: {sentence.split(" ")[-1].split(".")[0]}')