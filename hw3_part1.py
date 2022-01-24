COMMAND = 0
NAME = 2
PRICE = 3
AMOUNT = 4
SUBLIST_NAME = 0
SUBLIST_PRICE = 1
SUBLIST_AMOUNT = 2
PROFIT = 3


def process_commands(file_name):
    file = open(file_name, 'r')
    products = []
    for line in file:
        if(line[-1] == "\n"):
            line = line[:-1]
        current_line = line.split(" ")
        
        if(current_line[COMMAND] == "add"):
            current_line[PRICE] = float(current_line[PRICE])
            current_line[AMOUNT] = float(current_line[AMOUNT])
            already_exists = current_line[NAME] in [product[0] for product in products] # list of the names of products
            if(already_exists):
                continue
            if(current_line[PRICE] >= 0 and current_line[AMOUNT] >= 0):
                product = [current_line[NAME], current_line[PRICE], current_line[AMOUNT], 0]
                products.append(product)
        
        if(current_line[COMMAND] == "change"):
            current_line[AMOUNT-1] = float(current_line[AMOUNT-1]) # still refers to amount, command is simply 1 string shorter
            for sublist in products:
                if(sublist[SUBLIST_NAME] == current_line[NAME]):
                    sublist[SUBLIST_AMOUNT] += current_line[AMOUNT-1]
                    break
        
        if(current_line[COMMAND] == "ship"):
            current_line = line[11:]  # dumps first two words
            current_line = current_line.split(" -- ")
            for order_sublist in current_line:
                order_sublist = order_sublist.split(", ")
                order_sublist[1] = float(order_sublist[1])
                for products_sublist in products:
                    if(order_sublist[SUBLIST_NAME] == products_sublist[SUBLIST_NAME] and products_sublist[SUBLIST_AMOUNT] > 0 
                        and order_sublist[1] <= products_sublist[SUBLIST_AMOUNT]):
                        products_sublist[SUBLIST_AMOUNT] -= order_sublist[1]
                        products_sublist[PROFIT] += order_sublist[1] * products_sublist[1]
    file.close()
    return products

def find_best_selling_product(file_name):
    products = process_commands(file_name)
    products = sorted(products, key=lambda product: product[SUBLIST_NAME])
    products = sorted(products, key=lambda product: product[PROFIT], reverse = True)
    if products:
        return (products[0][0], products[0][PROFIT])
    return ("", 0)

def find_k_most_expensive_products(file_name, k):
    if(k <= 0):
        return []
    products = process_commands(file_name)
    if(not products):
        return []
    products = sorted(products, key=lambda product: product[SUBLIST_NAME])
    products = sorted(products, key=lambda product: product[1], reverse = True)
    return [product[0] for product in products[:k]]
              







