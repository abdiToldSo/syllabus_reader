from ics import Calendar, Event
import datefinder
c = Calendar()
e = Event()

with open('input.txt', 'r') as f:
    # lines = f.readlines()
    # columns = []
    # i = 1
    dates = f.read()
    dates_list = dates.splitlines()

    # for line in lines:
matches = datefinder.find_dates(dates)
# dates_f = [list(datefinder.find_dates(d)) for d in dates]
test_m = list(matches)
# for match in matches:
    # print(match, match.isoweekday)
    # list(match)

# print(dates_f) 
# print(dates_list[0])
# print(dates)i

# date_title_list = [ parsed if (isinstance(line[parsed], float) and parsed+1 <= len(line) ) for parsed in range(len(line)) for line in dates_list]
date_title_list = []
index = 0
for line in dates_list:
    # index = 0
    print(line)
    # for parsed in range(len(line)):
    for parsed in line.split():
        # print(line[parsed])
        # if ( isinstance(line[parsed], float) and parsed+1 <= len(line) ):
        # if ( isinstance(line[parsed], float) ):
        # print(parsed)
        try:
            if ( isinstance(float(parsed), float) and not float(parsed).is_integer() ):
        
                # print("True", parsed, line.split().index(parsed), line.split())
                parsed_index = line.split().index(parsed)
                parsed_index+=1
                while parsed_index< len(line.split()):
                    # parsed_index+=1
                # for ( len(line.split()) )
                    print(line.split()[parsed_index])
                    # date_title_list.append(line[parsed_index])
                    try:
                        date_title = ""
                        print(parsed_index)
                        # print(line)
                        # print(index, len(date_title_list), line[parsed_index])
                        date_title.join(line.split()[parsed_index])
                        # print(index)
                        # print(date_title)
                        # date_title_list[index]+= line.split()[parsed_index]
                        date_title_list.append(date_title)
                    except IndexError:
                        pass
                    parsed_index+=1
                # parsed_index+=1
        except ValueError: 
            pass
            # index+=1
            # print("false!")
                # print(parsed)
            

# for i in range(len(test_m)):
    # print(test_m[i].weekday(), dates_list[i])
    
    # if test_m[i].weekday() == 0:
        
print(date_title_list)
