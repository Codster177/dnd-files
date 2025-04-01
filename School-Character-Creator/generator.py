import tkinter as tk
import random as rd

# Creates fileList to store the files in.
fileList = []

# reset_file functions reset the file reader back to the start.
def reset_file(file):
    file.seek(0)

def reset_files():
    for x in fileList:
        reset_file(x)

# Reads in the files and adds them to the file list.
maleFirstNames = open("male-first-names.txt")
femaleFirstNames = open("female-first-names.txt")
middleNames = open("middle-names.txt")
lastNames = open("last-names.txt")
cliquesFile = open("cliques.txt")

fileList.append(maleFirstNames)
fileList.append(femaleFirstNames)
fileList.append(middleNames)
fileList.append(lastNames)
fileList.append(cliquesFile)

# Reads the count of the lines in the files then resets them.
maleFirstNamesCount = sum(1 for _ in maleFirstNames)
femaleFirstNamesCount = sum(1 for _ in femaleFirstNames)
middleNamesCount = sum(1 for _ in middleNames)
lastNamesCount = sum(1 for _ in lastNames)
cliquesFileCount = sum(1 for _ in cliquesFile)

reset_files()

# get_line() returns a line at a given number in a given file.
def get_line(file, lineNum):
    currentLine = 1
    for x in file:
        if (currentLine == lineNum):
            reset_file(file)
            return x
        else:
            currentLine = currentLine + 1

# get_random_line() uses get_line to find a random line in a given file.
def get_random_line(file, fileLineCount):
    randLineNum = rd.randint(1, fileLineCount)
    randLine = get_line(file, randLineNum)
    return randLine


# get_name() gets a full name (first, middle, last) depending on the genNum. If genNum = 0,
# it will select a random gender. If genNum = 1, it will select a male name, if genNum = 2,
# it will select a female name. Returns the names in a list.
def gen_name(genNum = 0):
    nameReturn = []
    if (genNum == 0):
        genNum = rd.randint(1, 2)
    if (genNum == 1):
        nameReturn.append(get_random_line(maleFirstNames, maleFirstNamesCount))
    else:
        nameReturn.append(get_random_line(femaleFirstNames, femaleFirstNamesCount))
    nameReturn.append(get_random_line(middleNames, middleNamesCount))
    nameReturn.append(get_random_line(lastNames, lastNamesCount))
    return nameReturn

# print_listName() takes a name list and joins them together into a printable format.
def print_listName(listName):
    return (" ".join((listName[0] + listName[1] + listName[2]).splitlines())) 


class Student:
    def generate_Clique(self, cliqueCount=3):
        self.cliqueList = []
        for x in range(cliqueCount):
            self.cliqueList.append(get_random_line(cliquesFile, cliquesFileCount))

    def __init__(self, genNum = 0):
        if (genNum == 0):
            genNum = rd.randint(1, 2)
        self.fullname = gen_name(genNum)
        self.gender = genNum
        self.generate_Clique()

    def return_fullname(self):
        return (" ".join((self.fullname[0] + self.fullname[1] + self.fullname[2]).splitlines()))
    
    def return_name(self):
        return (" ".join((self.fullname[0] + self.fullname[2]).splitlines()))
    
    def return_gender(self):
        if (self.genNum == 1):
            return "Male"
        else:
            return "Female"
    
    def return_cliques(self):
        cliqueReturn = ""
        for x in self.cliqueList:
            cliqueReturn += x
        return ", ".join((cliqueReturn.splitlines()))

        

# gui() creates the tkinter window.
def gui(studentMem):
    window = tk.Tk()
    window.title("School Character Generator")
    window.geometry("600x400")

    var2 = tk.StringVar()
    lb = tk.Listbox(window)
    lb.pack()
    

    def listBox_GenName():
        studentMem.append(Student())
        lb.insert('end', studentMem[len(studentMem) - 1].return_name())

    var1 = tk.StringVar()
    l = tk.Label(window, bg='white', fg='black',font=('Arial', 12), width=60, textvariable=var1)
    l.pack()

    def on_select(event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            selectedStudent = studentMem[int(selection[0])]
            selected_value = selectedStudent.return_cliques()
            var1.set(selected_value)

    def clear_list():
        lb.delete(0,'end')
        var1.set("")
        studentMem.clear()

    lb.bind('<<ListboxSelect>>', on_select)

    b1 = tk.Button(window, text='Generate Name', width=15, height=2, command=listBox_GenName)
    b1.pack()

    b2 = tk.Button(window, text='Clear List', width=15, height=2, command=clear_list)
    b2.pack()
    
    
    window.mainloop()

students = []
gui(students)