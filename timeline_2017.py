import matplotlib.pyplot as plot
import matplotlib.image as image
import csv
from pylab import imread
import numpy as np
import os

def mult255(n):
    return n*255

def get_colors(ncolors):
    # define the colormap
    cmap = plot.cm.jet
    # extract all colors from the .jet map
    step = cmap.N / ncolors
    cmaplist = ['#%02x%02x%02x' % tuple(map(mult255,cmap(i)[0:3])) for i in range(0,cmap.N,step)]
    return cmaplist

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

def plot_data(filename, annot_colors_, bottom, start_time, end_time):
    # Load data
    [num_annots, starts, ends, annots, status] = load_data(filename,start_time,end_time)
    for i in range(num_annots):
      color = annot_colors_[str(status[i])]

      left = (starts[i] - start_time) / (end_time-start_time)*fig_max_x
      height = graph_height
      width = max(.005, (ends[i]-starts[i])/(end_time-start_time))*fig_max_x
      rect = plot.Rectangle( (left, bottom), width, height, fc=color, linewidth=1, edgecolor="#000000")
      ax.add_patch(rect)
      if (i % 2 == 1):
        ax.text(left, bottom+height+36, str(annots[i]), fontsize=8)   # Print label
      else:
        ax.text(left, bottom+height+12, str(annots[i]), fontsize=8)   # Print label
      #print left, bottom, height, width, annot_colors_[str(annots[i])]

#def plot_transitions(bottom,start_time,end_time):
#    for event_start,event_end in zip(event_starts,event_ends):
#        if(event_start >= start_time and event_end <= end_time):
#            rect = plot.Rectangle( ((event_start)/(end_time-start_time),bottom),1/(end_time-start_time),graph_height*1.1,fc='#000000',linewidth=0)
#            ax.add_patch(rect)
#            rect = plot.Rectangle( ((event_end)/(end_time-start_time),bottom),1/(end_time-start_time),graph_height*1.1,fc='#ff0000',linewidth=0)
#            ax.add_patch(rect)

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

def mark_events(events,bottom,start_time,end_time):
    #even = 0
    for event_name,event_time in zip(events.keys(),events.values()):
        color='#FF0000'
        rect = plot.Rectangle( \
            ((event_time[0])/(end_time-start_time),bottom),\
            (event_time[1]-event_time[0])/(end_time-start_time),\
            graph_height*3+graph_gap*3,fc=color,alpha=0.2,linewidth=0)
        ax.add_patch(rect)
        #even = not even

def plot_transitions(events,bottom,start_time,end_time):
    for event_name,event_time in zip(events.keys(),events.values()):
        rect = plot.Rectangle( ((event_time[0])/(end_time-start_time),bottom),3/(end_time-start_time),graph_height*3+graph_gap*3,fc='#000000',alpha=0.2,linewidth=0)
        ax.add_patch(rect)

def plot_screenshots(bottom,start_time,end_time):
    step = fig_max_x / 14
    count = 0
    img_width=80
    img_gap=5
    for x in np.arange(0,fig_max_x,step):
        time = start_time + (end_time-start_time)*x/fig_max_x
        #print time
        screenshot_filename = take_screenshot(time)
        img=imread(screenshot_filename)
        imgplot = image.FigureImage(ax,offsetx=count*img_width+count*img_gap,offsety=graph_height*3+graph_gap*3)
        imgplot.set_data(img)
        #for event_name,event_time in zip(events.keys(),events.values()):
        #rect = plot.Point2d(img)
        ax.add_artist(imgplot)
        count = count+1


tot_time = 754.0

