class Tile:
    def describe(self):
        print("You walk in the beach. There is a light house on the west.\n")

    def action(self, player, do):
        print("I don't understand.")
    
    def leave(self, player, direction):
        if direction == "n":
            print("It's the open sea. You can't go anywhere near by "
                  "swimming.\n")
            return False
        else:
            return True