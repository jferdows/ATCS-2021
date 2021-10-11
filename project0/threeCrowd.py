names = ["Adrian", "Beatriz", "Connor", "Elenor"]
if len(names) > 3:
    print("The room is crowded")

del names[0:2]

if len(names) > 3:
    print("The room is crowded")