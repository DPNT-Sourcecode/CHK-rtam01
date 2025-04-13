from dataclasses import dataclass, field
from collections import Counter
from typing import List


@dataclass
class Discount:
    quantity: int
    price: int

@dataclass
class FreeItem:
    quantity: int
    free_sku: str

@dataclass
class InventoryItem:
    sku: str
    price: int
    bulk_discounts: List[Discount] = field(default_factory=list)
    free_items: List[FreeItem] = field(default_factory=list)


class CheckoutSolution:

    def __init__(self):
        # Define items
        self.inventory = {
            "A": InventoryItem(
                "A",
                50,
                [Discount(3, 130), Discount(5, 200)],
            ),
            "B": InventoryItem(
                "B",
                30,
                [Discount(2, 45)],
            ),
            "C": InventoryItem("C", 20),
            "D": InventoryItem("D", 15),
            "E": InventoryItem(
                "E",
                40,
                [],
                [FreeItem(2, "B")],
            ),
        }

    def input_valid(self, skus):
        # Check for undefined invent
        if not all(
                isinstance(sku, str) and
                len(sku) == 1 and
                sku.isalpha() and
                sku in self.inventory
                for sku in skus
        ):
            return False
        return True

    # skus = unicode string
    def checkout(self, skus):
        # Check for undefined invent
        if not isinstance(skus, str):
            return -1
        if not self.input_valid(list(skus)):
            return -1

        # Count occurrences
        counts = Counter(skus)
        total = 0

        # Sum up total
        for sku, count in counts.items():
            item = self.inventory[sku]
            # Check for free items
            for free_item in item.free_items:
                if count >= free_item.quantity:
                    free_count = count // free_item.quantity
                    if free_item.free_sku in counts:
                        # Remove from counts?
                        counts[free_item.free_sku] -= free_count

        for sku, count in counts.items():
            item = self.inventory[sku]
            if item.bulk_discounts:
                # Handle largest discount first to favor customer with best discount.
                for discount in sorted(item.bulk_discounts, key=lambda d: d.quantity, reverse=True):
                    if count >= discount.quantity:
                        total += count // discount.quantity * discount.price
                        count %= discount.quantity

            total += count * item.price

        return total


