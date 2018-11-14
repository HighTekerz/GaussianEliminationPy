import requests as req
import json

# if you want this file to run when you push f5 you will need to right click it
# in the solution explorer
# right click on the file name and choose, "set as startup file"

outFileName = "c:\\scouting\\matchData.csv"

def tableDataSpace(string):
    title = string.split(" -->")[0]
    red = string.split("<td")[1].split("> ")[1].split(" <")[0]
    blue = string.split("<td")[3].split("> ")[1].split(" <")[0]
    return title,red,blue

def tableDataParen(string):
    title = string.split(" -->")[0]
    red = string.split("<td")[1].split(">")[1].split(" ")[0]
    blue = string.split("<td")[3].split(">")[1].split(" ")[0]
    return title,red,blue

def tableDataNoSpace(string):
    title = string.split("-->")[0]
    red = string.split("<td")[1].split(">")[1].split("<")[0]
    blue = string.split("<td")[3].split(">")[1].split("<")[0]
    return title,red,blue

def tableDataBold(string):
    title = string.split(" -->")[0]
    red = string.split("<td")[1].split("<b>")[1].split("<")[0]
    blue = string.split("<td")[2].split("<b>")[1].split("<")[0]
    return title,red,blue

def tableDataPlus(string):
    formatted = string.replace(" ", "").replace("\n", "")
    return tableDataNoSpace(formatted)

with open('settings.json') as json_file:
    settings = json.load(json_file)
    outFile = settings['bluealliance']['outfile']


outFile = open(outFileName, "w")

applyHeaders = 0

for matchNumber in list(range(1,71)):
    url = "https://www.thebluealliance.com/match/2018waamv_qm" + str(matchNumber)
    print(url)
    webReq = req.get(url)


    starting = webReq.text.split('<table class="match-table">')

    colorteams = starting[1].split('data-team="')

    redteam1 = colorteams[1].split("\"")[0].split("frc")[1]
    redteam2 = colorteams[2].split("\"")[0].split("frc")[1]
    redteam3 = colorteams[3].split("\"")[0].split("frc")[1]

    bluescore = colorteams[2].split("<span")[0].split('>')[0].split('<')

    blueteam1 = colorteams[4].split("\"")[0].split("frc")[1]
    blueteam2 = colorteams[5].split("\"")[0].split("frc")[1]
    blueteam3 = colorteams[6].split("\"")[0].split("frc")[1]

    redscore = colorteams[2].split("<span")[0].split('>')[0].split('<')

    groups = starting[2].split("<!-- ")

    data = []

    data.append(tableDataSpace(groups[4]))
    data.append(tableDataSpace(groups[5]))
    data.append(tableDataSpace(groups[6]))
    data.append(tableDataSpace(groups[7]))
    data.append(tableDataBold(groups[8]))
    data.append(tableDataPlus(groups[9]))
    data.append(tableDataPlus(groups[10]))
    data.append(tableDataSpace(groups[11]))
    data.append(tableDataParen(groups[12]))
    data.append(tableDataParen(groups[13]))
    data.append(tableDataParen(groups[14]))
    data.append(tableDataSpace(groups[15]))
    data.append(tableDataNoSpace(groups[16]))
    data.append(tableDataNoSpace(groups[17]))
    data.append(tableDataNoSpace(groups[18]))
    data.append(tableDataSpace(groups[19]))
    data.append(tableDataBold(groups[20]))


    def td22f(string):
        title = "fouls committed"
        groups = string.split('<td')
        blue = groups[1].split(">+")[1].split('<')[0]
        red = groups[3].split(">+")[1].split('<')[0]
        return title,red,blue

    def td22a(string):
        title = "adjustments"
        groups = string.split('<td')
        red = groups[4].split(">")[1].split('<')[0]
        blue = groups[6].split(">")[1].split('<')[0]
        return title,red,blue

    def td22tot(string):
        title = "total"
        groups = string.split('<td')
        blue = groups[7].split("b>")[1].split('<')[0]
        red = groups[8].split("b>")[1].split('<')[0]
        return title,red,blue

    def td22rank(string):
        title = "RP"
        groups = string.split('<td')
        blue = groups[9].split(">+")[1].split(' ')[0]
        red = groups[11].split(">+")[1].split(' ')[0]
        return title,red,blue


    data.append(td22f(groups[22]))
    data.append(td22a(groups[22]))
    data.append(td22tot(groups[22]))
    data.append(td22rank(groups[22]))

    def cp(thisisData):
        outFile.write (thisisData)
        outFile.write(",")

    if applyHeaders == 0:
        applyHeaders = 1;
        cp("Match")
        cp("Color")
        cp("Team")
        for dataStr in data:
            cp(dataStr[0])
        outFile.write('\n')

    cp(str(matchNumber))
    cp(str("red"))
    cp(redteam1)
    for dataStr in data:
        cp(dataStr[1])
    outFile.write('\n')

    cp(str(matchNumber))
    cp(str("red"))
    cp(redteam2)
    for Datastr in data:
        cp(Datastr[1])
    outFile.write('\n')

    cp(str(matchNumber))
    cp(str("red"))
    cp(redteam3)
    for Datastr in data:
        cp(Datastr[1])
    outFile.write('\n')

    cp(str(matchNumber))
    cp(str("blue"))
    cp(blueteam1)
    for Datastr in data:
        cp(Datastr[2])
    outFile.write('\n')

    cp(str(matchNumber))
    cp(str("blue"))
    cp(blueteam2)
    for Datastr in data:
        cp(Datastr[2])
    outFile.write('\n')

    cp(str(matchNumber))
    cp(str("blue"))
    cp(blueteam3)
    for Datastr in data:
        cp(Datastr[2])
    outFile.write('\n')

    outFile.flush()

outFile.close()
