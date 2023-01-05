import math

def match_list(team_list:list, numteams:int):
  byes = math.pow(2,math.ceil(math.log(numteams,2))) - numteams
  bye_teams = []
  for i in range (byes-1):
    bye_teams.append(numteams[0])
    team_list.pop(0)
  matches = []
  for i in range (numteams-byes)-1:
    matches.append([team_list[0],team_list[-1]])
    team_list.pop(0)
    team_list.pop(-1)
  next_level = []
  for b in bye_teams:
    next_level.append([b,matches[-1]])
    matches.pop(-1)
  for m in matches:
    next_level.append(m)
  print(next_level)



  