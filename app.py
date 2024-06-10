import json

from flask import Flask, Response, request
from flask_cors import CORS
from pydantic.error_wrappers import ValidationError

import crud
from models import Receipt

app = Flask(__name__)
app.logger.setLevel("INFO")
cors = CORS(app)


@app.route('/')
def hello():
    return Response("hello")


@app.route("/receipts/process", methods=["POST"])
def process_receipts():
    try:
        if request.content_type != 'application/json' or request.json is None or not request.json:
            app.logger.error(f"The receipt is invalid")
            return Response(json.dumps("The receipt is invalid"), status=400, mimetype="application/json")
        data = request.json

        receipt: Receipt = Receipt(**data)
        receipt_id = crud.create_receipt(receipt)

        app.logger.info(f"Successfully created receipt {receipt_id}")
        return Response(json.dumps({"id": receipt_id}), status=201, mimetype="application/json")

    except ValidationError as e:
        app.logger.error(f"Error processing receipt: {e}")
        return Response(json.dumps("The receipt is invalid"), status=400, mimetype="application/json")

    except Exception as e:
        app.logger.error(f"Error processing receipt: {e}")
        return Response(json.dumps("Internal Server Error"), status=500, mimetype="application/json")


@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_receipts_points(receipt_id: str):
    try:
        app.logger.info(f"Id is {receipt_id}")
        receipt_points = crud.get_receipt_points(receipt_id)
        app.logger.info(f"Successfully retrieved points for receipt id : {receipt_id}")
        return Response(json.dumps({"points": receipt_points}), status=200, mimetype="application/json")

    except ValueError as e:
        app.logger.error(f"No receipt found for that id {receipt_id}")
        return Response(json.dumps("No receipt found for that id"), status=404, mimetype="application/json")
    except Exception as e:
        app.logger.error(f"Error fetching points for receipt {receipt_id}: {e}")
        return Response(json.dumps("Internal Server Error"), status=500, mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
