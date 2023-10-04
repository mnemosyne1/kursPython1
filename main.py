import random


def pi(how_many):
    """
    Evaluates pi using Monte-Carlo method
    :param how_many: how many points shall we draw
    :return: approximation of pi
    """
    inside = 0
    for x in range(how_many):
        x = random.random()  # x in [0, 1)
        y = random.random()  # y in [0, 1)
        r = x * x + y * y  # distance from point (0, 0)
        if r <= 1:  # is the point in a circle of radius 1 with a center at (0, 0)
            inside += 1
    return 4 * inside / how_many  # we considered a quarter of a circle, so its surface is pi/4


if __name__ == '__main__':
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    print(pi(100000))
    print(pi(1000000))
    print(pi(5000000))
