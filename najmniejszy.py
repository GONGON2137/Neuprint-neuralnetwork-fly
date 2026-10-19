for dzielna in range(2,21):
    for dzielnik in range(2, dzielna+1):
        if dzielna % dzielnik == 0:
            print(f"najmniejszy dzielnik {dzielna} to {dzielnik}")
            breakg