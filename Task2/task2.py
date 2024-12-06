import sys

def read_file_content(file_path):
    """reads the file content imported through terminal and does error handling for file name"""
    try:
        with open(file_path, "r") as file1:
            content = file1.readlines()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit()
        
def our_cat(content):
    """reads every line of file and counts how many times our cat entered and makes 2 list of our cat entry and exit time"""
    cat_count=0
    our_cat_enter=[]
    our_cat_exit=[]
    for line in content:
        if "OURS" in line:
            cat_count=cat_count+1
            parts=line.split(',')
            our_cat_enter.append(int(parts[1]))
            our_cat_exit.append(int(parts[2]))
    return cat_count,our_cat_enter,our_cat_exit
              
def their_cat(content):
    """counts the number of times the neighbour cat entered"""
    other_cat_enter=[]
    other_cat_exit=[]
    other_cat=0
    for line in content:     
        if "THEIRS" in line:
            other_cat=other_cat+1
            parts=line.split(',')
            other_cat_enter.append(int(parts[1]))
            other_cat_exit.append(int(parts[2]))
    return other_cat,other_cat_enter,other_cat_exit
  
def time(content):
    """cretes 2 list that adds entry and exit time of all cats"""
    entry_time=[]
    exit_time=[]     
    for line in content:
        parts=line.split(',')
        if len(parts)>=3:
            entry_time.append(int(parts[1]))
            exit_time.append(int(parts[2]))
    return entry_time, exit_time
    
def our_cattime(our_cat_enter,our_cat_exit): 
    """calculates time spend by our cat in the house"""
    our_cat_time=0        
    for i in range(len(our_cat_enter)):
        our_cat_time+=our_cat_exit[i]-our_cat_enter[i]
        hour=our_cat_time//60
        mins=our_cat_time%60
    return our_cat_time,hour,mins
 
def other_cattime(other_cat_enter,other_cat_exit): 
    """calculates time spend by other cat in the house"""
    other_cat_time=0        
    for i in range(len(other_cat_enter)):
        other_cat_time+=other_cat_exit[i]-other_cat_enter[i]
    hou=other_cat_time//60
    mis=other_cat_time%60
    return other_cat_time,hou,mis

def all_cat_time(entry_time,exit_time):
    """calculates total time spend by all cats in the house"""
    Total_time=0
    for i in range(len(entry_time)):
        Total_time+=exit_time[i]-entry_time[i]
    hr=Total_time//60
    min=Total_time%60
    return hr,min

def average(our_cat_time,cat_count):
    """calculates average time of visit of our cats"""
    avg_visit=int(our_cat_time/cat_count)
    return avg_visit

def long_short(our_cat_enter,our_cat_exit):
    """calculates the longest and shortest time spend by our cats"""
    longest=0       #value initialize as longest time must be sth above 0 mins or hours
    shortest=our_cat_exit[0]-our_cat_enter[0]      #value initialization as first time interval, as shortest could be as low as 1 min which could be selected through value swapping
    for i in range(len(our_cat_enter)):
        interval=our_cat_exit[i]-our_cat_enter[i]
        if interval>longest:
            longest=interval
        if interval<shortest:
            shortest=interval
    return longest,shortest
                
def long_hr(longest):
    """converts longest time of cat visit into hour and minutes"""
    longest_hr=longest//60
    longest_min=longest%60
    return longest_hr,longest_min

def short_hr(shortest):
    """converts shortest time of cat visit into hour and minutes """
    shortest_hr=shortest//60
    shortest_min=shortest%60
    return shortest_hr,shortest_min

def output(cat_count,other_cat,hour,mins,hou,mis,hr,min,avg_visit,longest_hr,longest_min,shortest_hr,shortest_min):
    """Output display"""
    print("Log File Analysis")
    print("=====================")   
    print(f"\nCat Visits: {cat_count}")
    print(f"Other Cats: {other_cat} \n")   
    print(f"Total time in House by our cats: {hour} hours,{mins} minutes")
    print(f"Total time in House by neighbour cats: {hou} hours,{mis} minutes")
    print(f"Total time in House by our cats and neighbours as well: {hr} hours,{min} minutes")
    print(f"\nAverage visit length of our cats: {avg_visit} minutes")
    if longest_hr>0:
        print(f"Longest visit: {longest_hr} hours, {longest_min} minutes")
    else:
        print(f"Longest visit: {longest_min} minutes")
    if shortest_hr>0:
        print(f"Shortest visit: {shortest_hr} hours, {shortest_min} minutes\n")
    else:
        print(f"Shortest visit: {shortest_min} minutes\n")
        
#checks if command line arguments is entered or not
if len(sys.argv)!=2:
    print("Missing command line argument")

#function call
else:  
    file_content=read_file_content(sys.argv[1])
    catcount,ourcatenter,ourcatexit=our_cat(file_content)
    theircat,othercatenter,othercatexit=their_cat(file_content)
    entrytime,exittime=time(file_content)
    ourcattime,hr,minute=our_cattime(ourcatenter,ourcatexit)
    othercattime,hou,mis=other_cattime(othercatenter,othercatexit)
    hour,min=all_cat_time(entrytime,exittime)
    avg=average(ourcattime,catcount)
    long,short=long_short(ourcatenter,ourcatexit)
    hours,mins=long_hr(long)
    hor,mi=short_hr(short)
    display=output(catcount,theircat,hr,minute,hou,mis,hour,min,avg,hours,mins,hor,mi)



