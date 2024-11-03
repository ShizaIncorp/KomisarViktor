# TODO Напишите функцию find_common_participants

def find_common_participants(list1, list2, sep = ","):
    list1 = list1.split(sep)
    list2 = list2.split(sep)
    list3 = []
    for _ in list1:
        for __ in list2:
            if _ == __:
                list3.append(__)
    return sorted(list3)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

Intersection_sort = find_common_participants(participants_first_group, participants_second_group,"|")

print(Intersection_sort)

# TODO Провеьте работу функции с разделителем отличным от запятой
