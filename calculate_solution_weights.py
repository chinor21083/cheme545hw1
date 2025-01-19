def calculate_solution_weights(molecular_weights, solutions_needed):
    output = []

#Create a list of chemicals from the input
    for solution in solutions_needed:
        try: 
            weight = round(molecular_weights[solution.split('-')[0]]*float(solution.split('-')[1][:-1]),2)
            weight=f"{weight:.2f}"
            output.append(solution+'-'+str(weight)+'g')
        except KeyError: 
            output.append('unknown')

    return output