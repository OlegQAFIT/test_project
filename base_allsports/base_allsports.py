import allure
import requests


class AllsportsBaseService:
    BASE_URL = 'https://www.allsports.fit/graphql'

    @allure.step('URL: {url}')
    def get(self, url, code=200):
        response = requests.get(self.BASE_URL + url)
        assert response.status_code == code, f'Have code = {response.status_code}'
        return response.json()

    @allure.step('URL: {url}')
    def post(self, url, body, code=200):
        response = requests.post(self.BASE_URL + url, json=body)
        assert response.status_code == code
        return response.json()
