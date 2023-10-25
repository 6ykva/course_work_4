import os
import requests
from abstract_class import GetAPI


class HeadHunterAPI(GetAPI):
    """
    Класс для получения вакансий по API c HH.ru
    """
    HH_API = 'https://api.hh.ru/vacancies'

    def __init__(self, vacancy):
        self.vacancy = vacancy
        self.params = {
            'per_page': 100,
            'text': vacancy,
            'area': 1
        }

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.params['per_page']}', {self.params['text']},"
                f" {self.params['area']}')")

    def get_vacancies(self):
        """
        Получение вакансий с сайта
        """
        response = requests.get(self.HH_API, self.params)
        return response.json()

    def formate_vacancies(self, all_vacancies):
        """
        Приведение списка вакансий к необходимой форме
        """
        vacancies_to_dict = {'vacancies': []}
        for vacancy in all_vacancies['items']:
            if vacancy['salary'] is None:
                salary = "З/п не указана"
            elif vacancy['salary']['from'] is None:
                salary = vacancy['salary']['to']
            elif vacancy['salary']['to'] is None:
                salary = vacancy['salary']['from']
            else:
                salary = (int(vacancy['salary']['from']) + int(vacancy['salary']['to'])) // 2
            my_form_dict = {'name': vacancy['name'], 'url': vacancy['url'], 'salary': salary,
                            'experience': vacancy['experience']['name']}
            vacancies_to_dict['vacancies'].append(my_form_dict)
        return vacancies_to_dict


class SuperJobAPI(GetAPI):
    """
    Класс для получения вакансий по API SuperJob.ru
    """

    def __init__(self, vacancy):

        self.base_url = "https://api.superjob.ru/2.0"
        self.SJ_API = 'https://api.superjob.ru/2.0/vacancies/'
        self.vacancy = vacancy
        self.params = {
            "keyword": self.vacancy,
            'id': 1,
            'count': 29
        }

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.params['count']}', {self.params['keyword']},"
                f" {self.params['id']}')")

    def get_vacancies(self):
        """
        Получение вакансий с сайта
        """
        url = f"{self.base_url}/vacancies"
        api_key = os.getenv('SJ_API')
        headers = {"X-Api-App-Id": api_key}
        response = requests.get(url, params=self.params, headers=headers)

        return response.json()

    def formate_vacancies(self, all_vacancies):
        """
        Приведение списка вакансий к необходимой форме
        """
        vacancies_to_dict = {'vacancies': []}
        for vacancy in all_vacancies['objects']:
            if vacancy['payment_from'] is None:
                salary = "З/п не указана"
            elif vacancy['payment_to'] is None:
                salary = vacancy['payment_from']['to']
            elif vacancy['payment_to'] is None:
                salary = vacancy['payment_from']['from']
            else:
                salary = (int(vacancy['payment_from']) + int(vacancy['payment_to'])) // 2
            my_form_dict = {'name': vacancy['profession'], 'url': vacancy['client']['link'], 'salary': salary,
                            'experience': vacancy['experience']['title']}
            vacancies_to_dict['vacancies'].append(my_form_dict)
        return vacancies_to_dict
