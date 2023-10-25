Курсовая работа.

Программа для сбора вакансий с сайта HH.ru и SuperJob по API.

Древо файлов:
    'main.py' - файл с кодом для запуска программы
    'abstract_class.py '- файл с абстрактным классом
    'class_for_save' - файл с классом для работы с файлом 'vacancies.json'
    'classes' - файл с классами для работы с сайтами HeadHunter.ru и SuperJob.ru по API
    'vacancy.py' - класс обработки данных с ресурса

Работа программы:

Пользователь: вводит ключевое слово вакансии
              выбирает платформу для поиска
              вводит количество вакансий для отображения

Программа по API делает запрос к сайту, по ключевому слову собирает информацию и записывает данные в файл 'vacancies.json'.
Затем редактирует информацию по необходимой форме, сортирует по зарплате в порядке убывания, выводит список в консоль.
