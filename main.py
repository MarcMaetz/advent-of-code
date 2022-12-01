# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # removing the new line characters
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    print(lines)
    calories = []
    for i in lines:
        try:
            e = int(i)
            calories.append(e)
        except:
            calories.append(-1)
    print(calories)
    elves = [[]]
    for i in calories:
        if i < 0:
            elves.append([])
        else:
            elves[-1].append(i)
    print(elves)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
