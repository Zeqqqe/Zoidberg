# Zoidberg App
A simple desktop app displaying a customizable Zoidberg image.

## Configuration - `config.ini`:
Edit this file to set default text, text color, and background type (solid or gradient) and colors. It's created automatically if missing.

## Command-Line Arguments:
Override `config.ini` settings for a single session. Use quotes for multi-word text or colors.

| Command | Shorthand | Description |
| :--- | :--- | :--- |
| `Zoidberg.exe --text "Text"` | `-t "Text"` | Sets display text. |
| `Zoidberg.exe --text-color "Color"` | `-tc "Color"` | Sets text color. |
| `Zoidberg.exe --background-color "Color"` | `-bg "Color"` | Sets solid background color. |
| `Zoidberg.exe --background-gradient1 "Color1"` and `Zoidberg.exe --background-gradient2 "Color2"` | `-bgg1 "Color1"` and `-bgg2 "Color2"` | Sets gradient start/end colors (both required). |
| `Zoidberg.exe --static-hue-offset <offset_value>` | `-sho <offset_value>` | Sets the hue shifting amount, 0 to 360. |

## Setup & Running:
* Extract **`Zoidberg.App.zip`** to a folder (e.g., `C:\ZoidbergApp`). This is required for the `Path.bat` files to work.
* Run **`Zoidberg.exe`** by double-clicking or from a terminal.
* To run from any terminal location, right-click **`System Path.bat`** in the app folder and run as administrator.

## Dependencies (Python Libraries):
* **Pillow (PIL):** For image loading and manipulation.
    * **How To Install:** Run `pip install Pillow` in Command Prompt.
* **Pygame:** For playing sound effects.
    * **How to install:** Run `pip install pygame` in Command Prompt.

**Note:** You do not need to install these dependencies to run the compiled `.exe` file.

## Requirements
* **Operating System:** Windows (Compiled for Windows).
* **Python**

### Python Install Tutorial:
[![Python Install Tutorial](https://i.ytimg.com/vi/ddGTXBhaGWA/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLBHgfdcWE4URTwe-kzMvYQ_gcqAYw)](https://www.youtube.com/watch?v=ddGTXBhaGWA)

## Troubleshooting
* **"Image not found" Error:** Ensure the main Zoidberg image (`Zoidberg Icon.png`) is located in a subfolder named `Zoidberg/` next to your `Zoidberg.exe` file. For example: `C:\ZoidbergApp\Zoidberg\Zoidberg Icon.png`.
* **"Config Created" Repeatedly:** `config.ini` might be missing or misplaced; ensure it's in the same folder as `Zoidberg.exe`.
* **Command-line Arguments Not Working:** Check quotes for multi-word/color values, and ensure you're using a new terminal window after PATH changes.
* **Antivirus Warnings:** Compiled `.exe` files can be flagged. If this occurs, you may need to add an exception for `Zoidberg.exe` in your antivirus settings.

## Command-Line Examples

##### **"Weird Mode" Command:**
`Zoidberg.exe -t "All Glory to the Hypnotoad!" -tc "#FF0000" -bgg1 "#00FF00" -bgg2 "#FF00FF"`
* **Description:** This sets text to "All Glory to the Hypnotoad!", text color to bright red, and a gradient from neon green to bright pink.

##### **"Ominous Mode" Command:**
`Zoidberg.exe -t "The shadows awaken..." -tc "#c0c0c0" -bgg1 "#1a0a2e" -bgg2 "#0a0a0a"`
* **Description:** This sets text to "The shadows awaken...", text color to silver/gray, and a gradient from dark purple to black.

##### **"Alien Mode" Command:**
`Zoidberg.exe -t "Woop woop woop!" -tc "#6f47ff" -s -ls "Woop woop woop!.mp3" -sho 90.0 -bg "#c93047"`
* **Description:** You can find more details on these and other arguments in [**Command-Line Arguments**](https://github.com/ackozu/Zoidberg/wiki/Gallery)

## Drag & Drop Config:
* Drop a `.ini` file onto the app to launch with its settings.

## Visuals
* Visit the **[Gallery](https://github.com/ackozu/Zoidberg/wiki/Gallery)** to see how the Zoidberg App looks.

###### **This app was made with AI**, Google Gemini to be exact.
