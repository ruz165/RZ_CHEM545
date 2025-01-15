def extract_parameter(unit_name, parameter_name, index):
    #check that the unit and parameter names and the index are valid strings or values
    try:
        unit = unit_operations_data[unit_name]
        parameter = unit[parameter_name]
        value = parameter[index]

        return f"{unit_name}_{parameter_name}_{value}"

    #if the values are not valid, return Invalid input
    except (KeyError, IndexError):
        return "Invalid input"