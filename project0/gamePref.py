games = ["Monopoly", "Jenga", "Uno", "Egyptian War"]
for x in games:
    print(x)

print()
new_game = input("What is a game you like? ")
games.append(new_game)

print("These are all the games we like to play: ")
for x in games:
    print(x)