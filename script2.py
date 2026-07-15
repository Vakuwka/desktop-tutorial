menu = ('===== СПИСОК ПОКУПОК =====','1 - Показать товары','2 - Добавить товар','3 - Удалить товар','4 - Найти товар','5 - Очистить список','0 - Выход')

print()
for _ in range(len(menu)):
    print(menu[_])
shopping_list = []

print()
choose = input('Что вы хотите сделать?\n> ')

while choose != '0':
    if choose == '1':
        if len(shopping_list) == 0:
            print('Список пуст.')
        else:
            print('Ваш список продуктов:')
            for _ in range(len(shopping_list)):
                print(f'Товар №{_} {shopping_list[_]}')

    elif choose == '2':
        product_number = 1
        append_list = input(f'Какой товар вы хотите добавить?\nЧто бы закончить добавлять товары, напишите - "выход"\n№{product_number}.')
        append_list = append_list.strip().lower()
        shopping_list.append(append_list)
        while append_list != "выход":
            product_number += 1
            append_list = input(f'№{product_number}.')
            append_list = append_list.lower()
            shopping_list.append(append_list)
        shopping_list.pop(-1)

    elif choose == '3':
        pop_list = input('какой товар вы хотите убрать?\n> ')
        pop_list = pop_list.lower()
        if pop_list in shopping_list:
            shopping_list.remove(pop_list)
            print(f'Товар {pop_list} был удален.')
        else:
            print('Данный товар не был обнаружен.\nПовторите попытку\n> ')

    elif choose == '4':
        find_list = input('Какой товар вы хотите найти?\n> ')
        find_list = find_list.lower()
        if find_list in shopping_list:
            print('Товар пресутвует в списке')
        else:
            print('Товар отсутвует в списке')

    elif choose == '5':
        shopping_list.clear()
        print('Список очищен.')

    else:
        print('команда не найдена.')

    choose = input('Что вы хотите сделать?\n> ')
print('конец программы.')