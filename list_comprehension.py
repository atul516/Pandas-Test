# Python is famous for allowing you to write code that’s elegant, easy to write, and almost as easy to read as plain English. 
# One of the language’s most distinctive features is the list comprehension, which you can use to create powerful functionality
# within a single line of code. However, many developers struggle to fully leverage the more advanced features of a list 
# comprehension in Python. Some programmers even use them too much, which can lead to code that’s less efficient and harder to read.

#Rewrite loops and map() calls as a list comprehension in Python

#Choose between comprehensions, loops, and map() calls
squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

#new_list = [expression for member in iterable]
squares1 = [x*x*x for x in range(10) if x%2==0]
print(squares1)

# Here, you have an iterable txns and a function get_price_with_tax(). You pass both of these arguments to map(), and store
#  the resulting object in final_prices. You can easily convert this map object into a list using list().
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
final_prices = map(get_price_with_tax, txns)
print(list(final_prices))

#range doesn't return list
print(isinstance(range(10), list))

#Supercharge your comprehensions with conditional logic

#Use comprehensions to replace filter()

#Profile your code to solve performance questions