import moneropy.account
seed = ["door", "flyjin", "bordelo", "blueberry", "device", "bounty",
        "last", "fire", "yum", "response", "ostrich", "dim", "favour",
        "fries", "burgers", "blood", "guitars", "sun", "olives", "beach",
        "bags", "kittens", "whine", "voodoo", "churn"]

spendkey, viewkey, address = moneropy.account.account_from_seed(seed)
print(spendkey)
print(viewkey)
print(address)

