def calculate_solution_weights(molecular_weights, solutions_needed):
    #add class variable (result) shared by all instances
    result = []
    #determine the molecular formula and the concentration of solution needed
    for solution in solutions_needed:
        #delimit
        formula, concentration = solution.split('-')
        #change the string to a value (float)
        concentration_value = float(concentration[:-1])
        
        # Check if the molecular formula exists in molecular_weights
        if formula in molecular_weights:
            # Calculate the weight of the chemical needed to make a 1L solution of the concentration
            weight = molecular_weights[formula] * concentration_value
            #to the clas variable result, add the output
            result.append(f"{formula}-{concentration}-{weight:.2f}g")
        else:
            result.append('unknown')
    
    return result