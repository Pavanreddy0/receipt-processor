from models.models import Receipt


def calculate_points_for_receipt(receipt: Receipt):
    """

    These rules collectively define how many points should be awarded to a receipt.

        One point for every alphanumeric character in the retailer name.
        50 points if the total is a round dollar amount with no cents.
        25 points if the total is a multiple of 0.25.
        5 points for every two items on the receipt.
        If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result 
            is the number of points earned.
        6 points if the day in the purchase date is odd.
        10 points if the time of purchase is after 2:00pm and before 4:00pm.

    """
    total_points = 0
    # 1. Find all alphanumeric character in the retailer name
    alphanumeric_Characters = [i for i in receipt.retailer if i.isalnum()]
    total_points += len(alphanumeric_Characters)
    # 2. 50 points if the total is a round dollar amount with no cents.
    if int(receipt.total) == receipt.total:
        total_points += 50
    # 3. 25 points if the total is a multiple of 0.25.
    if receipt.total % 0.25 == 0:
        total_points += 25
    # 4. 5 points for every two items on the receipt.
    total_points += (len(receipt.items) // 2) * 5
    # 5. If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to
    # the nearest integer. The result is the number of points earned.
    for item in receipt.items:
        if len(item.description.strip()) % 3 == 0:
            total_points += round(item.price * 0.2)
    # 6. 6 points if the day in the purchase date is odd.
    if receipt.purchaseDate.day % 2 != 0:
        total_points += 6
    # 7. 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    if receipt.purchaseTime.hour >= 14 and receipt.purchaseTime.hour < 16:
        total_points += 10
    return total_points
