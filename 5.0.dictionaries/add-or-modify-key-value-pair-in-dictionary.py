sports_team_roosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New Yor Giants": ["Eli Manning", "Odell Beckham"]
}

# print(sports_team_roosters["Pittsburgh Steelers"])
sports_team_roosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
# print(sports_team_roosters["Pittsburgh Steelers"])
# print(sports_team_roosters)

sports_team_roosters["New Yor Giants"] = ["Eli Manning"]
print(sports_team_roosters)

video_game_options = {}
#video_game_options = dict()

video_game_options["subtitles"] = True
video_game_options["difficult"] = "Medium"
video_game_options["volume"] = 7
print(video_game_options)

video_game_options["subtitles"] = False
video_game_options["difficult"] = "Hard"
print(video_game_options)

words = ["danger", "beware", "danger"]

def count_words(words):
    counts = {}
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    return counts

print(count_words(words))