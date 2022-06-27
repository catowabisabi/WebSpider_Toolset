import json
import jsonpath

# 建立json物件
json_obj = json.load(open('20_books.json', 'r', encoding='utf-8'))


# 書店所有書的作者
author_list = jsonpath.jsonpath(json_obj, '$.store.books[*].author')
print (author_list)

author = jsonpath.jsonpath(json_obj, '$.store.books[7].author')
print (author)

# 所有的作者
author_list = jsonpath.jsonpath(json_obj, '$..author') #所有author key
print (author_list)

# store的所有元素 包括books 和 bicycle
all_list = jsonpath.jsonpath(json_obj, '$.store.*')
print (f"\n {all_list}")

# store的所有isbn
price_list = jsonpath.jsonpath(json_obj, '$.store..isbn') 
print (f"\n {price_list}")

# store的第三本書
book3 = jsonpath.jsonpath(json_obj, '$..books[2]') 
print (f"\n book 3 = {book3}")

# store的第三本書
book_last = jsonpath.jsonpath(json_obj, '$..books[(@.length-1)]') 
print (f"\n book last = {book_last}")

# store的第三本書
book_last = jsonpath.jsonpath(json_obj, '$..books[(@.length-1)]') 
print (f"\n book last = {book_last}")

# store的前兩本書
book_0_1 = jsonpath.jsonpath(json_obj, '$..books[:2]') 
print (f"\n book 1 & 2 = {book_0_1}")

# 提出所有有isbn的書
book_with_isbn = jsonpath.jsonpath(json_obj, '$..books[?(@.test_title)]')
print ((f"\n 有isbn的書的資料為 = {book_with_isbn}"))

# 提出所有有isbn的書
book_with_isbn = jsonpath.jsonpath(json_obj, '$..books[?(@.test_title)]')
print ((f"\n 有isbn的書的資料為 = {book_with_isbn}"))

# 哪本書比10貴
book_greater_10 = jsonpath.jsonpath(json_obj, '$..books[?(@.price>10)]')
print ((f"\n 10元以上的書 = {book_greater_10}"))