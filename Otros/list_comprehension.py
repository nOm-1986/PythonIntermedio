"""Some examples of list Comprehension.
"""
import sys


def run():
    one = [ x**2 for x in [1,2,3] ]
    #[1,4,9]

    two = [ x/2 for x in [4,5,6,7,2,7,3,8,2] if x > 5 ]
    #[3.0, 3.5, 3.5, 4.0]

    three = [ f'{x}_{x}' for x in 'Tu nombre aquí']
    #['T_T', 'u_u', ' _ ', 'n_n', 'o_o', 'm_m', 'b_b', 'r_r', 'e_e', ' _ ', 'a_a', 'q_q', 'u_u', 'í_í']

    four = [ f'{x}_{x}' for x in 'Quitamos los espacios' if x!= ' ']
    #['Q_Q', 'u_u', 'i_i', 't_t', 'a_a', 'm_m', 'o_o', 's_s', 'l_l', 'o_o', 's_s', 'e_e', 's_s', 'p_p', 'a_a', 'c_c', 'i_i', 'o_o', 's_s']

    text = 'The powerful of python'
    five = [ord(x) for x in text]
    #[84, 104, 101, 32, 112, 111, 119, 101, 114, 102, 117, 108, 32, 111, 102, 32, 112, 121, 116, 104, 111, 110]

    sixe = [(x + 5 if x > 4 else x -10) for x in range(1,11)]
    #[-9, -8, -7, -6, 10, 11, 12, 13, 14, 15]

    seven = ["Python3"[i::-1] for i in range(7)]
    #['P', 'yP', 'tyP', 'htyP', 'ohtyP', 'nohtyP', '3nohtyP']
    ma = [1,2,3,4,5]
    mb = [6,7,8,9,0]
    eight = [x*y for x in ma for y in mb]
    #[6, 7, 8, 9, 0, 12, 14, 16, 18, 0, 18, 21, 24, 27, 0, 24, 28, 32, 36, 0, 30, 35, 40, 45, 0]
    
    nine = [[x for x in range(y+2)] for y in range(4)]
    #[[0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
    

def run2():
    """La principal ventaja que ofrecen las expresiones son su bajo uso de memoria.
       Recuerda que estas no guardan los valores en memoria, sino la manera de generarlos.
       Esto ahorra mucho espacio en memoria.
       A continuación realizo la comparación utilizando sys.
    """
    a = list(range(1,1001))
    b = (x for x in range(1, 1001))
    c = [x for x in range(1, 1001)]
    print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c))


if __name__ == '__main__':
    run()
    #run2()
