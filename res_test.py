import spisok_stud, quashion
# Начало работы
# Вызываем все функции  из модулей spisok_stud, quashion для прохождения теста
def callback():
    stud = spisok_stud.reg()
    avtoriz = spisok_stud.log()
    test = quashion.test_matematik()
    ser = quashion.serialize()
    sav = quashion.user_json_dumps()
    return sav
# Вывод данных в файл c использованием json.loads и добавления к этим данным фамилии и имени студента
import json
def test_stud_for_arhiv():
    c = str(input("Введите свою Фамилию: "))
    i = str(input("Введите свое Имя: "))
    list_stud = [c, i]
    total_data = {"Данные тестируемого": list_stud}
    fil = str(input("Введите с клавиатуры имя файла , откуда нужно взять данные теста студента  "))
    data_stud = {}
    with open(fil, "r") as f:
        json_loads_d = f.read()
        data_stud = json.loads(json_loads_d)
        data_stud.update(total_data)
    print(type(data_stud))
    print(data_stud)
    return data_stud
f = test_stud_for_arhiv()
# Функция сохранения данных в формате json  в файл 'архив'
def user_json_dumps(f):
    json_dumps_user = json.dumps(f)
    with open('архив', 'a') as f:
        f.write(json_dumps_user)
    print(json_dumps_user)
user_json_dumps(f)
# Функция сериализации данных словаря в строку для удобного просмотра на экране
def serialize(f):
    res = "Данные тестируемого: {}\n"\
          "Вопрос 2x2=?' :   {}\n"\
          "Вопрос 3x3=? :    {}\n" \
          "Вопрос 23-15=? :  {}\n" \
          "Вопрос sin(180)=?: {}\n" \
          "Вопрос 120:5=? :   {}\n"\
          "Вопрос 45x4=?   :  {}\n"\
          "Вопрос cos(90)=? : {}\n"\
          "Общее количество баллов: {}".format(f["Данные тестируемого"],
                                        f["Вопрос 2x2=?"],
                                        f["Вопрос 3x3=?"],
                                        f["Вопрос 23-15=?"],
                                        f["Вопрос sin(180)=?"],
                                        f["Вопрос 120:5=?"],
                                        f["Вопрос 45x4=?"],
                                        f["Вопрос cos(90)=?"],
                                        f["Общее количество баллов"])
    return res
ser_stud = serialize(f)
print(ser_stud)

