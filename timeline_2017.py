from hhm_event import *
from hhm_plot import *

tot_time = 754.0

start_time = all_events['napkin_pull'][0]
end_time = all_events['napkin_pull'][1]
start_time = all_events['apple_pick'][0]
end_time = all_events['apple_place'][1]
start_time = all_events['dentyne_pick'][0]
end_time = all_events['dentyne_place'][1]
start_time = all_events['milk_place'][0] * 29.97
end_time = all_events['milk_place'][1] * 29.97
event_name = "Milk bottle place #1"

make_plot(start_time,end_time,event_name);


