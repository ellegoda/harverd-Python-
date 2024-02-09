emojies = [
    {"name": ':1st_place_medal:', "emoji": '🥇'},
    {"name": ':2nd_place_medal:', "emoji": '🥈'},
    {"name": ':3rd_place_medal:', "emoji": '🥉'},
    {"name": ':money_bag:', "emoji": '💰'},
    {"name": ':smile_cat:', "emoji": '😸'},
    {"name": ':thumbs_up:', "emoji": '👍'},
    {"name": ':thumbsup:', "emoji": '👍'}
]


def search_emoji_by_name(emoji_name):
    for emoji in emojies:
        if emoji["name"].upper() == emoji_name.upper():
            return emoji
    return None


emoji_name = input("Item: ")

search_emoji = search_emoji_by_name(emoji_name)

if search_emoji:
    print("emoji:", search_emoji["emoji"])
else:
    print()
