import random
words = ['аббревиатура', 'абстрагирование', 'валидность', 'гармонизация', 'дезорганизация', 'детерминизм', 'группировка', 'диссертабельность', 'дублирование', 'заблуждение', 'закономерность', 'идентификация', 'издательство']
f = 0
while True:
    word = random.choice(words)
    w = '*' * len(word)
    print(w)
    while True:
        let = input().lower()
        if len(let) > 1 and let.isalpha():
            if let == word:
                f += 1
                print('Вы победили! Всего-то за ' + str(f) + ' попыток!')
                print('Если хотите сыграть ещё, введите 1.')
                z = input()
                if z == '1':
                    break
            else:
                print('Вы ввели неверное слово.')
        elif let in word and let.isalpha():
            f += 1
            x = word.find(let)
            x1 = word.rfind(let)
            if x == x1:
                y = w[x + 1:]
                y1 = w[:x]
                w1 = y1 + let + y
                w = w1
                print(w)
            else:
                y = w[x + 1:]
                y1 = w[:x]
                w1 = y1 + let + y
                w = w1

                y = w[x1 + 1:]
                y1 = w[:x1]
                w1 = y1 + let + y
                w = w1

                print(w)
        else:
            print('Вы ввели что-то не то.')
        if w == word and let.isalpha():
            print('Вы победили! Всего-то за ' + str(f) + ' попыток!')
            print('Если хотите сыграть ещё, введите 1.')
            z = input()
            if z == '1':
                break
