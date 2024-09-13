# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 9.3.5 answer

# CELL 1

def pairs(store: list, voucher: int) -> set:
    results = set()
    products_by_price = []
    for price in range(voucher):
        products_by_price.append([])

    for product in store:
        price = product[1]
        if price < voucher:
            products_by_price[price].append(product)
            for matched in products_by_price[voucher - price]:
                results.add( (matched, product) )
    return results