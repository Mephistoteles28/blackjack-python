# blackjack-python

This is my second project on my journey to learn Python. And this project is a game called **blackjack**.

Blackjack is a casino banking game. The most widely played casino banking game in the world, it uses decks of 52 cards and descends from a global family of casino banking games known as Twenty-One.

## How to play

You can play this game by **_click on the .exe file_** inside dist folder (dist\tiktaktoeV2.exe) and it will automatically run in your command prompt.

1. You can download it by using git command,
   `git clone https://github.com/Mephistoteles28/tictaktoe-python.git`
2. Run the file by selecting the .exe file inside **_dist\tiktaktoeV2.exe_**.

## Rules

And here some rules in this game:

1. This game just needs one player, and the player will against the system,
2. First you will asked by the system to choose wether you wanna to `play` or `exit` by selecting `1` or `2`,

```
Welcome to Black Jack
> Get as close to 21 as you can without going over!
> Dealer hits until she reaches 17. Aces count as 1 or 11.
1. Play
2. Exit
What you wanna do :
```

2. The player will be gifted 100 chips, and the player needs to input how much to put into the bet.

```
Welcome to Black Jack
> Get as close to 21 as you can without going over!
> Dealer hits until she reaches 17. Aces count as 1 or 11.
1. Play
2. Exit
What you wanna do : 1
Player chips : 100
Place a bet :
```

3. The system will show the player cards and ask if the player wants to hit it or not. (hit means take one card into player decks)

```
Player chips : 100
Place a bet : 10
Player cards : Jack of Spades & Two of Hearts
Player value : 12
Hit? [Y/N]:
```

4. The system will show the system/dealer cards and if the value of the player card is more than the dealer cards, the player wins and the player chip is increased according to the bet amount.
5. And if the player's card is less than the dealer cards, the player will lose and the player's chip will decrease according to the bet amount.

```
Hit? [Y/N]: y
Show some dealer card? [Y/N] : n
Player cards : Four of Clubs & Five of Spades & Six of Diamonds
Player cards value : 15
Hit? [Y/N]: n
Dealer value : 19
Dealer cards : Two of Spades & Five of Hearts & Six of Hearts
Six of Hearts
You lose
Player chips : 50
```

6. The game will end if the player exit the game and the player chip is 0.
