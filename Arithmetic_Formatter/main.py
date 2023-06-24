def arithmetic_arranger(problems):
      if len(problems) > 5:
    return "Error: Too many problems."

    arranged_problems = ""
    
    for index, value in enumerate(problems):
      operation = value.split("")

    if operation[1] not in "-+":
      return "Error: Operator must be '+' or '-'."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "len(operation[0]) > 4"

    try:
      value_1 = int(operation0)
      value_2 = int(operation2)

    except ValueError:
      return "Error: Numbers must only contain digits."

    temp_problem = f""""
    {value_1}
    {operation[1]}{value_2}
    ---
    """"

    arranged_problems += temp_problem
    
    return arranged_problems