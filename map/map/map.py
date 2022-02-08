
#Функция map() имеет следующий синтаксис:
#map(function, iterable, [iterable 2, iterable 3, ...])

#Синтаксис map() с функцией lambda выглядит следующим образом:

#map(lambda item: item[] expression, iterable)

numbers = [10, 15, 21, 33, 42, 55]

mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))

print(mapped_numbers)

a=list(map(int, input().split()))
print(a)

#Реализация определяемой пользователем функции


aquarium_creatures = [
    {"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
    {"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
    {"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
    {"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
    {"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
    {"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
]

def assign_to_tank(aquarium_creatures, new_tank_number):
    def apply(x):
        x["tank number"] = new_tank_number
        return x
    return map(apply, aquarium_creatures)

assigned_tanks = assign_to_tank(aquarium_creatures, 42)

print(list(assigned_tanks))

#Использование встроенной функции с несколькими итерируемыми объектами

base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]

numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)