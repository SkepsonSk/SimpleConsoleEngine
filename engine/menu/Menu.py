class Menu:

    menus = []

    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.options = []
        Menu.menus.append(self)

    def add_option(self, option):
        self.options.append(option)

    @staticmethod
    def initialize():
        print("Initializing menus...")

    @staticmethod
    def get(name):
        for menu in Menu.menus:
            if menu.name == name:
                return menu
        return None
