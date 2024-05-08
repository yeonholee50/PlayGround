import requests
import time
import heapq

while True:
    req = requests.get("https://financialmodelingprep.com/api/v3/symbol/NASDAQ?apikey=Scbitfo0qOuY4MTMjbqe6SRQjHjM7UAe")
    stocklist = req.json()
    neg_positions = []
    pos_positions = []
    with open("stocks", "w") as file:
    
            
            counter = 1
            for stock in stocklist:  
                file.write(f"{counter}. ")
                file.write(f"{stock["symbol"]} | ")
                file.write(f"{stock["name"]} | ")
                file.write(f"{stock["price"]}\n")
                counter+=1
                
                neg_positions.append((stock["changesPercentage"] if (stock["changesPercentage"] is not None) else float('inf'), 1/stock["volume"] if (stock["volume"] is not None and stock["volume"] != 0) else float('inf'), stock["symbol"]))
                pos_positions.append((-stock["changesPercentage"] if (stock["changesPercentage"] is not None) else float('inf'), 1/stock["volume"] if (stock["volume"] is not None and stock["volume"] != 0) else float('inf'), stock["symbol"]))
    with open("stocks_down", "w") as file:
        counter = 1
        heapq.heapify(neg_positions)
        while counter <= 20:
            stock = heapq.heappop(neg_positions)
            file.write(f"{counter}. ")
            file.write(f"{stock[-1]} | ")
            file.write(f"{stock[0]}\n")
            counter+=1

    
         
    with open("stocks_up", "w") as file:
        counter = 1
        heapq.heapify(pos_positions)
        while counter <= 20:
            stock = heapq.heappop(pos_positions)
            file.write(f"{counter}. ")
            file.write(f"{stock[-1]} | ")
            file.write(f"{-stock[0]}\n")
            counter+=1
         
         

    time.sleep(20)

