from math import ceil

case_base = [
    {"name": "Typhoon Ursula 2019", "problem": {"disaster_type": "typhoon", "flood_risk": True, "area_type": "urban", "population": 4200, "severity": 4}, "solution": {"evacuation": "Phased evacuation of low-lying barangays", "shelters": 14, "response_teams": 8, "resources": "Water, food packs, rescue boats, and medical kits"}},
    {"name": "Typhoon Odette 2021", "problem": {"disaster_type": "typhoon", "flood_risk": True, "area_type": "coastal", "population": 7000, "severity": 5}, "solution": {"evacuation": "Pre-emptive evacuation of coastal zones", "shelters": 24, "response_teams": 14, "resources": "Water, food packs, generators, and rescue boats"}},
    {"name": "Urban Flood 2023", "problem": {"disaster_type": "flood", "flood_risk": True, "area_type": "urban", "population": 3500, "severity": 3}, "solution": {"evacuation": "Evacuate homes near drainage canals first", "shelters": 12, "response_teams": 7, "resources": "Water, food packs, pumps, and medical kits"}},
    {"name": "Earthquake Drill 2024", "problem": {"disaster_type": "earthquake", "flood_risk": False, "area_type": "urban", "population": 5000, "severity": 3}, "solution": {"evacuation": "Move residents to designated open spaces", "shelters": 16, "response_teams": 10, "resources": "First-aid kits, radios, and assessment teams"}},
]


def similarity(new_case, old_case):
    score = 0

    if new_case["disaster_type"] == old_case["disaster_type"]:
        score += 30
    if new_case["flood_risk"] == old_case["flood_risk"]:
        score += 25
    if new_case["area_type"] == old_case["area_type"]:
        score += 15

    population_score = min(new_case["population"], old_case["population"]) / max(new_case["population"], old_case["population"])
    score += population_score * 15
    score += (1 - abs(new_case["severity"] - old_case["severity"]) / 4) * 15
    return score


new_case = {"disaster_type": "typhoon", "flood_risk": True, "area_type": "urban", "population": 4800, "severity": 4}

best_case = case_base[0]
best_score = similarity(new_case, best_case["problem"])

for case in case_base:
    score = similarity(new_case, case["problem"])
    print(case["name"], "similarity:", round(score, 1), "%")
    if score > best_score:
        best_case = case
        best_score = score

print("\nNew problem:", new_case)
print("Most similar case:", best_case["name"])

final_solution = dict(best_case["solution"])
final_solution["evacuation"] = "Prioritize a phased evacuation of flood-prone urban barangays before landfall"
final_solution["shelters"] = ceil(new_case["population"] / 300)
final_solution["response_teams"] = ceil(new_case["population"] / 600)
final_solution["resources"] = "Water, food packs, rescue boats, medical kits, radios, and backup generators"

print("\nAdapted final solution:")
for item, value in final_solution.items():
    print(item.title() + ":", value)

case_base.append({"name": "Urban Typhoon Flood Response 2026", "problem": new_case, "solution": final_solution})
print("\nNew case saved")
print("Updated case base:")
for case in case_base:
    print("-", case["name"])
