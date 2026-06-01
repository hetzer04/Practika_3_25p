import json
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QFileDialog

x = []
y = "books.json"


def a():
    global x
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Учет книг в библиотеке")
    w.resize(850, 620)
    w.setStyleSheet("""
        QWidget { background-color: #101828; color: #F9FAFB; font-size: 14px; }
        QLabel#title { font-size: 28px; font-weight: bold; color: #FACC15; padding: 12px; }
        QLabel { color: #E5E7EB; }
        QLineEdit { background-color: #1F2937; color: #F9FAFB; border: 2px solid #374151; border-radius: 8px; padding: 8px; }
        QPushButton { background-color: #2563EB; color: white; border-radius: 8px; padding: 10px; font-weight: bold; }
        QPushButton:hover { background-color: #1D4ED8; }
        QListWidget { background-color: #111827; color: #F9FAFB; border: 2px solid #374151; border-radius: 8px; padding: 8px; }
    """)
    l = QVBoxLayout()
    t = QLabel("📚 УЧЕТ КНИГ В БИБЛИОТЕКЕ")
    t.setObjectName("title")
    l.addWidget(t)
    r1 = QHBoxLayout()
    r1.addWidget(QLabel("Название:"))
    e1 = QLineEdit()
    e1.setPlaceholderText("Например: Python для начинающих")
    r1.addWidget(e1)
    l.addLayout(r1)
    r2 = QHBoxLayout()
    r2.addWidget(QLabel("Автор:"))
    e2 = QLineEdit()
    e2.setPlaceholderText("Например: Иван Петров")
    r2.addWidget(e2)
    l.addLayout(r2)
    r3 = QHBoxLayout()
    r3.addWidget(QLabel("Год:"))
    e3 = QLineEdit()
    e3.setPlaceholderText("Например: 2026")
    r3.addWidget(e3)
    l.addLayout(r3)
    r4 = QHBoxLayout()
    r4.addWidget(QLabel("Файл:"))
    e4 = QLineEdit()
    e4.setText(y)
    r4.addWidget(e4)
    l.addLayout(r4)
    s = QLineEdit()
    s.setPlaceholderText("Введите часть названия для поиска")
    l.addWidget(s)
    m = QListWidget()
    l.addWidget(m)
    b1 = QPushButton("➕ Добавить книгу")
    b2 = QPushButton("🗑️ Удалить по названию")
    b3 = QPushButton("🔎 Найти")
    b4 = QPushButton("📖 Показать все")
    b5 = QPushButton("💾 Сохранить")
    b6 = QPushButton("📂 Загрузить")
    b7 = QPushButton("📁 Выбрать файл")
    b8 = QPushButton("🚪 Выход")
    rr = QHBoxLayout()
    rr.addWidget(b1)
    rr.addWidget(b2)
    rr.addWidget(b3)
    rr.addWidget(b4)
    l.addLayout(rr)
    rr2 = QHBoxLayout()
    rr2.addWidget(b5)
    rr2.addWidget(b6)
    rr2.addWidget(b7)
    rr2.addWidget(b8)
    l.addLayout(rr2)
    w.setLayout(l)

    def p():
        m.clear()
        if len(x) == 0:
            m.addItem("⚠️ Список книг пуст")
        else:
            c = 1
            for i in x:
                m.addItem(str(c) + ". " + i["title"] + " | " + i["author"] + " | " + str(i["year"]))
                c = c + 1

    def b():
        t = e1.text()
        if t == "":
            QMessageBox.warning(w, "Ошибка", "Название не может быть пустым")
        else:
            q = e2.text()
            if q == "":
                q = "Неизвестный автор"
            z = e3.text()
            if z == "":
                z = "Не указан"
            x.append({"title": t, "author": q, "year": z})
            e1.setText("")
            e2.setText("")
            e3.setText("")
            p()
            QMessageBox.information(w, "Готово", "Книга добавлена")

    def c():
        global x
        t = e1.text()
        if t == "":
            QMessageBox.warning(w, "Ошибка", "Введите название книги для удаления в поле 'Название'")
        else:
            r = False
            n = []
            for i in x:
                if i["title"].lower() == t.lower() and r is False:
                    r = True
                else:
                    n.append(i)
            x = n
            p()
            if r:
                QMessageBox.information(w, "Готово", "Книга удалена")
            else:
                QMessageBox.warning(w, "Ошибка", "Книга не найдена")

    def d():
        t = s.text()
        if t == "":
            QMessageBox.warning(w, "Ошибка", "Введите название книги для поиска")
        else:
            m.clear()
            r = False
            ccc = 1
            for i in x:
                if t.lower() in i["title"].lower():
                    m.addItem(str(ccc) + ". " + i["title"] + " | " + i["author"] + " | " + str(i["year"]))
                    r = True
                ccc = ccc + 1
            if r is False:
                m.addItem("⚠️ Книги не найдены")

    def e():
        ppp = e4.text()
        if ppp == "":
            ppp = y
            e4.setText(ppp)
        try:
            f = open(ppp, "w", encoding="utf-8")
            json.dump(x, f, ensure_ascii=False, indent=2)
            f.close()
            QMessageBox.information(w, "Готово", "Данные сохранены в файл " + ppp)
        except Exception as err:
            QMessageBox.critical(w, "Ошибка", "Ошибка сохранения: " + str(err))

    def f():
        global x
        ppp = e4.text()
        if ppp == "":
            ppp = y
            e4.setText(ppp)
        if os.path.exists(ppp) is False:
            QMessageBox.critical(w, "Ошибка", "Файл не найден")
        else:
            try:
                ff = open(ppp, "r", encoding="utf-8")
                dd = json.load(ff)
                ff.close()
                if type(dd) == list:
                    x = dd
                    p()
                    QMessageBox.information(w, "Готово", "Данные загружены из файла " + ppp)
                else:
                    QMessageBox.critical(w, "Ошибка", "Неверный формат файла")
            except Exception as err:
                QMessageBox.critical(w, "Ошибка", "Ошибка загрузки: " + str(err))

    def g():
        zzz = QFileDialog.getOpenFileName(w, "Выберите JSON файл", "", "JSON files (*.json);;All files (*.*)")
        if zzz[0] != "":
            e4.setText(zzz[0])

    b1.clicked.connect(b)
    b2.clicked.connect(c)
    b3.clicked.connect(d)
    b4.clicked.connect(p)
    b5.clicked.connect(e)
    b6.clicked.connect(f)
    b7.clicked.connect(g)
    b8.clicked.connect(w.close)
    p()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    a()
