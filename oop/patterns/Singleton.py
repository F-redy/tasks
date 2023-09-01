class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            match args:
                case str(username), str(password), int(port), *_:
                    cls.__instance.username = username
                    cls.__instance.password = password
                    cls.__instance.port = port
                case _ as error:
                    raise AttributeError(f'{error}')
        return cls.__instance

    def __del__(self):
        self.__instance = None

    def __str__(self):
        return f'{self.username}:{self.password}:{self.port}'


db1 = DataBase('Fredy', '5644977', 80)
db2 = DataBase('XAM', '6771087', 50)
print(id(db1))
print(id(db2))
print(db1)
print(db2)
