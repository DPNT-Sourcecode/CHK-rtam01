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
class GroupDiscount:
    quantity: int
    skus: List[str]
    price: int


@dataclass
class InventoryItem:
    sku: str
    price: int
    bulk_discounts: List[Discount] = field(default_factory=list)
    free_items: List[FreeItem] = field(default_factory=list)


class CheckoutSolution:

    def __init__(self):
        # Define group discount(s)
        self.group_discount = GroupDiscount(
            quantity=3,
            skus=["S", "T", "X", "Y", "Z"],
            price=45
        )

        # Define items
        product_data = [
            {"sku": "A", "price": 50, "bulk_discounts": [(3, 130), (5, 200)]},
            {"sku": "B", "price": 30, "bulk_discounts": [(2, 45)]},
            {"sku": "C", "price": 20},
            {"sku": "D", "price": 15},
            {"sku": "E", "price": 40, "free_items": [(2, "B")]},
            {"sku": "F", "price": 10, "free_items": [(3, "F")]},
            {"sku": "G", "price": 20},
            {"sku": "H", "price": 10, "bulk_discounts": [(5, 45), (10, 80)]},
            {"sku": "I", "price": 35},
            {"sku": "J", "price": 60},
            {"sku": "K", "price": 70, "bulk_discounts": [(2, 120)]},
            {"sku": "L", "price": 90},
            {"sku": "M", "price": 15},
            {"sku": "N", "price": 40, "free_items": [(3, "M")]},
            {"sku": "O", "price": 10},
            {"sku": "P", "price": 50, "bulk_discounts": [(5, 200)]},
            {"sku": "Q", "price": 30, "bulk_discounts": [(3, 80)]},
            {"sku": "R", "price": 50, "free_items": [(3, "Q")]},
            {"sku": "S", "price": 20},
            {"sku": "T", "price": 20},
            {"sku": "U", "price": 40, "free_items": [(4, "U")]},
            {"sku": "V", "price": 50, "bulk_discounts": [(2, 90), (3, 130)]},
            {"sku": "W", "price": 20},
            {"sku": "X", "price": 17},
            {"sku": "Y", "price": 20},
            {"sku": "Z", "price": 21},
        ]

        # Populate inventory dynamically
        self.inventory = {
            product["sku"]: InventoryItem(
                sku=product["sku"],
                price=product["price"],
                bulk_discounts=[
                    Discount(quantity, price) for quantity, price in product.get("bulk_discounts", [])
                ],
                free_items=[
                    FreeItem(quantity, free_sku) for quantity, free_sku in product.get("free_items", [])
                ],
            )
            for product in product_data
        }

    def input_valid(self, skus):
        # Check for undefined input or inventory items.
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
        if not isinstance(skus, str):
            return -1
        if not self.input_valid(list(skus)):
            return -1

        # Count occurrences
        counts = Counter(skus)
        total = 0

        total += self.handle_group_discounts(counts)

        # Sum up total
        for sku, count in counts.items():
            item = self.inventory[sku]
            # Check for free items
            for free_item in item.free_items:
                if count >= free_item.quantity:
                    free_count = count // free_item.quantity
                    if free_item.free_sku in counts:
                        # Remove from counts?
                        # Will that ever be a disadvantage?
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

    def handle_group_discounts(self, counts):
        total = 0

        group_items = {sku: counts[sku] for sku in self.group_discount.skus if sku in counts}
        total_group_count = sum(group_items.values())
        if total_group_count >= self.group_discount.quantity:
            # How many groups we have
            group_discount_count = total_group_count // self.group_discount.quantity
            total += group_discount_count * self.group_discount.price

            # Remove grouped items from counts, expensive -> cheapest
            items_to_removed = group_discount_count * self.group_discount.quantity
            sorted_group_items = sorted(
                group_items.items(),
                key=lambda x: self.inventory[x[0]].price,
                reverse=True
            )
            for sku, count in sorted_group_items:
                if items_to_removed <= 0:
                    break
                # Remove as many items as possible
                remove_count = min(count, items_to_removed)
                # Remove from basket
                counts[sku] -= remove_count
                # Remove from group items
                items_to_removed -= remove_count
        return total


