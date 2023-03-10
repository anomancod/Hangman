import random
words = ['аббревиатура', 'абстрагирование', 'валидность', 'гармонизация', 'дезорганизация', 'детерминизм', 'группировка', 'диссертабельность', 'дублирование', 'заблуждение', 'закономерность', 'идентификация', 'издательство', 'экосистема']
f = 0
b = 0
while True:
    word = random.choice(words)
    wor = word
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
            for i in range(len(word)):
                if word[i:i + 1] == let:
                    b += 1

            for i in range(b):
                x = wor.find(let)

                wor1 = wor[:x]
                wor2 = wor[x + 1:]
                wor = wor1 + '*' + wor2

                w1 = w[:x]
                w2 = w[x + 1:]
                w = w1 + let + w2
            print(w)
            b = 0
        else:
            print('Вы ввели что-то не то.')
        if w == word and let.isalpha():
            print('Вы победили! Всего-то за ' + str(f) + ' попыток!')
            print('Если хотите сыграть ещё, введите 1.')
            z = input()
            if z == '1':
                break
