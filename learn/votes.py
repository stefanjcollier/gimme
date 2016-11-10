import csv
import os

csvfile = '%s/.stools_config/gimme/votes.csv' % os.path.expanduser('~')

def increment_votes(path):
    records = csv.reader(open(csvfile))
    #if path exists in file, then increment
    lines = [line for line in records]
    for line in lines:
        if line[0] == path:
            line[1] = int(line[1]) + 1
            writer = csv.writer(open(csvfile,'w'))
            writer.writerows(lines)
            return
    #path not encountered, append 
    records = open(csvfile, 'a')
    records.write('%s,1,\n' % path)
    records.close()

def get_votes(path):
    records = csv.reader(open(csvfile))
    for line in records:
        if line[0] == path:
            return line[1]
    return 0
