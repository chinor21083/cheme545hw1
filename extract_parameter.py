def extract_parameter(unit_name, parameter_name, index): 
    #add code to handle exceptions here
    unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
    }
    
    try: 
        parameter = unit_operations_data[unit_name][parameter_name][index]
        return unit_name + "_"+ parameter_name + "_"+str(parameter)
    except KeyError: 
        print("Invalid input")
