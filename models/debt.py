def calculate_dos(
    ten_year_yield,
    real_yield,
    rbi_cycle,
    yield_curve,
    credit_spread
):

    dos = (
        ten_year_yield * 0.25 +
        real_yield * 0.25 +
        rbi_cycle * 0.20 +
        yield_curve * 0.20 +
        credit_spread * 0.10
    )

    return round(dos, 1)
