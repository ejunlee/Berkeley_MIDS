#import libraries
import numpy as np

#Create User Class
class User:
    """This is the User Class and will be used for the Auction
    \nThere are no inputs.
    \n There is on method called show_ad"""
    def __init__(self):
        """Probability is hidden and randomly asssigned"""
        self.__probability = np.random.uniform()
        
    def show_ad(self):
        """Returns True if the user clicks the add"""
        result = np.random.choice([True,False], p=[self.__probability, 1-self.__probability])
        return result
    
class Auction:
    """This is the Aucton Class.
    \nIt takes two input (users, bidders)
    \nThe game holds the rules
    for the second price auction.
    """
    def __init__(self, users, bidders):
        """Pass in users and bidders."""
        self.users = users
        self.bidders = bidders
        
        #Create a dictionary of bidders and funds
        Auction.balances ={}
        #For loop to set bidders balance to 0
        for i in self.bidders:
            Auction.balances[i] = 0
            
        #Code that has been commented below was used for testing purposes
        # Auction.users = {}
        # for i in self.users:
        #     Auction.users[i]

    def execute_round(self):
        '''Choosing a random user'''
        Auction.chosen = np.random.randint(0,len(self.users))
        # print("Choosing User", Auction.chosen)
        
        #Biders bid and collate bid in a dictionary
        bid_dict = {}
        for i in self.bidders:
            bid_dict[i]=(i.bid(Auction.chosen))
        # print("These are all the bidder", bid_dict)
        
        #Find the highest bidder
        key_max = max(bid_dict.keys(), key=(lambda k: bid_dict[k]))
        
        #Code that has been commented below was used for testing purposes
        # print(f"Highest bidder {key_max}")
        # print(f"Highest bid was ${bid_dict[key_max]}" )
        
        #find the second highest bidder
        if len(self.bidders) > 1:
            value_max2 = sorted(bid_dict.values())[-2]
            key_max2_list = [k for k,v in bid_dict.items() if v == value_max2]
        else:
            value_max = bid_dict[key_max]
        # print(f"The second highest bid is ${value_max2}" )
        # print("The second highest bidder", key_max2_list[0])
        
        #Compare the highest and second highest bidder
        if len(self.bidders) > 1 and bid_dict[key_max] == bid_dict[key_max2_list[0]]:
            winner = np.random.choice([key_max,key_max2_list[0]])
            # print(winner)
        else:
            winner = key_max
            # print("Auction winner", winner)
            
        #user clicks ad or not
        clicked = self.users[Auction.chosen].show_ad()
        
        #update the auction balance of bidder who won the bid. The second highest bid is charged.
        if len(self.bidders)> 1: 
            Auction.balances[winner] -= value_max2
        else:
            Auction.balances[winner]=-value_max
            
        #Add a dollar to the bidder whose ad was watched
        if clicked:
            Auction.balances[winner] += 1
        
        #Notify the winner
        if len(self.bidders) > 1:
            winner.notify(True, value_max2, clicked)
        else:
            winner.notify(True, value_max, clicked)
        #Notify the other bidders if another bidder has won or not
        for i in self.bidders:
            if i != winner:
                i.notify(False, value_max2, None)
        
