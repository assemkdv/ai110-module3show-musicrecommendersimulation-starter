"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def run_profile(name, user_prefs, songs):
    print(f"\n===== {name} =====\n")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}\n")


def main():
    songs = load_songs("data/songs.csv")

    # Profile 1: High-Energy Pop
    profile1 = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9
    }

    # Profile 2: Chill Lofi
    profile2 = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.3
    }

    # Profile 3: Intense Rock
    profile3 = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95
    }

    # Profile 4: Edge case (conflicting preferences)
    profile4 = {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.9
    }

    run_profile("High-Energy Pop", profile1, songs)
    run_profile("Chill Lofi", profile2, songs)
    run_profile("Intense Rock", profile3, songs)
    run_profile("Conflicting (Pop + Sad + High Energy)", profile4, songs)


if __name__ == "__main__":
    main()