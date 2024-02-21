from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=-DrRBQxPNUg'

yt = YouTube(video_url)

# Video stream.
stream = yt.streams.get_highest_resolution()

# Audio only stream.
audio_stream = yt.streams.get_audio_only()
audio_stream.download()

output_path = 'downloads/'
stream.download(output_path, 'video.mp4')