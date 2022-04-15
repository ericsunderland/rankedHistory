import cassiopeia as cass
import os 
from riotwatcher import LolWatcher, ApiError
from collections import Counter
#https://cassiopeia.readthedocs.io/en/latest/cassiopeia/data.html#cassiopeia.data.Queue
#https://cassiopeia.readthedocs.io/en/latest/cassiopeia/match.html?highlight=match_history
#https://github.com/pseudonym117/Riot-Watcher
def getLocalAPIKey():
    if(os.path.exists('apiKey.txt')):
        f=open('apiKey.txt', "r")
        return f.read()
    else:
        return 0


cass.set_riot_api_key(str(getLocalAPIKey()))
#lol_watcher = LolWatcher(getLocalAPIKey())

#Support Other regions maybe

def call(summonerName):
    summoner = cass.get_summoner(name = summonerName, region ="NA")
    #summoner = lol_watcher.summoner.by_name('na1', summonerName)
    #print(summoner.match_history[0])
    match_history = cass.get_match_history(
        continent=summoner.region.continent,
        puuid=summoner.puuid,
        queue=cass.data.Queue.ranked_solo_fives,
    )
    champion_id_to_name_mapping = {
        champion.id: champion.name for champion in cass.get_champions(region="NA")
    }
    #print(match_history['Leona'])
    played_champions = Counter()
    for match in match_history:
        champion_id = match.participants[summoner].champion.id
        champion_name = champion_id_to_name_mapping[champion_id]
        played_champions[champion_name] += 1
    print("Length of match history:", len(match_history))
    print(f"Top 10 champions {summoner.name} played:")
    champOutput =[]
    for champion_name, count in played_champions.most_common(10):
        print(champion_name, count)
        champOutput+=(champion_name,count)
    print()
    return champOutput
    #print(summoner.match_history(begin_time=cass.Patch.from_str('11.19', region= "NA").start, continent ='Americas', puuid = summoner.puuid))
    #print(summoner.match_history(begin_time=cass.Patch.from_str("12.6", region="NA").start))
## We will truncate the summoner's match history so we don't pull thousands of matches
#match_history = Summoner(name="Dabblegamer", region="NA").match_history(begin_time=Patch.from_str("9.1", region="NA").start)
#all_teemo_games = match_history.search("Teemo")
