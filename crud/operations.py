from database import receiptDataStore
from models import Receipt
from utils import calculate_points_for_receipt


def create_receipt(receipt: Receipt):
    """ Used to generate the receipt_id for a given receipt

    For simplicity, assuming the (retailer, purchaseDate, purchaseTime, total) combination will be unique.
    
    If a receipt with these data is already present then return the id of the receipt else generate a new id
    
    Args:
        receipt (Receipt): _description_
    returns id of the receipt
    """

    # Check if the receipt already exists
    duplicate_receipt: Receipt = receiptDataStore.check_receipt_exists(receipt)

    # If the receipt already exists, then return the id of the receipt and return
    if duplicate_receipt is not None:
        return duplicate_receipt.id

    # create a new receipt if it doesn't exist
    receipt.points = calculate_points_for_receipt(receipt)
    receipt_id = receiptDataStore.create_receipt(receipt)
    return receipt_id


def get_receipt_points(receipt_id):
    receipt = receiptDataStore.get_receipt_with_id(receipt_id)
    if receipt is None:
        raise ValueError("Invalid receipt_id: %s" % receipt_id)
    return receipt.points
