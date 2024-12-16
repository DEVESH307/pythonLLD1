import threading


class dbConn:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)

        return cls.__instance


s1 = dbConn()
s2 = dbConn()

print(s1 == s2)


# TODO: 1. CREATE A LOGGER IN SINGLETON DP..
#       2. TEST the above code with and without locks in Multi threading env...
