n = int(input())
first_prices = list(map(int, input().split()))
second_prices = list(map(int, input().split()))
if n == 1:
    print(first_prices[0] * (second_prices[0] / (first_prices[0] + second_prices[0])))




