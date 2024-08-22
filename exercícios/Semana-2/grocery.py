# Escreva um programa que permita o usuário adicionar itens na lista e depois imprimi-la

LIST_ITEM = []

def grocery():
    is_grocery = True

    while is_grocery:
        list_item = input("Type a item do add or 0 to exit the grocery: ")
        if list_item != "0":
            LIST_ITEM.append(list_item)
        else:
            is_grocery = False
            
def print_list(grocery_list): 
    for item in grocery_list:
        print(f"Items list: {item}")

grocery()
print_list(LIST_ITEM)