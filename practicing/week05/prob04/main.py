def variance(numbers):
    if numbers < 2:
        return None
    mean = sum(numbers)/len(numbers)
    squared_differences = [(x - mean)**2 for x in numbers]
    variance = sum(squared_differences) / (len(numbers)-1)
    return variance

numbers = [int(x) for x in input(),split()]
if __name__ = "__main__":
    result = variance(numbers)
    if result is None
        print(None)
    else:
        print(result)