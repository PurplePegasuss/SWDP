# Кирилл Глинский, MS23
# 04.10.23
# @amrtized - tg

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.status = "в вольере"
  
class ZooKeeper:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.animals = []  

class Zoo:
    def __init__(self):
        self.animals = []
        self.zookeepers = []

    def sort_animals(self, key=lambda x: x.name):
        self.animals.sort(key=key)  

    def sort_zookeepers(self, key=lambda x: (x.first_name, x.last_name)):
        self.zookeepers.sort(key=key)


    def log_action(action):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                print(f"Запись: {action}")
                return result
            return wrapper
        return decorator

    @log_action("добавлено новое животное")
    def add_animal(self, name, species):
        self.animals.append(Animal(name, species))

    @log_action("принят новый сотрудник")
    def hire_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)

    def list_animals(self):
        return self.animals

    def list_zookeepers(self):
        return self.zookeepers 
  

# Класс для более специфических животных
class ExoticAnimal(Animal):
    def __init__(self, name, species, origin):
        super().__init__(name, species)
        self.origin = origin

# Класс для смотрителей-ветеринаров
class Veterinarian(ZooKeeper):
    def __init__(self, first_name, last_name, specialization):
        super().__init__(first_name, last_name)
        self.specialization = specialization

class ZooExtensionManager:
    def __init__(self):
        self.extensions = []

    def add_extension(self, extension_function):
        self.extensions.append(extension_function)

    def apply_extensions(self, zoo):
        for extension_function in self.extensions:
            extension_function(zoo)

# Создаем зоопарк
zoo = Zoo()

# Создаем расширение для зоопарка
zoo_extension_manager = ZooExtensionManager()

# Определяем функцию расширения 
def change_animal_status(zoo):
    for animal in zoo.animals: 
        if len(animal.name) > 10: 
            animal.status = "Ультраредкое животное!"

# Добавляем функцию расширения
zoo_extension_manager.add_extension(change_animal_status)

# Создаем животное
zoo.add_animal("Лунтик", "Инопришелец")  
 
# Применяем расширения
zoo_extension_manager.apply_extensions(zoo)
  
# Выводим статус животного
animal = zoo.animals[0]
print(f"Состояние животного: {animal.status}")