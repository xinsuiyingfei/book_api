from utils.interface import http
from api.public_variable import variable


class Book:

    def get_books(self, book_name=""):
        #获取书籍列表
        response = http.get(f"api/book/?book_name={book_name}")
        return response

    def add_book(self, book_name, branch_id):
        #添加书籍
        body = {"book_name": book_name, "branch_id": branch_id,
                "author": "张三", "press": "清华", "book_summary": "python从入门到精通"}
        response = http.post("api/book/", body)
        variable.book_id = response['id']   #存放书籍ID
        return response

    def up_book(self, id, book_name, branch_id):
        # 根据书籍ID，修改书籍信息
        body = {"book_name": book_name, "branch_id": branch_id,
                "author": "张三", "press": "清华", "book_summary": "python从入门到精通"}
        response = http.put(f"api/book/{id}/", body)
        return response

    def del_book(self,id):
        #删除书籍
        response = http.delete(f"api/book/{id}/")
        return response
