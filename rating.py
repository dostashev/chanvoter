ELO_BASE = 10
ELO_DENOMINATOR = 400
ELO_K = 32


def get_elo_change(rating_a, rating_b, res_a, res_b):
    if res_a + res_b == 0:
        res_a = res_b = 1
    q_a = ELO_BASE**(rating_a / ELO_DENOMINATOR)
    q_b = ELO_BASE**(rating_b / ELO_DENOMINATOR)
    e_a = q_a / (q_a + q_b)
    return ELO_K * (res_a / (res_a + res_b) - e_a)
