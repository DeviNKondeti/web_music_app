from flask import Flask, render_template, abort

app = Flask(__name__)

songs =songs = [
    {
        "id": 1,
        "title": "Despacito",
        "artist": "Luis Fonsi ft. Daddy Yankee",
        "spotify_url": "https://open.spotify.com/embed/track/6habFhsOp2NvshLv26DqMb"
    },
    {
        "id": 2,
        "title": "Love Me Like You Do",
        "artist": "Ellie Goulding",
        "spotify_url": "https://open.spotify.com/embed/track/0Cy7wt6IlRfBPHXXjmZbcP"
    },
    {
        "id": 3,
        "title": "I Wanna Be Yours",
        "artist": "Arctic Monkeys",
        "spotify_url": "https://open.spotify.com/embed/track/5XeFesFbtLpXzIVDNQP22n"
    },
    {
        "id": 4,
        "title": "Attention",
        "artist": "Charlie Puth",
        "spotify_url": "https://open.spotify.com/embed/track/5cF0dROlMOK5uNZtivgu50"
    },
    {
        "id": 5,
        "title": "Tadow",
        "artist": "Masego & FKJ",
        "spotify_url": "https://open.spotify.com/embed/track/51rPRW8NjxZoWPPjnRGzHw"
    },
    {
        "id": 6,
        "title": "Die for You",
        "artist": "The Weeknd & Ariana Grande",
        "spotify_url": "https://open.spotify.com/embed/track/4JNdwEfqwFRiAeEISC8RU8"
    },
    {
        "id": 7,
        "title": "Hips Don’t Lie",
        "artist": "Shakira ft. Wyclef Jean",
        "spotify_url": "https://open.spotify.com/embed/track/3ZFTkvIE7kyPt6Nu3PEa7V"
    },
    {
        "id": 8,
        "title": "Gasolina",
        "artist": "Daddy Yankee",
        "spotify_url": "https://open.spotify.com/embed/track/228BxWXUYQPJrJYHDLOHkj"
    },
    {
        "id": 9,
        "title": "Heat Waves",
        "artist": "Glass Animals",
        "spotify_url": "https://open.spotify.com/embed/track/3USxtqRwSYz57Ewm6wWRMp"
    },
    {
        "id": 10,
        "title": "Diet Mountain Dew",
        "artist": "Lana Del Rey",
        "spotify_url": "https://open.spotify.com/embed/track/20Dr6PsU4KweNgqDw7Vo0I"
    },
    {
        "id": 11,
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "spotify_url": "https://open.spotify.com/embed/track/0VjIjW4GlUZAMYd2vXMi3b"
    },
    {
        "id": 12,
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "spotify_url": "https://open.spotify.com/embed/track/7qiZfU4dY1lWllzX7mPBI3"
    },
    {
        "id": 13,
        "title": "Levitating",
        "artist": "Dua Lipa ft. DaBaby",
        "spotify_url": "https://open.spotify.com/embed/track/463CkQjx2Zk1yXoBuierM9"
    },
    {
        "id": 14,
        "title": "Watermelon Sugar",
        "artist": "Harry Styles",
        "spotify_url": "https://open.spotify.com/embed/track/6UelLqGlWMcVH1E5c4H7lY"
    },
    {
        "id": 15,
        "title": "Don't Start Now",
        "artist": "Dua Lipa",
        "spotify_url": "https://open.spotify.com/embed/track/3PfIrDoz19wz7qK7tYeu62"
    },
    {
        "id": 16,
        "title": "Sicko Mode",
        "artist": "Travis Scott",
        "spotify_url": "https://open.spotify.com/embed/track/2xLMifQCjDGFmkHkpNLD9h"
    },
    {
        "id": 17,
        "title": "God's Plan",
        "artist": "Drake",
        "spotify_url": "https://open.spotify.com/embed/track/6DCZcSspjsKoFjzjrWoCdn"
    },
    {
        "id": 18,
        "title": "Happier",
        "artist": "Marshmello ft. Bastille",
        "spotify_url": "https://open.spotify.com/embed/track/7KXjTSCq5nL1LoYtL7XAwS"
    },
    {
        "id": 19,
        "title": "Old Town Road",
        "artist": "Lil Nas X ft. Billy Ray Cyrus",
        "spotify_url": "https://open.spotify.com/embed/track/6u7jPi22kF8CTQ3rb9DHE7"
    },
    {
        "id": 20,
        "title": "One Love",
        "artist": "Blue",
        "spotify_url": "https://open.spotify.com/embed/track/7wGoVu4Dady5GV0Sv4UIsx"
    },
    {
        "id": 21,
        "title": "Someone Like You",
        "artist": "Adele",
        "spotify_url": "https://open.spotify.com/embed/track/4kflIGfjdZJW4ot2ioixTB"
    },
    {
        "id": 22,
        "title": "Night Changes",
        "artist": "One Direction",
        "spotify_url": "https://open.spotify.com/embed/track/3U4isOIWM3VvDubwSI3y7a"
    },
    {
        "id": 23,
        "title": "Closer",
        "artist": "The Chainsmokers ft. Halsey",
        "spotify_url": "https://open.spotify.com/embed/track/5QO79kh1waicV47BqGRL3g"
    },
    {
        "id": 24,
        "title": "Calm Down",
        "artist": "Rema",
        "spotify_url": "https://open.spotify.com/embed/track/34gCuhDGsG4bRPIf9bb02f"
    },
    {
        "id": 25,
        "title": "Swalla",
        "artist": "Jason Derulo ft. Nicki Minaj & Ty Dolla $ign",
        "spotify_url": "https://open.spotify.com/embed/track/0tgVpDi06FyKpA1z0VMD4v"
    },
    {
        "id": 26,
        "title": "Yummy",
        "artist": "Justin Bieber",
        "spotify_url": "https://open.spotify.com/embed/track/0LRbFwTS6j2fV4U6Z4qV5h"
    },
    {
        "id": 27,
        "title": "Roar",
        "artist": "Katy Perry",
        "spotify_url": "https://open.spotify.com/embed/track/6F5c58TMEs1byxUstkzVeM"
    },
    {
        "id": 28,
        "title": "Cheap Thrills",
        "artist": "Sia ft. Sean Paul",
        "spotify_url": "https://open.spotify.com/embed/track/7BPw9h8vCIX94N0rjFU12S"
    },
    {
        "id": 29,
        "title": "Desperado",
        "artist": "Raghav",
        "spotify_url": "https://open.spotify.com/embed/track/5J7YqY7Hg6N5X7KX8QcaNK"
    },
    {
        "id": 30,
        "title": "Heaven",
        "artist": "Bryan Adams",
        "spotify_url": "https://open.spotify.com/embed/track/7Ewz6bJ97vUqk5HdkvguFQ"
    },
    {
        "id": 31,
        "title": "People You Know",
        "artist": "Selena Gomez",
        "spotify_url": "https://open.spotify.com/embed/track/2GED7xRCADJQYkf9R4J3tZ"
    },
    {
        "id": 32,
        "title": "Falling",
        "artist": "Harry Styles",
        "spotify_url": "https://open.spotify.com/embed/track/1ZMiCix7XSAbfAJlEZWMCp"
    },
    {
        "id": 33,
        "title": "Under the Influence",
        "artist": "Chris Brown",
        "spotify_url": "https://open.spotify.com/embed/track/5IgjP7X4th6nMNDh4akUHb"
    }
]


@app.route('/')
def index():
    return render_template('index.html', songs=songs)

@app.route('/play/<int:song_id>')
def play(song_id):
    song = next((s for s in songs if s["id"] == song_id), None)
    if song:
        return render_template('play.html', song=song)
    abort(404)

# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug in production