import os
from menu import (  start_menu, database_menu )

class Controller:
    def __init__(self):
        self.__startup_menu = self.Start_menu(self)
        self.__db_menu = self.Database_menu(self)

    def run(self):
        self.__startup_menu.run()

    def create_new_database(self):
        self.__db_menu.create_new_database()

    def use_existing_database(self):
        self.__db_menu.use_existing_database()

    def get_db_name(self):
        return self.__db_name

    def set_db_name(self, db_name):
        self.__db_name = db_name

    def get_db(self):
        return self.__db

    def set_db(self, db):
        self.__db = db

    class Start_menu:
        def __init__(self, outer):
            self.__action = 0
            self.__outer = outer

        def run(self):
            start_menu()
            self.__read_startup_menu_action()
            print()
            self.__switch_action()
            print()

        def __read_startup_menu_action(self):
            self.__action = int(input("Was möchten Sie tun? "))

        def __switch_action(self):
            match self.__action:
                case 1:
                    self.__outer.create_new_database()
                case 2:
                    self.__outer.use_existing_database()
                case 3:
                    exit() 
     
    class Database_menu:
        def __init__(self, outer):
            self.__action = 0
            self.__outer = outer 
            
        def switch_db_menu_action(self):
            match self.__action:
                case 1:
                    self.read_file()
                case 2:
                      self.write_file()
                case 3:
                    self.delete_file()
                # case 4:
                #      self.update_file()
                case 5:
                        exit() 
        def __read_startup_menu_action(self):
            self.__action = int(input("Was möchten Sie tun? "))
           # self.switch_db_menu_action()
           # show_db_menu(self.__outer.get_db_name())
            
        def create_new_database(self):
            self.__outer.set_db_name(input("Name der neuen Datenbank: "))
            #db_name = input("Name der neuen Datenbank: ")
            my_file = open( str(self.__outer.get_db_name()), "w+")
            my_file.close()
            database_menu(self.__outer.get_db_name())
            self.__read_startup_menu_action()
            print()
            self.switch_db_menu_action()
            print()
        
    
        def use_existing_database(self):
            self.__outer.set_db_name(input("Name der Datenbank: "))
           # my_file = open( str(self.__outer.get_db_name()), "r+")
            #my_file.close()
            database_menu(self.__outer.get_db_name())
            self.__read_startup_menu_action()
            print()
            self.switch_db_menu_action()
            print()
            
    
        def write_file(self):
            my_file = open(str(self.__outer.get_db_name()), "a+")
            my_file.writelines("username: " + str(input("username: ")))
            my_file.writelines("  password: " +str(input("password: ")))
            my_file.write('\n')
            my_file.close()
            print("------------")
            print("fertig")
            
        
        def read_file(self):
            print("existierende Passwörter")
            my_file = open(str(self.__outer.get_db_name()), "r+")
            print(my_file.read())
               
        def delete_file(self):
            print("Löschung")
            os.remove(str(self.__outer.get_db_name()))
            print("------------")
            print("fertig")
            
            
        # def update_file():
        #     print("update")    