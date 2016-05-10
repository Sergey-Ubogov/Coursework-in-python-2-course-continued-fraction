from random import SystemRandom
import sys
from argparse import ArgumentParser

def rndondon(ceil):
    rnd = SystemRandom()
    return rnd.randint(1, ceil)
 
def calculate_fraction(arr):
    '''принимает массив с неполными частными, вычисляет цепную дробь,
    учитывая, что q0 = 0
    '''
    intermediate_results = [arr[-1]]
    len_arr = len(arr) - 1
    for i in range(1, len(arr)):
        intermediate_results.append(arr[len_arr-i]+1/intermediate_results[i-1])
    return 1/intermediate_results[-1]

def argument_parser():
    '''работа с аргументами'''
    arg_parse = ArgumentParser(description=('''
        Проверяет, как будут расположены значения цепных дробей на отрезке от 0 до 1,
        при заданном(или рандомном) количестве этажей каждой дроби и
        при заданном(или рандомном) количестве цепных дробей и
        при рандомных неполных частных для каждой дроби
        пример запуска: python -3 kur.py -r 100 -f 100 -c 10000
        '''))
    arg_parse.add_argument('--floor', '-f', type=int, help=('количество этажей'), default=rndondon(1000))
    arg_parse.add_argument('--podotrezki', '-p', type=int, help=('количество подотрезочков'), default=10)
    arg_parse.add_argument('--fraction', '-fr', type=int, help=('количество дробей'), default=rndondon(1000))
    arg_parse.add_argument('--ceil', '-c', type=int, help=('потолок для рандомных неполных частных'), default=rndondon(100000))
    return arg_parse.parse_args()

def main():
    args = argument_parser()
    values_fraction = []
    for i in range(args.fraction):
        values_fraction.append(#кладем значение в массив значений
            calculate_fraction(#вычисляем значение цепной дроби
                [rndondon(args.ceil) for i in range(args.floor)]#массив неполных частных для цепной дроби
                ))
    answer = ''
    answer += 'Количество дробей = '+str(args.fraction) + '\n'
    answer += 'Количество этажей в каждой дроби = '+ str(args.floor) + '\n'
    answer += 'Количество подотрезочков = '+ str(args.podotrezki) + '\n'
    answer += 'Потолок для рандомных неполных частных = '+ str(args.ceil) + '\n'

    answer += 'Чтобы хоть как нибудь представить,' + '\n'
    answer += 'как расположились значения на отрезке,' + '\n'
    answer += 'разобьем отрезок [0,1] на более мелкие ' + '\n'
    answer += 'и посчитаем сколько значений вошли в каждый' + '\n'
    answer += 'из подотрезочков:' + '\n'
    str_ = 2*('+'+41*'-')+'+'
    answer += str_ + '\n'
    answer += '| Подотрезочек'+28*' '+'| Количество значений, попавших в него    |' + '\n'
    length_podotr = 1/args.podotrezki
    znaki = len(str(length_podotr).split('.')[1])
    
    dict_values_fraction = {}
    for i in range(args.podotrezki):
        begin = round(i*length_podotr, znaki)
        end = round((i+1)*length_podotr, znaki)
        dict_values_fraction['['+str(begin)+','+str(end)+')'] = 0
    for i in range(args.podotrezki):
        for j in values_fraction:
            begin = round(i*length_podotr, znaki)
            end = round((i+1)*length_podotr, znaki)
            if begin <= j < end:
                dict_values_fraction['['+str(begin)+','+str(end)+')'] += 1

    for i in range(args.podotrezki):
        answer += str_ +'\n'
        begin = round(i*length_podotr, znaki)
        end = round((i+1)*length_podotr, znaki)
        otrezok = '['+str(begin)+','+str(end)+')'
        answer += '|'+otrezok+ (41-len(otrezok))*' '+'|'+\
            str(dict_values_fraction[otrezok])+' '*(41-len(str(dict_values_fraction[otrezok]))) +'|' +'\n'
    answer += str_ + '\n'
    print(answer)
    with open('out.txt', 'w') as f:
        f.write(answer)
 
if __name__ == '__main__':
    main()