"""
HackerRank
TASK
----
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. 
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for  is not found, print Not found instead.

Input Format
--------------
The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. 
The first value is a friend's name, and the second value is an -digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.
"""

if __name__ == '__main__':
    n = int(input('How many Entries? '))
        
    e = [input('Enter Name (firstname in lowercase) and Number: ').split(' ') for _ in range(n)]
    
    q = []
    while True:
        key = input('Find Whom (firstname in lowercase): ').split()
        if len(key) == 0:
            break
        else:
            q.append(key)
            continue

            
entries = dict(e)
for query in q:
    for name in query:
        if name in entries:
            print(f"\n{name}={entries[name]}")
        else:
            print('\n',name,': Not found')
            continue
