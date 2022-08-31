"""
HackerRank
------------
Repeated String

Find and print the number of letter a's in the 
first n letters of an infinitely large periodic string
"""
def string_repeat(word, letter):

    # count letter in word given
    count = 0
    for i in word:
        if i == letter:
            count += 1
        else:
            continue
    
    print(f"Letter repeats : {count} times\n")


if __name__ == '__main__':
    
    # assign variables
    word = input("Enter a word of any length :\n")
    letter = input("Enter the letter to count for:\n")

    string_repeat(word, letter)