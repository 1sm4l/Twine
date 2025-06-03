#class card
class card:
    #constructor 
    def __init__(self, nname, ntype, ndmg, nheal, ncost, ndescription, nid):
        self.name = str(nname)
        self.type = str(ntype)
        self.dmg = int(ndmg)
        self.heal = int(nheal)
        self.cost = int(ncost)
        self.description = str(ndescription)
        self.id = int(nid)

#getters and setters
    def getname(self):
            return self.name
    

    def gettype(self):
            return self.type


    def getdmg(self):
            return self.dmg
    
    def setdmg(self, gdmg):
            self.dmg = gdmg


    def getheal(self):
            return self.heal
    
    def setheal(self, gheal):
            self.heal = gheal


    def getcost(self):
            return self.cost
    

    def getdescription(self):
            return self.description


    def getid(self):
            return self.id


#class player
class player:
    #constructor 
    def __init__(self, nname, nhealth, nis_turn):
        self.name = str(nname)
        self.health = int(nhealth)
        self.deck = None
        self.hand = None
        self.discard_pile = None
        self.status_effects = None
        self.is_turn = bool(nis_turn)

#getters and setters
    def getname(self):
        return self.name
    
    def setname(self, gname):
        self.name = gname


    def gethealth(self):
        return self.health
    
    def sethealth(self, ghealth):
        self.health = ghealth


    def getdeck(self):
        return self.deck
    
    def setdeck(self, gdeck):
        self.deck = gdeck


    def gethand(self):
        return self.hand
    
    def sethand(self, ghand):
        self.hand = ghand

    def getdiscard_pile(self):
        return self.discard_pile
    
    def setdiscard_pile(self, gdiscard_pile):
        self.discard_pile = gdiscard_pile


    def getstatus_effects(self):
        return self.status_effects
    
    def setstatus_effects(self, gstatus_effects):
        self.status_effects = gstatus_effects


    def getis_turn(self):
        return self.is_turn
    
    def setis_turn(self, gis_turn):
        self.is_turn = gis_turn
    

#class game
class game:
    #constructor 
    def __init__(self, nturn_counter, ncurrent_player_index):
        self.players = []
        self.turn_counter = int(nturn_counter)
        self.current_player_index = int(ncurrent_player_index)
        self.game_over = False
        self.winner = None

#getters and setters
    def getplayers(self):
            return self.players
    
    def setplayers(self, gplayers):
            self.players.append(gplayers)


    def getturn_counter(self):
            return self.turn_counter
    
    def setturn_counter(self, gturn_counter):
            self.type = gturn_counter


    def getcurrent_player_index(self):
            return self.current_player_index


    def getgame_over(self):
            return self.game_over
    
    def setgame_over(self):
            self.game_over = True


    def getwinner(self):
            return self.winner

    def setwinner(self, gwinner):
            self.winner = str(gwinner)


# initialise cards
soldier_type_1 = card("Soldier", "Attack", 10, 0, 2, "Soldier ready for duty.\nDamage: 10\nHealing: 0", 1)
soldier_type_2 = card("Sleepy Soldier", "Attack", 5, 0, 1, "What time is it???\nDamage: 5\nHealing: 0", 2)
soldier_type_3 = card("Crazed Soldier", "Attack", 30, -20, 3, "If I'm going down, you're coming with me.\nDamage: 30\nHealing: -20", 3)

support_1 = card("Flagbearer", "Support", 0, 30, 4, "Ego? But when have I lost?\n[Adds 30 health for 3 rounds.]\nDamage: 0\nHealing: +30", 4) #add condition to main loop to check if effect is active
support_2 = card("Medic", "Support", 0, 10, 2, "Soldier ready for duty.\nDamage: 0\nHealing: +10", 5)

#initialise players
player_1 = player("JohnDoe", 100, False)
player_2 = player("JaneDoe", 100, False)

#deck/hand/discard input test
player_1.setdeck([soldier_type_1, soldier_type_2])
player_1.sethand([soldier_type_3])
player_1.setdiscard_pile([support_1])

#current game
new_game = game(1, 1)

player_1.setis_turn(True)
new_game.setwinner("Player 1")
new_game.setgame_over()

#displays players info
print(f"""Players:
      
      Player 1:
      Name: {player_1.getname()}
      Health: {player_1.gethealth()}
      Deck: {player_1.getdeck()}
      Hand: {player_1.gethand()}
      Discard Pile: {player_1.getdiscard_pile()}
      Status Effects: {player_1.getstatus_effects()}
      Is_Turn: {player_1.getis_turn()}
      
      Player 2:
      Name: {player_2.getname()}
      Health: {player_2.gethealth()}
      Deck: {player_2.getdeck()}
      Hand: {player_2.gethand()}
      Discard Pile: {player_2.getdiscard_pile()}
      Status Effects: {player_2.getstatus_effects()}
      Is_Turn: {player_2.getis_turn()}""")


#completed iteration 1