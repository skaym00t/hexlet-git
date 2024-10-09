#Цель упражнения — функция count_all(). Эта функция должна принимать на вход итерируемый источник и возвращать словарь. Ключами этого словаря должны стать элементы источника, при этом значения должны отражать количество повторов элемента в коллекции-источнике.

#Посмотрим на этих примерах, как должна работать эта функция:

#count_all(["cat", "dog", "cat"])  # {"cat": 2, "dog": 1}
#count_all("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#count_all("*" * 20)  # {'*': 20}

def count_all(item):
    count_dict = {}
    for i in item:
        count_dict[i] = count_dict.get(i, 0) + 1
    return count_dict

print(count_all("hello"))


#Цель упражнения — написать функцию collect_indexes(). Эта функция должна:

#Принимать на вход коллекцию — некий итератор или итерируемый элемент
#Возвращать словарь или подобную ему коллекцию. Ключом будет элемент коллекции, а значением для ключа — список индексов коллекции, по которым встречается этот элемент
#d = collect_indexes("hello")
#d["h"]  # [0]
#d["e"]  # [1]
#d["l"]  # [2, 3]

def collect_indexes(item):
    d = {}
    start_index = 0
    for i in item:
        d.setdefault(i, []).append(item.index(i, start_index))
        start_index += 1
    return d

print(collect_indexes("hello"))