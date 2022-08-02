import csv

def OpenFile(_path):
    data = []
    f = open(_path)
    for row in csv.reader(f):
        data.append(row)
    f.close()
    return data

def AddProduct(data):
    tt = 1
    while tt == 1:
        id = input('Enter product ID: ')
        productname = input('Enter product name: ')
        unit = input('Enter unit: ')
        unitprice = eval(input('Enter unit price: '))
        quantity = eval(input('Enter inventory quantity: '))
        category = input('Enter product category: ')
        data.append([id, productname, unit, unitprice, quantity, category])
        tt = int(input('Do you want to continue adding another product? (1: Continue / 0: Finish) '))
    return

def SaveProductFile(_path, data):
    f = open(_path, 'a', newline='')
    csv.writer(f).writerows(data)
    f.close()
    return

def PrintProductList(data):
    print('ID\tProduct name\tUnit\tUnit price\tInventory quantity\tCategory')
    for row in data:
        print(row[0], '\t',row[1], '\t',row[2], '\t',row[3], '\t',row[4], '\t',row[5])
    return

def FindProductByID(data, mavt):
    for row in data:
        if row[0] == mavt:
            return row
    return None

def DeleteProductByID(data, mavt):
    for i in range(len(data)):
        row = data[i]
        if row[0] == mavt:
            del(data[i])
            return 1
    return 0

def InventoryCount(data):
    sum = 0
    for i in range(len(data)):
        row = data[i]
        sum += row[4]
    return sum

def SortProductByCategory(data):
    sorted_data = sorted(data, key=lambda x: x[5])
    return sorted_data