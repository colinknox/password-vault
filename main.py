class PasswordVault:
    def __init__(self, master_password):
        self.__master_password = master_password
        self.__stored_password = None
        self.__is_locked = True
        self.__failed_attempts = 0

    def unlock(self, password_attempt):
        if self.__validate_master_password(password_attempt):
            self.__is_locked = False
            self.__reset_attempts()
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
    
    def __validate_master_password(self, password):
        if password == self.__master_password:
            return True
        else:
            return False
        
    def __reset_attempts(self):
        self.__failed_attempts = 0
