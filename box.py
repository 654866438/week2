#这题的idea非常简单，直接用split函数构造list，然后取整就行了

def sml_in_big():
    s_width, s_height, s_depth = input(
        'Width, Height and Depth of small box: ').split('x')
    b_width, b_height, b_depth = input(
        'Width, Height and Depth of big box: ').split('x')

    x = (int(b_width) * int(b_height) * int(b_depth)) / \
        (int(s_width) * int(s_height) * int(s_depth))
#不过话说回来，要是他们的长，宽，高float部分都小于0.5，但是乘起来之后大于0.5怎么办？
#example：1.4*1.4*1.4=2.744=2，1*1*1=1 怎么解决？
    print('Number of {}x{}x{} that will fit in {}x{}x{} box is: {}'.format(
        s_width, s_height, s_depth, b_width, b_height, b_depth, int(x)
    ))


if __name__ == '__main__':
    sml_in_big()

