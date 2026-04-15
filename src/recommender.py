from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    songs: List[Dict] = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                song = {
                    'id': int(row['id']),
                    'title': row.get('title', '').strip(),
                    'artist': row.get('artist', '').strip(),
                    'genre': row.get('genre', '').strip(),
                    'mood': row.get('mood', '').strip(),
                    'energy': float(row['energy']) if row.get('energy') not in (None, '') else 0.0,
                    'tempo_bpm': int(float(row['tempo_bpm'])) if row.get('tempo_bpm') not in (None, '') else 0,
                    'valence': float(row['valence']) if row.get('valence') not in (None, '') else 0.0,
                    'danceability': float(row['danceability']) if row.get('danceability') not in (None, '') else 0.0,
                    'acousticness': float(row['acousticness']) if row.get('acousticness') not in (None, '') else 0.0,
                }
            except KeyError as e:
                raise ValueError(f"Missing expected column in CSV: {e}") from e
            except ValueError as e:
                raise ValueError(f"Invalid value when parsing CSV row {row}: {e}") from e

            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Returns: (score, reasons)
    """
    score = 0.0
    reasons: List[str] = []

    # Genre match (strong)
    if song["genre"] == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match
    if song["mood"] == user_prefs.get("favorite_mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity
    user_energy = user_prefs.get("target_energy", 0.5)
    song_energy = song.get("energy", 0.0)

    similarity = 1 - abs(song_energy - user_energy)
    similarity = max(0.0, similarity)

    score += similarity
    reasons.append(f"energy close to preference (+{similarity:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score every song and collect explanations. Keep original index to preserve stable tie-breaking.
    scored: List[Tuple[Dict, float, str, int]] = []
    for idx, song in enumerate(songs):
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "no matching reasons"
        scored.append((song, score, explanation, idx))

    # Sort by score (highest first). Use original index as secondary key to keep ordering stable on ties.
    scored_sorted = sorted(scored, key=lambda t: (-t[1], t[3]))

    # If k is not positive, return all results; otherwise return up to k results.
    if k is None or k <= 0:
        top = scored_sorted
    else:
        top = scored_sorted[:k]

    # Strip out the index before returning
    return [(song, score, explanation) for (song, score, explanation, _idx) in top]
