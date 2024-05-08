import uuid
import logging
import time

__author__ = "UdayKiran and Praveen"

logging.getLogger().setLevel(logging.INFO)


class Auction:
    def __init__(self, item, time):
        if item.is_sold:
            logging.error("Item {} already sold".format(item.name))
        else:
            self.id = uuid.uuid1()
            self.item = item
            self.is_started = False
            self.has_failed = None
            self.highest_bid = None
            self.starting_time = time.start
            self.ending_time = time.stop 
            

class Item:
    def __init__(self, name, reserved_price):
        self.id = uuid.uuid1()
        self.name = name
        self.reserved_price = reserved_price
        self.is_sold = False

class Participant:
    def __init__(self, name):
        self.id = uuid.uuid1()
        self.name = name

    def bid(self, auction, amount):
        Bid(self, auction, amount)
            
class Bid:
    def __init__(self, bidder, auction, amount):
        if not auction.is_started:
            logging.warning("Auction {} has not been started yet. "
                            "Bid is not allowed".format(auction.id))
        elif auction.highest_bid is not None \
                and auction.highest_bid.amount >= amount:
            logging.error("A new bid has to have a price higher than "
                          "the current highest bid.")
        else:
            self.id = uuid.uuid1()
            self.bidder = bidder
            self.amount = amount
            self.auction = auction
            self.auction.highest_bid = self
            logging.info("{} bids {} for auction {}".format(bidder.name,
                                                            amount,
                                                            auction.id))            
    def start(self):
        if self.has_failed is not None:
            logging.error("Auction {} already performed "
                          "on this item.".format(self.id))
        else:
            self.is_started = True
            logging.info("Auction {} has been started".format(self.id))

    
    def stop(self):
        if self.is_started:
            highest_bid = self.highest_bid
            starting_time = self.starting_time
            if (highest_bid is None or
                    (highest_bid is not None and
                     self.item.reserved_price > highest_bid.amount)):
                self.has_failed = True
                logging.warning("Auction {} did not reach "
                                "the reserved price".format(self.id))
            else:
                self.has_failed = False
                self.item.is_sold = True
            self.is_started = False
            logging.info("Auction {} has been stopped".format(self.id))
        else:
            logging.error("Auction {} is not started. "
                          "You can't stop it.".format(self.id))
            
