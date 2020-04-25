'''
26. Write a Python program to create a histogram from a given list of integers.
'''

def Histogram(h):
    x = 0
    y = 0
    starstr = "";
    for x in h:
        for m in range(h[y]):
            starstr = starstr + "*"  # add a star incrementally until it reaches the number in the list
        print(str(h[y]) + " " + starstr)  # print out the bar graph for that number
        starstr = ""; # clear the star string variable
        y = y + 1

histo = [1, 3, 5, 7, 9, 5, 3, 1]
Histogram(histo)

