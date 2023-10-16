import allure

from allsports_api.allsports_api import AllsportsApiService
from base_allsports.base_allsports import AllsportsBaseService


@allure.suite('Supplier tests')
@allure.title('Supplier ID check')
@allure.step('Check ID of supplier')
def test_supplier_id():
    allsports_service = AllsportsApiService()
    response = allsports_service.get_supplier_info(1400)
    assert response["id"] == 1400, "ID test failed!"


@allure.suite('Supplier tests')
@allure.title('Supplier name check')
@allure.step('Check name of supplier')
def test_supplier_name():
    allsports_service = AllsportsApiService()
    response = allsports_service.get_supplier_info(1400)
    assert response["name"] == "SupplierName", "Name test failed"


@allure.suite('Supplier tests')
@allure.title('Supplier info check')
@allure.step('Check info of supplier')
def test_supplier_info():
    allsports_service = AllsportsApiService()
    response = allsports_service.get_supplier_info(1400)
    assert response["info"] == "SupplierInfo", "Info test failed"


@allure.suite('License Page tests')
@allure.title('Check License Page data')
@allure.step('Check License Page data')
def test_license_page_data():
    allsports_service = AllsportsBaseService()
    response = allsports_service.get('/page-data/by/license/230306_license/page-data.json')

    assert 'title' in response, "Title not found in the response"
    assert 'description' in response, "Description not found in the response"
    assert 'content' in response, "Content not found in the response"


@allure.suite('Policy Page tests')
@allure.title('Check Policy Page data')
@allure.step('Check Policy Page data')
def test_policy_page_data():
    allsports_service = AllsportsBaseService()
    response = allsports_service.get('/page-data/by/policy/220218_processing_personal_data/page-data.json')

    assert 'title' in response, "Title not found in the response"
    assert 'description' in response, "Description not found in the response"
    assert 'content' in response, "Content not found in the response"
