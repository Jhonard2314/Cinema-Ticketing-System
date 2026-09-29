# Cinema Ticketing System
# Paradigm: Imperative / Structured (sequence, selection, iteration)

PRICES = {"regular": 250, "vip": 400}


def ask_seat():
    """Keep asking until the user enters a valid seat type."""
    while True:
        seat = input("  Seat type (Regular/VIP): ").strip().lower()
        if seat in PRICES:
            return seat
        print("  Invalid seat type. Please type Regular or VIP.")


def ask_tickets():
    """Keep asking until the user enters a valid ticket count."""
    while True:
        text = input("  Number of tickets: ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("  Please enter a whole number greater than 0.")


def main():
    transactions = []
    total_tickets = 0
    total_income = 0

    print("=== CINEMA TICKETING SYSTEM ===")
    print("Prices: Regular = P250, VIP = P400")
    print("Type 'done' as the customer name to finish.\n")

    # Input multiple customer transactions
    while True:
        name = input("Customer name: ").strip()
        if name.lower() == "done":
            break
        if name == "":
            print("  Name cannot be empty.")
            continue

        tickets = ask_tickets()
        seat = ask_seat()

        total = tickets * PRICES[seat]
        transactions.append((name, tickets, seat, total))

        total_tickets += tickets
        total_income += total
        print(f"  -> {name} pays P{total:,}\n")

    # Print the receipt and summary
    print("\n=== SALES REPORT ===")
    if not transactions:
        print("No transactions recorded.")
        return

    print(f"{'Customer':<15}{'Seat':<10}{'Tickets':>8}{'Total':>12}")
    print("-" * 45)
    for name, tickets, seat, total in transactions:
        print(f"{name:<15}{seat.upper():<10}{tickets:>8}{'P' + format(total, ','):>12}")
    print("-" * 45)
    print(f"Total tickets sold: {total_tickets}")
    print(f"Total income:       P{total_income:,}")


main()
