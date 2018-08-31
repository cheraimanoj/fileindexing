import sys
import copy

#Adding space in [intending the line for +/-]
def getSpace(prev_dot,listofline,i,val, sp = 0):
    prev = prev_dot[0]
    space_dots = (prev_dot[1]*" ") + val
    listofline[prev]= listofline[prev].replace(prev_dot[1]*'.',space_dots,1)

    if sp:
        for j in range(prev + 1, i):
            listofline[j] = ((prev_dot[1]+1)*" ") + listofline[j]

listofline=[]
for line in sys.stdin:
    if(line != '\n'):
        listofline.append(line.strip())

prev_dot = ()
list_star = []
dot_star = []
#checking for * and . in first charater postion
for i,line in enumerate(listofline):
    if(line.startswith('*')):
        len_stars = (len(line) - len(line.lstrip('*')))
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

        each_line = '.'.join(str(x) for x in list_star)
        listofline[i] = listofline[i].replace(len_stars*'*',each_line,1)

    if (line.startswith('.')):
        dot_count = (len(line) - len(line.lstrip('.')))
        #Fetchin first dot in first star
        if(not prev_dot):
            dot_star=copy.copy(list_star)
            prev_dot =(i,dot_count)
        elif(dot_star==list_star):
            if(prev_dot[1] < dot_count):
                getSpace(prev_dot,listofline,i,'+', 1)
                prev_dot = (i, dot_count)
            else:
                getSpace(prev_dot, listofline, i,'-', 1)
                prev_dot = (i, dot_count)
        else:
            dot_star = copy.copy(list_star)
            getSpace(prev_dot, listofline, i,'-')
            prev_dot = (i, dot_count)
if(prev_dot):
	getSpace(prev_dot,listofline,i,'-')
print('\n'.join(listofline))