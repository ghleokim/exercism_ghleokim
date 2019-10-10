def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores, reverse=True)[0]


def personal_top_three(scores):
    if len(scores) >= 3:
        return sorted(scores, reverse=True)[:3]
    else:
        return sorted(scores, reverse=True)
    
