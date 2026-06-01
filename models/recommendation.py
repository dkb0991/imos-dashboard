def get_market_assessment(imos):

    if imos >= 80:
        return "Strong Bull Market"

    elif imos >= 60:
        return "Healthy Market"

    elif imos >= 40:
        return "Neutral Market"

    elif imos >= 20:
        return "Weak Market"

    return "High Risk Market"


def get_deployment_action(cdi):

    if cdi >= 80:
        return "Deploy Aggressively"

    elif cdi >= 60:
        return "Deploy Normally"

    elif cdi >= 40:
        return "Deploy Gradually"

    elif cdi >= 20:
        return "Defensive"

    return "Wait"


def get_debt_assessment(dos):

    if dos >= 80:
        return "Very Attractive"

    elif dos >= 60:
        return "Attractive"

    elif dos >= 40:
        return "Neutral"

    elif dos >= 20:
        return "Weak"

    return "Unattractive"
