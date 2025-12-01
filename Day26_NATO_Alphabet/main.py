import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_word = input("Enter your word: ").upper()
nato_word_list = [nato_dict[letter] for letter in user_word]


print(nato_word_list)