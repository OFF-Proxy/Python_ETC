import random
import datetime

random_list = [random.randint(0, 100000000) for _ in range(1000000)]

checked_list = [random.randint(0, 100000000) for _ in range(100)]
start_a = datetime.datetime.now()

for temp in checked_list: #←checked_listが100個のリスト
        if temp in random_list:#a:←aが100万個のリスト
            print(f'temp:{temp} in a')
start_a = datetime.datetime.now()-start_a
print (start_a)

random_set = set(random_list)
start_a = datetime.datetime.now()

for temp in checked_list: #←checked_listが100個のリスト
        if temp in random_set:#a:←aが100万個のリスト
            print(f'temp:{temp} in a')
start_a = datetime.datetime.now()-start_a
print (start_a)