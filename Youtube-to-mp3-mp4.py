from pytube import YouTube

def download_youtube_video(url, output_path, download_as_mp3=False):
    try:
        yt = YouTube(url)

        if download_as_mp3:
            # Get the highest quality audio stream (MP3)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path)
            print(f"Downloaded audio from '{yt.title}' as MP3 to {output_path}")
        else:
            # Get the highest resolution video stream
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path)
            print(f"Downloaded video '{yt.title}' as MP4 to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output path (e.g., 'video.mp4' or 'audio.mp3'): ")
    download_as_mp3 = input("Download as MP3? (yes or no): ").lower() == "yes"

    download_youtube_video(video_url, output_path, download_as_mp3)
