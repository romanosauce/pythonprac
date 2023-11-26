import sys


in_data = sys.stdin.buffer.read().decode('UTF8', errors='replace')
print(in_data.encode('latin1', 'replace').decode('CP1251', 'replace'))
