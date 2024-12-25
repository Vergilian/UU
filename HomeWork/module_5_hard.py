from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        self.age = int(age)

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname and hash(self.password) == hash(other.password)
        return False


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.video = []
        self.current_user = None

    def __contains__(self, item):
        # Если item строка, проверяем наличие видео с таким названием
        if isinstance(item, str):
            for video in self.video:
                if item == video.title:
                    return True
        if isinstance(item, Video):
            return item in self.video
        if isinstance(item, User):
            return item in self.users
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        temp_user = User(nickname, password, 0)
        for user in self.users:
            if user == temp_user:
                self.current_user = user
                return

    def log_out(self):
        print(f"{self.current_user} вышел из системы.")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.video:
                self.video.append(video)

    def get_videos(self, search):
        list_video = []
        for video in self.video:
            if search.lower() in video.title.lower():
                list_video.append(video)
        return list_video

    def watch_video(self, title_film):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.video:
            if title_film == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for sec in range(1, video.duration + 1):
                    sleep(1)
                    print(sec, end=' ')
                print("Конец видео")
                video.time_now = 0
                return


# Код для проверки:
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
