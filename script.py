import sys
import copy

#Adding space in [intending the line for +/-]
def getSpace(prev_dot,listofline,dot_count,i,val, sp = 0):
    prev = prev_dot[0]
    space_dots = listofline[prev].split()
    space_dots[0] = ''.join([' '] * prev_dot[1]) + val
    listofline[prev] = ' '.join(space_dots)

    if sp:
        for j in range(prev + 1, i):
            listofline[j] = ''.join([' '] * prev_dot[1]) + '  ' + listofline[j]

#with open(sys.argv[1],'r') as filedata: 
#    listofline = filedata.readlines()
listofline=[]
for line in sys.stdin:
    if(line != '\n'):
        listofline.append(line.strip())

list_star = []
list_dot=[]
dot_star = []
#checking for * and . in first charater postion
for i,line in enumerate(listofline):
    if(line.startswith('*')):
        len_stars = len(line.split()[0])
        #Fetchin first star
        if(not list_star):
            list_star.append(1)
        else:
            if(len_stars > len(list_star)):
                list_star.append(1)
            elif(len(list_star) == len_stars):
                list_star[-1]+=1
            else:
                list_star=list_star[:len_stars-len(list_star)]
                list_star[-1]+=1

        each_line = line.split()
        each_line[0] ='.'.join(str(x) for x in list_star)
        listofline[i] = ' '.join(each_line)
        
    if (line.startswith('.')):
        dot_count=len(line.split()[0])
        #Fetchin first dot in first star
        if(not dot_star):
            dot_star=copy.copy(list_star)
            prev_dot =(i,dot_count)
        elif(dot_star==list_star):
            if(prev_dot[1] < dot_count):
                getSpace(prev_dot,listofline,dot_count,i,'+', 1)
                prev_dot = (i, dot_count)
            else:
                getSpace(prev_dot, listofline, dot_count, i,'-', 1)
                prev_dot = (i, dot_count)
        else:
            dot_star = copy.copy(list_star)
            getSpace(prev_dot, listofline, dot_count, i,'-')
            prev_dot = (i, dot_count)

getSpace(prev_dot,listofline,dot_count,i,'-')
print('\n'.join(listofline))