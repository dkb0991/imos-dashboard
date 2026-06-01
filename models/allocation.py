def calculate_cdi(
    imos,
    valuation,
    crash_risk,
    drawdown,
    vix
):

    cdi = (
        imos * 0.35 +
        valuation * 0.25 +
        crash_risk * 0.20 +
        drawdown * 0.10 +
        vix * 0.10
    )

    return round(cdi, 1)
