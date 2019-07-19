'''
    CS5001
    Fall 2018
    HW4
    Brad Egan
'''

'''
Ran tests of remove letter function on words containing / not containing letter.
Ran tests of find letter function on words containing letter and not containing
letter.
Ran tests of play_or_not function on valid / invalid input
Ran tests of read_wordlist function
Ran tests of read_highscore function
Ran tests of read_scorelist function
Ran tests of write_highscore function
Ran tests of append_score function
Ran all_tests function to confirm all tests passed (all returned True)

'''

# Import all functions from spaceship file.
from spaceship import *

def helper(boolean):
    ''' function helper
        Input: boolean
        Return: "valid" or "invalid", a string
        Does: Returns valid for true, and invalid for false
    '''
    if boolean:
        return "valid"
    else:
        return "invalid"


def test_remove_letter(input_list, letter, output_list):
    ''' function test_remove_letter
        Input: input_list, a list
               letter, str, letter to be removed
               output_list, a list of expected outputs
        Return: Boolean - True / False
        Does: Tests removing letters from given input_list for given letter
              and check if output of function matches output_list. Returns
              boolean of whether or not all test passed. True if all passed.
              False otherwise.
    '''
    success_count = 0
    failure_count = 0

    for i in range(len(input_list)):
        output = remove_letter(letter, input_list[i])

        if output == output_list[i]:
            test_result = "SUCCESS"
            success_count += 1
        else:
            test_result = "FAILURE"
            failure_count += 1

        print("Testing removing", letter, "from", input_list[i] + "...",
        test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)
    if failure_count == 0:
        return True
    else:
        return False

def test_find_letter(input_list, letter, letter_location):
    ''' function test_find_letter
        Input: input_list, list of inputs
               letter, a str to be found
               letter_location, list of lists of letter indicies
        Return: Boolean
        Does: Tests find letter function on input_list for given letter
              and checks if output of function matches letter_location.
              Returns true if all tests pass, false otherwise.
    '''
    success_count = 0
    failure_count = 0

    for i in range(len(input_list)):
        output = find_letter_location(letter, input_list[i])

        if output == letter_location[i]:
            test_result = "SUCCESS"
            success_count += 1
        else:
            test_result = "FAILURE"
            failure_count += 1

        print("Testing",letter, "location in", input_list[i] + "...",
        test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)
    if failure_count == 0:
        return True
    else:
        return False

def test_play_or_not(again, play_again_output):
    ''' function test_play_or_not
        Input: again, list of strings
               play_again_output, boolean
        Return: Boolean
        Does: Tests play_or_not function on list of inputs
              Returns true if output matches expected output.

    '''
    success_count = 0
    failure_count = 0

    for i in range(len(again)):
        valid = helper(play_again_output)
        output = play_or_not(again[i])
        if output == play_again_output:
            test_result = "SUCCESS"
            success_count += 1
        else:
            test_result = "FAILURE"
            failure_count += 1

        print("Testing", again[i], "is", valid + "...", test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)
    if failure_count == 0:
        return True
    else:
        return False

def test_read_wordlist(filename, wordlist_output):
    ''' function test_read_wordlist
        Input: filename, a str
               wordlist_output, a list
        Return: Boolean
        Does: Checks if output of read_wordlist matches wordlist_output.
              Returns true if it does
    '''
    success_count = 0
    failure_count = 0

    output = read_wordlist(filename)

    if output == wordlist_output:
        test_result = "SUCCESS"
        success_count += 1
    else:
        test_result = "FAILURE"
        failure_count += 1

    print("Testing", filename, "reading to wordlist_output"+  "...",
    test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)
    if failure_count == 0:
        return True
    else:
        return False


def test_read_highscore(filename, highscore_output_score):
    ''' function test_read_highscore
        Input: filename, a str
               highscore_output_score, an int
        Return: Boolean
        Does: Checks if highscore of filename matches highscore_output_score
              Returns true if it does, false otherwise.
    '''
    success_count = 0
    failure_count = 0

    output = read_highscore(filename)

    if output == highscore_output_score:
        test_result = "SUCCESS"

        success_count += 1
    else:
        test_result = "FAILURE"
        failure_count += 1

    print("Testing", filename, "reading to highscore_output"+  "...",
    test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)

    if failure_count == 0:
        return True
    else:
        return False

