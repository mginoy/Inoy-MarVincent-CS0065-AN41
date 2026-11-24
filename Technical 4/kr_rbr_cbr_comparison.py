# PART 1 - Knowledge Representation
facts = {
    "temperature": 33,
    "is_raining": True,
    "humidity": 88,
    "wind_speed": 48,
    "flood_warning": True,
    "power_outage": False,
}


# PART 2 - Rule-Based Reasoning
def rule_hot(facts):
    if facts["temperature"] > 30:
        return "Turn on cooling equipment and advise residents to stay hydrated."


def rule_rainy(facts):
    if facts["is_raining"]:
        return "Bring umbrellas and monitor road conditions."


def rule_humid(facts):
    if facts["humidity"] >= 85:
        return "Prepare ventilation and drinking-water stations."


def rule_windy(facts):
    if facts["wind_speed"] >= 40:
        return "Secure loose outdoor objects and suspend small-boat travel."


def rule_flood(facts):
    if facts["flood_warning"]:
        return "Pre-position rescue teams and prepare flood-prone areas for evacuation."


rules = [rule_hot, rule_rainy, rule_humid, rule_windy, rule_flood]
actions = []

for rule in rules:
    action = rule(facts)
    if action:
        actions.append(action)

print("PART 1 - Knowledge Representation")
for fact, value in facts.items():
    print(fact + ":", value)

print("\nPART 2 - Rule-Based Reasoning Actions")
for action in actions:
    print("-", action)


# PART 3 - Case-Based Reasoning
case_base = [
    {"name": "Case 1 - Hot Day", "problem": {"temperature": 34, "is_raining": False, "flood_warning": False, "wind_speed": 10}, "solution": "Open cooling stations and distribute drinking water."},
    {"name": "Case 2 - Heavy Rain", "problem": {"temperature": 27, "is_raining": True, "flood_warning": False, "wind_speed": 22}, "solution": "Issue rain advisory and inspect drainage channels."},
    {"name": "Case 3 - Flood Alert", "problem": {"temperature": 29, "is_raining": True, "flood_warning": True, "wind_speed": 35}, "solution": "Pre-position rescue teams and prepare evacuation centers."},
    {"name": "Case 4 - Strong Wind", "problem": {"temperature": 28, "is_raining": True, "flood_warning": False, "wind_speed": 55}, "solution": "Secure outdoor structures and suspend small-boat travel."},
]


def similarity(new_problem, old_problem):
    score = 0
    score += max(0, 1 - abs(new_problem["temperature"] - old_problem["temperature"]) / 20)
    score += new_problem["is_raining"] == old_problem["is_raining"]
    score += new_problem["flood_warning"] == old_problem["flood_warning"]
    score += max(0, 1 - abs(new_problem["wind_speed"] - old_problem["wind_speed"]) / 60)
    return score / 4


new_problem = {
    "temperature": facts["temperature"],
    "is_raining": facts["is_raining"],
    "flood_warning": facts["flood_warning"],
    "wind_speed": facts["wind_speed"],
}

best_case = case_base[0]
best_score = similarity(new_problem, best_case["problem"])

for case in case_base:
    score = similarity(new_problem, case["problem"])
    if score > best_score:
        best_case = case
        best_score = score

final_solution = best_case["solution"]
if new_problem["wind_speed"] >= 45:
    final_solution += " Also suspend small-boat travel because of strong winds."

case_base.append({"name": "Case 5 - Current Weather Event", "problem": new_problem, "solution": final_solution})

print("\nPART 3 - Case-Based Reasoning")
print("New problem:", new_problem)
print("Retrieved case:", best_case["name"], "-", round(best_score * 100, 1), "% similar")
print("Reuse step:", best_case["solution"])
print("Revise step:", final_solution)
print("Retain step: New case saved")
print("Updated case base:")
for case in case_base:
    print("-", case["name"])
