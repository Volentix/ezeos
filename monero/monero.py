import moneropy.account
seed = ["vixen", "eavesdrop", "fuming", "aching", "react", "waffle",
        "nowhere", "water", "upon", "scoop", "aztec", "sunken", "diplomat",
        "salads", "rift", "inkling", "null", "testing", "sixteen", "return",
        "kitchens", "narrate", "moisture", "nucleus", "testing"]

spendkey, viewkey, address = moneropy.account.account_from_seed(seed)

