# TikTok Unreposter

> Automatically detects TikTok's repost button, clicks it to remove the repost, and moves to the next video — without relying on fixed screen coordinates.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automation-00A67E?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge\&logo=windows\&logoColor=white)

A lightweight Python automation tool for removing TikTok reposts in bulk.

Instead of clicking a fixed location, the program uses **OpenCV template matching** to locate the repost button on the screen. This allows it to handle small changes in the button's position between videos.

---

## ✨ Features

* 🔍 **Automatic button detection**

  * Uses OpenCV to locate the repost button on screen.

* 🖱️ **Automatic clicking**

  * Moves the mouse to the detected button and clicks it.

* ⬇️ **Automatic navigation**

  * Presses `↓` to move to the next TikTok video.

* 🛡️ **Anti-double-click protection**

  * Waits for the button to disappear/change after clicking before continuing.
  * Prevents accidentally reposting the video again.

* 🎯 **No fixed coordinates**

  * The button can move slightly between videos without breaking the automation.

* ⚙️ **Configurable**

  * Detection confidence, delays, search interval, and other settings can be adjusted.

* 🚨 **Emergency stop**

  * PyAutoGUI's failsafe allows you to stop the program by moving the mouse to the top-left corner.

---

## 🖥️ How It Works

The program follows this process:

```text
┌──────────────────────┐
│      Start Script    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Capture Screen       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Find Repost Button   │
│     Using OpenCV     │
└──────────┬───────────┘
           ↓
      Button Found?
        /       \
      No         Yes
      ↓           ↓
    Wait      Move Mouse
                  ↓
               Click
                  ↓
        Wait for Button
        to Change/Disappear
                  ↓
             Press ↓
                  ↓
          Next Video Loads
                  ↓
              Repeat
```

The important difference from a traditional autoclicker is that the program **doesn't assume the button is always at the same coordinates**.

---

# 📦 Requirements

* Windows
* Python 3.x
* TikTok opened in a browser
* A screenshot/template of the repost button

### Python packages

The project uses:

