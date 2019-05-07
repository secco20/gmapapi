# -*- coding: utf-8
import gmapapi
import sys, argparse
import csv

def get_args():
    parser = argparse.ArgumentParser()
    enc = 'shift_jis'
    # enc = 'utf-8'
    parser.add_argument('inputfile', type=argparse.FileType('r', encoding=enc)) 
    parser.add_argument('outputfile', type=argparse.FileType('w', encoding=enc)) 
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()

    # with open(args.inputfile, 'r', encoding='shift_jis') as f:
    f = args.inputfile
    reader = csv.reader(f)
    header = next(reader)
    # fw = open(args.outputfile, 'w', encoding='shift_jis')
    fw = args.outputfile
    writer = csv.writer(fw)
    writer.writerow(header + ['KIYKSH_ADD_IDO', 'KIYKSH_ADD_KEIDO', 'KIYKJI_ADD_KNJ'])

    for row in reader:
        try:
            geo = gmapapi.geocode(row[1])
            lat = geo['results'][0]['geometry']['location']['lat']
            lng = geo['results'][0]['geometry']['location']['lng']
        except Exception as e:
            lat = e
            lng = e

        try:
            rev = gmapapi.reverse_geocode('%s,%s'%(row[2], row[3]))
            addr = rev['results'][0]['formatted_address']
        except Exception as e:
            addr = e
        ret = row + [lat, lng, addr]
        writer.writerow(ret)
        
            # rev = gmapapi.reverse_geocode()

