word_categories = ["adjective", "noun", "verb", "place", "food", "animal", "weather", "emotion", "sound", "exclamation"]

def collect_words():
    words = {}
    for category in word_categories:
        print("Enter a", category + ":")
        words[category] = input()
    return words

def generate_story(words):
    story = "One " + words["weather"] + " summer day, I went to the " + words["place"] + ". "
    story = story + "I was feeling " + words["emotion"] + " when suddenly I heard a loud '" + words["sound"] + "'! "
    story = story + "I turned and saw a " + words["adjective"] + " " + words["animal"] + " wearing sunglasses and sipping on " + words["food"] + ". "
    story = story + "It was " + words["verb"] + " like it owned the place. "
    story = story +"I couldn't believe my eyes, so I yelled '" + words["exclamation"] + "'! "
    story = story + "My friend laughed and said, 'This is the most " + words["noun"] + " kind of summer ever!'"

    return story

user_words = collect_words()
print("Here is your summer adventure: " + generate_story(user_words))

