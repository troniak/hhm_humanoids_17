all_events={'pistachio_pick':(0,4.9065),'mounds_pick':(4.9465,11.0462),'zone_pick':(11.0857,21.5996),'zone_place':(21.6405,29.0677),'dentyne_pick':(29.1382,36.3694),'dentyne_place':(36.4094,44.2750),'grapes_pick':(44.3150,49.6291),'grapes_place':(49.6691,55.9030),'fridge_close':(55.9430,61.3846),'mdew_pick':(61.4246,67.9125),'mdew_place':(67.9525,73.7866),'icetea_pick':(73.8266,80.7299),'icetea_place':(80.7699,88.8871),'silk_pick':(88.9271,96.3476),'silk_place':(96.3876,102.4719),'pellegrino_place':(102.5119,108.4981),'amp_pick':(108.5381,113.7064),'amp_place':(113.7498,117.3121),'dressing_pick':(117.3555,122.1213),'dressing_place':(122.1582,125.4575),'turnstile_turn':(125.4975,130.8889),'dressing_pick_2':(130.9289,136.5280),'dressing_place_2':(136.5680,147.1853),'salad_pick':(147.2253,154.6794),'salad_place':(154.7194,159.7369),'cream_pick':(159.7769,169.2719),'cream_place':(169.3119,179.3562),'creamer_pick':(179.3962,191.8979),'creamer_place':(191.9379,196.4264),'creamer_pick_2':(196.4664,203.5256),'creamer_place_2':(203.5656,207.2519),'yogurt_pick':(207.2919,211.9301),'yogurt_place':(211.9701,216.0834),'milk_pick':(216.1234,221.0878),'milk_place':(221.1879,226.4595),'milk_pick_2':(226.4995,233.3997),'milk_place_2':(233.4675,239.1674),'pasta_pick':(239.2074,245.2812),'pasta_place':(245.3212,249.0475),'cup_pick':(249.0875,254.9149),'cup_place':(254.9549,260.9173),'cup_pick_2':(260.9607,269.9747),'cup_push':(270.0256,276.2492),'tea_pick':(276.2892,281.9955),'tea_place':(282.0492,285.5910),'tea_pull':(285.6310,293.8653),'tea_push':(293.9053,304.1561),'stick_pick':(304.1961,310.9447),'stick_place':(310.9847,315.6408),'cutlery_pick':(315.6808,335.5305),'cutlery_place':(335.5705,355.6720),'cutlery_pick_2':(355.7120,394.0752),'cutlery_place_2':(394.1152,403.5952),'napkin_pull':(403.6352,415.5835),'salt_pick':(415.6235,421.9992),'salt_place':(422.0392,424.2754),'sign_push':(424.3154,432.8144),'bag_pull':(432.8544,439.0947),'shaker_pick':(439.1347,448.8883),'squeezer_pick':(448.9283,454.4320),'squeezer_place':(454.4720,460.2882),'shaker_pick_2':(460.3282,466.3131),'shaker_place':(466.3531,470.9966),'doritos_pick':(471.0366,480.1084),'doritos_place':(480.1484,490.7760),'doritos_pull':(490.8160,496.1354),'doritos_push':(496.1754,504.3920),'lays_pick':(504.57,515.7958),'lays_place':(515.8358,523.1675),'combos_pick':(523.2075,529.4466),'combos_place':(529.4866,536.7107),'crackerjack_pick':(536.7507,546.0327),'crackerjack_place':(546.0727,562.1215),'cracker_pick':(562.1615,568.7489),'cracker_place':(568.7889,575.2407),'pizza_pick':(575.2807,586.4770),'pizza_place':(586.5170,591.5235),'plate_pick':(591.5640,599.7854),'plate_place':(599.8254,606.5973),'sub_pick':(606.6373,618.3534),'sub_place':(618.3934,624.2054),'apple_pick':(624.2454,630.6276),'apple_place':(630.6676,641.0123),'salsacup_assemble':(641.0523,667.3220),'salsacup_disassemble':(667.3620,685.3525),'tongs_pick':(685.3925,698.3351),'tongs_place':(698.3751,706.1719),'icecream_pick':(706.2119,717.4585),'icecream_place':(717.4985,725.5255),'cone_pick':(725.5655,744.2733),'cone_place':(744.3133,754.234)}

#interesting_events=['dentyne_pick','dentyne_place','cutlery_pick_2','apple_pick','apple_place','napkin_pull']
interesting_events=['zone_pick','zone_place','mdew_pick','milk_place','cup_pick','cutlery_pick_2','lays_pick','pizza_pick']
event_names = ["Zone bar pick", "Zone bar place", "Mountain Dew pick", "Milk bottle place #1", "Pepsi cup pick", "Cutlery pick #2", "Lay's chips pick", "Pizza box pick"]


events={}
for event in interesting_events:
    events[event] = all_events[event]

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

