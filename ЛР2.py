# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator = ","):
    list_1 = participants_first_group.split(separator)
    list_2 = participants_second_group.split(separator)
    set_1 = set(list_1)
    set_2 = set(list_2)
    common_participants = list(set(list_1).intersection(list_2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator = ","))