def test_read_scorelist(filename, scorelist_output):
    ''' function test_read_scorelist
        Input: filename, a str
               scorelist_output, a list
        Return: Boolean
        Does: Checks if read_scorelist function output matches predetermined
              list of scorelist_output. Returns true is failure count is zero.
    '''
    success_count = 0
    failure_count = 0

    output = read_scorelist(filename)

    if output == scorelist_output:
        test_result = "SUCCESS"
        success_count += 1
    else:
        test_result = "FAILURE"
        failure_count += 1

    print("Testing", filename, "reading to scorelist_output"+  "...",
    test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)
    if failure_count == 0:
        return True
    else:
        return False

def test_write_highscore(name, high_score, write_filename,
                         expected_output_filename):
    ''' function test_write_highscore
        Input: name, str
               high_score, int
               write_filename, str
               expected_output_filename, str
        Return: Boolean
        Does: Writes file and tests if written file matches dummy file
              (expected_output_filename) Returns true if it does, false
              otherwise.
    '''
    success_count = 0
    failure_count = 0

    write_highscore(name, high_score, write_filename)

    if (read_scorelist(write_filename) ==
    read_scorelist(expected_output_filename)):
        test_result = "SUCCESS"
        success_count += 1
    else:
        test_result = "FAILURE"
        failure_count += 1

    print("Testing", "writing",write_filename, "against",
    expected_output_filename+
          "...", test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)
    if failure_count == 0:
        return True
    else:
        return False

def test_append_score(name, score, write_filename, expected_output_filename):
    ''' function test_append_score
        Input: name, str
               score, int
               write_filename, str
               expected_output_filename, str
        Return: Boolean
        Does: Tests append_score function. Checks if function writing to first
              file matches dummy file (expected_output_filename) Returns true
              if it does, false otherwise.
    '''
    success_count = 0
    failure_count = 0


    append_score(name, score, write_filename)

    if (read_scorelist(write_filename) ==
    read_scorelist(expected_output_filename)):
        test_result = "SUCCESS"
        success_count += 1
    else:
        test_result = "FAILURE"
        failure_count += 1


    print("Testing", "writing",write_filename, "against",
          expected_output_filename+  "...", test_result + "!")

    # Prints total passes and failures.
    print("Passed ", success_count, "tests and failed ", failure_count)

    if failure_count == 0:
        return True
    else:
        return False

def test_all_tests(lst):
    ''' function test_all_tests
        Input: lst, a list
        Return: boolean
        Does: Checks if all elements in list are true, and returns
        true if so. Returns false otherwise.
    '''
    
    for item in lst:
        if item == False:
            print ("FAILURE")
            return False
    print ("PASSED ALL TESTS")
    return True


def main():
    ''' function main
        Input: none
        Return: none
        Does: Main function to start test functions.

    '''

    #INPUTS
    input_list = ["Hello", "Jello", "lllll", "lola", "l", "", "word"]
    play_again_list = ["Y"]
    play_again_list_false = ["N", "n", "no", "no thank you", "etc", "y"]
    write_highscore = ['Bob 10\n', 'Darb 2\n', 'brad1 0\n']


    #EXPECTED OUTPUTS
    output_list = ["Heo", "Jeo", "", "oa", "", "", "word"]
    letter_location = [[-3, -2], [-3, -2], [-5, -4, -3, -2, -1], [-4, -2],
                       [-1], [], []]
    wordlist_output = ['sap\n', 'sat\n', 'sad\n', 'rat\n', 'rap\n', 'ram\n',
                       'rag\n', 'nap\n', 'Nat\n', 'mat\n']
    scorelist_output = ['bradddd 9\n', 'brad 0\n', 'brad1 0\n']


    test1 = test_remove_letter(input_list, "l" , output_list)
    test2 = test_find_letter(input_list, "l", letter_location)
    test3 = test_play_or_not(play_again_list, True)
    test4 = test_play_or_not(play_again_list_false, False)
    test5 = test_read_wordlist("wordlist_test.txt", wordlist_output)
    test6 = test_read_highscore("scores_test.txt", 9)
    test7 = test_read_scorelist("scores_test.txt", scorelist_output)
    test8 = test_write_highscore("Laney", 20, "scores_test_mod.txt",
                                 "scores_expected_output.txt")
    test9 = test_append_score("Yankees", 0, "scores_test_mod2.txt",
                              "append_score_expected.txt")

    # Every test returns a boolean, all_tests is a list of these booleans.
    all_tests = [test1, test2, test3, test4, test5, test6, test7, test8, test9]
    test_all_tests(all_tests)

main()
