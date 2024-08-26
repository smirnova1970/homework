import time

"""
модуль time, который используется для решения задач, связанных со временем. Функция time() 
возвращает число секунд, прошедших с начала эпохи. 

"""


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname    # имя
        self.password = password
        self.age = age     # возраст

    def __hash__(self):
        return hash(self.password)   # Хеширование пароля

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):

        # title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
        # adult_mode(ограничение по возрасту, bool (False по умолчанию))
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title}"


class UrTube:
    def __init__(self):
        self.users = []  # Список зарегистрированных пользователей
        self.videos = []  # Список доступных видео
        self.current_user = None  # Текущий пользователь

    #  пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует,
    #  то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    def long_in(self, nickname: str, password: str) -> None:
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int) -> None:
        # Метод register, который принимает три
        # аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует
        # (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        # После регистрации, вход выполняется автоматически.
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.long_in(user.nickname, user.password)

    def log_out(self):
        # Метод log_out для сброса текущего пользователя на None.
        self.current_user = None

    def add(self, *videos):  # Метод add, который принимает неограниченное кол-во объектов класса Video и все
        # добавляет в videos, если с таким же названием видео ещё не существует.
        # В противном случае ничего не происходит.
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, text: str):
        # принимает поисковое слово и возвращает список названий всех видео, содержащих
        # поисковое слово не учитывать регистр
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str) -> None:   # Метод watch_video, который принимает название фильма, если
        # не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит, ведётся
        # отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return f"{self.videos}"


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
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
    
