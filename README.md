🎬 YTInstaller

YTInstaller is a simple open-source application that allows users to download:

📹 Video (without audio)

🎧 Audio only

🎥 Video with audio

from publicly accessible YouTube content through an easy-to-use graphical interface.

⚠️ Important Notice

This project DOES NOT include FFmpeg.

FFmpeg is a third-party tool required for media processing.
Due to licensing reasons, it must be installed manually by the user.

YTInstaller only detects and uses an existing FFmpeg installation available on your system.

📦 Requirements

Before running the application, make sure you have installed:

Python 3.10 or newer

FFmpeg (must be available in your system PATH)

🔧 Installing FFmpeg

Download FFmpeg from the official website:

👉 https://ffmpeg.org/download.html

After downloading:

Windows

Extract the downloaded archive.

Move the folder to a permanent location (example: C:\ffmpeg).

Add the bin folder to your System PATH:

C:\ffmpeg\bin


Restart your terminal.

To verify installation:

ffmpeg -version

Linux (Debian/Ubuntu)
sudo apt install ffmpeg

macOS (Homebrew)
brew install ffmpeg

▶️ Running the Project

Clone the repository:

git clone https://github.com/your-username/ytinstaller.git
cd ytinstaller


Install dependencies:

pip install -r requirements.txt


Run the application:

python main.py

⚖️ Legal Disclaimer

This software is a technical tool.

It does not host, store, or distribute any media content.

It does not bypass authentication, paywalls, or access controls.

Users are solely responsible for how they use this software.

You must comply with:

YouTube’s Terms of Service

Your local copyright laws

Any applicable regulations in your country

The developers of this project assume no liability for misuse.

🔗 Third-Party Software

This project uses:

yt-dlp
 — licensed under permissive terms (Unlicense/MIT-like).

FFmpeg — developed by the FFmpeg project (not distributed with this application).

FFmpeg is not bundled, redistributed, or modified by this project.

📜 License

This project is licensed under the MIT License.

See the LICENSE file for full details.

💡 Project Purpose

This project was created for:

Educational use

Personal workflow automation

Open-source learning

Interface experimentation with Flet

It is not intended to facilitate piracy or copyright infringement.