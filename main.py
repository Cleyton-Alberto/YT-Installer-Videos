import flet as ft
from functions.download_functions import downloadVideo, downloadAudio, downloadVideoAudio
from style.widgets import styled_textfield, styled_button
from style import colors as c
import threading

def main(page: ft.Page):
    page.title = 'Download YT Videos'
    page.bgcolor = c.PAGE_BG
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    url_field = styled_textfield()
    
    status_text = ft.Text('Loading...', size=16, color=ft.Colors.WHITE)
    progress_bar = ft.ProgressBar(width=600, bgcolor=ft.Colors.RED_ACCENT)
    progress_column = ft.Column(spacing=5, controls=[status_text, progress_bar])
    
    def run_download(download_func):
        if progress_column not in main_layout.controls:
            main_layout.controls.insert(0, progress_column)
            page.update()

        url = url_field.value
        status_text.value = "Loading..."
        progress_bar.value = 1
        page.update()

        def task():
            try:
                download_func(url)
                status_text.value = "Done!"
                progress_bar = 0
                page.update()
            except Exception as e:
                status_text.value = f"Erro: {e}"
                page.update()
            finally:
                page.update()

        threading.Thread(target=task).start()
    
    def download_video_only_click(e):
       run_download(downloadVideo)
        
    def download_audio_only_click(e):
        run_download(downloadAudio)
        
    def download_video_audio_click(e):
        run_download(downloadVideoAudio)
        


    main_layout = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[url_field]
            ),
            ft.Container(
                width=350,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        styled_button("Video", icon=ft.Icons.VIDEOCAM, bgcolor=c.BTN_VIDEO, on_click=download_video_only_click),
                        styled_button("Audio", icon=ft.Icons.MUSIC_NOTE, bgcolor=c.BTN_AUDIO, on_click=download_audio_only_click),
                        styled_button("Video + Audio", icon=ft.Icons.VIDEOCAM, bgcolor=c.BTN_VIDEO_AUDIO, on_click=download_video_audio_click)
                    ]
                )
            )
        ]
    )

    page.add(main_layout)

ft.run(main)