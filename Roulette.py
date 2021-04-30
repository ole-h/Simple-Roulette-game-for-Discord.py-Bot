import random

        if message.content == "help roulette":
            await message.channel.send("Für Roulette: roulette gesetzt eingeben, wobei gesetzt = \n schwarz \n rot \n 0 \n sein muss.")

        if message.content.startswith("roulette"):
            gesetzt = message.content.split(' ')[1]
            gesetzt_param = -3
            if gesetzt.lower() == "schwarz":
                gesetzt_param = -1
            elif gesetzt.lower() == "rot":
                gesetzt_param = -2
            else:
                try:
                    gesetzt_param = int(gesetzt)
                except:
                    gesetzt_param = -3
            if gesetzt_param == -3:
                await message.channel.send("Ungültige Eingabe")
                return
            result = random.randint(0,36)
            print(result)

            if gesetzt_param == -1:
                won = result%2 == 0 and not result == 0
            elif gesetzt_param == -2:
                won = result%2 == 1
            else:
                won = result == gesetzt_param
            if won:
                await message.channel.send("Du hast gewonnen!!")
            else:
                await message.channel.send("Leider verloren :(")
