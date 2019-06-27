import sys

book='pythön!'
b_book=book.encode()

for b in b_book:
    print(b)

new=b_book.__sizeof__()

len_book=len(book)
len_b_book=len(b_book)
size_book_size=sys.getsizeof(book)
size_b_book=sys.getsizeof(b_book)
1==1