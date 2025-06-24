Zoidberg App"Why not Zoidberg?" is a simple, fun desktop application that displays an image of Zoidberg with customizable text and background. You can personalize its appearance by editing a configuration file or by passing arguments directly when launching the app.FeaturesCustomizable Display Text: Change the iconic Zoidberg phrase.Customizable Text Color: Choose any color for the displayed text.Flexible Backgrounds:Solid background color.Vertical gradient background with two colors.Dynamic Resizing: The Zoidberg image and text scale automatically when you resize the window.Configuration File (config.ini): Easily set default preferences.Command-Line Arguments: Override settings from config.ini for specific launches without editing the file.How to Use1. Download and SetupDownload the Application: Obtain the Zoidberg_App.zip file.Create a Folder: Create a new, empty folder on your computer (e.g., C:\Apps\Zoidberg or Desktop\ZoidbergApp).Extract Files: Extract the entire contents of Zoidberg_App.zip directly into this new folder.Inside, you should find Zoidberg.exe, config.ini, and a Zoidberg subfolder containing the image.2. Running the ApplicationOnce extracted, you have a few ways to run the Zoidberg.exe:Double-Click: Simply double-click Zoidberg.exe in its folder. It will launch with settings from config.ini.From Command Prompt/PowerShell (Full Path): Open a Command Prompt or PowerShell, navigate to the ZoidbergApp folder, and type:.\Zoidberg.exe



or, provide the full path:"C:\Apps\Zoidberg\Zoidberg.exe"



From Command Prompt/PowerShell (After Adding to PATH): (See "Making it Accessible from Anywhere" section below). After adding the application's directory to your system PATH, you can simply type Zoidberg from any location in your terminal:Zoidberg



3. Customizing with config.iniThe config.ini file allows you to set default preferences for the application. It will be created automatically with default values if it doesn't exist when you first run the app.Example config.ini content:[Settings]
display_text = Woop woop woop!
text_color = #c5d8ed

[Background]
type = solid
color = #1a0c11
; Default Maroon Background Color

; To use a gradient background, change 'type' to 'gradient' and optionally adjust colors:
; type = gradient
start_color = #c93047
; Zoidbergish Red
end_color = #290b0f
; Zoidbergish Dark Red



display_text: The text shown on Zoidberg.text_color: The color of the display text (e.g., "red", "blue", or hex codes like "#RRGGBB").type (under [Background]): Can be solid or gradient.color: Used if type = solid.start_color / end_color: Used if type = gradient.To use a gradient: Change type = solid to type = gradient and ensure start_color and end_color are set.4. Customizing with Command-Line ArgumentsYou can override config.ini settings for a single launch by passing arguments to Zoidberg.exe via Command Prompt or PowerShell. Remember to use quotes for multi-word text or color values.Available Arguments:-t "Your Text Here" or --text "Your Text Here"Sets the display text.Example: Zoidberg.exe -t "Good news everyone!"-bg "ColorName" or --background-color "ColorName"Sets a solid background color. This will disable any gradient settings for this session.Example: Zoidberg.exe -bg "purple" or Zoidberg.exe --background-color "#00FFFF"-bgg1 "StartColor" and -bgg2 "EndColor" or --gradient-color1 "StartColor" and --gradient-color2 "EndColor"Sets a gradient background from StartColor to EndColor. Both arguments must be provided to activate the gradient.Example: Zoidberg.exe -bgg1 "lime" -bgg2 "navy"-tc "TextColor" or --text-color "TextColor"Sets the color of the display text.Example: Zoidberg.exe -tc "white" or Zoidberg.exe --text-color "#FFD700"Combining Arguments:You can combine multiple arguments:Zoidberg.exe -t "I am a doctor!" -tc "red" -bg "black"



5. Making it Accessible from Anywhere (Adding to System PATH)To be able to type just Zoidberg in any Command Prompt or PowerShell window, you can add the application's folder to your system's PATH environment variable.Locate System Path.bat: Find this batch file in the folder where you extracted Zoidberg.exe.Run as Administrator: Right-click on System Path.bat and select "Run as administrator."Follow Prompts: Approve any User Account Control (UAC) prompts. The script will add the application's directory to your system's PATH.Restart Terminal: Close any open Command Prompt/PowerShell windows and open a new one.Test: You should now be able to simply type Zoidberg and press Enter from any directory.RequirementsOperating System: Windows (The .exe is compiled for Windows).Troubleshooting"Image not found" Error:Ensure the Zoidberg subfolder containing the Zoidberg 324.png image file is located in the same directory as Zoidberg.exe."Config Created" Message Repeatedly:This usually means the config.ini file is not in the same directory as Zoidberg.exe (or your Python script if running directly). Ensure it is.Command-line arguments not working:Are you enclosing multi-word text or color names in double quotes (e.g., "Hello World", "#RRGGBB")?Are you running the command from a new Command Prompt/PowerShell window if you've recently added to PATH?Antivirus Warnings: Some antivirus software might flag newly compiled .exe files as suspicious. If this occurs, you may need to add an exception for this app in your antivirus settings.
