#Importing Libraries
import numpy as np
class Bidder:
    """This is the Bidder class and used for the Auction.
    \nBidder(num_users, num_rounds)
    \nThere are two methods: Bid and Notify"""
    #Initialize the Bidding Class
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.user_dict ={} 
        self.winning_list = {True:0, False:0}
        self.bid_num = 0
        self.user_dict_total={}
    #Function to call for a bid based on the user selected by the auction
    def bid(self, user_id):
        """Bidder function to bid or not. Pass in user_id """
        self.user_id = user_id
        self.bid_num +=1
        
        #create user id
        user = "user_id " +str(self.user_id)
        #if the user is in the user dictionary list update their probability number of clicking the add or not
        if user in self.user_dict:
            chosen_user_ratio = self.user_dict[user]/self.user_dict_total[user] 
        #if statment on whether to bid or not
        if self.user_dict == {} and self.num_rounds>100 and self.bid_num < 50:
            # bid_amount = 1
            bid_amount = 1
            return bid_amount
        #if the use is in the dictionary and has a probability of 50% or greater then bid 75 cents 
        elif user in self.user_dict:
            if chosen_user_ratio > 0.5:
                bid_amount = 0.75
                return bid_amount
        # otherwise just bid 50 cents and play your odds to win
            else:
                bid_amount = 0.5
                return bid_amount
        #in the scenario where the game is short just bid 50 cents and play it random
        else:
            bid_amount = 0.5
            return bid_amount
    # The notify function will notify the bidder if the user watched the ad or not
    def notify(self, auction_winner, price, clicked):
        """Adding auction win. Pass in auction_winner, price of bid, and if the user clicked or not."""
        #this code will execute if the bidder wins to show their ad
        self.winning_list[auction_winner] +=1
        # this code is to store the user info temporarily
        user = "user_id " +str(self.user_id)
        #Stores information if the bidder chooses to watch the add or not
        if auction_winner == True and clicked == True:
            #if the user is already in the bidders list of dictionary add to their number of times bid to that user
            if user in self.user_dict:
                self.user_dict[user] += 1
            #if the bidder hasnt stored information then create and add the user to the list
            else:
                self.user_dict[user] = 1
        #Update if the user is in the bidders list and has clicked to watch the add
        if user in self.user_dict_total:
                self.user_dict_total[user] += 1
        #Add the user to the list of watched adds
        else:
            self.user_dict_total[user] = 1
            # print("You won the auction and the cost of the bid was", price)
            # print("User choose to click:",clicked)
