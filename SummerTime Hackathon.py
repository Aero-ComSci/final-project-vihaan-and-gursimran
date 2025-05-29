word_categories = ["adjective", "noun", "verb", "place", "food", "animal", "weather", "emotion"]

def collect_words():
    words = {}
    for category in word_categories:
        print("Enter a", category + ":")
        words[category] = input()
    return words

def generate_story(words):
    story = "One hot summer day, I went to the " + words["place"] + ". The weather was " + words["weather"] + ", and I felt very " + words["emotion"] + ". Suddenly, I saw a " + words["adjective"] + " " + words["animal"] + " sitting on a beach chair. It was " + words["verb"] + " while eating some delicious " + words["food"] + ". I couldn't believe my eyes! I told my friend, and they said, 'Wow, what a " + words["noun"] + " kind of day!'"
    return story

user_words = collect_words()
print("Here is your summer adventure: " + generate_story(user_words))

