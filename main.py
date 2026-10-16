# Billing System (OOP-based) - Week 3 Assignment


class Product:
    """Represents an individual product item in the inventory/bill."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """Returns the total price for this product (Price * Quantity)."""
        return self.price * self.quantity


class Bill:
    """Manages product collection, calculates totals + tax, and prints formatted bill."""

    def __init__(self, tax_rate: float = 0.05):
        self.items = []
        self.tax_rate = tax_rate  # Default 5% tax

    def add_product(self, product: Product):
        """Adds a Product object to the bill."""
        self.items.append(product)
        print(f"Added '{product.name}' (x{product.quantity}) to bill successfully!")

    def calculate_subtotal(self) -> float:
        """Calculates subtotal before tax."""
        return sum(item.calculate_total_price() for item in self.items)

    def calculate_tax(self) -> float:
        """Calculates tax amount based on tax_rate."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_grand_total(self) -> float:
        """Calculates final total including tax."""
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        """Displays the itemized bill in a formatted table."""
        if not self.items:
            print("\nThe bill is currently empty. Please add products first.\n")
            return

        print("\n" + "=" * 62)
        print("                   INVOICE / FINAL BILL                   ")
        print("=" * 62)
        print(f"{'Item Name':<22} | {'Price ($)':<10} | {'Qty':<6} | {'Total ($)':<12}")
        print("-" * 62)

        for item in self.items:
            print(
                f"{item.name:<22} | ${item.price:<9.2f} | {item.quantity:<6} | ${item.calculate_total_price():<11.2f}"
            )

        print("-" * 62)
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        grand_total = self.calculate_grand_total()

        print(f"{'Subtotal:':<43} ${subtotal:>15.2f}")
        print(f"{f'Tax ({self.tax_rate * 100:.0f}%):':<43} ${tax:>15.2f}")
        print("=" * 62)
        print(f"{'GRAND TOTAL:':<43} ${grand_total:>15.2f}")
        print("=" * 62 + "\n")


def main():
    bill = Bill(tax_rate=0.05)  # 5% tax rate

    while True:
        print("==========================================")
        print("        OOP BILLING SYSTEM MENU           ")
        print("==========================================")
        print("1. Add Product to Bill")
        print("2. Display Itemized Bill")
        print("3. Reset Bill")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter Product Name: ").strip()
            try:
                price = float(input("Enter Unit Price ($): "))
                quantity = int(input("Enter Quantity: "))
                if price <= 0 or quantity <= 0:
                    print("Error: Price and Quantity must be positive numbers!\n")
                    continue
                product = Product(name, price, quantity)
                bill.add_product(product)
            except ValueError:
                print("Error: Invalid input! Price must be a number and Quantity an integer.\n")

        elif choice == "2":
            bill.display_bill()

        elif choice == "3":
            bill = Bill(tax_rate=0.05)
            print("\nBill reset successfully! All items removed.\n")

        elif choice == "4":
            print("\nThank you for using the OOP Billing System. Goodbye!")
            break

        else:
            print("Invalid selection! Please choose a number between 1 and 4.\n")


if __name__ == "__main__":
    main()