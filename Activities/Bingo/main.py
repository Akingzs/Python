import random
class Jogador:
    '''Class representing a Player from Bingo game'''
    def __init__(self,name):
        self._name = name
        self._player_numbers = []
        self._numbers_played = []
        
    # Name Getter 
    @property
    def name(self):
        return self._name
    
    # Verify if the current player win 
    def check(self):
        if len(self._player_numbers) == 0:
            return True
        
    # Show player info, if needed 
    def show_info(self):
        print(f'Jogador: {self._name}\nNumeros restantes: {self._numbers_left}')
        return self._name,self._numbers_left
    
class Bingo:
    '''Class representing Bingo game'''
    def __init__(self,max_number):
        self._number_list = [x for x in range(1,max_number+1)]
        random.shuffle(self._number_list)
        self._players = []
        self._winners = []
        self._sorted_numbers = []

    # Add player to Bingo game
    def add_player(self, name):
        player = Jogador(name)
        self._players.append(player)
        # Create new list to shuffle to not change the original list
        self._player_number_list = self._number_list
        random.shuffle(self._player_number_list)
        
        # Get 30% of numbers_len
        numbers_len = int(len(self._player_number_list) * 0.3)
        player._player_numbers = random.sample(self._player_number_list,numbers_len)
        
    def see_players(self):
        for player in self._players:
            print (player.name) 

    def sort_number(self):
        number_sorted = self._number_list.pop()
        self._sorted_numbers.append(number_sorted)
        self.update_players(number_sorted)

    def update_players(self, number_sorted):
        for player in self._players:
            player._numbers_played.append(number_sorted)
            if number_sorted in player._player_numbers:
                player._player_numbers.remove(number_sorted)
                self.check_winner(player)
            
    def check_winner(self, player):
        if player.check() == True:
            self._winners.append(player.name)


    def win(self):
        if len(self._winners) > 0:
            for winnners in self._winners:
                print(f'The winner of the game was {winnners}')
            return True
   
    @property                
    def has_players(self):
        if len(self._players) > 0:
            return True 

        

def main():
    jogo1 = Bingo(10)
    jogo1.add_player('Arthur')
    jogo1.add_player('Luanna')
    
    if jogo1.has_players == True:
        while True:
            jogo1.sort_number()        
            if jogo1.win() == True:          
                break
            
if __name__ == '__main__':
    main()