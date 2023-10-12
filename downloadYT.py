import os
from pytube import YouTube, Search
import ffmpeg

# YouTube動画をダウンロードする関数

class downloadYT():
    def __init__(self):
        pass

    def url_download(self,url,output_dir):
        video_file = self.download_youtube_video(url, output_dir)
        mp3_file = self.convert_to_mp3(os.path.join( output_dir, video_file), output_dir)
        musicInfo = {
            "musicName" : self.name,
            "musicAuthor" : self.channelName,
            "thumbnail_url":self.thumbnail_url
        }
        return musicInfo
    
    def search(self,keyword):
        search = Search(keyword)
        # 最初の結果を取得
        result = {}
        for i in range(6):
            video = search.results[i]
            title = video.title
            thumbnail_url = video.thumbnail_url
            author = video.author
            url = "https://www.youtube.com/watch?v=" + video.video_id
            result[i] = {
                "title":title,
                "thumbnail_url":thumbnail_url,
                "author":author,
                "url":url
            }
        return result
        



    def download_youtube_video(self,url, output_dir):
        yt = YouTube(url)
        self.channelName = yt.author
        self.thumbnail_url = yt.thumbnail_url
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=output_dir)
        return video_stream.default_filename

    # MP4をMP3に変換する関数
    def convert_to_mp3(self,input_path, output_dir):
        video_name = os.path.basename(input_path)
        mp3_name = os.path.splitext(video_name)[0] + ".mp3"
        self.name = os.path.splitext(video_name)[0]
        mp3_output_path = os.path.join(output_dir, mp3_name)

        input_audio = ffmpeg.input(input_path)
        output_audio = ffmpeg.output(input_audio,mp3_output_path)
        ffmpeg.run(output_audio)
        os.remove(input_path)
        return mp3_output_path



# if __name__ == "__main__":
#     youtube_url = "https://www.youtube.com/watch?v=Ci_zad39Uhw&pp=ygUP44GX44GQ44KM44GG44GE"

#     output_directory = "audio"

#     # YouTube動画をダウンロード
#     video_file = download_youtube_video(youtube_url, output_directory)

#     # MP3に変換
#     mp3_file = convert_to_mp3(os.path.join( output_directory, video_file), output_directory)

#     print(f"MP3は {mp3_file} として保存されました。")
