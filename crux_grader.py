import pandas as pd

def grader(func_name, test_cases):
    tests = pd.read_csv(test_cases, converters={'inputs':eval, 'outputs':eval})
    
    num_tests = len(tests)
    
    curr_test = 1
    num_correct = 0

    print(f"================================================================================================")
    for _, row in tests.iterrows():
        input = row['inputs']
        expected_output = row['outputs']

        print(f"Testcase #{curr_test}")
        print(f"    Input:           {input}")
        print(f"    Expected output: {expected_output}")

        output = func_name(input)
        print(f"    Your output:     {output}")

        if output == expected_output:
            num_correct += 1

        curr_test += 1
        print(f"================================================================================================")
    
    print(f"Total score: {num_correct}/{num_tests}")

