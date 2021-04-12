import csv
import sys

def grader(func_name, test_cases):
    with open(test_cases, newline='') as infile:
        tests = csv.reader(infile)
    
    for test in tests:
        input = test[0]
        output = test[1]

        if (func_name(input) == output):
            print("Test passed")
        else:
            print("Test failed")

if __name__ == "__main__":
    main()

def main():
    if len(sys.argv) != 2:
        print("Grader requires function name and testcase file")
        sys.exit(1)
    
    grader(argv[0]), argv[1])
    
