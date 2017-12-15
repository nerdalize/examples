class Transport:
    """This class calculates the amount of kilometers per transport type for an amount of CO2 (in kg)."""
    co2_kg = 0

    def __init__(self, co2_kg):
        self.co2_kg = co2_kg

    # source: https://www.delijn.be/en/overdelijn/organisatie/zorgzaam-ondernemen/milieu/co2-uitstoot-voertuigen.html
    def car(self):
        return self.co2_kg / 0.1

    # source: https://www.delijn.be/en/overdelijn/organisatie/zorgzaam-ondernemen/milieu/co2-uitstoot-voertuigen.html
    def train(self):
        return self.co2_kg / 0.028

    # source: http://www.carbonindependent.org/sources_aviation.html
    def airplane(self):
        return self.co2_kg / 0.101
