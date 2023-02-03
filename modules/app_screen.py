import customtkinter
# створюємо клас App 
class App1(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH}+{self.PC_SCREEN_HEIGHT - self.APP_HEIGHT // 2}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
class App2(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
class App3(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH}+{0}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")

class App4(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{self.PC_SCREEN_HEIGHT - self.APP_HEIGHT // 2}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
class App5(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.PC_SCREEN_WIDTH // 2}+{self.PC_SCREEN_HEIGHT // 2}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
        



app1 = App1(app_width= 400, app_height = 300)
app2 = App2(app_width= 400, app_height = 300)
app3 = App3(app_width= 400, app_height = 300)
app4 = App4(app_width= 400, app_height = 300)
app5 = App5(app_width= 400, app_height = 300)
