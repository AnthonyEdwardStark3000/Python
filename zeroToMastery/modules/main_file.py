import utilities
import shopping.shopping_cart as shopping_cart
from shopping.shopping_cart import max

if __name__ == '__main__':
    print(utilities.multiply(1, 20))
    print(shopping_cart.cart(['Cashew', 'plums', 'cake']))
    print(f'I wish to say {max([1,3,2,45,6])}')
    print(__name__)
