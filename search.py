#!/usr/bin/env python3
import os
import argparse
from pokemon import *
import csv

file_name = "pokemon_data.csv"

pokemons = []
def name_like(args):
    partial_name = args.name_like[0].lower()
    if partial_name == None:
        return
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
            if partial_name in pk.name.lower():
                pokemons.append(pk)
    for pk in pokemons:
        pk.print_short_pokemon()      
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "Search For a Pokemons!")
 
    # defining arguments for parser object
    parser.add_argument("--name_like", type = str, nargs = 1,
                        metavar = "Value", default = None,
                        help = "Check for Pokémon by Partial Name.")
    
    args = parser.parse_args()

    if args.name_like != None:
        name_like(args) 
 

        
       
if __name__ == "__main__":
    # calling the main function
    main()
