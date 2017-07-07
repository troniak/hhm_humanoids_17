import matplotlib.pyplot as plot
import numpy as np
from hhm_io import *
import matplotlib.image as image
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)

annot_colors = {'In taxonomy': '#999999', 'New': '#99ff99'}

def plot_transitions(events,bottom,start_time,end_time):
    for event_name,event_time in zip(events.keys(),events.values()):
        rect = plot.Rectangle( ((event_time[0])/(end_time-start_time),bottom),3/(end_time-start_time),graph_height*4+graph_gap*3,fc='#000000',alpha=0.2,linewidth=0)
        ax.add_patch(rect)

def plot_screenshots(bottom,start_time,end_time):
    step = fig_max_x / 12
    count = 0
    img_width=75
    img_gap=0
    for x in np.arange(0,fig_max_x,step):
        time = start_time + (end_time-start_time)*x/fig_max_x
        print 'plotting @ time: ' + str(time)
        screenshot_filename = take_screenshot(time)
        arr_img=plot.imread(screenshot_filename, format='png')
        imagebox = OffsetImage(arr_img, zoom=.6)
        imagebox.image.axes = ax

        offx=img_width/2 + count*img_width+count*img_gap
        offy=graph_height*4+graph_gap*4 + img_width/1.78

	ab = AnnotationBbox(imagebox, [offx,offy],
	    xybox=(0., 0.),
	    xycoords='data',
	    boxcoords="offset points",
	    pad=0,
	    arrowprops=dict(
		arrowstyle="->",
		connectionstyle="angle,angleA=0,angleB=90,rad=3")
	    )

        print 'plotting image '+screenshot_filename+' at ('+str(offx)+','+str(offy)+')'
        #imgplot = image.FigureImage(ax,offsetx=offx,offsety=offy)
        #imgplot.set_data(img)
        #for event_name,event_time in zip(events.keys(),events.values()):
        #rect = plot.Point2d(img)
        ax.add_artist(ab)
        count = count+1

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

def make_plot(start_time,end_time,event_name):
    plot_screenshots(graph_height*4+graph_gap*4, start_time / 29.97, end_time / 29.97)

    plot.text(-105, graph_height*0+graph_gap*0+15, "Miscellaneous")
    plot.text(-105, graph_height*1+graph_gap*1+15, "BMD")
    plot.text(-105, graph_height*2+graph_gap*2+15, "Pose")
    plot.text(-105, graph_height*3+graph_gap*3+15, "Intrinsic\nmanipulation")

    plot_data(misc_filename, annot_colors,graph_height*0+graph_gap*0,start_time,end_time)
    plot_data(bmd_filename, annot_colors,graph_height*1+graph_gap*1,start_time,end_time)
    plot_data(feix_filename, annot_colors,graph_height*2+graph_gap*2,start_time,end_time)
    plot_data(ec_filename, annot_colors,graph_height*3+graph_gap*3,start_time,end_time)

    plot.suptitle(event_name+" timeline")

    plot.show()

fig = plot.figure(figsize=(11, 3.5))
fig_max_x = 900
fig_max_y = 500
graph_height = .05*fig_max_y
graph_gap = .14*fig_max_y
#ax = fig.add_axes([0, 0, 1, 1],xticks=[0,fig_max_x],yticks=[0,fig_max_y])
xlabels = ['%i' % i for i in range(0,fig_max_x,30)]
ax = fig.add_axes([0, .2, 1, .7],xticks=range(0, fig_max_x, 30), yticks=[0,fig_max_y])
ax.set_xticklabels(xlabels,rotation=40)
ax.set_aspect(.5)
ax.yaxis.set_visible(False)
ax.set_xlabel("Time (frames)")
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
