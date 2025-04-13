from dataclasses import dataclass
from collections import Counter


@dataclass
class InventoryItem:
    sku: str
    price: int
    bulk: int
    bulk_price: int


class CheckoutSolution:

    def __init__(self):
        # Define items
        self.inventory = {
            "A": InventoryItem("A", 50, 3, 130),
            "B": InventoryItem("B", 30, 2, 45),
            "C": InventoryItem("C", 20, 1, 0),
            "D": InventoryItem("D", 15, 1, 0),
        }

    # skus = unicode string
    def checkout(self, skus):
        # Check for undefined invent
        if not isinstance(skus, list):
            return -1
        if not all(isinstance(sku, str) and len(sku) == 1 for sku in skus):
            return -1
        

        # Count occurrences
        counts = Counter(skus)
        total = 0

        # Sum up total

