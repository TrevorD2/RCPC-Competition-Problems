def solution(measurement: float, unit: str, ingrediant: str) -> str:
    weight_convert = {
        "pound" : 16,
        "ounce" : 1
    }
    vol_convert = {
        "gallon" : 128,
        "quart" : 32,
        "pint" : 16,
        "cup" : 8,
        "fluid ounce" : 1,
        "tablespoon" : 1/2,
        "teaspoon" : 1/6
    }

    if unit in weight_convert:
        metric_measurement = measurement * vol_convert[unit] *  28.35
    if unit in vol_convert:
        metric_measurement = measurement * vol_convert[unit] *  29.57


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(inpt)}\n{solution(inpt) == io_dict[inpt]}\n")
