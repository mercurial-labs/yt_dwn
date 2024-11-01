from pytube import Playlist
from downloader import download_video


url = 'https://www.youtube.com/watch?v=VclPWSbLs2E&list=PLWpVvJ8o7wzySAIgpmVc2JYfCcapDmT8h&ab_channel=BlueYNC'
save_path = 'D:/code/youtube_playlist_downloader/destination'

# Retrieve URLs of videos from playlist
playlist = Playlist(url)
print('Number Of Videos In playlist: %s' % len(playlist.video_urls))

urls = []
for url in playlist:
    downloaded_video = download_video(save_path, url)


print(urls)

print('Attempting to download first video.')
