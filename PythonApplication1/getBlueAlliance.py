import requests as req, json

# if you want this file to run when you push f5 you will need to right click it in the solution explorer
# right click on the file name and choose, "set as startup file"

#
# what data you can get is documented here
# https://www.thebluealliance.com/apidocs/v3
#
# settings.json has the file settings

with open('settings.json') as json_file:  
    settings = json.load(json_file)
    outfile = settings['bluealliance']['outfile']

outFile = "c:\\scouting\\teamdata.csv"
url = "https://www.thebluealliance.com/api/v3/teams/2"
headers = {'X-TBA-Auth-Key': 'K8xmQc6P0e8trnfxLXl7kCgYGX4bNxx7WZVWyWIQcq1kcgVimIJR1Mc1XV67UWpH'}
r = req.get(url, headers = headers)

teams = json.loads(r.text)

    #
    # change what you want to output here
    #   \/   \/   \/   \/
data = ['team_number', 'name', 'nickname']

f = open(outFile,"w")

for team in teams:

    for i in range(len(data)):
        f.write(str(team[data[i]]) + ',')
    f.write('\n')
f.close()
