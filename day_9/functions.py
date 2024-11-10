def find_highest_bidder(bidding_dict):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")