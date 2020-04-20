# Функция тестирования знаний студентов по математике
def test_matematik():
    answer_student = {'Вопрос 2x2=?': {'2': False, '3': False, '4': True, '5': False},
               'Вопрос 3x3=?': {'7': False, '8': False, '9': True, '10': False},
               'Вопрос 23-15=?': {'14': False, '15': False, '16': False, '8': True},
               'Вопрос sin(180)=?': {'1,7': False, '1': False, '0': True, '-1': False},
               'Вопрос 120:5=?': {'15': False, '24': True, '16': False, '17': False},
               'Вопрос 45x4=?': {'190': False, '170': False, '180': True, '345': False},
               'Вопрос cos(90)=?': {'-1': False, '3': False, '0': True, '1': False}}

    test = {}
    mistake = 0
    for i in list(answer_student.keys()):
        print(i + '\n' + ' '.join(answer_student[i].keys()))
        answer = input('Выберите правильный ответ:\n')
        if answer_student[i][answer] == True:
            mistake += 5
            print('Ответ верный!')
            test_answer = {i: answer_student[i][answer]}
            test.update(test_answer)
        else:
            print('Ответ не верный!')
            test_answer = {i: answer_student[i][answer]}
            test.update(test_answer)
    if mistake > 30:
        print('Вы прекрасно справились с заданием, оценка - отлично  Вы набрали ' + str(mistake) + '  баллов')
    elif mistake > 25 and mistake <= 30:
        print('Вы неплохо справились с заданием, оценка - хорошо   Вы набрали  ' + str(mistake) + '  баллов')
    elif mistake > 20 and mistake <= 25:
        print("Вы плохо справились с заданием, оценка - удовлетворительно  Вы набрали  " + str(mistake) + '  баллов')
    else:
        print("Вам следует больше уделить внимания этому тесту, оценка плохо Вы набрали" + str(mistake) + '  баллов')
    mistake = {"Общее количество баллов": mistake}
    test.update(mistake)
    return test
test_student = test_matematik()
print(test_student)
# Функция сериализации данных словаря в строку для удобного вывода на экран
def serialize(test_student):
    res = "Вопрос 2x2=?' :   {}\n"\
          "Вопрос 3x3=? :    {}\n" \
          "Вопрос 23-15=? :  {}\n" \
          "Вопрос sin(180)=?: {}\n" \
          "Вопрос 120:5=? :   {}\n"\
          "Вопрос 45x4=?   :  {}\n"\
          "Вопрос cos(90)=? : {}\n"\
          "Общее количество баллов: {}".format(test_student["Вопрос 2x2=?"],
                                         test_student["Вопрос 3x3=?"],
                                         test_student["Вопрос 23-15=?"],
                                         test_student["Вопрос sin(180)=?"],
                                         test_student["Вопрос 120:5=?"],
                                         test_student["Вопрос 45x4=?"],
                                         test_student["Вопрос cos(90)=?"],
                                         test_student["Общее количество баллов"])
    return res
ser_stud = serialize(test_student)
print(ser_stud)

import json
# Функция сохранения данных в формате json  в файл fil
def user_json_dumps():
    fil = input("Введите с клавиатуры имя файла, в который нужно записать данные:  ")
    json_dumps_user = json.dumps(test_student)
    with open(fil, 'w') as f:
        f.write(json_dumps_user)
    print(json_dumps_user)
user_json_dumps()