
import random
import time
import google.generativeai as genai

# Setup Gemini AI API Key
genai.configure(api_key="")

def ai_roll_dice():
    return random.randint(1, 6)

class SnakesAndLadders:
    def __init__(self, players, board_size=100, ai_player=None):
        self.board_size = board_size
        self.players = {player: 1 for player in players}  # Posisi awal di kotak 1
        self.snakes = {32: 10, 36: 6, 48: 26, 88: 24, 95: 56}
        self.ladders = {3: 22, 8: 30, 28: 84, 58: 77, 80: 99}
        self.power_ups = {14: 'boost', 44: 'extra_turn', 72: 'trap'}  # Kotak spesial
        self.turns = 0
        self.max_turns = 50  # Untuk mode time attack
        self.ai_player = ai_player
    
    def roll_dice(self, player):
        if player == self.ai_player:
            print(f"{player} (AI) is thinking...")
            time.sleep(1)
            return ai_roll_dice()
        else:
            input(f"{player}, tekan Enter untuk melempar dadu...")
            return random.randint(1, 6)
    
    def move_player(self, player):
        roll = self.roll_dice(player)
        print(f"{player} rolls a {roll}")
        new_pos = self.players[player] + roll
        
        if new_pos in self.snakes:
            print(f"Oh no! {player} got bitten by a snake! Moving to {self.snakes[new_pos]}")
            new_pos = self.snakes[new_pos]
        elif new_pos in self.ladders:
            print(f"Yay! {player} climbed a ladder to {self.ladders[new_pos]}")
            new_pos = self.ladders[new_pos]
        
        if new_pos in self.power_ups:
            self.apply_power_up(player, self.power_ups[new_pos])
        
        if new_pos >= self.board_size:
            print(f"{player} has reached the final square and won!")
            return True
        
        self.players[player] = new_pos
        print(f"{player} is now at {new_pos}\n")
        self.display_board()
        return False
    
    def apply_power_up(self, player, power_up):
        if power_up == 'boost':
            print(f"{player} found a boost! Moving forward 5 spaces.")
            self.players[player] += 5
        elif power_up == 'extra_turn':
            print(f"{player} gets an extra turn!")
            self.move_player(player)
        elif power_up == 'trap':
            print(f"{player} hit a trap! Skipping next turn.")
            pass  # Bisa ditambahkan efek tambahan
    
    def display_board(self):
        board = ['.'] * self.board_size
        for pos, player in self.players.items():
            board[player - 1] = pos[0].upper()
        
        for i in range(10, 0, -1):
            row = board[(i-1)*10:i*10]
            if i % 2 == 0:
                row.reverse()
            print(' '.join(row))
        print()
    
    def play_game(self):
        print("\nWelcome to Snakes and Ladders! 🎲")
        print("Commands:")
        print("- Players take turns rolling the dice.")
        print("- Snakes move you backward, ladders move you forward.")
        print("- Special power-ups (Boost, Extra Turn, Trap) may appear!")
        print("- The game ends when a player reaches 100 or max turns are reached.\n")
        
        players = list(self.players.keys())
        while self.turns < self.max_turns:
            for player in players:
                if self.move_player(player):
                    return
            self.turns += 1
        print("Game over! Max turns reached.")

if __name__ == "__main__":
    mode = input("Choose game mode: 1 for Player vs Player, 2 for Player vs AI: ")
    if mode == "1":
        players = input("Enter player names separated by commas: ").split(",")
        game = SnakesAndLadders(players)
    elif mode == "2":
        player_name = input("Enter your name: ")
        game = SnakesAndLadders([player_name, "GeminiAI"], ai_player="GeminiAI")
    else:
        print("Invalid mode selection. Exiting game.")
        exit()
    
    game.play_game()
