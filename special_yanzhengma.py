import random
import string

def generate_code(bit_num):
    '''
    :param bit_num: 生成验证码位数
    :return: 返回生成的验证码
    '''

    all_str = string.printable
    code = ''.join([random.choice(all_str) for i in range(bit_num)])
    return code

if __name__ == '__main__':
    code = generate_code(6)
    print(code)