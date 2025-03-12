test_scores = [20, 175, 212, 2703, 2973, 15875]

for score in test_scores:
  
    if score <= 100:
        bonus = 5
    elif score <= 1000:
        bonus = score * 0.2
    else:
        bonus = score * 0.1

    if score % 2 == 0:
        bonus += 1
    if score % 10 == 5:
        bonus += 2

    total_score = score + bonus
    print(f"Score: {score}, Bonus: {bonus}, Total Score: {total_score}")
