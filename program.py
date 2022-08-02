from libs.function import *
filename = input('Enter supplies filename: ')
_path = 'files/' + filename
data = []
tt = 1
while tt == 1:
    print('')
    print('--- PRODUCT MANAGEMENT ---')
    print('1. Open file\n2. Add a product\n3. Save product file\n4. Print product list\n5. Find product by ID\n6. Delete product by ID\n7. Inventory count\n8. Sort product by category')
    action = int(input('Choose an action: '))
    if action == 1:
        file = OpenFile(_path)
        print(file)
    elif action == 2:
        AddProduct(data)
        print('Added.')
    elif action == 3:
        SaveProductFile(_path, data)
        print('Saved.')
    elif action == 4:
        print('PRODUCT LIST')
        PrintProductList(data)
    elif action == 5:
        mavt = input('Enter product ID to find: ')
        result = FindProductByID(data, mavt)
        if result != None:
            print(result)
        else:
            print('Not found.')
    elif action == 6:
        mavt = input('Enter product ID to delete: ')
        result = DeleteProductByID(data, mavt)
        if result == 1:
            print('Done.')
        else:
            print('Not found.')
    elif action == 7:
        print('Inventory quantity = ', InventoryCount(data))
    elif action == 8:
        print('PRODUCT LIST BY CATEGORY')
        print(SortProductByCategory(data)) 
    tt = int(input('Do you want to choose another action? (1: Continue / 0: Quit) '))