'''
2023/11/05 00:00|Дополнительное практическое задание по модулю*
Дополнительное практическое задание по модулю: "Классы и объекты."
Файл с кодом (module5hard.py) прикрепите к домашнему заданию или
пришлите ссылку на ваш GitHub репозиторий с файлом решения.
'''
import time
# импортирую модуль time  для работы функции sleep(), отложить исполнение на кол-во сек

class User:
    # класс User атрибутами
    # nickname - логин строка,
    # password - пароль число
    # age - возраст число
    def __init__(self, nickname: str, password: int, age: int):
        # Инициализация объекта с атрибутами, password,age
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        # предназначен для создания читаемых пользователем строковых представлений объектов
        return self.nickname

class Video:
    # класс Video с атрибутами
    # title - название фильма строка,
    # duration - продолжительность видео, секунды
    # adult_mode - фиксирует ограничение по возрасту boll True False
    # time_now- секунда остановки число
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    # класс UrTube с атрибутами
    # users - список пользователей,
    # videos - список видео,
    # current_user - текущий пользователь
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, log_user: str, password: str):
        # Метод log_in, аргументы:
        # nickname- пользователь,
        # password- пароль,
        # Поиск пользователя в users список пользователей с такими же логином и паролем.
        # Если пользователь есть, то current_user меняется на найденного.
        for user in self.users:
            if log_user == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        # Метод register, регистрация пользователя в списке пользователя аргументы:
        # nickname- пользователь строка,
        # password- пароль строка,
        # age- возраст,
        # Проверка пользователя в users список пользователей с такими же логином.
        # Если пользователь есть, то Вывод Пользователь {nickname} уже существует.
        # Если нет - присваиваем New_user атрибуты класса и значения, добавляем в список,
        # присваиваем текущему пользователю нового пользователя
        password = hash(password)
        # хэширование пароля
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        # Метод log_out,
        # Текущий пользователь не имеет аргумент
        self.current_user = None

    def add(self, *args):
        # Метод add если нет такого видео - добавить в список видео
        for vidi in args:
            if vidi not in self.videos:
                self.videos.append(vidi)

    def get_videos(self, search_say: str):
        # Метод get_videos принимает поисковое слово search_say
        # и возвращает список названий всех видео list_vidi,
        # содержащих поисковое слово
        list_vidi = []
        for vidi in self.videos:
            if search_say.lower() in vidi.title.lower():
                list_vidi.append(vidi.title)
            return list_vidi

    def watch_video(self, vidi: str):
        # Метод watch_video принимает название фильма list_.
        # Проверяет если текущий пользователь не задан- "Войдите в аккаунт, чтобы смотреть видео".
        # Eсли не находит точного совпадения c vidi,то ничего не воспроизводится,
        # если же находит:
        # Проверяет на ограничение видео в возрасте, возрат текущего пользователя,
        #Если есть ограничение - Вам нет 18 лет, пожалуйста, покиньте страницу,
        #Остановка, если разрешено вывод отчёта
        # в консоль на какой секунде duration ведётся просмотр и интервалом 1сек
        # time.sleep(1)
        # После текущее время просмотра данного видео сбрасывается.

        if not self.current_user:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return

        for list_ in self.videos:
            if list_.title == vidi:
                if list_.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(list_.duration):
                    time.sleep(1)
                    j = i + 1
                    print(j, end=' ')
                    list_.time_now += 1

                list_.time_now = 0
                print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавить видео V1, V2
ur.add(v1, v2)

## Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
