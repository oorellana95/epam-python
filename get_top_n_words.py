#!/bin/python3

"""
1. Create a function that receives a list of strings WORDS and an integer N. The function should return the N-most frequent words in the list in descending order.
   If the number of different words in the list is less or equal to argument N, then it does not alter the result.

Examples:
words = ['one', 'two', 'three', 'two', 'three', 'three'], n=2,
The function should return ['three', 'two'], because 'three' is used 3 times, 'two' 2 times and 'one' just 1 time. The two most used words are 'three' and 'two'

words = ['one', 'two', 'three', 'two', 'three', 'three'], n=10,
The function should return ['three', 'two', 'one'], because 'three' is used 3 times, 'two' 2 times and 'one' just 1 time. The size n does not modify the size of the output.

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'], n=5
The function should return ['one', 'two', 'three', 'four', 'five'], as each word appears only once in the input list, and the output size is smaller than the number of different words.

words = ['one', 'one', 'one', 'one', 'one', 'one'], n=5
The function should return ['one'], as the input list only contains one word. The size n does not modify the size of the output.

* You can assume that the import statements are not needed
* Do not use collections.Counter

sorted_iterable = sorted(iterable, key=callable, reverse=boolean)
"""

"""
def get_top_n_words(words, N=10):
    dic = {}
    for word in words:
        if dic.get(word) is None:
            dic[word] = 1
        else:
            dic[word] += 1

    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    output = []

    n = 0
    for d in sorted_dic:
        output.append(d[0])
        n += 1
        if n == N:
            break

    print(output)"""


def get_top_n_words(words, N=10):
    dic = {}
    for word in words:
        if dic.get(word) is None:
            dic[word] = 1
        else:
            dic[word] += 1

    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    output = [x[0] for x in sorted_dic][0:N]
    print(output)


if __name__ == '__main__':
    get_top_n_words(['one', 'two', 'three', 'two', 'three', 'three'], N=2)
