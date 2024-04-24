from random import randrange

players = []
try:
  resaultsR = open("resaults.txt", "r")
  data = resaultsR.read().split("\n")
  resaultsR.close();
  data.pop()
  for item in data:
    players.append({'name': item.split()[0], 'win': int(item.split()[1]), 'lose': int(item.split()[2])})
except:
  players = []

myStrs = ["orange", "red", "green", "yellow"]
myStr = myStrs[randrange(len(myStrs))]
myStrHidden = list("-"*len(myStr))
count = 1
f = 0
userName = input("write your name ")
for item in players:
  if item['name'] == userName:
    f = 1 
if f:
    print(f"welcome back, {userName}")
    currentPlayer = userName
else:
    print(f"nice to meet ya, {userName}")
    players.append({'name':userName, 'win':0, 'lose':0})
    currentPlayer = userName
while count != 8:
  print(myStrHidden)
  userChar = input(f"chance {count} out of 7: ")
  while userChar.isdigit() or len(userChar) != 1:
    userChar = input(f"chance {count} out of 7: ")
  if userChar in myStr:
    if userChar in myStrHidden:
      print("try again")
      count += 1
    else:
      positionsList = []
      for i in range(len(myStr)):
        if userChar == myStr[i]:
          positionsList.append(i)
      for daIndex in positionsList:
        myStrHidden[daIndex] = userChar
      if "-" not in myStrHidden:
        print(myStrHidden)
        print(f"you did it, {currentPlayer}")
        for item in players:
          if item['name'] == currentPlayer:
            item['win'] += 1
        break
  else:
    print("try again")
    count+=1


if count == 8:
  print(f"sorry for your loss, {currentPlayer}")
  for item in players:
    if item['name'] == currentPlayer:
      item['lose'] += 1
resaultsW = open("resaults.txt", "w")
for item in players:
  resaultsW.writelines(f"{item['name']} {item['win']} {item['lose']}\n")
resaultsW.close();
