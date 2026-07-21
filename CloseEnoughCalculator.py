## TODO input handling
    # length
    # units

# TODO def list of functions to convert unit to unit (each precision should have its own function definitely)

# TODO def convert fraction to decimal

# TODO def round to the nearest precision (each precision should have its own function probably)

# TODO error handling (if number inputted has anything besides numerals, ., and /.)
    # accepted formats x, x.x, x/x, x.x/x.x, x.x/x.x

# TODO parse mixed fractions AND parentheses into floats
    # some sort of recursion is required
    # if (, then the entire term until the next ) ......that doesnt work for ((4/3)/4)
    # parse expression
    # if (, then grab expression. parse smallerExpr should run and eliminate all open brackets that come before a close bracket
    # parse smallerExpr should parse expression.
    # parse expression has if (, so else case 

# TODO earlier than the parser, just dont accept mixed fractions or parenths


# TRY converting to postfix, solving via postfix
