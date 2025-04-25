class pokemon:
    def __init__(self,name,type_1,type_2,hp,attack,defense,speed):
        self.name = name
        self.type_1=type_1
        self.type_2 = type_2
        self.hp = hp
        self.attack = attack
        self.defense= defense
        self.speed=speed
    def print_full_pokemon(self):
        print("===================")
        print("Name: " +str(self.name))
        print("Type 1 " + str(self.type_1))
        print("Type 2 " + str(self.type_2))
        print("Hp " + str(self.hp))
        print("Attack " + str(self.attack))
        print("Defense " + str(self.defense))
        print("Speed " + str(self.speed))
    def print_fields(self,message):
        field = message.split(",") 
        message = ""
        if self.name != None:
            message = message + "Name : " + field[0]+ ". "
        if self.type_1 != None:
            message = message + "type_1 : " + field[1]  +  ". "
        if self.type_2 != None:
            message = message + "type_2 : " + field[2] +  ". "    
        if self.hp != None:
            message = message + "Hp : " +field[3]+ ". "            
        if self.attack != None:
            message = message + "Attack : " +field[4] +  ". "        
        if self.defense != None:
            message = message + "Defense : " +field[5] +  ". "    
        if self.speed != None:
            message = message + "Speed : " + field[6]          
        print(message)
    def print_short_pokemon(self):
        print(f"Name: {self.name}, Type 1: {self.type_1},  Type 2: {self.type_2} ")