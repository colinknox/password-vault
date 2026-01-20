class PasswordVault:
    def __init__(self, master_password):
        self.__master_password = master_password
        # self.__stored_password = None
        self.__is_locked = True
        self.__failed_attempts = 0
        print(f"DEBUG: is locked = {self.__is_locked}")
        print(f"DEBUG: failed attempts = {self.__failed_attempts}")

    def unlock(self, password_attempt):
        if password_attempt == self.__master_password:
            self.__is_locked = False
            self.__failed_attempts = 0



finster = PasswordVault("power")
print(finster.unlock("power"))
