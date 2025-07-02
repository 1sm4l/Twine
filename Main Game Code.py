import random

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
    def __init__(self, nname, nhealth, nenergy, nis_turn):
        self.name = str(nname)
        self.health = int(nhealth)
        self.energy = int(nenergy)
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


    def getenergy(self):
        return self.energy
    
    def setenergy(self, genergy):
        self.energy = genergy


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


    #methods
    def draw_card(self):
        if self.deck: #if deck is not empty
            if len(self.hand) < 5: #if hand isn't full
                self.hand.append(self.deck.pop(0)) #remove top card from deck and append to hand
            else:
                print("Hand is full.")
        else:
            self.shuffle_deck()
            self.hand.append(self.deck.pop(0))
            
    def discard_card(self):
        if self.hand: #if hand is not empty
            for card in selected_cards:
                if card in self.hand:
                    self.hand.remove(card) #remove card from hand
                    self.discard_pile.append(card) #appends to discard_pile
                else:
                    print("Card not found in hand.")
            selected_cards.clear() #clear selected cards for next player
        else:
            print("Hand is empty.")
            
    def shuffle_deck(self):
        if self.deck: #checks if there are cards in deck
            random.shuffle(self.deck)
        elif self.discard_pile: 
            self.setdeck(self.discard_pile[:]) #copies discard_pile into deck (else when discard_pile gets deleted, so does deck)
            self.setdiscard_pile([])
            random.shuffle(self.deck)
        else:
            print("No cards to shuffle.")	
            

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


    def switch_current_player(self):
        if self.current_player_index == 1:
            self.current_player_index = 2
        else:
            self.current_player_index = 1


    def getgame_over(self):
        return self.game_over
    
    def setgame_over(self):
        self.game_over = True


    def getwinner(self):
        return self.winner

    def setwinner(self, gwinner):
        self.winner = str(gwinner)


    #methods
    def next_turn(self):
        self.turn_counter += 1


def start_game():
    new_game = game(1, 1)
    new_game.setplayers([player_1, player_2])
    for player in new_game.getplayers():
        player.shuffle_deck()
        for i in range(5):
            player.draw_card()
    
    player_1.setis_turn(True)
    player_2.setis_turn(False)

    return new_game


def check_current_player():
    if new_game.getcurrent_player_index() == 1:
        current_player = player_1
        opponent = player_2
    else:
        current_player = player_2
        opponent = player_1
    return current_player, opponent


def switch_turn():
    current_player, opponent = check_current_player()
    current_player.draw_card()
    current_player.setenergy(current_player.getenergy() + 2)

    new_game.switch_current_player()
    current_player, opponent = check_current_player()
    current_player.setis_turn(True)
    opponent.setis_turn(False)


#applies selected cards effects
def apply_card_effect():
    current_player, opponent = check_current_player()

    total_damage = 0
    total_heal = 0
    total_energy_cost = 0

    for card in selected_cards:
        total_energy_cost += card.getcost()

    if current_player.getenergy() < total_energy_cost:
        print("Not enough energy to play all selected cards.")
        return None  # Don't apply effects

    for card in selected_cards:
        damage = card.getdmg()
        heal = card.getheal()
        cost = card.getcost()

        current_player.setenergy(current_player.getenergy() - cost)
        opponent.sethealth(opponent.gethealth() - damage)
        current_player.sethealth(current_player.gethealth() + heal)

        total_damage += damage
        total_heal += heal

    return total_damage, total_heal, total_energy_cost


#on click select and if clicked again deselect
def select_card(clicked_card): #clicked_card is selected from card in hand by click
    if clicked_card in selected_cards:
        selected_cards.remove(clicked_card)
    else:
        selected_cards.append(clicked_card)
    return selected_cards

def take_turn():
    current_player, _ = check_current_player()

    #if card is clicked then do this
    select_card(clicked_card)

    #if end turn is clicked
    result = apply_card_effect()
    if result is None:
        print("Turn not ended. Not enough energy.")
        return  #player must modify selection and try again

    total_damage, total_heal, total_energy_cost = result #take total_damage, total_heal, total_energy_cost as parameters to change ui
    print(f"Used {total_energy_cost} energy, dealt {total_damage} damage, healed {total_heal} HP.")
    
    current_player.draw_card()
    new_game.next_turn()  
    switch_turn()


#checks if a player hits 0 health, then sets the other player as the winner and sets game as over
def check_game_over():
    current_player, opponent = check_current_player()
    if current_player.gethealth() == 0 and opponent.gethealth() == 0: #if both players die
        new_game.setwinner("Draw.")
        new_game.setgame_over()
        return True
    elif new_game.getturn_counter() == 11: #if turn counter = max rounds + 1 (if no one dies)
        if current_player.gethealth() > opponent.gethealth(): #if player has more health than opponent
            new_game.setwinner(current_player.getname())
            new_game.setgame_over()
            return True
        elif current_player.gethealth() < opponent.gethealth():  #if opponent has more health than player
            new_game.setwinner(opponent.getname())
            new_game.setgame_over()
            return True
        else: #if they have the same health at the end of the game
            new_game.setwinner("Draw.")
            new_game.setgame_over()
            return True
    elif opponent.gethealth() == 0: #if opponent dies
        new_game.setwinner(current_player.getname())
        new_game.setgame_over()
        return True
    elif current_player.gethealth() == 0: #if current player kills themself
        new_game.setwinner(opponent.getname())
        new_game.setgame_over()
        return True
    else:
         return False


run = True
while run:
    
	#key variables
    player_1 = player("JohnDoe", 100, 10, False)
    player_2 = player("JaneDoe", 100, 10, False)
    clicked_card = 0 #placeholder and card selected will be from click which i cant do right now
    selected_cards = []
     
    choice = str(input("Play a game? (y/n): ")).lower()
    if choice == 'y':
        new_game= start_game()
        while not check_game_over():
            take_turn()
        print(f"Winner: {new_game.getwinner()}")

        continue_choice = str(input("Play again? (y/n): ")).lower()
        if continue_choice != 'y':
            run = False
    else:
        run = False
