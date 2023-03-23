def gay(work_list: list) -> list: # функция возвращающая лист получая лист
    lowest_rating = 0 # просо 0
    to_return = [] # лист
    for statement in work_list: # для строки в листе
        rating = int(statement.split(" ")[0]) # нахожу значение до пробела и отделяю от строки
        if rating > lowest_rating: # понятно
            lowest_rating = rating # понятно
            to_return.append(statement.replace(f"{rating} ", "")) # добавляю строку заменяя рейтинг на пустоту
    return to_return # возвращаю значение


if __name__ == "__main__": # вызов
    work_list = [] # а вот и тот самый лист
    while True:
        to_add_string = input("Enter string to add: ") # добавление значений
        if to_add_string:
            work_list.append(to_add_string)
        else:
            break

    print(gay(work_list))