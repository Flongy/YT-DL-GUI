import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import nametofont
import subprocess as sp
from io import BytesIO

import httpx
from PIL import Image, ImageTk


THUMBNAIL_WIDTH = 640
THUMBNAIL_HEIGHT = 360
SAVE_FOLDER = "media"


def get_info(link: str, download_thumbnail=True) -> (str, str, Image):
    proc = sp.run(["youtube-dl", "-e", "--get-thumbnail", "--get-duration", link],
                  encoding='utf-8',
                  capture_output=True)

    try:
        title, thumb_link, duration = proc.stdout.splitlines()[:3]
    except:
        return None

    thumb_bytes = BytesIO(httpx.get(thumb_link).content)
    thumb_ext = thumb_link.rsplit('.', 1)[-1]

    if download_thumbnail:
        thumbnail = Image.open(thumb_bytes, formats=['webp', 'jpeg', thumb_ext])
    else:
        thumbnail = None

    return title, duration, thumbnail


def download(link: str, quality: str = 'worst') -> bool:
    proc = sp.run(["youtube-dl", "-f", quality, "--restrict-filenames", link, "-o", f"{SAVE_FOLDER}/%(title)s.%(ext)s"])
    return proc.returncode == 0


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.pack(fill='x', expand=True)

        nametofont("TkDefaultFont").config(size=12, weight='bold')
        nametofont("TkTextFont").config(size=12)

        self.url_entry = tk.Entry(self)
        self.url_entry.pack(fill='x', padx=6, pady=2)
        self.url_entry.focus()

        self.check_button = tk.Button(self, text="CHECK", command=self.check)
        self.check_button.pack(fill='x', padx=6, pady=2)

        self.img = ImageTk.PhotoImage(Image.new('RGB', (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT), (255, 255, 255)))
        self.video_thumbnail = tk.Label(self, image=self.img)
        self.video_thumbnail.pack()

        self.video_title = tk.Label(self, text="Title", wraplength=THUMBNAIL_WIDTH)
        self.video_title.pack()

        self.video_duration = tk.Label(self, text="Duration")
        self.video_duration.pack()

        self.download_button = tk.Button(self, text="DOWNLOAD", command=self.download_cmd)
        self.download_button.pack(side='bottom', fill='x', padx=6, pady=2)

        self.quality_combo = ttk.Combobox(self)
        self.quality_combo['values'] = ('bestvideo+bestaudio', 'best', 'bestvideo', 'bestaudio', 'worst')
        self.quality_combo.current(0)
        self.quality_combo.pack(side='bottom', fill='x', padx=6, pady=2)

        self.pack()

    def check(self):
        video_info = get_info(self.url_entry.get())
        if video_info is None:
            messagebox.showerror("Video Info Error", "Could not retrieve media info.")
            return

        title, duration, img = video_info

        width, height = img.size
        width = int(width * (THUMBNAIL_HEIGHT / height))
        height = THUMBNAIL_HEIGHT

        img = img.resize((width, height))
        self.img = ImageTk.PhotoImage(img)
        self.video_thumbnail["image"] = self.img
        self.video_thumbnail.pack()

        self.video_title["text"] = title
        self.video_title.pack()

        self.video_duration["text"] = duration
        self.video_duration.pack()

    def download_cmd(self):
        success = download(self.url_entry.get(), self.quality_combo.get())
        if success:
            messagebox.showinfo("Complete", "The download is complete!")
        else:
            messagebox.showerror("Error", "Failed to download the media.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Media Downloader")
    app = Application(master=root)
    app.mainloop()
