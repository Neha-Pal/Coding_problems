# Birthday Cake Candles
# Example - 
# candles = [4,4,1,3]
# the maximum height candles are 4 unit. there are 2 of them, so return 2.

def output(candles):
    max_height = max(candles)
    return candles.count(max_height)
candles = [4,4,1,3]
print(output(candles))