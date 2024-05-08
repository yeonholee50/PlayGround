import requests
import heapq

def analyze_ratings(ratings):
    buy = ratings["analystRatingsbuy"]
    hold = ratings["analystRatingsHold"]
    sell = ratings["analystRatingsSell"]
    strong_buy = ratings["analystRatingsStrongBuy"]
    strong_sell = ratings["analystRatingsStrongSell"]
    
    # Calculate the total number of ratings
    total_ratings = buy + hold + sell + strong_buy + strong_sell
    
    # Calculate the percentage of buy, hold, and sell ratings
    buy_percentage = (buy + strong_buy) / total_ratings
    hold_percentage = hold / total_ratings
    sell_percentage = (sell + strong_sell) / total_ratings
    
    # Apply the grading criteria
    if buy_percentage > sell_percentage and buy_percentage > 0.5:
        return ("Buy", buy_percentage - sell_percentage)
    elif sell_percentage > buy_percentage and sell_percentage > 0.5:
        return ("Sell", sell_percentage - buy_percentage)
    else:
        return ("Hold", 0)

def main():
    buy = []
    sell = []
    req = requests.get("https://financialmodelingprep.com/api/v3/symbol/NASDAQ?apikey=Scbitfo0qOuY4MTMjbqe6SRQjHjM7UAe")
    stocklist = req.json()
    """
    we have stock list now
    """
    symbol_list = [stock["symbol"] for stock in stocklist]
    
    for symbol in symbol_list:
        """
        for those using, my api subscription ended so use your own api key:(
        """
        req = requests.get(f"https://financialmodelingprep.com/api/v3/analyst-stock-recommendations/{symbol}?apikey=Scbitfo0qOuY4MTMjbqe6SRQjHjM7UAe")
        print(req.status_code)
        analysts_rating = req.json()
        
        rating = analyze_ratings(analysts_rating)
        print(symbol)
        
        if rating[0] == "Buy":
            heapq.heappush(buy, (-rating[-1], symbol))
        elif rating[0] == "Sell":
            heapq.heappush(sell, (-rating[-1], symbol))
        
    with open("analyst_official_ratings", "w") as file:
        file.write("T40 Buy Rating: \n")
        for i in range(40):
            file.write(f"{i}. ")
            content = heapq.heappop(buy)
            file.write(f"{content[-1]} | ")
            file.write(f"{-content[0]} | ")
        file.write("T40 Sell Rating: \n")
        for i in range(40):
            file.write(f"{i}. ")
            content = heapq.heappop(sell)
            file.write(f"{content[-1]} | ")
            file.write(f"{-content[0]} | ")


        





if __name__  == "__main__":
    main()