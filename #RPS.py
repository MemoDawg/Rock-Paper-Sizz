import time
import random

class RPSGame:
    def __init__(self):
        self.choices = ('Rock', 'Paper', 'Scissors')
        self.image = ('🪨', '📄', '✂️')
        self.menus = ('Play', 'Stats', 'Leave')
        self.delay = 0.5
        self.started = False
        self.wins = 0
        self.losses = 0
        self.streak = 0

    def record_win(self):
        self.wins += 1
        self.streak += 1

    def record_loss(self):
        self.losses += 1
        self.streak = 0

    def find(self, value):
        return self.choices.index(value)
    
    def determine_outcome(self, plr_input='Rock', rng_input=None):
        rng_input = rng_input or random.choice(self.choices)
        try:
            p1, p2 = self.find(plr_input), self.find(rng_input)
            
            img1, img2 = self.image[p1], self.image[p2]

            if p1 == p2:
                return self.color_text(f"Draw! {img1} = {img2}",93)
            elif (p1 - p2) % len(self.choices) == 1:
                self.record_win()
                return self.color_text(f"YOU Win! {img1} > {img2}",92)
            else:
                self.record_loss()
                return self.color_text(f"Robot Won! {img1} < {img2}",91)
        except ValueError:
            return 'Character does not exist!'
        except:
            return 'A General Error has Occurred!'
        

    def start_game(self):
        if self.started:
            print("\nGame already started!\n")
            self.menu()
            return

        self.started = True
        plr_choice = input(f'\nChoose a Character! {self.choices}\n').strip().capitalize()
        print('')

        for choice in self.choices:
            print(choice)
            time.sleep(self.delay)

        print('SHOOT!\n')
        time.sleep(self.delay / 2)
        print(self.determine_outcome(plr_choice))
        time.sleep(self.delay)

        self.started = False
        self.menu()

    def menu(self):
        plr_choice = input(f'\nWhat would you like to do? {self.menus}\n').strip().lower()

        if plr_choice == 'play':
            self.start_game()
        elif plr_choice == 'stats':
            self.show_stats()
        elif plr_choice == 'leave':
            print('\nThanks for playing, Goodbye!')
            pass
        else:
            print('Put a Valid Input')
            time.sleep(self.delay)
            self.menu()

    def show_stats(self):
        print(f'\n| Wins: {self.wins} | Losses: {self.losses} | Streak: {self.streak}\n')
        time.sleep(self.delay)
        self.menu()
        
    #not needed but cool
    def color_text(self, text, colorValue):
        return f"\033[{colorValue}m{text}\033[0m"
if __name__ == "__main__":
    game = RPSGame()
    game.menu()
