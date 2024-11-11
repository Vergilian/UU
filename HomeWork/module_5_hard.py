from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other,User):
            return self.nickname == other.nickname and self.password == hash(other.password)
        return False

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=bool(False)):
        self.title = title
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
        if isinstance(item, User):
            return any(user == item for user in self.users)
        elif isinstance(item, Video):
            return any(existing_video.title == item.title for existing_video in self.video)
        elif isinstance(item, str):
            return any(item.lower() in video.title.lower() for video in self.video)
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.log_in(nickname, password)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            self.current_user = user
            # print(f"Добро пожаловать {nickname}")
            return



    def log_out(self, nickname, password):
        print(f"{self.current_user} вышел из системы.")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video in self:
                print('Данное видео добавлено ранее')
            else:
                self.video.append(video)

    def get_videos(self, search):
        search = search.lower()
        list_search = []
        for video in self.video:
            if search in video.title.lower():
                list_search.append(video)
        return list_search

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.video:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(video.time_now, video.duration):
                    sleep(1)
                    print(f"{second + 1}", end=" ", flush=True)
                    video.time_now = second + 1
                print("Конец видео")
                if video.time_now == video.duration:
                    video.time_now = 0
                return


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
