import json
import os

x = []
y = "books.json"


def a():
    global x
    while True:
        print("\n=== Учет книг в библиотеке ===")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу по названию")
        print("4. Показать список книг")
        print("5. Сохранить данные в файл")
        print("6. Загрузить данные из файла")
        print("0. Выход")
        z = input("Выберите действие: ")
        if z == "1":
            t = input("Введите название книги: ")
            if t == "":
                print("Название не может быть пустым")
            else:
                q = input("Введите автора книги: ")
                if q == "":
                    q = "Неизвестный автор"
                w = input("Введите год издания: ")
                if w == "":
                    w = "Не указан"
                e = {"title": t, "author": q, "year": w}
                x.append(e)
                print("Книга добавлена")
        elif z == "2":
            t = input("Введите название книги для удаления: ")
            if t == "":
                print("Название не может быть пустым")
            else:
                r = False
                n = []
                for i in x:
                    if i["title"].lower() == t.lower() and r is False:
                        r = True
                    else:
                        n.append(i)
                x = n
                if r:
                    print("Книга удалена")
                else:
                    print("Книга не найдена")
        elif z == "3":
            t = input("Введите название книги для поиска: ")
            if t == "":
                print("Название не может быть пустым")
            else:
                r = False
                c = 1
                for i in x:
                    if t.lower() in i["title"].lower():
                        print(str(c) + ". " + i["title"] + " | " + i["author"] + " | " + str(i["year"]))
                        r = True
                    c = c + 1
                if r is False:
                    print("Книги не найдены")
        elif z == "4":
            if len(x) == 0:
                print("Список книг пуст")
            else:
                c = 1
                for i in x:
                    print(str(c) + ". " + i["title"] + " | " + i["author"] + " | " + str(i["year"]))
                    c = c + 1
        elif z == "5":
            p = input("Введите имя файла или нажмите Enter для books.json: ")
            if p == "":
                p = y
            try:
                f = open(p, "w", encoding="utf-8")
                json.dump(x, f, ensure_ascii=False, indent=2)
                f.close()
                print("Данные сохранены в файл " + p)
            except Exception as err:
                print("Ошибка сохранения: " + str(err))
        elif z == "6":
            p = input("Введите имя файла или нажмите Enter для books.json: ")
            if p == "":
                p = y
            if os.path.exists(p) is False:
                print("Файл не найден")
            else:
                try:
                    f = open(p, "r", encoding="utf-8")
                    d = json.load(f)
                    f.close()
                    if type(d) == list:
                        x = d
                        print("Данные загружены из файла " + p)
                    else:
                        print("Неверный формат файла")
                except Exception as err:
                    print("Ошибка загрузки: " + str(err))
        elif z == "0":
            print("Выход из программы")
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    a()
