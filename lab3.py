activities={}


def add():
    activity = input("Podaj nazwe aktywności: ")
    time_spent = int(input("Podaj czas aktywności "))
    if activity not in activities:
        activities[activity] = [time_spent]
    else:
        activities[activity].append(time_spent)


def show_time():
    activity = input("Podaj nazwe aktywności: ")
    if activity not in activities:
        print("Aktywność nieznaleziona -> t = 0")
    else:
        timeTotal = 0
        for timeSpent in activities[activity]:
            timeTotal += timeSpent
        print("Spędziony czas:", timeTotal)


def show_top():
    time_count = []
    for activity in activities.keys():
        time_total = 0
        for timeSpent in activities[activity]:
            time_total += timeSpent
        time_count.append((time_total, activity))
    time_count = sorted(time_count, reverse=True)
    printed_activities = min(3, len(time_count))
    for i in range(printed_activities):
        print(str(i + 1) + ".", time_count[i][1], " -> ", time_count[i][0])


if __name__ == '__main__':
    while True:
        order = input("Wybierz funkcjonalność: [D]odawanie, [C]zas, [T]op: ")
        if order == 'D':
            add()
        elif order == 'C':
            show_time()
        elif order == 'T':
            show_top()
        else:
            print("Nieznane polecenie")
