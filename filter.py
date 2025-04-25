#!/usr/bin/env python3
import os
import argparse
from pokemon import *
import csv
import operator
file_name = "pokemon_data.csv"


def sort_by(args):
    stat = args.sort_by[0] 
    pokemons = []
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],int(field[3]),int(field[4]),int(field[5]),int(field[6]))
            pokemons.append(pk)
    if stat=="speed":
        pokemons.sort(key=operator.attrgetter("speed"))
        for poke in pokemons:
            print("Name: " + poke.name + ", Speed: " + str(poke.speed))       
    elif stat=="attack":
        pokemons.sort(key=operator.attrgetter("attack"))
        for poke in pokemons:
            print("Name: " + poke.name + ", Attack: " + str(poke.attack))       
    elif stat=="hp":
        pokemons.sort(key=operator.attrgetter("hp"))
        for poke in pokemons:
            print("Name: " + poke.name + ", Hp: " + str(poke.hp))       
    elif stat=="defense":
        pokemons.sort(key=operator.attrgetter("defense"))
        for poke in pokemons:
            print("Name: " + poke.name + ", Defense: " + str(poke.defense))  
def order_by_lowest(args):
    pokemons = []
    type1 = args.first_type[0]
    sort = (args.sort_by[0])
    max_results = args.max_results[0]
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],int(field[3]),int(field[4]),int(field[5]),int(field[6]))
            if(type1==pk.type_1 ):
                pokemons.append(pk)
        pokemons.sort(key=operator.attrgetter(sort))
        for i in range(0,int(max_results)):
            pokemons[i].print_full_pokemon()
def first_second_type(args):
    type1 = args.first_type[0]
    type2 = args.secondary_type[0]
    if (type2=="None"):
        with open(file_name, newline='') as csvfile:
            for row in csvfile:
                field = row.split(",")
                pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
                if(type1==pk.type_1 and field[2]=="" ):
                    pk.print_full_pokemon()    
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
            if(type1==pk.type_1 and type2==pk.type_2  ):
                pk.print_full_pokemon()    

def first_type(args):
    type1 = args.first_type[0]
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
            if(type1==pk.type_1 ):
                pk.print_full_pokemon()
def second_type(args):
    type2 = args.secondary_type[0]
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            field = row.split(",")
            pk = pokemon(field[0],field[1],field[2],field[3],field[4],field[5],field[6])
            if(type2==pk.type_2):
                pk.print_full_pokemon()
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "Searching For a Pokemon!")
 
    # defining arguments for parser object
    parser.add_argument("--first_type", type = str, nargs = 1,
                        metavar = "[Type1]", default = None,
                        help = "List Pokémon of Type_1.")
    parser.add_argument("--secondary_type", type = str, nargs = 1,
                        metavar = "[Type2]", default = None,
                        help = "List Pokémon of Type_2.")
    parser.add_argument("--sort_by", type = str, nargs = 1,
                        metavar = "[stat]", default = None,
                        help = "List Pokémon Sorted by a Stat")
    parser.add_argument("--max_results", type = str, nargs = 1,
                        metavar = "[stat]", default = None,
                        help = "max line of results") 
    args = parser.parse_args()

    if args.first_type != None and args.secondary_type != None:
        first_second_type(args) 
    elif  args.first_type != None and args.sort_by != None and args.max_results != None:
        order_by_lowest(args)
        
       
if __name__ == "__main__":
    # calling the main function
    main()
