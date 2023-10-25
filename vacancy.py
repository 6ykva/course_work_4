from class_for_save import JsonSave


class Vacancy:
    """
    Класс для работы с вакансиями
    """
    list_vacancies = []

    def __init__(self, name, url, salary, exp):
        self.name = name
        self.url = url
        if int == type(salary):
            self.salary = salary
        else:
            self.salary = 0
        self.exp = exp

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', '{self.url}',"
                f" {self.salary}, '{self.exp}')")

    def __str__(self):
        return (f"{self.__class__.__name__} Профессия: {self.name}, Адрес объявления: {self.url},"
                f"  Зарплата: {self.salary}, Опыт: {self.exp})")

    @staticmethod
    def instantiate_from_json():

        data = JsonSave.get_vacancy()

        for vacancy in data['vacancies']:
            Vacancy.list_vacancies.append(Vacancy(vacancy['name'], vacancy['url'],
                                                  vacancy['salary'], vacancy['experience']))
        return Vacancy.list_vacancies

    @classmethod
    def sort_vacancies(cls):
        """
        Сортировка вакансий по заработной плате.
        """
        cls.list_vacancies.sort(key=lambda vacancy: vacancy.salary, reverse=True)
        return cls.list_vacancies

    @staticmethod
    def get_top_vacancies(top: int, vacancies: list) -> list:
        """
        Получаем топ вакансий из списка.
        """
        return vacancies[:top]

    @staticmethod
    def print_vacancies(for_print: list):
        """
        Форма вывода данных о вакансии в консоль
        """
        count = 1
        for vacancy in for_print:
            print(
                f'Вакансия №{count}:\nНазвание:{vacancy.name}\nЗарплата:{vacancy.salary} '
                f'рублей\nОпыт работы: {vacancy.exp}\nАдрес объявления: {vacancy.url}\n')
            count += 1

    @staticmethod
    def output_final_result(all_vacancies, total_view):
        """
        Конечный результат вывода информации о вакансиях
        """

        JsonSave.add_vacancy(all_vacancies)  # Добавляем в файл json список с вакансиями.
        vacancies = Vacancy.instantiate_from_json()  # создаём список экземпляров класса из json файла
        sort_vacancies = Vacancy.sort_vacancies()
        top_vacancies = Vacancy.get_top_vacancies(top=total_view, vacancies=sort_vacancies)

        Vacancy.print_vacancies(top_vacancies)
