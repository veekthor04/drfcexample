# drfc-example
django rest framework example

In this project you have to hide specific data from anonymous/logged out users.

Use the admin to login 
id: admin
password: 1234

Hide the Price and Maker field to logged out/anonymous users only.

Below is the example of API:
http://127.0.0.1:8000/app/car/


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

