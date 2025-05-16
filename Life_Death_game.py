import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.hp = 1
        self.items = {
            "cigarette": 1,
            "energy_drink": 1,
            "magnifying_glass": 1,
            "handcuffs": 1
        }

class BuckshotRoulette:
    def __init__(self):
        self.level = 1
        self.max_level = 3
        self.round = 1
        self.player = Player("You")
        self.dealer = Player("Dealer")
        self.skip_dealer_turn = False
        self.force_dealer_shoot = False

    def generate_shells(self):
        if self.level == 1:
            shells = ['live'] + ['blank'] * 5
        elif self.level == 2:
            shells = ['live'] * 2 + ['blank'] * 4
        else:
            shells = ['live'] * 3 + ['blank'] * 3
        random.shuffle(shells)
        return shells

    def draw_shell(self):
        return self.shells.pop(0) if self.shells else None 
        # short hand if-else statement 

    def peek_shell(self):
        return self.shells[0] if self.shells else "none"

    def shoot(self, shooter, target):
        shell = self.draw_shell()
        print(f"\n{shooter.name} aims at {target.name} and pulls the trigger...")
        time.sleep(1)

        if not shell:
            print("The gun clicks... it's empty. The game ends in a draw.")
            return 'draw'

        if shell == 'live':
            print("💥 BANG! It's a live round!")
            target.hp -= 1
            if target.hp <= 0:
                target.alive = False
                return 'win' if shooter.name == self.player.name else 'lose'
            else:
                print(f"{target.name} survived thanks to extra HP!")
                return 'continue'
        else:
            print("Click. It was a blank.")
            return 'continue'

    def use_item(self, player, opponent):
        print("\nWhich item do you want to use?")
        for item, count in player.items.items():
            print(f"{item} - {count} left")
        choice = input("Enter item name or 'cancel': ").strip().lower()

        if choice not in player.items or player.items[choice] == 0:
            print("Invalid or unavailable item.")
            return 'continue'

        if choice == "cigarette":
            player.hp += 1
            print(f"{player.name} smokes a cigarette and gains +1 HP. (HP: {player.hp})")
        elif choice == "energy_drink":
            self.force_dealer_shoot = True
            print(f"{player.name} drinks an energy drink. Skipping their turn and forcing the opponent to shoot next.")
        elif choice == "magnifying_glass":
            peek = self.peek_shell()
            print(f"{player.name} uses magnifying glass: The next shell is {'LIVE' if peek == 'live' else 'BLANK'}.")
        elif choice == "handcuffs":
            self.skip_dealer_turn = True
            print(f"{player.name} uses handcuffs! Dealer's next turn is skipped.")

        player.items[choice] -= 1
        time.sleep(1)
        return 'continue'

    def player_turn(self):
        print(f"\nYour HP: {self.player.hp} | Dealer HP: {self.dealer.hp}")
        print("Your turn. Choose an action:")
        print("1. Shoot yourself")
        print("2. Shoot the dealer")
        print("3. Use item")

        choice = input("Enter 1, 2, or 3: ").strip()
        while choice not in ['1', '2', '3']:
            choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

        if choice == '3':
            return self.use_item(self.player, self.dealer)

        target = self.player if choice == '1' else self.dealer
        return self.shoot(self.player, target)

    def dealer_turn(self):
        if self.skip_dealer_turn:
            print("\nDealer is handcuffed and misses their turn!")
            self.skip_dealer_turn = False
            return 'continue'

        if self.force_dealer_shoot:
            print("\nDealer is forced to shoot due to your energy drink!")
            self.force_dealer_shoot = False
            target = self.dealer
        else:
            if self.level == 1:
                target = random.choice([self.player, self.dealer])
            elif self.level == 2:
                target = self.player if random.random() < 0.7 else self.dealer
            else:
                if len(self.shells) == 1 and self.shells[0] == 'live':
                    target = self.dealer
                else:
                    target = self.player

        return self.shoot(self.dealer, target)

    def play_round(self):
        print(f"\n=== Round {self.round} - Level {self.level} ===")
        self.shells = self.generate_shells()
        self.turn = 0
        self.player.alive = True
        self.dealer.alive = True
        self.player.hp = max(1 , self.player.hp)
        self.dealer.hp = 1

        while self.player.alive and self.dealer.alive and self.shells:
            if self.turn == 0:
                result = self.player_turn()
                if self.force_dealer_shoot:
                    self.turn = 1  # force dealer to go again
            else:
                result = self.dealer_turn()

            if result in ['win', 'lose', 'draw']:
                return result

            self.turn = 1 - self.turn  # Switch turns

    def start(self):
        print("=== Welcome to Buckshot Roulette: Enhanced Edition ===")
        print("Survive and use items wisely to beat all levels!")
        input("Press Enter to begin...\n")

        while self.level <= self.max_level:
            result = self.play_round()
            if result == 'win':
                print("\n You survived this round.")
                if self.level < self.max_level:
                    self.level += 1
                    self.round += 1
                    print(" Difficulty increased!")
                else:
                    print("\n Congratulations! You've beaten all levels!")
                    break
            elif result == 'lose':
                print("\n You were shot. Game over.")
                break
            elif result == 'draw':
                print("\ The chamber was empty. It's a draw.")
                break

if __name__ == "__main__":
    game = BuckshotRoulette()
    game.start()




        

    


