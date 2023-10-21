from math import *

def_func = {'quit': ({'s': None, 'def_num': None, 'line_num': None},
                     's.format(def_num,line_num)')}
def_func_num = 1
line_num = 0
quit_flag = False
out_line = ''
while True:
    line = input()
    line_num += 1
    if line[0] == ':':
        line = line[1:].split()
        def_func[line[0]] = ({par: None for par in line[1:-1]},
                             line[-1])
        def_func_num += 1
    else:
        split_line = line.split()
        param = def_func[split_line[0]][0]
        func = def_func[split_line[0]][1]
        if split_line[0] == 'quit':
            param['s'] = eval(line[line.find(' ')+1:])
            param['def_num'] = len(def_func)
            param['line_num'] = line_num
            quit_flag = True
        elif len(param) == 1:
            for key in param.keys():
                param[key] = eval(line[line.find(' ')+1:])
        else:
            i = 1
            for key in param.keys():
                param[key] = eval(split_line[i])
                i += 1
        print(eval(func, globals() | param))
        if quit_flag:
            break