all_events={'pistachio_pick':(0,4.9065),'mounds_pick':(4.9465,11.0462),'zone_pick':(11.0857,21.5996),'zone_place':(21.6405,29.0677),'dentyne_pick':(29.1382,36.3694),'dentyne_place':(36.4094,44.2750),'grapes_pick':(44.3150,49.6291),'grapes_place':(49.6691,55.9030),'fridge_close':(55.9430,61.3846),'mdew_pick':(61.4246,67.9125),'mdew_place':(67.9525,73.7866),'icetea_pick':(73.8266,80.7299),'icetea_place':(80.7699,88.8871),'silk_pick':(88.9271,96.3476),'silk_place':(96.3876,102.4719),'pellegrino_place':(102.5119,108.4981),'amp_pick':(108.5381,113.7064),'amp_place':(113.7498,117.3121),'dressing_pick':(117.3555,122.1213),'dressing_place':(122.1582,125.4575),'turnstile_turn':(125.4975,130.8889),'dressing_pick_2':(130.9289,136.5280),'dressing_place_2':(136.5680,147.1853),'salad_pick':(147.2253,154.6794),'salad_place':(154.7194,159.7369),'cream_pick':(159.7769,169.2719),'cream_place':(169.3119,179.3562),'creamer_pick':(179.3962,191.8979),'creamer_place':(191.9379,196.4264),'creamer_pick_2':(196.4664,203.5256),'creamer_place_2':(203.5656,207.2519),'yogurt_pick':(207.2919,211.9301),'yogurt_place':(211.9701,216.0834),'milk_pick':(216.1234,221.0878),'milk_place':(221.1879,226.4595),'milk_pick_2':(226.4995,233.3997),'milk_place_2':(233.4675,239.1674),'pasta_pick':(239.2074,245.2812),'pasta_place':(245.3212,249.0475),'cup_pick':(249.0875,254.9149),'cup_place':(254.9549,260.9173),'cup_pick_2':(260.9607,269.9747),'cup_push':(270.0256,276.2492),'tea_pick':(276.2892,281.9955),'tea_place':(282.0492,285.5910),'tea_pull':(285.6310,293.8653),'tea_push':(293.9053,304.1561),'stick_pick':(304.1961,310.9447),'stick_place':(310.9847,315.6408),'cutlery_pick':(315.6808,335.5305),'cutlery_place':(335.5705,355.6720),'cutlery_pick_2':(355.7120,394.0752),'cutlery_place_2':(394.1152,403.5952),'napkin_pull':(403.6352,415.5835),'salt_pick':(415.6235,421.9992),'salt_place':(422.0392,424.2754),'sign_push':(424.3154,432.8144),'bag_pull':(432.8544,439.0947),'shaker_pick':(439.1347,448.8883),'squeezer_pick':(448.9283,454.4320),'squeezer_place':(454.4720,460.2882),'shaker_pick_2':(460.3282,466.3131),'shaker_place':(466.3531,470.9966),'doritos_pick':(471.0366,480.1084),'doritos_place':(480.1484,490.7760),'doritos_pull':(490.8160,496.1354),'doritos_push':(496.1754,504.3920),'lays_pick':(504.57,515.7958),'lays_place':(515.8358,523.1675),'combos_pick':(523.2075,529.4466),'combos_place':(529.4866,536.7107),'crackerjack_pick':(536.7507,546.0327),'crackerjack_place':(546.0727,562.1215),'cracker_pick':(562.1615,568.7489),'cracker_place':(568.7889,575.2407),'pizza_pick':(575.2807,586.4770),'pizza_place':(586.5170,591.5235),'plate_pick':(591.5640,599.7854),'plate_place':(599.8254,606.5973),'sub_pick':(606.6373,618.3534),'sub_place':(618.3934,624.2054),'apple_pick':(624.2454,630.6276),'apple_place':(630.6676,641.0123),'salsacup_assemble':(641.0523,667.3220),'salsacup_disassemble':(667.3620,685.3525),'tongs_pick':(685.3925,698.3351),'tongs_place':(698.3751,706.1719),'icecream_pick':(706.2119,717.4585),'icecream_place':(717.4985,725.5255),'cone_pick':(725.5655,744.2733),'cone_place':(744.3133,754.234)}

#interesting_events=['dentyne_pick','dentyne_place','cutlery_pick_2','apple_pick','apple_place','napkin_pull']
interesting_events=['zone_pick','zone_place','mdew_pick','milk_place','cup_pick','cutlery_pick_2','lays_pick','pizza_pick']
event_names = ["Zone bar pick", "Zone bar place", "Mountain Dew pick", "Milk bottle place #1", "Pepsi cup pick", "Cutlery pick #2", "Lay's chips pick", "Pizza box pick"]