* [PyAutoGUI](https://pyautogui.readthedocs.io/) — mouse and keyboard automation
* [OpenCV](https://opencv.org/) — image detection
* [NumPy](https://numpy.org/) — image processing
* [Pillow](https://python-pillow.org/) — screenshot/image handling

---

# 🚀 Installation

## 1. Install Python

Download and install Python from:

https://www.python.org/

During installation, make sure to enable:

```text
☑ Add Python to PATH
```

Verify the installation:

```bash
python --version
```

---

## 2. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tiktok-unreposter.git
cd tiktok-unreposter
```

Or download the repository as a ZIP and extract it.

---

## 3. Install dependencies

Run:

```bash
pip install pyautogui opencv-python pillow numpy
```

---

# 🖼️ Creating `button.png`

The program needs an image template of the button it should detect.

Open TikTok and find a video where the repost button is visible.

Take a screenshot and crop it so that it contains **only the relevant button/icon**.

Your project should look like:

```text
tiktok-unreposter/
│
├── unrepost.py
├── button.png
└── README.md
```

### Template tips

For the best detection:

* Crop the button closely.
* Avoid including large parts of the surrounding UI.
* Use a clear screenshot.
* Keep the browser zoom consistent.
* Use the same display scaling when possible.

A good template should look roughly like:

```text
┌─────────────┐
│             │
│      ↻      │
│             │
└─────────────┘
```

rather than an entire screenshot of the TikTok interface.

---

# ▶️ Usage

Open TikTok and navigate to your reposted videos.

Then run:

```bash
python unrepost.py
```

The program will wait a few seconds before starting.

During the startup delay, make sure TikTok is the active window.

The program will then:

1. Search for the repost button.
2. Move the mouse to it.
3. Click it.
4. Wait for TikTok to update the button.
5. Press `↓`.
6. Wait for the next video.
7. Repeat.

---

# ⚙️ Configuration

The main settings are located near the top of `unrepost.py`.

```python
BUTTON_IMAGE = "button.png"

CONFIDENCE = 0.80

SEARCH_INTERVAL = 0.25

AFTER_CLICK_WAIT = 1.2

BUTTON_CHANGE_TIMEOUT = 3.0

NEXT_VIDEO_WAIT = 1.5

START_DELAY = 3
```

### `CONFIDENCE`

Controls how closely the screen needs to match your template.

```python
CONFIDENCE = 0.80
```

Higher values are stricter:

```text
0.90 → Very strict
0.85 → Strict
0.80 → Recommended starting point
0.75 → More tolerant
0.65 → Very tolerant / potentially inaccurate
```

If the program is detecting the wrong thing, increase this value.

---

### `SEARCH_INTERVAL`

Controls how frequently the program checks for the button.

```python
SEARCH_INTERVAL = 0.25
```

Lower values search more frequently.

Higher values reduce CPU usage.

---

### `AFTER_CLICK_WAIT`

Minimum time to wait after clicking.

```python
AFTER_CLICK_WAIT = 1.2
```

If TikTok is slow to update, increase this value.

---

### `BUTTON_CHANGE_TIMEOUT`

Maximum amount of time the program waits for the button to disappear or change after clicking.

```python
BUTTON_CHANGE_TIMEOUT = 3.0
```

This is part of the protection against accidentally clicking the same button twice.

---

### `NEXT_VIDEO_WAIT`

Time to wait after pressing `↓`.

```python
NEXT_VIDEO_WAIT = 1.5
```

If videos take longer to load, increase this value.

---

# 🛡️ Safety

This script controls your mouse and keyboard automatically, so **test it carefully before letting it run for a large number of videos**.

The program includes PyAutoGUI's emergency failsafe:

```python
pyautogui.FAILSAFE = True
```

If something goes wrong, move your mouse to the **top-left corner of the screen**.

PyAutoGUI will trigger its failsafe and stop the automation.

### Recommended first test

Start with only a few videos:

```text
3–5 videos
   ↓
Verify everything works
   ↓
Increase the number of videos
```

Do not leave the script unattended until you've confirmed that it behaves correctly with your browser/window setup.

---

# 🧠 Why Not Use a Normal Autoclicker?

A traditional autoclicker usually works with a fixed coordinate:

```text
Click → (1420, 650)
```

That becomes unreliable when TikTok moves the interface slightly:

```text
Video 1 → button at Y = 650
Video 2 → button at Y = 663
Video 3 → button at Y = 641
```

This project instead searches for the button visually:

```text
Screen
  ↓
Screenshot
  ↓
OpenCV
  ↓
Find button
  ↓
Calculate center
  ↓
Move mouse
  ↓
Click
```

This makes it much more tolerant of small UI movements.

---

# 🐛 Troubleshooting

## `button.png was not found`

Make sure your files are arranged like this:

```text
tiktok-unreposter/
├── unrepost.py
└── button.png
```

Then run the script from that directory.

---

## Button isn't detected

Try lowering:

```python
CONFIDENCE = 0.80
```

to:

```python
CONFIDENCE = 0.75
```

Also make sure your `button.png` matches the button's appearance and size on your current screen.

---

## It detects the wrong thing

Increase the confidence:

```python
CONFIDENCE = 0.85
```

or:

```python
CONFIDENCE = 0.90
```

A smaller and more precise `button.png` can also improve accuracy.

---

## It moves to the correct button but clicks twice

The script includes protection against this.

If TikTok is particularly slow, increase:

```python
AFTER_CLICK_WAIT = 2.0
```

and/or:

```python
BUTTON_CHANGE_TIMEOUT = 4.0
```

---

## It moves to the next video too quickly

Increase:

```python
NEXT_VIDEO_WAIT = 2.0
```

You can increase it further if your connection or browser takes longer to load videos.

---

# 📁 Project Structure

```text
tiktok-unreposter/
│
├── unrepost.py       # Main automation script
├── button.png        # Button detection template
└── README.md         # Documentation
```

---

# ⚠️ Disclaimer

This project is provided for educational and personal automation purposes.

TikTok's interface and terms may change over time, which can cause the script to stop working or behave unexpectedly.

Use automation responsibly and review TikTok's current rules before using automated interaction with the platform.

The author is not responsible for account restrictions, unexpected clicks, or other consequences resulting from the use of this software.

---

# 🤝 Contributing

Contributions are welcome!

If you find a bug or have an improvement:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/my-improvement
```

3. Make your changes.
4. Commit them.

```bash
git commit -m "Add my improvement"
```

5. Push the branch.

```bash
git push origin feature/my-improvement
```

6. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for more information.

---

## ⭐ Support the Project

If this project helped you, consider giving the repository a ⭐ on GitHub.

Issues, suggestions, and pull requests are welcome.
