done = False
player_a, player_b = "", ""
r,p,s = "Rock", "Paper", "Scissors"
final = ""


def vaild_move(player, type):
    while True:
        player = input(f"Player {type}: Enter [R,P,S]: ").lower()
        if player == "r" or player == "p" or player == "s":
            break
        else: 
            print("Invaild Input: Please Try Again")
            continue
    return player

def check(player_a, player_b):
    if player_a == "r":
        match player_b:
            case "r":
                return f"Player A: {r} vs Player B: {r}: Its a Tie!"
            case "p":
                return f"Player A: {r} vs Player B: {p}: Paper covers Rock"
            case "s":
                return f"Player A: {r} vs Player B: {s}: Rock breaks Scissors"
    elif player_a == "p":
        match player_b:
            case "r":
                return f"Player A: {p} vs Player B: {p}: Its a Tie!"
            case "p":
                return f"Player A: {p} vs Player B: {r}: Paper covers Rock"
            case "s":
                return f"Player A: {p} vs Player B: {s}: Scissors cuts Paper"
    else:
        match player_b:
            case "s":
                return f"Player A: {s} vs Player B: {s}: Its a Tie!"
            case "r":
                return f"Player A: {s} vs Player B: {r}: Rock breaks Scissors"
            case "p":
                return f"Player A: {s} vs Player B: {p}: Scissors cuts Paper"



while not done:
    player_a, player_b = vaild_move(player_b, "A"), vaild_move(player_b, "B")
    final = check(player_a, player_b)
    print(final)
    if(input("Play again? [Y/N]: ").lower() == "y"):
        continue
    else:
        done = True
