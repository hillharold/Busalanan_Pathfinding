from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Busalanan_Dijkstra's algorithm")

# variables
grid = []
matrix = []
c = 0
count = 0
start, end = None, None
btn = None
rst = None
find = False
d = []
p = []
visited = []
u = -1
s = 0
e = 0
array_path = []
widd = int(input("input width: "))
hei = int(input("input length: "))
# initially path array contains -1
for x in range(hei * widd):
    d.append(500)
    p.append(-1)
    visited.append(0)


# dijkastra algorithm
def dijk():
    global u, s, e
    s = start.grid_info()["row"] * widd+ start.grid_info()["column"]
    e = end.grid_info()["row"] * widd + end.grid_info()["column"]
    d[s] = 0
    for i in range(hei*widd):
        mini = 500
        for j in range(hei*widd):
            if (d[j] < mini) and (visited[j] == 0):
                mini = d[j]
                u = j

        visited[u] = 1
        for v in range(hei*widd):
            if ((d[u] + matrix[u][v]) < d[v]) and (u != v) and (visited[v] == 0):
                d[v] = d[u] + matrix[u][v]
                p[v] = u


# finding path according to dijkstra's algorithm
def path(v, source):
    global array_path
    if p[v] != -1:
        path(p[v], source)
    if v != source:
        array_path.append(v)


# To store the path in the array so that we can backtrack
def display(source, n):
    for i in range(n):
        if d[i] < 500:
            if i != source:
                path(i, source)
            if i != source:
                if array_path[-1] != e:
                    array_path.clear()
                else:
                    return

def counter(n):
    global c
    if n - widd < 0:
        return c, n
    else:
        c += 1
        return counter(n - widd)

def make_matrix():
    global c
    for i in range(hei*widd):
        matrix.append([])
        for j in range(hei*widd):
            c = 0
            i_r, i_c = counter(i)
            c = 0
            j_r, j_c = counter(j)
            if i == j:
                matrix[i].append(0)
            elif i_r == j_r:
                if (i_c == j_c - 1) or (i_c == j_c + 1):
                    if grid[i_r][i_c]["bg"] == "black" or grid[j_r][j_c]["bg"] == "black":
                        matrix[i].append(500)
                    else:
                        matrix[i].append(1)
                else:
                    matrix[i].append(500)
            elif i_c == j_c:
                if (i_r == j_r - 1) or (i_r == j_r + 1):
                    if grid[i_r][i_c]["bg"] == "black" or grid[j_r][j_c]["bg"] == "black":
                        matrix[i].append(500)
                    else:
                        matrix[i].append(1)
                else:
                    matrix[i].append(500)
            else:
                matrix[i].append(500)

def make_grid():
    for i in range(hei):
        grid.append([])
        for j in range(widd):
            b = Button(root, bg="blue", width=2, bd=1)
            b.grid(row=i, column=j)
            grid[i].append(b)

def restart():
    global start, end, grid, count, c, matrix, btn, rst, find, d, p, visited, u, s, e, array_path
    start = None
    end = None
    grid.clear()
    count = 0
    c = 0
    matrix.clear()
    find = False
    d.clear()
    p.clear()
    visited.clear()
    u = -1
    s = 0
    e = 0
    array_path.clear()
    for k in range(hei*widd):
        d.append(500)
        p.append(-1)
        visited.append(0)
    # creating grid again
    make_grid()

def backtrack():
    if len(array_path) == 0:
        print("No Path Found")
    global c, find
    for ele in array_path[:-1]:
        c = 0
        r, col = counter(ele)
        grid[r][col]["bg"] = "light blue"
    find = True

def start_func():
    if count == 0 or count == 1:
        pass
    elif not find:
        make_matrix()
        dijk()
        display(s, hei*widd)
        backtrack()

def start_fun():
    global btn, rst, start
    btn = Button(root, text="START", command=start_func, borderwidth = 1)
    btn.grid(row=2, column=22, columnspan=2)
    #btn.place(x= 90, y= 250)
    rst = Button(root, text="RESTART", command=restart, borderwidth = 1)
    rst.grid(row=3, column=22, columnspan=3)
    #rst.place(x= 85, y= 290)

def click(event):
    global count, start, end
    if count == 0 and event.widget != btn and event.widget != rst:
        start = event.widget
        start["bg"] = "red"
        count += 1
    elif count == 1 and event.widget != btn and event.widget != start and event.widget != rst:
        end = event.widget
        end["bg"] = "green"
        count += 1
    else:
        if event.widget != start and event.widget != end and event.widget != btn and event.widget != rst and not find:
            event.widget["bg"] = "black"
            count += 1


"""def clear():
    len.delete(1.0, END)
    wid.delete(1.0, END)"""

"""def get_text():
    my_len = len.get(1.0,END)
    my_len1 = int(my_len)
    my_wid = wid.get(1.0, END)
    my_wid1 = int(my_wid)
    return (my_len1,my_wid1)

def get_len():
    my_len = len.get(1.0, END)
    #my_len1 = int(my_len)
    return my_len
def get_wid():
    my_wid= len.get(1.0, END)
    #my_wid1 = int(my_wid)
    return my_wid"""

make_grid()
start_fun()
root.bind("<Button-1>", click)
root.mainloop()