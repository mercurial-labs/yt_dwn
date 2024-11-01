from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_video(save_path, url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(' downloading: ', yt.title)

        ys = yt.streams.get_highest_resolution()
        downloaded_video = ys.download(output_path=save_path)
        return downloaded_video
    except Exception as e:
        print('Error occurred: ', e)
        return None
