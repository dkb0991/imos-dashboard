def calculate_imos(
    structural_health,
    liquidity,
    risk_appetite,
    momentum,
    sentiment,
    crash_risk,
    ipo_heat
):

    imos = (
        structural_health * 0.30 +
        liquidity * 0.25 +
        risk_appetite * 0.15 +
        momentum * 0.10 +
        sentiment * 0.05 +
        crash_risk * 0.10 +
        ipo_heat * 0.05
    )

    return round(imos, 1)
