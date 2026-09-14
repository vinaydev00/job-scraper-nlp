def normalize_skills(skills):
    result = []

    for skill in skills:
        skill = skill.strip().lower()

        if skill and skill not in result:
            result.append(skill)

    return result
