import allure

from base_allsports.base_allsports import AllsportsBaseService


class AllsportsApiService(AllsportsBaseService):

    @allure.step('Get supplier info')
    def get_supplier_info(self, supplier_id):
        response = self.get(f'supplier(id:{supplier_id})')
        return response
