import os
from pylab import imread
import csv

bmd_filename= "BMDannotations-print.tsv"
ec_filename = "ECannotations-yuzi.tsv"
ck_filename = "CKannotations-sheet1.tsv"
feix_filename = "Grasp annotations - Feix.tsv"
misc_filename = "errorcontactannotations.tsv"

def load_data(filename,start,end):
  num_annots = 0
  starts = []
  ends = []
  annots = []
  status = []
  with open(filename) as tsv:
    lines = csv.reader(tsv, delimiter="\t")
    lines.next()   # skip header row
    for line in lines:
      if(float(line[0]) >= start and float(line[1]) <= end):
          starts.append(float(line[0]))
          ends.append(float(line[1]))
          annots.append(line[2])
          status.append(line[3])
          num_annots += 1
  #print list(set(annots))
  return [num_annots, starts, ends, annots, status]

def mult255(n):
    return n*255
def get_colors(ncolors):
    # define the colormap
    cmap = plot.cm.jet
    # extract all colors from the .jet map
    step = cmap.N / ncolors
    cmaplist = ['#%02x%02x%02x' % tuple(map(mult255,cmap(i)[0:3])) for i in range(0,cmap.N,step)]
    return cmaplist


def take_screenshot(time):
    screenshot_filename = 'screenshots/screenshot'+str(time)+'.png'
    hours = int(time/3600.0)
    mins = int(time/60.0)
    secs = int((int(time))%60)
    msecs = time-(int(time))
    #command='ffmpeg -ss '+str(hours)+':'+str(mins)+':'+str(secs+msecs)+' -i /Users/troniak/Desktop/nsh_shop_120.mp4 -y -f image2 -vframes 1 -s \'80x45\' '+screenshot_filename
    command='ffmpeg -ss '+str(hours)+':'+str(mins)+':'+str(secs+msecs)+' -i ../../nsh_shop_120.mp4 -y -f image2 -vframes 1 -s \'80x45\' '+screenshot_filename
    os.system(command)
    return screenshot_filename



