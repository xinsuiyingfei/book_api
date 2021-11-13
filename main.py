import  pytest

pytest.main(['-s','test_book','--alluredir','./report/'])   
# pytest.main(['-s','test_book','-k','book','--alluredir','./report/'])   #执行所有包含book的文件
# pytest -s  test_book --alluredir ./report/ --setting test2    
