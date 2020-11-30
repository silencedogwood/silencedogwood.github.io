import time 
from datetime import datetime
import json

#today = time.time()
today = int( time.mktime(
    datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0).timetuple()) )

# Count number of lines 
with open("zettels.md", "r") as f:
    for i,l in enumerate(f):
        pass
num_lines = i + 1

# Create JSON file if it doesn"t exist or add new lines for the day
try:
    with open("count.json", "x", encoding="utf-8") as f:
        json.dump({ "total": num_lines, 
                    str(today): num_lines }, 
                f, ensure_ascii=False, indent=4 )
except:
    with open("count.json", "r") as f:
        data = json.loads( f.read() )

    # Lines for today are difference between numLines and total
    # If key already exists for today, modify its value and total 
    write = False # This way Jekyll does loop forever after rewriting same value
    if ( str(today) in data ):
        lines_written = max(0, num_lines - data["total"] + data[str(today)])
        if lines_written != data[str(today)]:
            data[str(today)] = lines_written
            write = True
    else: 
        data[str(today)] = max(0, num_lines - data["total"])
        write = True
    if data["total"] != num_lines:
        data["total"] = num_lines
        write = True
    
    # Write to file 
    if write:
        with open("count.json", "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

