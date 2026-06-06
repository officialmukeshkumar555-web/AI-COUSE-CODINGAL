import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Built-in Movie Dataset
movies = [
    ["Inception", "Action", 8.8, "A thief enters dreams to steal secrets."],
    ["Interstellar", "Sci-Fi", 8.7, "A team travels through a wormhole to save humanity."],
    ["The Dark Knight", "Action", 9.0, "Batman battles the Joker in Gotham City."],
    ["Forrest Gump", "Drama", 8.8, "A man experiences key moments in American history."],
    ["Toy Story", "Animation", 8.3, "Toys come alive when humans are away."],
    ["Finding Nemo", "Animation", 8.2, "A fish searches for his lost son."],
    ["The Shawshank Redemption", "Drama", 9.3, "A prisoner maintains hope through adversity."],
    ["Avengers: Endgame", "Action", 8.4, "Heroes unite to save the universe."],
    ["Titanic", "Romance", 7.9, "A tragic love story aboard a doomed ship."],
    ["The Pursuit of Happyness", "Drama", 8.0, "A struggling father fights for a better future."]
]

df = pd.DataFrame(
    movies,
    columns=["Series_Title", "Genre", "IMDB_Rating", "Overview"]
)

# Available Genres
genres = sorted(df["Genre"].unique())

# Loading Animation
def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
    print()

# Sentiment Label
def senti(p):
    if p > 0:
        return "Positive 😊"
    elif p < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Movie Recommendation Function
def recommend(genre=None, mood=None, rating=None, n=5):
    d = df.copy()

    if genre:
        d = d[d["Genre"].str.contains(genre, case=False)]

    if rating is not None:
        d = d[d["IMDB_Rating"] >= rating]

    if d.empty:
        return "No suitable movie recommendations found."

    recommendations = []

    for _, row in d.iterrows():
        polarity = TextBlob(row["Overview"]).sentiment.polarity

        if mood:
            if polarity >= 0:
                recommendations.append(
                    (row["Series_Title"], polarity)
                )
        else:
            recommendations.append(
                (row["Series_Title"], polarity)
            )

        if len(recommendations) == n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

# Display Recommendations
def show(recs, name):
    print(Fore.YELLOW + f"\n🍿 Movie Recommendations for {name}:\n")

    for i, (title, polarity) in enumerate(recs, start=1):
        print(
            f"{Fore.CYAN}{i}. 🎥 {title} "
            f"(Polarity: {polarity:.2f}, {senti(polarity)})"
        )

# Genre Input
def get_genre():
    print(Fore.GREEN + "Available Genres:\n")

    for i, g in enumerate(genres, start=1):
        print(f"{Fore.CYAN}{i}. {g}")

    while True:
        choice = input(
            Fore.YELLOW + "\nEnter Genre Number: "
        ).strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(genres):
                return genres[choice - 1]

        print(Fore.RED + "Invalid choice. Try again.")

# Rating Input
def get_rating():
    while True:
        choice = input(
            Fore.YELLOW +
            "Enter minimum IMDB rating (7.5 - 9.5) or 'skip': "
        ).strip()

        if choice.lower() == "skip":
            return None

        try:
            rating = float(choice)

            if 7.5 <= rating <= 9.5:
                return rating

            print(Fore.RED + "Rating out of range.")

        except ValueError:
            print(Fore.RED + "Invalid input.")

# Main Program
print(Fore.BLUE + "🎥 Welcome to AI Movie Recommendation Assistant 🎥\n")

name = input(Fore.YELLOW + "Enter your name: ").strip()

print(Fore.GREEN + f"\nHello {name}! Let's find a movie for you.\n")

genre = get_genre()

mood = input(
    Fore.YELLOW +
    "\nHow are you feeling today? "
).strip()

print(Fore.BLUE + "\nAnalyzing your mood", end="")
dots()

mood_polarity = TextBlob(mood).sentiment.polarity

if mood_polarity > 0:
    mood_type = "Positive 😊"
elif mood_polarity < 0:
    mood_type = "Negative 😞"
else:
    mood_type = "Neutral 😐"

print(
    Fore.GREEN +
    f"Detected Mood: {mood_type} "
    f"(Polarity: {mood_polarity:.2f})\n"
)

rating = get_rating()

print(Fore.BLUE + "\nFinding movies", end="")
dots()

recommendations = recommend(
    genre=genre,
    mood=mood,
    rating=rating,
    n=5
)

if isinstance(recommendations, str):
    print(Fore.RED + recommendations)
else:
    show(recommendations, name)

while True:
    again = input(
        Fore.YELLOW +
        "\nWould you like more recommendations? (yes/no): "
    ).lower()

    if again == "yes":
        recommendations = recommend(
            genre=genre,
            mood=mood,
            rating=rating,
            n=5
        )

        if isinstance(recommendations, str):
            print(Fore.RED + recommendations)
        else:
            show(recommendations, name)

    elif again == "no":
        print(
            Fore.GREEN +
            f"\nEnjoy your movies, {name}! 🎬🍿"
        )
        break

    else:
        print(Fore.RED + "Please enter yes or no.")