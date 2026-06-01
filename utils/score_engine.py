from data.sample_data import sample_inputs

from models.imos import calculate_imos
from models.allocation import calculate_cdi
from models.debt import calculate_dos


def get_scores():

    imos = calculate_imos(
        sample_inputs["structural_health"],
        sample_inputs["liquidity"],
        sample_inputs["risk_appetite"],
        sample_inputs["momentum"],
        sample_inputs["sentiment"],
        sample_inputs["crash_risk"],
        sample_inputs["ipo_heat"]
    )

    cdi = calculate_cdi(
        imos,
        sample_inputs["valuation"],
        sample_inputs["crash_risk"],
        sample_inputs["drawdown"],
        sample_inputs["vix"]
    )

    dos = calculate_dos(
        sample_inputs["ten_year_yield"],
        sample_inputs["real_yield"],
        sample_inputs["rbi_cycle"],
        sample_inputs["yield_curve"],
        sample_inputs["credit_spread"]
    )

    return {
        "imos": imos,
        "cdi": cdi,
        "dos": dos
    }
