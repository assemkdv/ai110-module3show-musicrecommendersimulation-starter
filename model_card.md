# Model Card: Music Recommender Simulation

## 1. Model Name  

VibeFinder 1.0  

---

## 2. Intended Use  

This recommender is designed to suggest songs based on a user’s preferences, such as genre, mood, and energy level.  

It assumes that users know what kind of music they like and can describe it using simple features like “happy,” “chill,” or “high energy.”  

This system is mainly for classroom exploration and learning how recommendation systems work. It is not intended for real users or real-world music platforms.  

---

## 3. How the Model Works  

The model looks at features of each song, including genre, mood, and energy.  

It also looks at the user’s preferences, such as their favorite genre, preferred mood, and target energy level.  

Each song gets a score based on:
- Whether the genre matches the user’s favorite genre  
- Whether the mood matches  
- How close the song’s energy is to the user’s preferred energy  

Songs with higher scores are ranked higher, and the top songs are recommended.  

Compared to the starter logic, I added clearer scoring rules and explanations so the user can see why a song was recommended.  

---

## 4. Data  

The model uses a small dataset of about 18 songs stored in a CSV file.  

The dataset includes different genres such as pop, lofi, rock, hip hop, and classical, along with moods like happy, chill, intense, and relaxed.  

I expanded the dataset by adding more songs with different genres and moods.  

However, the dataset is still limited and does not include many music styles, languages, or cultural influences.  

---

## 5. Strengths  

The system works well for clear and consistent user preferences.  

For example, the “High-Energy Pop” profile produces upbeat pop songs, and the “Chill Lofi” profile produces calm, relaxing tracks.  

The scoring system correctly captures patterns like matching genre and energy level.  

In many cases, the recommendations matched what I would expect based on the user’s preferences.  

---

## 6. Limitations and Bias  

To test the system, I reduced the importance of genre and increased the importance of energy. The genre score was lowered from +2.0 to +1.0, while the energy similarity score was doubled.

After applying this change, the recommendations shifted toward songs with higher energy levels, even if they did not match the user's preferred genre. This made the recommendations more diverse but sometimes less precise in terms of genre.

This experiment shows that the system is highly sensitive to feature weights, and small changes can significantly impact the results.

---

## 7. Evaluation

I tested the recommender system using several different user profiles, including "High-Energy Pop," "Chill Lofi," "Intense Rock," and a conflicting profile with mixed preferences (pop + sad + high energy).

For the "High-Energy Pop" profile, the system correctly recommended upbeat pop songs with high energy levels. The results felt accurate and matched expectations.

For the "Chill Lofi" profile, the system returned low-energy, relaxing tracks, mostly from the lofi genre. This showed that the system can successfully adjust to different moods and energy levels.

For the "Intense Rock" profile, the top recommendation was a high-energy rock song, which confirmed that the system prioritizes both genre and energy effectively.

One surprising result was that the song "Gym Hero" appeared frequently across multiple profiles, even when it did not fully match all preferences. This happens because the song has very high energy, and energy is a strong factor in the scoring system.

In the conflicting profile (pop + sad + high energy), the system struggled to find perfect matches and instead recommended songs based on genre and energy only. This shows that the system cannot fully resolve conflicting preferences and relies on the strongest available signals.

Overall, the system performs well for clear user preferences but shows limitations when preferences are ambiguous or contradictory.

---

## 8. Future Work  

To improve the model, I would:

- Add more songs to increase variety and better represent different music styles  
- Include more features such as lyrics, tempo preferences, or listening history  
- Improve how the system handles conflicting preferences so recommendations feel more balanced  

---

## 9. Personal Reflection  

Through this project, I learned how recommender systems use simple rules and data to make suggestions. One important thing I discovered is how much the results depend on feature weights. Even small changes can completely change the recommendations.

My biggest learning moment was realizing how sensitive the scoring system is. For example, when I changed the weight of energy, the recommendations changed a lot, even though the rest of the system stayed the same.

Using AI tools like Copilot and Claude helped me work faster, especially when writing code and structuring functions. However, I had to double-check their suggestions to make sure they matched my logic and assignment requirements. Sometimes the AI gave correct code, but it did not fully match what I needed, so I had to understand and adjust it.

One surprising thing was how even a simple algorithm could feel like a real recommendation system. Even though it only used a few features like genre, mood, and energy, the results often felt accurate and meaningful.

If I extended this project, I would add more data and features, like user listening history or lyrics. I would also improve how the system handles conflicting preferences so the recommendations feel more balanced.