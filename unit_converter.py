def length_converter(value, from_unit, to_unit):
    length_units = {
        "meter": 1.0,
        "kilometer": 0.001,
        "centimeter": 100.0,
        "millimeter": 1000.0,
        "mile": 0.000621371,
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701
    }
    if from_unit not in length_units or to_unit not in length_units:
        return "Invalid unit!"
    return value * (length_units[to_unit] / length_units[from_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "kilogram": 1.0,
        "gram": 1000.0,
        "milligram": 1000000.0,
        "pound": 2.20462,
        "ounce": 35.274
    }
    if from_unit not in weight_units or to_unit not in weight_units:
        return "Invalid unit!"
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    valid_units = {"celsius", "fahrenheit", "kelvin"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return "Invalid unit!"
    if from_unit == "celsius":
        return value * 9/5 + 32 if to_unit == "fahrenheit" else value + 273.15
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32
    return value

def main():
    print("Unit Converter: Length, Weight, Temperature")
    categories = {"length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
                  "weight": ["kilogram", "gram", "milligram", "pound", "ounce"],
                  "temperature": ["celsius", "fahrenheit", "kelvin"]}
    
    category = input("Enter category (length/weight/temperature or 'exit' to quit): ").strip().lower()
    if category == "exit":
        print("Goodbye!")
        return
    
    if category not in categories:
        print("Invalid category!")
        return
    
    print(f"Available units: {', '.join(categories[category])}")
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid number!")
        return
    
    from_unit = input("Enter from unit: ").strip().lower()
    to_unit = input("Enter to unit: ").strip().lower()
    
    if category == "length":
        result = length_converter(value, from_unit, to_unit)
    elif category == "weight":
        result = weight_converter(value, from_unit, to_unit)
    elif category == "temperature":
        result = temperature_converter(value, from_unit, to_unit)
    else:
        print("Invalid category!")
        return
    
    print(f"Converted Value: {result} {to_unit}")

if __name__ == "__main__":
    main()
