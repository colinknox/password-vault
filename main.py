class PasswordVault:
    def __init__(self, master_password):
        self.__master_password = master_password
        # self.__stored_password = None
        self.__is_locked = True
        self.__failed_attempts = 0

    def unlock(self, password_attempt):
        if password_attempt == self.__master_password:
            self.__is_locked = False
            self.__failed_attempts = 0
        elif self.__failed_attempts >= 3:
            print("Vault locked permanently!")
        else:
            self.__failed_attempts += 1
            print(f"ERROR: Incorrect password. You have {self.__failed_attempts}/3 attempts left.")
        
        print(f"DEBUG: Is vault locked?: {self.__is_locked}")
        print(f"DEBUG: How many failed attempts: {self.__failed_attempts}")

            
    def lock(self):
        self.__is_locked = True
        print(f"DEBUG: Is locked?: {self.__is_locked}")





finster = PasswordVault("power")
print(finster.unlock("water"))
print(finster.unlock("gas"))
print(finster.unlock("solid"))
print(finster.unlock("lmao"))
# print(finster.unlock("power"))
# print(finster.lock())