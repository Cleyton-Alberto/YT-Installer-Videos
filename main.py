import flet as ft
from functions.download_functions import downloadVideo, downloadAudio, downloadVideoAudio
from style.widgets import styled_textfield, styled_button
from style import colors as c

def main_page(page: ft.Page):
    page.title = 'YTInstaller'
    page.bgcolor = c.PAGE_BG
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    url_field = styled_textfield()
    
    status_text = ft.Text(color=ft.Colors.WHITE)
    progress_bar = ft.ProgressBar(width=600, bgcolor=ft.Colors.RED_ACCENT, visible=False)
    progress_bar_column = ft.Column(spacing=5, controls=[status_text, progress_bar])
    
    async def start_download(download_func):
        url = url_field.value.strip()
        if not url:
            status_text.value = "Please Insert URL"
            progress_bar.visible = False
            page.update()
            return
        
        status_text.value = "Loading..."
        progress_bar.value = None
        progress_bar.visible = True
        page.update()
        
        await download_func(url, status_text, progress_bar, page)
        
        progress_bar.value = 0
        status_text.value = "Done!"
        page.update()
    
    async def download_video_only_click(e):
        await start_download(downloadVideo)
            
    async def download_audio_only_click(e):
        await start_download(downloadAudio)
        
    async def download_video_audio_click(e):
        await start_download(downloadVideoAudio)
        
    main_layout = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            progress_bar_column,
            
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

ft.run(main_page)