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
def fields(args):
    pk = pokemon(None,None,None,None,None,None,None)   
    for i in range(0,3): 
        if ( args.fields[i]=="name"):
            pk.name = args.fields[i] 
        elif (args.fields[i]=="type_1"):
           pk.type_1 = args.fields[i]
        elif (args.fields[i]=="type_2"):
           pk.type_2 = args.fields[i]
        elif (args.fields[i]=="hp"):
           pk.hp = args.fields[i]
        elif (args.fields[i]=="attack"):
           pk.attack = args.fields[i]
        elif (args.fields[i]=="defense"):
           pk.defense = args.fields[i]         
        elif (args.fields[i]=="speed"):
           pk.speed = args.fields[i]      
    with open(file_name, newline='') as csvfile:
        for row in csvfile:
            pk.print_fields(row)
        
def main():
    # create parser object
    parser = argparse.ArgumentParser(description = "List Pokemons!")
 
    # defining arguments for parser object
   
    parser.add_argument("--sort_by", type = str, nargs = 1,
                        metavar = "[stat]", default = None,
                        help = "List Pokémon Sorted by a Stat")
   
    parser.add_argument("--fields", type = str, nargs = 3,
                        metavar = "field", default = None,
                        help = "List Pokémon based on fields.")
 
    
    args = parser.parse_args()
    if args.sort_by!=None:
        sort_by(args)
    elif args.fields!=None:
        fields(args)    
       
if __name__ == "__main__":
    # calling the main function
    main()
