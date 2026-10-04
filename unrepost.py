import pyautogui
import cv2
import numpy as np
import time

# -----------------------------
# SETTINGS
# -----------------------------

BUTTON_IMAGE = "button.png"

# How accurately the image must match.
# Higher = stricter.
CONFIDENCE = 0.80

# Time between attempts to find the button
SEARCH_INTERVAL = 0.2

# Time to wait after clicking the button
AFTER_CLICK_WAIT = 0.7

# Time to wait after going to the next video
NEXT_VIDEO_WAIT = 1.5

# Safety delay when starting
START_DELAY = 3


# -----------------------------
# LOAD BUTTON IMAGE
# -----------------------------

template = cv2.imread(BUTTON_IMAGE)

if template is None:
    print("ERROR: Could not find button.png")
    print("Make sure button.png is in the same folder as this script.")
    input("Press Enter to exit...")
    exit()

template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

template_height, template_width = template_gray.shape


# -----------------------------
# FIND BUTTON
# -----------------------------

def find_button():

    screenshot = pyautogui.screenshot()

    screenshot = np.array(screenshot)

    screenshot = cv2.cvtColor(
        screenshot,
        cv2.COLOR_RGB2BGR
    )

    screenshot_gray = cv2.cvtColor(
        screenshot,
        cv2.COLOR_BGR2GRAY
    )

    result = cv2.matchTemplate(
        screenshot_gray,
        template_gray,
        cv2.TM_CCOEFF_NORMED
    )

    _, max_value, _, max_location = cv2.minMaxLoc(result)

    print(f"Match: {max_value:.2f}")

    if max_value >= CONFIDENCE:

        x = max_location[0]
        y = max_location[1]

        center_x = x + template_width // 2
        center_y = y + template_height // 2

        return center_x, center_y, max_value

    return None


# -----------------------------
# MAIN LOOP
# -----------------------------

print("--------------------------------")
print("TikTok Unreposter")
print("--------------------------------")
print()
print("Starting in 3 seconds...")
print("Move your mouse to the corner if something goes wrong.")
print()

time.sleep(START_DELAY)


while True:

    print("\nSearching for button...")

    found = find_button()

    if found:

        x, y, confidence = found

        print(
            f"Button found at ({x}, {y}) "
            f"confidence={confidence:.2f}"
        )

        # Move mouse to button
        pyautogui.moveTo(
            x,
            y,
            duration=0.15
        )

        # Click
        pyautogui.click()

        print("Clicked!")

        # Wait for TikTok to process it
        time.sleep(AFTER_CLICK_WAIT)

        # Go to next video
        pyautogui.press("down")

        print("Next video...")

        time.sleep(NEXT_VIDEO_WAIT)

    else:

        print("Button not found.")

        time.sleep(SEARCH_INTERVAL)