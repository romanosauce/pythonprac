import math
import sys


lines = sys.stdin.readlines()
commands_lines = []
label_map_defined = {}
label_set_used = set()
namespace = {}
i = 0
for line in lines:
    new_line = line.strip()
    match new_line.split(':'):
        case [label, arg, *other]:
            match label in label_map_defined and len(label) != 0:
                case 1:
                    sys.exit()
            label_map_defined[label] = i
            new_line = ':'.join([arg] + other)
    match new_line.split():
        case ['stop', *other]:
            match other:
                case []:
                    commands_lines += [new_line]
                    i += 1
        case ['store', *other]:
            match other:
                case [_, _]:
                    commands_lines += [new_line]
                    i += 1
        case ['add' | 'sub' | 'div' | 'mul', *other]:
            match other:
                case [_, _, _]:
                    commands_lines += [new_line]
                    i += 1
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle', *other]:
            match other:
                case [_, _, label]:
                    label_set_used |= {label}
                    commands_lines += [new_line]
                    i += 1
        case ['out', *other]:
            match other:
                case [_]:
                    commands_lines += [new_line]
                    i += 1

for label in label_set_used:
    match label not in label_map_defined:
        case 1:
            sys.exit()

i = 0
while True:
    command = commands_lines[i].split()
    match command:
        case ['stop', *other]:
            sys.exit()
        case ['store', *other]:
            try:
                val = float(other[0])
            except Exception:
                val = 0
            namespace[other[1]] = val
            i += 1
        case ['add' | 'sub' | 'div' | 'mul' as op, *other]:
            op1 = namespace.get(other[0], 0)
            op2 = namespace.get(other[1], 0)
            try:
                match op:
                    case 'add':
                        namespace[other[2]] = op1 + op2
                    case 'sub':
                        namespace[other[2]] = op1 - op2
                    case 'div':
                        namespace[other[2]] = op1 / op2
                    case 'mul':
                        namespace[other[2]] = op1 * op2
            except Exception:
                namespace[other[2]] = math.inf
            i += 1
        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as op, *other]:
            op1 = namespace.get(other[0], 0)
            op2 = namespace.get(other[1], 0)
            match op:
                case 'ifeq':
                    res = op1 == op2
                case 'ifne':
                    res = op1 != op2
                case 'ifgt':
                    res = op1 > op2
                case 'ifge':
                    res = op1 >= op2
                case 'iflt':
                    res = op1 < op2
                case 'ifle':
                    res = op1 <= op2
            match res == 1:
                case 1:
                    i = label_map_defined[other[2]]
                case 0:
                    i += 1
        case ['out', *other]:
            print(namespace.get(other[0], 0))
            i += 1
    match i >= len(commands_lines):
        case 1:
            break
