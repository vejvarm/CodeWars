"""Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine;
there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles!
The resulting two Sheldons go to the end of the queue.
Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:
 - Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

Write a program that will return the name of the person who will drink the n-th cola.
"""


def whoIsNext(names, r):
    # the amount of every person and the length of the list after running through it once is doubled
    # we are looking for a number len(names)*(2**0 + 2**1 + 2**2 + ... + 2**mul) + residue == r
    # that means we have a geometric sequence with a quotient of q = 2 and we are looking for the last sum of first n
    # elements which is less than or equal to r
    name_dict = dict(enumerate(names, 0))
    reverse_dict = {v: k for k, v in name_dict.items()}
    queue = [reverse_dict[name] for name in names]

    a = len(queue)  # initial length of the list
    q = 2  # quotient
    mul = 0  # initial multiplier
    seq_sum = 0  # the sum of the geometric sequence

    while seq_sum <= r:
        mul += 1
        seq_sum = a * (q ** mul - 1) // (q - 1)

    # correct the multiplier and subtract last element of the sequence so that seq_sum is smaller than r
    mul -= 1
    seq_sum -= a * q ** mul
    residue = r - seq_sum - 1

    # return the person which is going to be at the beginning
    return name_dict[residue // 2 ** mul]

def inverse_mapping(f):
    return f.__class__(map(reversed, f.items()))

if __name__ == '__main__':
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    r = 1
    res = whoIsNext(names, r)
    print(res)

