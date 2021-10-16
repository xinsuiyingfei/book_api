import pytest
import allure
from  utils.custom_logger import logger_cls
from api.public_variable import variable
from api.all_api import  api

@pytest.fixture(scope='class', autouse=True)  #autouse,自动执行
def front():
    logger_cls.info("类级别的-前置条件")
    return "111"



@pytest.fixture(scope='class', autouse=True)
def after():
    yield after
    logger_cls.info("类级别的-后置条件")

class Test_01:

    @allure.feature("获取书籍列表")
    def test_get_book(self):
        books=api.get_books("python从入门到精通")
        b=False
        for book in books:
            if book['book_name'] =="python从入门到精通":
                b=True
        assert b == True, "预期结果不等于实际结果"


    @allure.feature("添加书籍")
    @pytest.mark.parametrize('branch_id',[1,2,3]) 
    #parametrize 参数装饰器,有几个参数就执行几次这条用例  branch_id =1 branch_id =2 
    def test_add_book(self,branch_id):
        book=api.add_book(f"测试书籍{branch_id}",branch_id)
        assert book['book_name'] ==f"测试书籍{branch_id}", "预期结果不等于实际结果"


    @allure.feature("修改书籍")
    def test_up_book(self):
        id = variable.book_id  #获取刚才新增的书籍ID
        book=api.up_book(id,"自动化",1)
        assert book['book_name'] ==f"自动化", "预期结果不等于实际结果"


