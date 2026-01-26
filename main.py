class PasswordVault:
    def __init__(self, master_password):
        self.__master_password = master_password
        self.__stored_password = None
        self.__is_locked = True
        self.__failed_attempts = 0

    def unlock(self, password_attempt):
        if password_attempt == self.__master_password:
            self.__is_locked = False
            self.__failed_attempts = 0
        else:
            self.__failed_attempts += 1
            print(f"ERROR: Incorrect password. You have {self.__failed_attempts}/3 attempts left.")
            
            if self.__failed_attempts >= 3:
                print("Vault locked permanently!")
        
    def lock(self):
        self.__is_locked = True

    def store_password(self, password):
        if self.__is_locked == True:
            print("ERROR: Your password vault is locked.")
        else:
            self.__stored_password = password

    def get_password(self):
        if self.__is_locked == True:
            print("ERROR: Your password vault is locked.")
            return None
        else:
            return self.__stored_password

    def get_failed_attempts(self):
        return self.__failed_attempts


finster = PasswordVault("power")

finster.unlock("pow")
finster.unlock("posw")
finster.unlock("power")
finster.store_password("floor")
print(finster.get_password())
print(finster.get_failed_attempts())

# print(finster.lock())