events={}
for event in interesting_events:
    events[event] = all_events[event]

bmd_filename= "BMDannotations-print.tsv"
ec_filename = "ECannotations-yuzi.tsv"
ck_filename = "CKannotations-sheet1.tsv"
feix_filename = "Grasp annotations - Feix.tsv"
misc_filename = "errorcontactannotations.tsv"
annot_colors = {'In taxonomy': '#999999', 'New': '#99ff99'}

fig = plot.figure(figsize=(11, 4))
fig_max_x = 900
fig_max_y = 800
graph_height = .05*fig_max_y
graph_gap = .1*fig_max_y
#ax = fig.add_axes([0, 0, 1, 1],xticks=[0,fig_max_x],yticks=[0,fig_max_y])
ax = fig.add_axes([0, .1, 1, .9],xticks=range(0, fig_max_x, 30), yticks=[0,fig_max_y])

ax.set_aspect(.5)
#ax.grid(True, which='both')

##plot all data
#plot_data(bmd_filename,bmd_annot_colors,graph_height*0+graph_gap*0,0,tot_time)
#plot_data( ec_filename, ec_annot_colors,graph_height*1+graph_gap*1,0,tot_time)
#plot_data( ck_filename, ck_annot_colors,graph_height*2+graph_gap*2,0,tot_time)
##plot_transitions(0,0,tot_time)
#mark_events(events,graph_height*0+graph_gap*0,0,tot_time)
#plot_transitions(all_events,0,0,tot_time)
#plot.show()
#plot.savefig('timelines/all_data.png',bbox_inches='tight')
#plot subset of data
start_time = all_events['napkin_pull'][0]
end_time = all_events['napkin_pull'][1]
start_time = all_events['apple_pick'][0]
end_time = all_events['apple_place'][1]
start_time = all_events['dentyne_pick'][0]
end_time = all_events['dentyne_place'][1]
start_time = all_events['milk_place'][0] * 29.97
end_time = all_events['milk_place'][1] * 29.97
event_name = "Milk bottle place #1"
#plot_screenshots(graph_height*3+graph_gap*3, start_time / 29.97, end_time / 29.97)
plot_data(misc_filename, annot_colors,graph_height*0+graph_gap*0,start_time,end_time)
plot.text(-100, graph_height*0+graph_gap*0+15, "Miscellaneous")
plot_data(bmd_filename, annot_colors,graph_height*1+graph_gap*1,start_time,end_time)
plot.text(-100, graph_height*1+graph_gap*1+15, "BMD")
plot_data(feix_filename, annot_colors,graph_height*2+graph_gap*2,start_time,end_time)
plot.text(-100, graph_height*2+graph_gap*2+15, "Pose")
plot_data(ec_filename, annot_colors,graph_height*3+graph_gap*3,start_time,end_time)
plot.text(-100, graph_height*3+graph_gap*3+15, "Intrinsic manip.")
plot.suptitle(event_name+" timeline")
plot.show()
#plot.show()
#plot.savefig('timelines/napkin_pull.png',bbox_inches='tight')
#plot.savefig('timelines/apple.png',bbox_inches='tight')
#plot.savefig('timelines/dentyne.png',bbox_inches='tight')
#plot.savefig('timelines/cutlery_pick.png',bbox_inches='tight')
#
#for event_start,event_end,event_name in zip(event_starts,event_ends,event_names):
#    plot_data(bmd_filename,bmd_annot_colors,.00,event_start,event_end)
#    plot_data( ec_filename, ec_annot_colors,.35,event_start,event_end)
#    plot_data( ck_filename, ck_annot_colors,.70,event_start,event_end)
#    plot.savefig('timelines/'+event_name+'.png',bbox_inches='tight')
#    plot.cla()

#plot_transitions(.65-graph_height*.05,0,tot_time)

#plot.xticks(range(0,11,1))

