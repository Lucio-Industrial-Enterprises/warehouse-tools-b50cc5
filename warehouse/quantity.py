"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative integer quantity, raising ValueError otherwise."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return quantity
