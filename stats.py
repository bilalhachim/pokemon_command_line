#!/usr/bin/env python3
import os
import argparse
from pokemon import *
import csv

file_name = "pokemon_data.csv"

def min_max_hp(args):
    min_hp = int(args.min_hp[0])
    max_hp = int(args.max_hp[0])
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
            if (int(pk.hp)>=min_hp and int(pk.hp)<=max_hp):
                pk.print_full_pokemon()    
def min_attack_min_speed(args):
    min_attack  = int(args.min_attack[0])
    min_speed = int(args.min_speed[0])
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
            if (int(pk.attack)>= min_attack  and int(pk.speed)>=min_speed):
                pk.print_full_pokemon()                    
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "Stats For Pokemons!")
 
    # defining arguments for parser object
   
    parser.add_argument("--min_hp", type = str, nargs = 1,
                        metavar = "[Value]", default = None,
                        help = "Show Pokémon with a minimum HP value")
    parser.add_argument("--max_hp", type = str, nargs = 1,
                        metavar = "[Value]", default = None,
                        help = "Show Pokémon with a maximum HP value.")
    parser.add_argument("--min_attack", type = str, nargs = 1,
                        metavar = "[Value]", default = None,
                        help = "Show Pokémon with a min Attack value.")
    parser.add_argument("--min_speed", type = str, nargs = 1,
                        metavar = "[Value]", default = None,
                        help = "Show Pokémon with a min Speed value.")
    
    args = parser.parse_args()
    if args.min_hp!= None and args.max_hp!=None:
        min_max_hp(args)
    elif args.min_attack != None and args.min_speed!= None:
        min_attack_min_speed(args)
        
       
if __name__ == "__main__":
    # calling the main function
    main()
