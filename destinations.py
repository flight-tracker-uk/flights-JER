"""Jersey Airport (JER) destinations — April 2026."""

DESTINATIONS = {
    "JER": {
        "name": "Jersey",
        "routes": {
            "AGP": "Malaga",
            "AMS": "Amsterdam",
            "BFS": "Belfast International",
            "BHX": "Birmingham",
            "BOD": "Bordeaux",
            "BRS": "Bristol",
            "CDG": "Paris CDG",
            "DUB": "Dublin",
            "DUS": "Dusseldorf",
            "EDI": "Edinburgh",
            "EMA": "East Midlands",
            "EXT": "Exeter",
            "FAO": "Faro",
            "FNC": "Funchal",
            "GCI": "Guernsey",
            "GLA": "Glasgow",
            "IBZ": "Ibiza",
            "LBA": "Leeds Bradford",
            "LGW": "London Gatwick",
            "LHR": "London Heathrow",
            "LPL": "Liverpool",
            "LTN": "London Luton",
            "MAN": "Manchester",
            "MUC": "Munich",
            "NCL": "Newcastle",
            "NWI": "Norwich",
            "PMI": "Palma",
            "SEN": "Southend",
            "SOU": "Southampton",
            "TFS": "Tenerife South",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
