hits = input("Please enter how many times you'd like to hit: ")
hits = int(hits)
hit_reps = range(0,hits,1)
hit_type = ("Miss, Bad, Good, or Perfect?: ")
score = 0
multiplier = 1

final_score = score * (1+multiplier)

for i in hit_type:
    

    if i == "miss":
        score + 0
        multiplier = 1

    elif "bad":
        score + 50
        multiplier + 1

    elif "good":
        score + 100
        multiplier + 1
    elif "perfect":
        score + 300
        multiplier + 1
    