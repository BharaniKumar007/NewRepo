def stable_marriage(preferences):
    n = len(preferences) // 2
    men_preferences = preferences[:n]
    women_preferences = preferences[n:]
    engaged = [-1] * n
    women_engaged = [-1] * n
    men_free = list(range(n))

    while men_free:
        man = men_free.pop(0)
        man_pref = men_preferences[man]
        for preference in man_pref:
            woman = int(preference[1:]) - 1  # Adjust the index to start from 0
            if women_engaged[woman] == -1:
                engaged[man] = woman
                women_engaged[woman] = man
                break
            else:
                current_husband = women_engaged[woman]
                woman_pref = women_preferences[woman]
                if woman_pref.index(f'M{man + 1}') < woman_pref.index(f'M{current_husband + 1}'):
                    engaged[man] = woman
                    women_engaged[woman] = man
                    men_free.append(current_husband)
                    break

    stable_marriage_result = []
    for man, woman in enumerate(engaged):
        stable_marriage_result.append(f"M{man + 1} W{woman + 1}")

    return stable_marriage_result


def main(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()

    preferences = [line.split() for line in lines]

    if len(preferences) % 2 != 0:
        print("Error: The number of men and women preferences must be the same.")
        return

    stable_marriage_men = stable_marriage(preferences)
    stable_marriage_women = stable_marriage(list(zip(*preferences[::-1])))

    for match in stable_marriage_men:
        print(match)
    for match in stable_marriage_women:
        print(match)


if __name__ == "__main__":
    input_file = "preferences.txt"  # Replace with the actual input file name
    main(input_file)
