#!/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    total_cost = round(meal_cost*(1+ (tip_percent+tax_percent)/100.))
    print ("The total meal cost is %d dollars." %total_cost)
