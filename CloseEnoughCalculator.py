import re

def main():
    while (True):
        expr = input("Enter a mixed number: ") # change test expression
        if (expr == "q"):
            break
        else:
            fixedExpr = convertToPostfix(expr)
            print(f"You entered {expr}, which turned into {fixedExpr}") # change test expression
    

## TODO input handling
    # length
    # units

# TODO def list of functions to convert unit to unit (each precision should have its own function definitely)

# TODO def convert fraction to decimal

# TODO def round to the nearest precision (each precision should have its own function probably)

# TODO error handling (if number inputted has anything besides numerals, ., and /.)
    # accepted formats x, x.x, x/x, x.x/x.x, x.x/x.x

# TODO low priority try to implement a tree version of evaluating infix instead of postfix

# TODO earlier than the parser, just dont accept mixed fractions or parenths

# TODO sanitize inputs and use ast to assert mathematical expression is valid
# TODO convert to postfix
""" RULES FOR INFIX to POSTFIX:
- extra step for mixed numbers: replace all spaces with + (or rather replace all spaces followed by a digit)
- remove extra spaces
- going left to right...
- numbers go on the output stack
- when encountering an operator
    - while operator isnt a left paren AND it has a lesser or equal prescendence
        - pop the top of the stack
        - REMEMBER, left operators of equal precedence have GREATER precedence because left to right rule (rule of associativity)
    - push operator onto operator stack
- when encountering a left paren
    - push it onto the stack 
- when encountering a right paren
    - pop every operator on the stack until you get to a left paren (while loop)
        - make sure stack is not empty before hitting a left paren, if so return error "unexpected item in bagging area"
        - remember you still follow rules of precedence while dealing with parens
    - pop and destroy the left paren once you hit it
- when empty, pop all the operators remaining on the output stack
"""
def convertToPostfix(expr:str):
    postfix = ""

    # CONVERTING MIXED NUMBERS INTO POSTFIX-FRIENDLY EXPRESSIONS
    # Why not just convert instances of spaces into +'s if you assume no user error?
        # "3 * 1 1/8" would be incorrect due to order of operations
    expr = re.sub(
        r"(\d+)\s+(\d+)\s*/\s*(\d+)",
        r"(\1+\2/\3)",expr)
        # Parentheses "capture" an instance of the expression we are currently replacing
        # Each capture is assigned to 1, 2, 3... etc, and thus can be manipulated as such
        # re.sub will replace all instances so no need for a loop
    expr = expr.replace(" ", "")

    operatorStack = list()
    finalExpr = list()

    tokenList = re.findall(r"\d+|[+-/*()^]", expr) #cleaner than bottom, no need to capture
    precedence = {
        '+':1,
        '-':1,
        '*':2,
        '/':2,
        '^':3,
        '(':4,
        ')':4
    }
    # MAIN LOOP
    for token in tokenList:
        print (f"Current postfix expression: {finalExpr}")

        if (token.isdigit()): #check if number
            finalExpr.append(token) # straight on the stack

        elif (operatorStack==[]): # if operator stack is empty
            operatorStack.append(token) # push the operator onto the stack
        # if token is an operator with lower or equal precedence

        elif (token != "(" and precedence[token]<=precedence[operatorStack[-1]]):
            # pop the stack onto the final expression until you hit something of lower precedence
            while(operatorStack!=[] and precedence[token]<=precedence[operatorStack[-1]]):
                # loop will pop onto finalExpr until you hit a right paren, as that's only resolved when token is a right paren
                if (operatorStack[-1] == "("):
                    break # not sure if breaking is bad coding
                else:
                    finalExpr.append(operatorStack[-1])
                operatorStack.pop()
            # finally place your token onto a precedence-free stack
            operatorStack.append(token)

        elif (token != ")"): # can only be (
            print (f"Adding {token} to operator stack")
            operatorStack.append(token)

        else: # can only be )
            while (operatorStack!=[] and operatorStack[-1]!="("):
                if (operatorStack[-1]!='('):
                    # pop from operators, and push to final
                    finalExpr.append(operatorStack[-1])
                    operatorStack.pop()
                # this last one pops the hanging paren
                operatorStack.pop()
                break

    # take remaining operator stack and pop each to final
    while (operatorStack != []):
        finalExpr.append(operatorStack[-1])
        operatorStack.pop()
    print (finalExpr)

    #check if unmatched parentheses
    for char in finalExpr:
        if (char == "(" or char == ")"):
            raise ValueError("Unexpected item in bagging area - unmatched parentheses!")

    return finalExpr

# TODO evaluate postfix
"""Rules for evaluating postfix
- push numbers onto the stack as they come
- when encountering an operator, pop the last two numbers and evaluate them them
    - push the result back onto the stack
- repeat until only one number remains and you've run through the whole expression
"""

if __name__ == "__main__":
    # i think this setup means that this file will act as a library unless run directly
    main()