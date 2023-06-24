def arithmetic_arranger(problems):
  if len(problems) > 5:
    return "Error: Too many problems."

    arranged_problems = ""
    
    for index, value in enumerate(problems):
      operation = value.split("")

    if operation[1] not in "-+":
      return "Error: Operator must be '+'"
      or '-'."

    try:
      value_1 = int(operation0)
      value_2 = int(operation2)
    return arranged_problems