from tkinter import *
 
root = Tk()
f_bot = Frame(root)
x = 16
frame = Frame(f_bot, height=x, width=x)

scrollbarV = Scrollbar(root)
scrollbarH = Scrollbar(root, orient=HORIZONTAL)
root.title('Новый текстовый документ.txt - Блокнот')
mainmenu = Menu(root) 
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Создать")
filemenu.add_command(label="Новое окно")
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Сохранить")
filemenu.add_command(label="Сохранить как...")
filemenu.add_separator()
filemenu.add_command(label="Параметры страницы...")
filemenu.add_command(label="Печать...")
filemenu.add_separator()
filemenu.add_command(label="Выход")

editmenu = Menu(mainmenu, tearoff=0)
editmenu.add_command(label="	Отменить")
editmenu.add_separator()
editmenu.add_command(label="Вырезать")
editmenu.add_command(label="Копировать")
editmenu.add_command(label="Вставить")
editmenu.add_command(label="Удалить")
editmenu.add_separator()
editmenu.add_command(label="Поиск с помощью Bing...")
editmenu.add_command(label="Найти...")
editmenu.add_command(label="Найти далее")
editmenu.add_command(label="Найти ранее")
editmenu.add_command(label="Заменить...")
editmenu.add_command(label="Перейти...")
editmenu.add_separator()
editmenu.add_command(label="Выделить все")
editmenu.add_command(label="Дата и время")

formatmenu = Menu(mainmenu, tearoff=0)
formatmenu.add_command(label="Перенос по словам")
formatmenu.add_command(label="Шрифт...")

windowmenu = Menu(mainmenu, tearoff=0)
scalemenu = Menu(windowmenu, tearoff=0)
windowmenu.add_cascade(label="Масштаб",
						menu=scalemenu)
windowmenu.add_command(label="Строка состояния")

scalemenu.add_command(label="Увеличить")
scalemenu.add_command(label="Уменьшить")
scalemenu.add_command(label="Восстановить масштаб по умолчанию")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Посмотреть справку")
helpmenu.add_command(label="Отправить отзыв")
helpmenu.add_separator()
helpmenu.add_command(label="О программе")
 
mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
mainmenu.add_cascade(label="Правка",
					 menu=editmenu)
mainmenu.add_cascade(label="Формат", 
					 menu=formatmenu)
mainmenu.add_cascade(label="Вид",
					 menu=windowmenu)
mainmenu.add_cascade(label="Справка",
                     menu=helpmenu)
scrollbarH = Scrollbar(f_bot, orient=HORIZONTAL)

scrollbarV = Scrollbar(root)


text = Text()

scrollbarV.config(command=text.yview)
scrollbarH.config(command=text.xview)
f_bot.pack(side="bottom",fill="x")
scrollbarH.pack(side="left", fill="x",expand=1)
frame.pack(side="left",anchor=SE)
scrollbarV.pack(side="right", fill="y")
text.pack(side="top", fill="both", expand=1)


root.iconbitmap('C:/Users/Root/Downloads/notepad.ico')
root.mainloop() 
