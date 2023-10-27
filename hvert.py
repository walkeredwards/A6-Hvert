# 1 = Reykjavik
# 2 = Akureyri

linkCities = {
    "Reykjavik" : 1,
    "Kopavogur" : 1,
    "Hafnarfjordur" : 1,
    "Reykjanesbaer" : 1,
    "Akureyri" : 2,
    "Gardabaer" : 1,
    "Mosfellsbaer" : 1,
    "Arborg" : 1,
    "Akranes" : 1,
    "Fjardabyggd" : 2,
    "Mulathing" : 2,
    "Seltjarnarnes" : 1,
}

def answer(c) -> int:
    """returns either a 1 or 2, 
    1 = Reykjavik
    2 = Akureyri

    Args:
        c (str): name of input city

    Returns:
        int: 1 or 2 indicating which city
    """
    return linkCities.get(c)

def solve() -> None:
    """main function for hvert problem
    """
    city = input()
    if answer(city) == 1:
        print("Reykjavik")
    else:
        print("Akureyri")

if __name__ == "__main__":
    solve()
