import random
from helper import check_sort

def monkey_sort(list):
    sorted_list = list.copy()
    indexes = []

    for i in range(len(list)):
        indexes.append(i)

    while (not check_sort(sorted_list)):
        sorted_list = []
        indexes = []
        while (len(sorted_list) != len(list)):
            print(len(sorted_list))
            ran = random.randint(0, len(list)-1)
            #this line makes it even slower
            if (ran in indexes):
                continue

            sorted_list.append(list[ran])
            indexes.append(ran)

    return sorted_list

def main():
    l = []
    for n in range(200):
        l.append(random.randint(1, 100))

    print(monkey_sort(l))

if __name__ == '__main__':
    main()
