# TODO Напишите функцию find_common_participants

def find_common_participants(list1, list2, separator=","):
    list1 = list1.split(separator)
    list2 = list2.split(separator)
    list3 = []
    for last_name1 in list1:
        for last_name2 in list2:
            if last_name1 == last_name2:
                list3.append(last_name2)
    return sorted(list3)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

intersection_sort = find_common_participants(participants_first_group, participants_second_group, "|")

print(intersection_sort)

# TODO Провеьте работу функции с разделителем отличным от запятой

