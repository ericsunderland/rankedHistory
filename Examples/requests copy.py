import cassiopeia as cass
import os 
from riotwatcher import LolWatcher, ApiError
#https://cassiopeia.readthedocs.io/en/latest/cassiopeia/data.html#cassiopeia.data.Queue
#https://cassiopeia.readthedocs.io/en/latest/cassiopeia/match.html?highlight=match_history
#https://github.com/pseudonym117/Riot-Watcher
#Start times https://github.com/CommunityDragon/Data/blob/master/patches.json
# 11.19 1632294000
def getLocalAPIKey():
    f=open('apiKey.txt', "r")
    return f.read()


#cass.set_riot_api_key(str(getLocalAPIKey()))
lol_watcher = LolWatcher(getLocalAPIKey())

#Support Other regions maybe

def call(summonerName):
    #summoner = cass.get_summoner(name = summonerName, region ="NA")
    summoner = lol_watcher.summoner.by_name('na1', summonerName)
    print(summoner['puuid'])
    print(lol_watcher.match.matchlist_by_puuid(puuid=summoner['puuid'], region = 'na1', start_time = '1632294000'))
    #print(summoner.match_history(begin_time=cass.Patch.from_str("12.6", region="NA").start))
## We will truncate the summoner's match history so we don't pull thousands of matches
#match_history = Summoner(name="Dabblegamer", region="NA").match_history(begin_time=Patch.from_str("9.1", region="NA").start)
#all_teemo_games = match_history.search("Teemo")
