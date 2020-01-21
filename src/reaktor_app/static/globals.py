import os

#Dict to hold the package data
data = {}

#This is where mock data file lives (could also be taken from /var/lib/dpkg/status)
file = open('static/status.real', 'r')

#Parse the package file
dump = file.read().split('\n\n')
for item in dump:
    for line in item.replace('\n ', '¨').split('\n'):
        try:
            #Get key and value pairs from the file
            line_splitted = line.split(':', 1)
            key, val = line_splitted[0], line_splitted[1].strip()
            #Store only the interesting ones
            if key == 'Package':
                current_pkg = val
                data[current_pkg] = {'Name':val, 'Description':'', 'Depends': [], 'Reverse': []}

            #Get Description
            elif key == 'Description':
                data[current_pkg][key] = val.replace('¨', '\n ')

            #Get Dependencies
            elif key == 'Depends':
                for i in val.split(' '):
                    #Parse version numbers
                    if '(' not in i and ')' not in i and '|' not in i and not i.replace(',','').isnumeric():
                        new_entry = [i.replace(',',''), 0]
                        #Filter dublicate packages
                        if new_entry not in data[current_pkg]['Depends']:
                            data[current_pkg][key].append(new_entry)

        except IndexError:
            #Unneccessery lines from the file are skipped
            pass

#Form the dependencies links between packages
for pkg in data:
    for dep in data[pkg]['Depends']:
        if dep[0] in data:
            dep[1] = 1
        #Fill reverse dependencies
            data[dep[0]]['Reverse'].append([pkg, 1])
        else:
            try:
                data[dep[0]]['Reverse'].append([pkg, 0])
            except KeyError:
                pass

file.close()
