import csv

def grader(func_name, test_cases):
    with open(test_cases, newline='') as infile:
        tests = csv.reader(infile)
    
    for test in tests:
        input = test[0]
        output = test[1]

        if (func_name(input) == output):
            print("Test passed")
        else
            print("Test failed")