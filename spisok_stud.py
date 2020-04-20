
import json
# Функция регистрации данных студента
def reg():
        login = input("Введите свой логин :")
        password = input("Введите свой пароль :")
        email = input("Введите свой email : ")
        # Запишем все регистрационные данные в файл(например список)
        with open("список", "w") as f:
                data = {}
                data["login"] = login
                data["password"] = password
                data["email"] = email
                json.dump(data, f)
                print(data)
save = reg()
print(save)
# Функция проверки введенных данных пользователя
def log(save):
        avtorizacia = "true"
        while avtorizacia == "true":
                login = input("Для авторизации введите ваш логин: ")
                password = input("Для авторизации введите ваш пароль:  ")
                with open("список", "r") as f:
                        data = json.load(f)
                        log = data["login"]
                        passw = data["password"]
                        if log == login and passw == password:
                                print("Данные введены корректно, авторизация прошла успешно")
                                break
                        else:
                                print("Некорректно введены логин или пароль")
                k = int(input("Если хотите еще раз попробовать авторизоваться, нажмите 1"))
                if k == 1:
                        avtorizacia = "true"
                else:
                        avtorizacia = "false"
                        break
s = log(save)
