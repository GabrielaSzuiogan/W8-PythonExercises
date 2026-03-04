import statistics


def number_stats(numbers):
    odds = 0
    if len(numbers) == 0:
        print("No numbers given")
        return
    else:
        nr_min = min(numbers)
        nr_max = max(numbers)
        avg = statistics.mean(numbers)
        for n in numbers:
            if n%2 != 0:
                odds += 1

    print(f" Smallest number: {nr_min}\n \
    Largest number: {nr_max}\n \
    Average of the numbers: {avg}\n \
    Nr of odds: {odds}")

number_stats([0,3,6])
number_stats([])

# li = []
# li = input("Enter numbers separated by space:  ").split()
# print(f"List: {li}")
# number_stats(li)