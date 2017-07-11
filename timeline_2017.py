from hhm_event import *
from hhm_plot import *

tot_time = 754.0



for event_start, event_end, event_name, file_name in zip(event_starts,event_ends,event_names,interesting_events):
    make_plot(event_start*29.97, event_end*29.97, event_name)
    plot.savefig('timelines/'+file_name+'.png',bbox_inches='tight')
    plot.cla()


#start_time = all_events['milk_place'][0] * 29.97
#end_time = all_events['milk_place'][1] * 29.97
#event_name = "Milk bottle place #1"

#make_plot(start_time,end_time,event_name);


