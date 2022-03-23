from string import Template

def gatherstats(seconds: int) -> list:
    print(f"initial input: {seconds}")
    maxtime = 359999
    mintime = 0
    hour = 0
    minute = 0
    second = 0
    day = 0
    year = 0
    
    if seconds == mintime:
        return "now"

    while seconds != 0:
        second = second + 1
        if second == 60:
            minute = minute + 1
            second = 0
        if minute == 60:
            hour = hour + 1
            minute = 0
        if hour == 24:
            day = day + 1
            hour = 0
        if day == 365:
            year = year + 1
            day = 0
        seconds = seconds - 1
    
    bank = [("years", year), ("days", day), ("hours", hour), ("minutes", minute), ("seconds", second)]
    useful = []
    ##getting useful stats
    for i in bank:
        if i[1] > 0:
            useful.append(i)
        
    return useful
    
def format(useful: list) -> str:
    ##formatting
    result = ""
    for i in useful:
        ##remove plurals
        if i[1] <= 1:
            temp = i[0]
            temp = temp[:-1]
            num = str(i[1])
            result = result + num + " " + temp + ", "
            continue
        
        ##if no plurals
        num = str(i[1])
        result = result + num + " " + i[0] + ", "
    
    result = result[:-2]
            
    if len(useful) > 1:
        result = ",".join(result.split(",")[:-1]) + ", and" + result.split(",")[-1]
    elif len(useful) == 0:
        result = ",".join(result.split(",")[:-1]) + " and" + result.split(",")[-1]
    return result

def main():
    keepgoing = "Y"
    while keepgoing == "y" or keepgoing == "Y":
        time = int(input("enter number of seconds: "))
        if time < 0:
            print(f"input value: {time}, is less than 0")
        else:
            stats = gatherstats(time)
            result = format(stats)
            print(f"converted time: {result}")
        keepgoing = str(input("Do you want to continue? Enter Y to continue: "))

main()
