def calculate_power(voltage, current):
    return round(voltage * current, 2)


def calculate_efficiency(output_power, input_power):
    if input_power == 0:
        return 0

    efficiency = (output_power / input_power) * 100
    return round(efficiency, 2)