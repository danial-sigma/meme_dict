meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "СИГМА":"крутой",
            "СКУФ":"пухлый 40 летний холостяк"
            }
print('Пишите слова которые вы не знаете')
word_list = meme_dict.keys()
for i in word_list:
    print(i)
while True:
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('слово не нашлось')
