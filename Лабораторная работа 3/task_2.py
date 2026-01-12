def find_common_participants(group1: str, group2: str, separator: str = ",") -> list:
    participants_1 = group1.split(separator)
    participants_2 = group2.split(separator)
    com_participants = list(set(participants_1) & set(participants_2))
    com_participants.sort()
    return com_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

druz = find_common_participants(participants_first_group,participants_second_group,separator="|")
print(f"Общие участники: {druz}")