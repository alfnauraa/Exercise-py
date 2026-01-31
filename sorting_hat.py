gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1 = int(input('do u like dawn or dusk? 1) dawn 2) dusk: '))

if q1 == 1:
  print('Gryffindor and Ravenclaw get a +1')
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  print('Hufflepuff and Slytherin get a +1')
  hufflepuff += 1
  slytherin += 1
else:
  print('wrong input')

q2 = int(input('Q2) When I’m dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold: '))
if q2 == 1:
  print('Hufflepuff +2')
  hufflepuff += 2
elif q2 == 2:
  print('Slytherin +2')
  slytherin += 2
elif q2 == 3:
  print('Ravenclaw +2')
  ravenclaw += 2
elif q2 == 4:
  print('Gryffindor +2')
  gryffindor += 2
else:
  print('wrong input')

q3 = int(input('Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum: '))
if q3 == 1:
  print('Slytherin +4')
  slytherin += 4
elif q3 == 2:
  print('Hufflepuff +4')
  hufflepuff += 4
elif q3 == 3:
  print('Ravenclaw +4')
  ravenclaw += 4
elif q3 == 4:
  print('Gryffindor +4')
  gryffindor += 4
else:
  print('wrong input')

print("\n--- 🏁 Total Scores 🏁 ---")
print(f"Gryffindor: {gryffindor}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Slytherin: {slytherin}")

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)  

if gryffindor == most_points:
  print('🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
