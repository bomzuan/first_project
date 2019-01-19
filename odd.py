from datetime import datetime #импортируем модуль из стандартной библиотеки

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
this_minute = datetime.today().minute #thisMinute
if this_minute in odds:
    print("odd")
else:
    print("not odd")


