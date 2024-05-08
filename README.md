# ATOP-auction-SMC
# Overview:
A smart contract is developed in order to deploy an English auction/open ascending price auction in Algorand blockchain with the help of PyTEAL(python library) which is set up in sandbox environment.


# Smart contract algorithm for creating an english auction :
It stipulates that an environment where participants bid openly against one another, with subsequent bid required to be higher than the previous bid, starting from a reserved(base) price chosen by seller. At the end highest bid wins.

# Key facets that need to setup by the constructor are :
1. The assignee (external account representing the seller of any digital asset that begins the auction by creating contract)
2. Start time
3. End time
4. Withdraw/delivery time
5. Reserve price
6. Minimum increment

# Key aspects for deploying Bidding function() :
1. Initially initiate the function bid()
2. A bid must be done before the auction ends
3. It must be higher than the reserved price
4. It must be higher than the previous bid price
5. It must come from a valid bidder(Not from seller)
6. If the bid satisfies all the constraints, it'll be acepted and recored as the highest bid
7. At last, the auction creator should close the bid


