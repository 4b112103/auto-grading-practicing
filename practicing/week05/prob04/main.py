def variance(numbers):
    if len(numbers) < 2:
        return None
    mean = sum(numbers)/len(numbers)
    squared_differences = [(x - mean)**2 for x in numbers]
    variance = sum(squared_differences) / (len(numbers)-1)
    return variance

input_numbers = [int(x) for x in input().split()]

if __name__ == "__main__":
    result = variance(input_numbers)
    if result is not None:
        print(result)
    else:
        print(None)