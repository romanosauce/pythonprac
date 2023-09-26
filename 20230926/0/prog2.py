num_list = [i for i in range(5, 16)]
char_list = list('abcdefghk')
num_list[4:8] = char_list[-5:]
print(num_list)
print(num_list[-1:len(num_list) // 2:-2])
