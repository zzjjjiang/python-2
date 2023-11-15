# define your methods here.
# ex1() - ex10()
from .WordCounter import WordCounter
from .TaxMan import TaxMan
from .Calculator import Calculator
from .CarCollector import CarCollector
from pprint import pprint
from .Fighter import Fighter
from .Dwarf import Dwarf
from .Invoice import Invoice
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'asc')
    print(people_list)
    
def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)

def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)
    
def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.
    
def ex6():
    items = [
    {"id": 1, "desc": "clock", "price": 1.00},
    {"id": 2, "desc": "socks", "price": 2.00},
    {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())
    
def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

def ex8():
    pprint(CarCollector.get_data()) 
    
def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)
    
def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]
    # invoice_data = list(map(lambda r: Invoice(r.split(", ")), data))
    invoice_data = [Invoice(*x.split(", ")) for x in data]
    # invoice_data = [Invoice(invoice_id, user_id, amount, paid) for i in list(map(lambda l: l.split(", "), data)) for invoice_id, user_id, amount, paid in i ]
    #invoice_data = list(map(lambda l: Invoice(l[0], l[1], l[2], l[3]), list(map(lambda r: r.split(", "), data))))
    pprint(invoice_data)
    

def sort_people(lst, key, dir):
    lst.sort(reverse=False if dir == "asc" else True, key = lambda p : p[key])
    
def filter_males(lst):
    return list(filter(lambda p: p['sex']=='male', lst))

def calc_bmi(people_list):
    lst = list(map(lambda p: {
        'bmi' : round(p['weight_kg']/p['height_meters'] ** 2, 1)}, people_list))
    i=0
    while i < len(people_list):
        people_list[i].update(lst[i])
        i+=1
    return people_list
    
    
    # return list(map(lambda p: {
    #     'id' : p['id'],
    #     'name' : p['name'],
    #     'weight_kg' : p['weight_kg'],
    #     'height_meters' : p['height_meters'],
    #     'bmi' : round(p['weight_kg']/p['height_meters'] ** 2, 1)}, people_list))
    
def get_people(lst):
    return [p['name'] for p in lst if p['age'] >= 15]