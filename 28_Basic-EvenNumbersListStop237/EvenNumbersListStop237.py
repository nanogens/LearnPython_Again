'''
28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the
printing of any numbers that come after 237 in the sequence. Go to the editor
Sample numbers list :

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
'''

#MT Solution.  Note : break; breaks out of the for loop once 237 is encountered
def EvenStop237(list):
    for element in list:
        if(element % 2 == 0):
            print(element)
        elif (element == 237):
            break;

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
EvenStop237(numbers)