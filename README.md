# receipt-processor

## steps to run the project

## install docker if it's not already installed

```
docker build -t receipt-processor .
docker run -d -p 8080:8080 receipt-processor
```

## host url
```
http://127.0.0.1:8080
```

## sample API call
```
POST API 

curl --location 'http://127.0.0.1:8080/receipts/process' \
--header 'Content-Type: application/json' \
--data '{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.498"
        },
        {
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
        },
        {
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
        },
        {
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
        },
        {
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
        }
    ],
    "total": "35.35"
}'

GET API

curl --location 'http://127.0.0.1:8080/receipts/6e680fe8-7c4f-4e1d-a665-d0972f19b1e/points'
```