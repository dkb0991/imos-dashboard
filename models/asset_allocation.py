def get_asset_allocation(
    imos,
    cdi,
    dos
):

    # Strong environment

    if cdi >= 80:

        return {
            "Equity": 70,
            "Debt": 15,
            "REITs": 5,
            "Gold": 5,
            "Cash": 5
        }

    # Healthy environment

    elif cdi >= 60:

        return {
            "Equity": 60,
            "Debt": 20,
            "REITs": 10,
            "Gold": 5,
            "Cash": 5
        }

    # Neutral environment

    elif cdi >= 40:

        return {
            "Equity": 45,
            "Debt": 25,
            "REITs": 10,
            "Gold": 10,
            "Cash": 10
        }

    # Defensive environment

    elif cdi >= 20:

        return {
            "Equity": 30,
            "Debt": 35,
            "REITs": 10,
            "Gold": 10,
            "Cash": 15
        }

    # High caution

    return {
        "Equity": 15,
        "Debt": 40,
        "REITs": 10,
        "Gold": 10,
        "Cash": 25
    }
