
import argparse
from operations import *
from solve_digits import *
import argparse

def main(numbers,target,helpful):
    ops =  [add,subtract,multiply,divide]
    possible_solutions = create_it_list(numbers,ops)
    found,solution = find_solutions(possible_solutions,target)
    newlist = [x.__name__  if callable(x) else x for x in solution]
    if (found and helpful):
        print("This is the digits solution. Perform the operations specified one after the other from left to right.\n\
    for example if you have the output [5, 'multiply', 7, 'add', 9, 'subtract', 20, 'multiply', 19] then you would multiply\n\
    5 and 7 then you would add 9 to that result then subtract 20 and then multiply 19 to get to your target of 456")
        print(newlist)
    elif( found ):
        print(newlist)
    else :
        print (" A solution could not be found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numbers", nargs="+", type=int, help="Your list of digit numbers your would like to solve")
    parser.add_argument("-t", "--target",type=int, help="A single target number to solve your list of digit numbers")
    parser.add_argument("-q", "--helpful", action="store_true", help="Gives an instruction on how to use the output along with the output")
    args = parser.parse_args()
    main(args.numbers,args.target,args.helpful)
