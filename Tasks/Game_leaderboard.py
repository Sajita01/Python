# Scores live in a Day 06 dictionary. sorted() with reverse=True puts the biggest first, and slicing [:3] , takes the top 3.

scores = {"Ram": 450, "Sita": 720, "Hari": 380, "Gita": 610}

top = sorted(scores.values(), reverse=True)
print(f"Top 3 scores: {top[:3]}")      # [720, 610, 450]

print(f"Players: {len(scores)}")       # 4
print(f"Total points: {sum(scores.values())}")   # 2160

# key=scores.get: compare the names by their score
print(f"Winner: {max(scores, key=scores.get)}")  # Sita

#  print every name A to Z, numbered with enumerate()
for number, name in enumerate(sorted(scores), start=1):
    print(f"{number}. {name}")

# print who came last, with min(..., key=scores.get)
print(f"Last: {min(scores, key=scores.get)}")

"""
Output:
Top 3 scores: [720, 610, 450]
Players: 4
Total points: 2160
Winner: Sita
1. Gita
2. Hari
3. Ram
4. Sita
Last: Hari

"""