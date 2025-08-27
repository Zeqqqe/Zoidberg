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

<details>
  <summary>Python Install Tutorial</summary>

> ### [Python Installation Guide](https://www.youtube.com/watch?v=ddGTXBhaGWA)
> #### [@Amit.Thinks](https://www.youtube.com/@Amit.Thinks)
> 
>  <a href="https://www.youtube.com/watch?v=ddGTXBhaGWA">
> <div align="center">
>
>  https://github.com/user-attachments/assets/f069793d-8245-4164-aaeb-631a388f9df3
>  </div>
>
> In this video, learn to download and install Python 3.13.5 on Windows 11. We will also run a sample Python code.
>
>
> Python Tutorial (English): https://bit.ly/3znnb1y
>
> Python Tutorial (Hindi): https://youtu.be/b97WsOM9BYg
>
> Python Study Material: https://studyopedia.com/tutorials/python3/
> 
> Google Colab Tutorial: https://youtu.be/iMlMfrXJYSg
> 
> Anaconda Tutorial: https://youtu.be/ovlID7gefzE
> 
> Jupyter Notebook Tutorial: https://youtu.be/Ou-7G9VQugg
> 
> PyCharm Tutorial: https://youtu.be/nixcq6mEGWQ
> 
> Pandas Tutorial (English): https://youtu.be/yFoVs3_wvPo
> 
> Pandas Tutorial (Hindi): https://youtu.be/57POFzZ7f60
> 
> NumPy Tutorial (English): https://youtu.be/WsENswmSz6M
> 
> NumPy Tutorial (Hindi): https://youtu.be/roqStVWNR7Q
> 
> Matplotlib Tutorial (English): https://youtu.be/DFBkTIhptOQ
> 
> Matplotlib Tutorial (Hindi): https://youtu.be/vBCXsAd_swk
> 
> #Python #Windows #installation
> -------------------------------------------------------------------------------
> 
> ✔️My Website - https://studyopedia.com
> 
> ✔️Join Us at 59/month: https://bit.ly/3WV9sXK
> 
> ✔️Data Analytics Tutorial: https://bit.ly/48MxVTU
> 
> ✔️Web Dev Tutorial: https://bit.ly/3tl9nlp
> 
> ✔️Free Study Material: https://bit.ly/3K7lzbP
> 
> 👉  Follow me
> LinkedIn - https://bit.ly/3C1CY4v
> Instagram - https://bit.ly/3z8Fg1d
> ---------------------------------------------------------------------------------
> 
> Tableau Tutorial⭐️https://youtu.be/4aTvjpdOMT4
> 
> Power BI Tutorial⭐️https://youtu.be/OITCW7ETz-M
> 
> Generative AI Course (English)⭐️https://bit.ly/3Vhsbxv
> 
> Generative AI Course (Hindi) ⭐️ https://bit.ly/3V76ZKp
> 
> Python Tutorial (English)⭐️ https://youtu.be/HakXpkXcjdI
> 
> Python Tutorial (Hindi)⭐️ https://youtu.be/b97WsOM9BYg
> 
> Pandas Tutorial (English)⭐️https://youtu.be/yFoVs3_wvPo
> 
> Pandas Tutorial (Hindi)⭐️https://youtu.be/57POFzZ7f60
> 
> NumPy Tutorial (English)⭐️https://youtu.be/WsENswmSz6M
> 
> NumPy Tutorial (Hindi)⭐️https://youtu.be/roqStVWNR7Q
> 
> Matplotlib Tutorial (English)⭐️https://youtu.be/DFBkTIhptOQ
> 
> Matplotlib Tutorial (Hindi)⭐️https://youtu.be/vBCXsAd_swk
> 
> Google Colab Tutorial ⭐️https://youtu.be/iMlMfrXJYSg
> 
> Anaconda Tutorial ⭐️ https://youtu.be/ovlID7gefzE
> 
> PyCharm Tutorial ⭐️https://youtu.be/nixcq6mEGWQ
> 
> SQL Tutorial ⭐️https://youtu.be/7dcYlJcGhqk
> 
> MySQL Tutorial⭐️https://youtu.be/sgpDAiF-18o
> 
> MySQL Workbench Tutorial: https://youtu.be/UzodkZUt5JY
> 
> HTML Tutorial ⭐️https://bit.ly/3VHaUvq
> 
> jQuery Tutorial (English)⭐️https://youtu.be/5BTWmXFOKlc
> 
> jQuery Tutorial (Hindi)⭐️https://youtu.be/bvmAsDvQ1NM
> 
> Bootstrap Tutorial⭐️https://youtu.be/nahewStckVU
> 
> ►  Programming - Free Study Material (Downloadable)
> 
> Machine Learning⭐️ https://studyopedia.com/tutorials/machine-learning
> 
> Deep Learning⭐️https://studyopedia.com/tutorials/deep-learning
> 
> Tableau ⭐️https://studyopedia.com/tutorials/tableau
> 
> Power BI ⭐️https://studyopedia.com/tutorials/power-bi
> 
> Python ⭐️https://studyopedia.com/tutorials/python3
> 
> Numpy ⭐️https://studyopedia.com/tutorials/numpy
> 
> Pandas ⭐️https://studyopedia.com/tutorials/pandas
> 
> Matplotlib ⭐️https://studyopedia.com/tutorials/matplotlib
> 
> Java ⭐️https://studyopedia.com/tutorials/java
> 
> C ⭐️https://studyopedia.com/tutorials/c-programming
> 
> C++ ⭐️https://studyopedia.com/tutorials/cpp/
> 
> C# ⭐️https://studyopedia.com/tutorials/csharp/
> 
> Android ⭐️https://studyopedia.com/tutorials/android
> R ⭐️https://studyopedia.com/tutorials/r-tutorial
> 
> Bootstrap⭐️https://studyopedia.com/tutorials/bootstrap/
> 
> HTML5 ⭐️https://studyopedia.com/tutorials/html5
> 
> JavaScript⭐️https://studyopedia.com/tutorials/javascript/
> 
> jQuery⭐️https://studyopedia.com/tutorials/jquery/
> 
> ►  Database  - Free Study Material (Downloadable)
> SQL ⭐️https://studyopedia.com/tutorials/sql
> 
> MySQL ⭐️https://studyopedia.com/tutorials/mysql
> 
> MongoDB⭐️https://studyopedia.com/tutorials/mongodb
> 
> Python🔥https://studyopedia.com/java/java-interview-questions-and-answers
> 
> Java 🔥https://studyopedia.com/python3/python-multiple-choice-questions/
> 
> Android🔥https://studyopedia.com/android/android-interview-questions/
> 
> ReactJS🔥https://studyopedia.com/reactjs/react-interview-questions
> 
> Bootstrap 🔥https://studyopedia.com/bootstrap/bootstrap-interview-questions
> 
> SQL 🔥https://studyopedia.com/sql/sql-interview-questions
> 
> MongoDB 🔥https://studyopedia.com/mongodb/mongodb-interview-questions
> 
> MySQL 🔥https://studyopedia.com/mysql/mysql-interview-questions
> 
> 👉 About Amit Thinks YouTube Channel
> I am Amit Diwan, a self-made Entrepreneur, running "Amit Thinks", a Tech YouTube Channel. Also running an E-Learning website "[studyopedia.com](https://studyopedia.com)".  We publish videos in  English and Hindi on Programming, Databases, and Web Dev Technologies. I have left a job offer from Accenture and 3 government jobs to follow my dream of being an
> entrepreneur.
>
> Join this channel to get access to the perks:
> https://www.youtube.com/channel/UCgnr2Lkl1LZf0IOKRDAoJ2g/join
>
> ►  Subscribe
> https://www.youtube.com/@Amit.Thinks/
</details>



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
[![Visuals of Zoidberg](https://raw.githubusercontent.com/Zwarb/Zoidberg/refs/heads/main/zoidberg_app_screenshot.png)](https://github.com/Zwarb/Zoidberg/wiki/Gallery)
* Visit the [Gallery](https://github.com/Zwarb/Zoidberg/wiki/Gallery) to see more visuals.

###### **This app was made with AI**, Google Gemini to be exact.
