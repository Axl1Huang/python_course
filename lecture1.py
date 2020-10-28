#! /usr/bin/python3  
def function_with_return(input_to_function1,input_to_function2,input_to_function3):
    variable_that_we_return_from_function=input_to_function1 + input_to_function2+ input_to_function3
    return variable_that_we_return_from_function

answer_to_print1= function_with_return(1,4,5)
def function_with_return2(input_to_function1,input_to_function2,input_to_function3):
    variable_that_we_return_from_function=input_to_function1 + input_to_function2+ input_to_function3
    return variable_that_we_return_from_function

answer_to_print2= function_with_return2(1,2,3)
print(answer_to_print1)
print(answer_to_print2)