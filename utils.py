import json


def load_candidates_from_json():
    """
    Загрузка JSON-файла
    :return:
    """
    with open("templates/candidates.json", "r", encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    """
    Вернет кандидата по candidate_id
    :param candidate_id:
    :return:
    """
    candidates = load_candidates_from_json()
    return candidates[candidate_id - 1]


def get_candidates_by_name(candidate_name):
    """
    Вернёт кандитдата по candidate_name
    :param candidate_name:
    :return:
    """
    candidates = load_candidates_from_json()
    result = []
    for i in candidates:
        words = i["name"].lower().split()
        if candidate_name.lower() in words:
            result.append(i)
    return result


def get_candidates_by_skill(skill_name):
    """
    Вернет кандидатов по навыку
    :param skill_name:
    :return:
    """
    candidates = load_candidates_from_json()
    result = []
    for i in candidates:
        words = i["skills"].lower().split(",")
        g_words = []
        for j in words:
            g_words.append(j.strip())
        if skill_name.lower() in g_words:
            result.append(i)
    return result
