import random

nums = random.sample(range(1,300), 100)

def average(n : int, d : int) -> float:
    avg = n / d
    return avg

def running_average(numbers : list[int]) -> list[float]:
    avgs = []
    total = 0 
    for i, num in enumerate(numbers):
        total += num 
        current_avg = average(total, i + 1)
        avgs.append(current_avg)
    return avgs

print("Running Average: ", running_average(nums))