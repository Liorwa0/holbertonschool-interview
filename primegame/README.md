# Prime Game

Maria and Ben take turns removing a prime number and its multiples from
the numbers 1 through n. Maria plays first, and the player with no valid
move loses.

## Solution

Each prime can be selected exactly once. The number of moves in a round is
therefore the number of primes less than or equal to n. Maria wins when
this count is odd; otherwise, Ben wins.

`0-prime_game.py` uses the Sieve of Eratosthenes and prefix counts to
determine the winner across all rounds.

## Usage

```python
isWinner = __import__('0-prime_game').isWinner
print(isWinner(5, [2, 5, 1, 4, 3]))
# Ben
```

No third-party packages are required.
