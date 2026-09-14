scores = [72, 85, 90, 60, 78]
def average(numbers):
    return sum(numbers)/len(numbers)

total_high = 0
for s in scores: 
    if s >= 80:
        total_high += 1


print("Average score:", average(scores))
print("Number of high scores (>=80):", total_high)

student = {"name": "Ali", "score": 85}
print(student["name"], "got", student["score"])