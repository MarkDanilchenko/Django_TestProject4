from . import models

# Report_1
def report1__nameSurname__seller():
    result_arr = []
    result = models.Seller.objects.values('name', 'surname').distinct()
    for i in result:
        result_arr.append(f'{i["name"]} {i["surname"]}')
    return result_arr

# Report_3
def report3__itemName():
    result_arr = []
    result = models.Item.objects.values('name').distinct()
    for i in result:
        result_arr.append(i['name'])
    return result_arr