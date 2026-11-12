"""A small, colorful console slot machine."""
import random
import time


def icon():
    return {
        "🍒": 2,
        "🍉": 3,
        "🍋": 4,
        "🫑 ": 5,
        "⭐": 10,
    }


def spin():
    symbols = list(icon())
    result = [random.choice(symbols) for _ in range(3)]

    print("\n      ┌─────┬─────┬─────┐")
    print("      │ " + "  │ ".join(result)  + "  │")
    print("      └─────┴─────┴─────┘")
    return result


def get_bet(balance):
    while True:
        entry = input(f"Place your bet (1–{balance}, or Q to quit): $").strip()
        if entry.lower() == "q":
            return None
        try:
            amount = int(entry)
        except ValueError:
            print("Please enter a whole dollar amount.")
            continue
        if 1 <= amount <= balance:
            return amount
        print(f"Bet must be between $1 and ${balance}.")


def main():
    balance = 100
    payouts = icon()

    print("╔══════════════════════════════╗")
    print("║     🎰  SLOT MACHINE  🎰     ║")
    print("╚══════════════════════════════╝")
    print("Match three symbols to win your bet times the multiplier:\n")
    print("   " + "   ".join(f"{symbol} ×{multiplier}" for symbol, multiplier in payouts.items()))

    while balance > 0:
        print(f"\nYour balance: ${balance}")
        bet = get_bet(balance)
        if bet is None:
            break

        balance -= bet
        print("Spinning", end="", flush=True)
        for _ in range(3):
            time.sleep(0.25)
            print(".", end="", flush=True)
        print()

        result = spin()
        if result[0] == result[1] == result[2]:
            winnings = bet * payouts[result[0]]
            balance += winnings
            print(f"🎉 JACKPOT! Three {result[0]} symbols! You won ${winnings}.")
        else:
            print(f"No match this time. You lost ${bet}.")

    if balance == 0:
        print("\nYou're out of money. Game over!")
    else:
        print("\nThanks for playing! 🎰")
    print(f"Final balance: ${balance}")


if __name__ == "__main__":
    main()
