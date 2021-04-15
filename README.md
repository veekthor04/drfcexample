# drftest
django rest framework test

In this project you have to hide a specific data from anonymous users.

Below is the example of exposed API:
http://127.0.0.1:8000/app/car/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "car_name": "Meteor",
        "engine": {
            "id": 1,
            "displacement": "2500 CC",
            "power": "240 BHP",
            "maker": "Nova" (HIDE THIS SPECIFIC FIELD TO ANONYMOUS USER)
        },
        "price": { (HIDE THIS ENTIRE FIELD TO ANONYMOUS USER)
            "id": 1,
            "price": 2000
        }
    },
    {
        "id": 2,
        "car_name": "Ingot",
        "engine": {
            "id": 2,
            "displacement": "4500",
            "power": "360",
            "maker": "Asta"
        },
        "price": {
            "id": 2,
            "price": 5000
        }
    }
]

RESULT: To the anonymous user the api should look like the example beleow:

[
    {
        "id": 1,
        "car_name": "Meteor",
        "engine": {
            "id": 1,
            "displacement": "2500 CC",
            "power": "240 BHP"
        }
    }
    {
        "id": 2,
        "car_name": "Ingot",
        "engine": {
            "id": 2,
            "displacement": "4500",
            "power": "360"
        }
    }
]

