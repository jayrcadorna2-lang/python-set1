def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def check_status(grades):
    return "PASSED" if grades and calculate_average(grades) >= 75 else "FAILED"

def get_highest(grades):
    return max(grades) if grades else None

def get_lowest(grades):
    return min(grades) if grades else None