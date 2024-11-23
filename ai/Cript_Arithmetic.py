import re
def solve_arithmetic(expression):
    expression=expression.lower()
    expression=re.sub(r'plus','+',expression)
    expression=re.sub(r'minus','-',expression)
    expression=re.sub(r'multiplied by','*',expression)
    expression=re.sub(r'divide by','/',expression)
    try:
        result=eval(expression)
        return f"The result of'{expression}'is{result}."
    except Exception as e:
        return "Sorry,i couldn't understand or solve the problem."
print("Welcome to the AI Arithmetic Solver!")
print("You can enter problems like '5 plus 3','10 minus 4',or'6 multiplied by 2'.Type 'exit' to quit.")
while True:
    user_input=input("\nEnter your arithmetic problem:")
    if user_input.lower()=='exit':
        print("Goodbye!")
        break
    print(solve_arithmetic(user_input))
