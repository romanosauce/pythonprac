class Maze:
    def __init__(self, N):
        self.size = N
        self.adj_list = {}

    def __str__(self):
        s = ["" for _ in range(self.size * 2 + 1)]
        s[0] = '\u2588' * (self.size * 2 + 1)
        for i in range(1, self.size * 2):
            line = '\u2588'
            y = (i - 1) // 2
            for j in range(1, self.size * 2):
                x = (j - 1) // 2
                if i % 2:
                    if j % 2 or (x, y) in self.adj_list and \
                            (x + 1, y) in self.adj_list[(x, y)]:
                        line += '\u00B7'
                    else:
                        line += '\u2588'
                else:
                    if j % 2 and (x, y) in self.adj_list and \
                            (x, y + 1) in self.adj_list[(x, y)]:
                        line += '\u00B7'
                    else:
                        line += '\u2588'
            line += '\u2588'
            s[i] = line
        s[self.size * 2] = '\u2588' * (self.size * 2 + 1)
        return '\n'.join(s)

    def __setitem__(self, *args):
        x0 = args[0][0]
        y0 = args[0][1].start
        x1 = args[0][1].stop
        y1 = args[0][2]
        value = args[-1]
        if x0 != x1 and y0 != y1:
            return
        if value == '\u2588':
            if x0 == x1:
                for i in range(min(y0, y1), max(y0, y1)):
                    if (x0, i) in self.adj_list:
                        self.adj_list[(x0, i)] ^= {(x0, i + 1)}
                    if (x0, i + 1) in self.adj_list:
                        self.adj_list[(x0, i + 1)] ^= {(x0, i)}
            else:
                for i in range(min(x0, x1), max(x0, x1)):
                    if (i, y0) in self.adj_list:
                        self.adj_list[(i, y0)] ^= {(i + 1, y0)}
                    if (i + 1, y0) in self.adj_list:
                        self.adj_list[(i + 1, y0)] ^= {(i, y0)}
        else:
            if x0 == x1:
                for i in range(min(y0, y1), max(y0, y1)):
                    if (x0, i) in self.adj_list:
                        self.adj_list[(x0, i)] |= {(x0, i + 1)}
                    else:
                        self.adj_list[(x0, i)] = {(x0, i + 1)}
                    if (x0, i + 1) in self.adj_list:
                        self.adj_list[(x0, i + 1)] |= {(x0, i)}
                    else:
                        self.adj_list[(x0, i + 1)] = {(x0, i)}
            else:
                for i in range(min(x0, x1), max(x0, x1)):
                    if (i, y0) in self.adj_list:
                        self.adj_list[(i, y0)] |= {(i + 1, y0)}
                    else:
                        self.adj_list[(i, y0)] = {(i + 1, y0)}
                    if (i + 1, y0) in self.adj_list:
                        self.adj_list[(i + 1, y0)] |= {(i, y0)}
                    else:
                        self.adj_list[(i + 1, y0)] = {(i, y0)}

    def __getitem__(self, *args):
        x0 = args[0][0]
        y0 = args[0][1].start
        x1 = args[0][1].stop
        y1 = args[0][2]

        fin = (x1, y1)
        st = (x0, y0)
        if st == fin:
            return True
        to_visit = {st}
        reach = {st}
        while to_visit:
            new_visit = set()
            for u in to_visit:
                if u in self.adj_list:
                    new_visit |= self.adj_list[u] - reach
                    reach |= self.adj_list[u]
                    if u == fin:
                        return True
            to_visit = new_visit
        return False

import sys
exec(sys.stdin.read())
