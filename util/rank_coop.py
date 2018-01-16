from collections import defaultdict

SEED = [
    ['Facebook', ['Facebook', 'Google', 'Figma', 'Coursera', 'Quora', 'Microsoft']],
    ['Yelp', ['Yelp', 'Monstercat', 'Noom', 'Klick', 'Sequence', 'Test']],
    ['Yelp', ['Snapchat', 'Facebook', 'Google', 'Uber', 'Pivotal']],
    ['Yelp', ['Snapchat', 'Facebook', 'Google', 'Uber', 'Pivotal']],
    ['Yelp', ['Snapchat', 'Facebook', 'Google', 'Uber', 'Pivotal']],
];


def rank_companies(companies):
    rankings = defaultdict(int)
    # Cleanse data
    for i, entry in enumerate(companies):
        # REMOVE DUPLICATES
        # People go back for different reasons: can't find a coop, or really
        # liked it. Since we don't have enough signal, we won't interpret the
        # results differently
        companies[i][1] = list(set(entry[1]))

    for i, entry in enumerate(companies):
        # Winner
        rankings[entry[0]] += 25
        for _, loser in enumerate(entry[1]):
            if loser != entry[0]:
                # LOSER
                rankings[loser] -= 25 / (len(entry[1]) - 1)

    print(rankings)

rank_companies(SEED)
