class Tile:
    def __init__(self):
        self.challenge_completed = False

    def describe(self):
        print("The rocks led you to a path uphill.\n*Poof* A purrr-sian cat "
              "appears in front of you!\n")
        if not self.challenge_completed:
            self.challenge()
        else:
            print("The rocks led you to a path uphill.\nIt's a little bit "
                  "windy and a flock of seagulls is flying above you.")

    def challenge(self):
        print("Meow good traveler! I have a question for you.\n"
              "You might as well go away and ignore me and my awesome fur but "
              "if you pass my little test I will reward you!\n\n"
              "Here is a series of numbers.\n"
              "What is the next number in the sequence?\n"
              "1\n"
              "11\n"
              "21\n"
              "1211\n"
              "111221\n"
              "312211\n"
              "13112221\n")
    #The next number in the sequence is 1113213211, because the rule for 
    #creating the next number is to simply describe the previous number. 
    #The first number is 1, or 1 (one) 1, so you get 11. 
    #To describe 11, you have two 1's, or 21. Now you have one 2 and one 1, 
    #so the next number is 1211. The solution is to simply continue describing 
    #the previous number using only numbers.\n")
     
    def action(self, player, do):
        if not self.challenge_completed:
            pass
        else:
            print("I don't understand...")
            
    def leave(self, player, direction):
        if direction == "s":
            print("Oh dear Basdet! You can't go north, you will fall of the "
                   "cliff!\n")
            return False
        elif direction == "n":
            print("It looks like the side of a wooden hut.\n"
                  "Since you don't walk though walls (yet) you can't go there.")
            return False
        else:
            return True