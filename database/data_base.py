from uuid import uuid4

from models import Receipt


class ReceiptDataStore:
    data_store: list[Receipt] = []

    def __init__(self):
        self.data_store = []

    def create_receipt(self, receipt: Receipt):
        receipt.id = str(uuid4())
        self.data_store.append(receipt)
        return receipt.id

    def get_receipt_with_id(self, receipt_id):
        receipt: Receipt = next((receipt for receipt in self.data_store if receipt.id == receipt_id), None)
        return receipt

    def check_receipt_exists(self, new_receipt):
        duplicate_receipt: Receipt = (receipt for receipt in self.data_store if
                                      receipt.retailer == new_receipt.retailer
                                      and receipt.purchaseDate == new_receipt.purchaseDate
                                      and receipt.purchaseTime == new_receipt.purchaseTime
                                      and receipt.total == new_receipt.total)
        duplicate_receipt = next(duplicate_receipt, None)
        return duplicate_receipt
