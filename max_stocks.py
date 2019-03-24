def argmax(array, start_index):
    return start_index + max(zip(array[start_index:], range(len(array[start_index:]))))[1]

def max_profit(prices):
    total_profit = 0
    n = len(array)
    index = 0
    while index < n:
        sell_index = argmax(array, index)
        total_profit += (sell_index - index)*prices[sell_index] - sum(prices[index:sell_index])
        index = sell_index + 1
    return total_profit
        

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        input()
        array = [int(x) for x in input().strip().split()] # get the input array
        print(max_profit(array))                          # solve the problem


