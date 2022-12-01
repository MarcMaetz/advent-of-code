# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # removing the new line characters
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    elves = [[]]
    for i in lines:
        try:
            e = int(i)
            elves[-1].append(e)
        except:
            elves.append([])
    sums = [sum(elve) for elve in elves]
    print(max(sums))
    sums.sort()
    print(sum(sums[-3:]))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
