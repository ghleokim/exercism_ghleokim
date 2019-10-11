count_num = [
    "",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]

lyric = [
    "",
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",    
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, "
]

start = lambda n: f"On the {count_num[n]} day of Christmas my true love gave to me: "

def recite(start_verse, end_verse):
    res = []
    
    for i in range(start_verse,end_verse+1):
        if i == 1:
            res.append(start(1)+lyric[1])
        else:
            tmp = start(i)
            for j in range(i,1,-1): tmp += lyric[j]
            tmp += 'and ' + lyric[1]
            res.append(tmp)
    
    return res
