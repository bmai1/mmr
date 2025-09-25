import discogs_client
import random
import time

d = discogs_client.Client('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36')

while True:
    track_id = random.randint(1, 36000000)
    try:
        release = d.release(track_id)
        artist_names = ", ".join(artist.name for artist in release.artists)
        track = f"{release.title} - {artist_names}"
        print(track)
        with open("tracklist.txt", "a") as f:
            f.write(track + "\n")
        break

    except discogs_client.exceptions.HTTPError as e:
        if e.status_code == 404:
            continue
        elif e.status_code == 429:
            print("Rate limited")
            time.sleep(60)
            continue
        else:
            raise

    except Exception as e:
        raise