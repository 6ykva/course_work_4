from class_for_save import JsonSave
from classes import HeadHunterAPI, SuperJobAPI
from vacancy import Vacancy

if __name__ == "__main__":
    print(f"Программа для поиска вакансий\n")

    JsonSave.remove_file()
    vacancy = input(f"Введите ключевое слово для поиска вакансии, например 'Java': ")
    platform = input(f"Выбери платформу для поиска:\n"
                     f"1 - HeadHunter\n"
                     f"2 - SuperJob\n"
                     f"0 - Выход из поиска\n"
                     f"-> ")

    if platform == "1":
        total_view = int(input(f"Введите количество вакансий для вывода: "))
        print(f'Выводим список из {total_view} вакансий отсортированных по зарплате:\n')

        hh_api = HeadHunterAPI(vacancy)  # Создаём экземпляр Класса для извлечения информации по API
        all_vacancy = hh_api.get_vacancies()  # Получаем список вакансий с HH
        all_vacancies = hh_api.formate_vacancies(all_vacancy)  # Форматируем список по шаблону

        Vacancy.output_final_result(all_vacancies, total_view)  # Выводим конечный результат

    elif platform == "2":
        total_view = int(input(f"Введите количество вакансий для вывода: "))
        print()
        print(f'Вывожу список из {total_view} вакансий отсортированных по зарплате:\n')
        print()
        sj_api = SuperJobAPI(vacancy)  # Создаём экземпляр Класса для извлечения информации по API
        all_vacancy = sj_api.get_vacancies()  # Получаем список вакансий с HH
        all_vacancies = sj_api.formate_vacancies(all_vacancy)  # Форматируем список по шаблону

        Vacancy.output_final_result(all_vacancies, total_view)  # Выводим конечный результат

    elif platform == "0":
        print("Выход из поиска")

    else:
        print('В этой программе нет такой платформы')
