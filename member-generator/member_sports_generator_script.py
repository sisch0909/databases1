import random

member_list = range(1, 201)
sport_list = range(1, 13)

member_id = 1

members_sports_id = 1

while member_id <= 200:
    sport_id = random.choice(sport_list)
    print("insert into members_sports (member_sports_ID, member_ID, sport_ID) values ("+ str(members_sports_id) + ", " +
          str(member_id) + ", " + str(sport_id) + ");")
    member_id = member_id + 1
    members_sports_id = members_sports_id + 1


counter = 1

while counter <= 100:
    member_id = random.choice(member_list)
    sport_id = random.choice(sport_list)
    print("insert into members_sports (member_sports_ID, member_ID, sport_ID) values ("+ str(members_sports_id) + ", "  +
          str(member_id) + ", " + str(sport_id) + ");")
    counter = counter + 1
    members_sports_id = members_sports_id + 1
