#!/usr/bin/env python3
import os
import argparse
from pokemon import *
import csv

file_name = "pokemon_data.csv"

pokemons = []
def command(args):
    command = args.command[0]
    if command == None:
        return
    if command=="filter":
        os.system("./filter.py --help")
    elif command=="stats":
        os.system("./stats.py --help")
    elif command=="search":
        os.system("./filter.py --help")
    elif command=="list":
        os.system("./list.py --help")
                            

    for pk in pokemons:
        pk.print_short_pokemon()      
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "Helppp!")
 
    # defining arguments for parser object
    parser.add_argument("--command", type = str, nargs = 1,
                        metavar = "Value", default = None,
                        help = "Check for Pokémon by Partial Name.")
    
    args = parser.parse_args()

    if args.command != None:
        command(args) 
 

        
       
if __name__ == "__main__":
    # calling the main function
    main()
