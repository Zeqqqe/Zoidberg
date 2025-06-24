import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from PIL import Image, ImageTk
import configparser
import os
import sys
import argparse
import threading
import pygame # UPDATED: Import pygame directly for full initialization

# --- Color Utility Functions ---
def get_rgb_from_color_string(widget, color_string):
    """
    Converts a color string (name or hex) to an RGB tuple (0-255 range).
    Uses Tkinter's winfo_rgb for robustness with color names.
    Args:
        widget: A Tkinter widget (e.g., root window or canvas) to call winfo_rgb on.
        color_string: The color name (e.g., "red", "darkblue") or hex code (e.g., "#RRGGBB").
    Returns:
        An RGB tuple (R, G, B) where each component is 0-255. Defaults to black if invalid.
    """
    try:
        # winfo_rgb returns 16-bit values, so divide by 256 for 8-bit (0-255)
        r, g, b = widget.winfo_rgb(color_string)
        return (r // 256, g // 256, b // 256)
    except tk.TclError:
        # If winfo_rgb fails (invalid color name or malformed hex), fallback to black
        return (0, 0, 0) # Default to black if all else fails

def rgb_to_hex(rgb_tuple):
    """Converts an RGB tuple (R, G, B) to a hex color string (e.g., '#RRGGBB')."""
    # Ensure values are within 0-255 range
    r = max(0, min(255, rgb_tuple[0]))
    g = max(0, min(255, rgb_tuple[1]))
    b = max(0, min(255, rgb_tuple[2]))
    return '#%02x%02x%02x' % (r, g, b)

def interpolate_color(color1_rgb, color2_rgb, ratio):
    """
    Interpolates smoothly between two RGB colors based on a ratio.
    Ratio should be a float between 0.0 (fully color1) and 1.0 (fully color2).
    """
    r = int(color1_rgb[0] + (color2_rgb[0] - color1_rgb[0]) * ratio)
    g = int(color1_rgb[1] + (color2_rgb[1] - color1_rgb[1]) * ratio)
    b = int(color1_rgb[2] + (color2_rgb[2] - color1_rgb[2]) * ratio)
    return (r, g, b)


class ZoidbergApp:
    def __init__(self, master):
        self.master = master
        master.title("Why not Zoidberg?")
        master.geometry("500x550")
        master.minsize(300, 350)

        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser()

        # Initialize all config-related instance variables with defaults
        self.display_text = ""
        self.text_color = "black"
        self.background_type = "solid"
        self.background_color = "#F0F0F0"
        self.gradient_start_color = "#ADD8E6"
        self.gradient_end_color = "#87CEEB"
        self.sound_enabled = False # Sound feature flag
        self.launch_sound_filename = "woop.wav" # Default launch sound filename

        # Determine the application base path
        if getattr(sys, 'frozen', False):
            # Running from a PyInstaller executable
            self.application_base_path = os.path.dirname(sys.executable)
        else:
            # Running as a .py script
            self.application_base_path = os.path.dirname(os.path.abspath(__file__))

        self._load_config()
        self._parse_and_apply_command_line_args()

        # Image related instance variables
        self.original_zoidberg_pil = None
        self.zoidberg_photo = None

        # Path to the image relative to the application base path
        image_path = os.path.join(self.application_base_path, "Zoidberg", "Zoidberg Icon.png")

        if not os.path.exists(image_path):
            messagebox.showerror("Image Error", (f"Zoidberg image not found at '{image_path}'.\n"
                                                  "Please ensure the image path is correct."))
            master.destroy()
            return

        try:
            self.original_zoidberg_pil = Image.open(image_path)
            self.original_zoidberg_pil = self.original_zoidberg_pil.convert("RGBA")
        except Exception as e:
            messagebox.showerror("Image Error", f"Failed to load Zoidberg image: {e}")
            master.destroy()
            return

        self.canvas = tk.Canvas(master, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas_image_id = None
        self.canvas_text_id = None

        self._resize_job = None

        self.canvas.bind("<Configure>", self._on_resize_debounced)
        self.master.protocol("WM_DELETE_WINDOW", self._on_closing) # NEW: Handle window close event

        self.master.update_idletasks()
        self._draw_content()

        # Play launch sound if enabled
        if self.sound_enabled:
            sound_path = os.path.join(self.application_base_path, "Zoidberg", "Sounds", self.launch_sound_filename)
            self._play_sound(sound_path)


    def _on_closing(self):
        """Handler for window closing event to properly quit pygame mixer."""
        if self.sound_enabled:
            pygame.mixer.quit() # Properly shut down the mixer
        self.master.destroy()


    def _play_sound(self, sound_file_path):
        """Plays a sound file in a separate thread using pygame.mixer. (Basic implementation)"""
        if not self.sound_enabled:
            return

        print(f"DEBUG: Attempting to load and play sound from: '{sound_file_path}'")

        if not os.path.exists(sound_file_path):
            print(f"Warning: Sound file not found at '{sound_file_path}'")
            return
        
        # Define the threaded function that loads and plays the sound
        def play_threaded_sound():
            try:
                sound = pygame.mixer.Sound(sound_file_path) # Load the sound
                sound.play() # Play the sound
            except Exception as e:
                print(f"Error playing sound '{sound_file_path}': {e}")

        # Start the sound playback in a new thread
        threading.Thread(target=play_threaded_sound, daemon=True).start()


    def _parse_and_apply_command_line_args(self):
        """
        Parses command-line arguments and applies them, overriding config settings.
        Gradient arguments take precedence over solid background if both are provided.
        """
        parser = argparse.ArgumentParser(
            description="Launch Zoidberg application with custom settings."
        )

        parser.add_argument(
            "-t", "--text",
            type=str,
            help="Set the display text for Zoidberg."
        )

        parser.add_argument(
            "-bg", "--background-color",
            type=str,
            help="Set the single background color (e.g., 'red', '#RRGGBB')."
        )

        parser.add_argument(
            "-bgg1", "--gradient-color1",
            type=str,
            help="Set the first gradient color."
        )

        parser.add_argument(
            "-bgg2", "--gradient-color2",
            type=str,
            help="Set the second gradient color."
        )

        parser.add_argument(
            "-tc", "--text-color",
            type=str,
            help="Set the color of the display text (e.g., 'white', '#RRGGBB')."
        )

        # Argument for sound
        parser.add_argument(
            "-s", "--enable-sound",
            action="store_true", # This makes it a boolean flag (true if present)
            help="Enable sound effects (e.g., launch sound)."
        )
        parser.add_argument(
            "-ls", "--launch-sound",
            type=str,
            help="Specify a custom launch sound filename (e.g., 'custom.wav'). Must be in Zoidberg/Sounds/."
        )

        args = parser.parse_args()

        # Apply text if provided
        if args.text:
            self.display_text = args.text

        # Apply text color if provided
        if args.text_color:
            self.text_color = args.text_color

        # Apply sound settings if provided (command line overrides config)
        if args.enable_sound:
            self.sound_enabled = True
        if args.launch_sound:
            self.launch_sound_filename = args.launch_sound

        # Determine background type and colors based on command-line arguments
        # Gradient arguments take precedence if both are given.
        if args.gradient_color1 and args.gradient_color2:
            self.background_type = "gradient"
            self.gradient_start_color = args.gradient_color1
            self.gradient_end_color = args.gradient_color2
        elif args.background_color:
            self.background_type = "solid"
            self.background_color = args.background_color
        # If neither explicit background argument is provided,
        # the background_type and colors will remain as loaded from config.ini,
        # which is the desired fallback.


    def _sanitize_config_value(self, value_string):
        """
        Removes potential inline comments, leading/trailing whitespace,
        and ensures consistent line endings from a config string.
        """
        if not isinstance(value_string, str):
            value_string = str(value_string)

        value_string = value_string.replace('\r', '').replace('\n', '')

        if ';' in value_string:
            value_string = value_string.split(';', 1)[0]

        if '#' in value_string and not value_string.strip().startswith('#'):
            value_string = value_string.split('#', 1)[0]

        return value_string.strip()


    def _load_config(self):
        """
        Loads all settings from config.ini, including background options and new sound options.
        Creates default sections if they don't exist and writes back only if modified.
        """
        config_modified = False

        # Determine config.ini path FIRST, before checking for its existence
        if getattr(sys, 'frozen', False):
            # Running from a PyInstaller executable
            self.config_file = os.path.join(os.path.dirname(sys.executable), 'config.ini')
        else:
            # Running as a .py script
            self.config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        # NOW check if the file exists at the determined path
        if not os.path.exists(self.config_file):
            # Config file not found, so create default sections
            self.config['Settings'] = {
                'display_text': "Woop woop woop!",
                'text_color': "#c5d8ed",
                'sound_enabled': 'False', # Default to False
                'launch_sound': 'woop.wav' # Default launch sound
            }
            self.config['Background'] = {
                'type': 'gradient', # Changed default to gradient to demonstrate
                'color': '#1a0c11',
                'start_color': '#87CEEB', # Lighter blue for better contrast
                'end_color': '#4682B4'   # Steel blue for clear gradient
            }
            config_modified = True
            messagebox.showinfo("Config Created", f"'{self.config_file}' was not found and has been created with default settings.\n"
                                                   "You can edit its sections ([Settings], [Background]) to customize text and background.")
        else:
            # Config file found, read it
            self.config.read(self.config_file)

            # Ensure sections and new options exist in memory; add defaults if missing
            if not self.config.has_section('Settings'):
                self.config['Settings'] = {
                    'display_text': "Woop woop woop!",
                    'text_color': "#c5d8ed",
                    'sound_enabled': 'False',
                    'launch_sound': 'woop.wav'
                }
                config_modified = True
            else: # Check for individual new options if section exists
                if not self.config.has_option('Settings', 'sound_enabled'):
                    self.config['Settings']['sound_enabled'] = 'False'
                    config_modified = True
                if not self.config.has_option('Settings', 'launch_sound'):
                    self.config['Settings']['launch_sound'] = 'woop.wav'
                    config_modified = True


            if not self.config.has_section('Background'):
                self.config['Background'] = {
                    'type': 'gradient', # Default to gradient
                    'color': '#1a0c11',
                    'start_color': '#87CEEB', # Lighter blue
                    'end_color': '#4682B4'   # Steel blue
                }
                config_modified = True

        if config_modified:
            self._write_config_with_comments()

        # Load values into instance variables from the (potentially updated) in-memory config
        self.display_text = self._sanitize_config_value(self.config.get('Settings', 'display_text', fallback="Default Text"))
        self.text_color = self._sanitize_config_value(self.config.get('Settings', 'text_color', fallback="#1a1a1a"))
        self.sound_enabled = self.config.getboolean('Settings', 'sound_enabled', fallback=False)
        self.launch_sound_filename = self._sanitize_config_value(self.config.get('Settings', 'launch_sound', fallback='woop.wav'))

        self.background_type = self._sanitize_config_value(self.config.get('Background', 'type', fallback='solid'))
        self.background_color = self._sanitize_config_value(self.config.get('Background', 'color', fallback='#F0F0F0'))
        self.gradient_start_color = self._sanitize_config_value(self.config.get('Background', 'start_color', fallback='#ADD8E6'))
        self.gradient_end_color = self._sanitize_config_value(self.config.get('Background', 'end_color', fallback='#87CEEB'))


    def _write_config_with_comments(self):
        """
        Writes the config to file, manually adding desired comments. This provides more control over the output format and comments.
        """
        with open(self.config_file, 'w') as f:
            f.write('[Settings]\n')
            f.write(f'display_text = {self.config.get("Settings", "display_text")}\n')
            f.write(f'text_color = {self.config.get("Settings", "text_color")}\n')
            f.write(f'sound_enabled = {self.config.get("Settings", "sound_enabled")}\n')
            f.write('; Set to True to enable sound effects.\n')
            f.write(f'launch_sound = {self.config.get("Settings", "launch_sound")}\n')
            f.write('; Filename of the sound to play on app launch (e.g., "woop.wav"). Must be in Zoidberg/Sounds/.\n')
            f.write('\n')

            f.write('[Background]\n')
            f.write(f'type = {self.config.get("Background", "type")}\n')
            f.write('; To use a solid background, change \'type\' to \'solid\' and adjust \'color\':\n')
            f.write(f'color = {self.config.get("Background", "color")}\n')
            f.write('; Default Maroon Background Color (used if type = solid)\n')
            f.write('\n')
            f.write('; For gradient background, ensure \'type\' is \'gradient\' and adjust colors:\n')
            f.write(f'start_color = {self.config.get("Background", "start_color")}\n')
            f.write('; Light Blue (Start of Gradient)\n')
            f.write(f'end_color = {self.config.get("Background", "end_color")}\n')
            f.write('; Steel Blue (End of Gradient)\n')


    def _on_resize_debounced(self, event):
        """
        Handles the resize event with debouncing.
        Only calls _draw_content after a short delay (250ms), canceling previous pending calls.
        This prevents continuous redrawing during an active drag operation.
        """
        if self._resize_job:
            self.master.after_cancel(self._resize_job)
        self._resize_job = self.master.after(250, self._draw_content)

    def _draw_content(self):
        """
        Handles scaling the Zoidberg image and drawing it along with the text on the canvas.
        This function now also draws the background (solid or gradient).
        """
        if not self.original_zoidberg_pil:
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width <= 0 or canvas_height <= 0:
            return

        self.canvas.delete("all")

        # --- Draw Background (Solid or Gradient) ---
        if self.background_type == 'solid':
            self.canvas.config(bg=self.background_color)
        elif self.background_type == 'gradient':
            # Use the new robust color conversion for gradient colors
            start_rgb = get_rgb_from_color_string(self.master, self.gradient_start_color)
            end_rgb = get_rgb_from_color_string(self.master, self.gradient_end_color)

            # Create gradient rectangles
            for i in range(canvas_height):
                ratio = i / (canvas_height - 1) if canvas_height > 1 else 0
                interpolated_rgb = interpolate_color(start_rgb, end_rgb, ratio)
                interpolated_hex = rgb_to_hex(interpolated_rgb)

                self.canvas.create_rectangle(0, i, canvas_width, i + 1,
                                             fill=interpolated_hex, outline="")
        else:
            self.canvas.config(bg='#F0F0F0') # Fallback to a default color


        # --- Draw Zoidberg Image ---
        original_width, original_height = self.original_zoidberg_pil.size

        # Calculate scale factor for the image to fit, and then reduce it slightly
        # to ensure more background is visible around Zoidberg.
        width_scale = canvas_width / original_width
        height_scale = canvas_height / original_height

        # Use 85% of the fitting scale to leave some margin
        scale_factor = min(width_scale, height_scale) * 0.85 

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        if new_width < 1: new_width = 1
        if new_height < 1: new_height = 1

        scaled_zoidberg_pil = self.original_zoidberg_pil.resize((new_width, new_height), Image.LANCZOS)
        self.zoidberg_photo = ImageTk.PhotoImage(scaled_zoidberg_pil)

        image_x = canvas_width / 2
        image_y = canvas_height / 2

        self.canvas_image_id = self.canvas.create_image(image_x, image_y,
                                                         image=self.zoidberg_photo,
                                                         anchor=tk.CENTER)

        # --- Draw Text ---
        text_offset_y_ratio = 0.20

        text_y_on_image = new_height * text_offset_y_ratio
        final_text_y = (image_y - new_height / 2) + text_y_on_image

        final_text_x = image_x

        base_font_size = 20
        base_image_width_for_font = 300

        font_size = max(8, int(base_font_size * (new_width / base_image_width_for_font)))
        font_style = ("Helvetica", font_size, "bold")

        text_wrap_width_pixels = new_width * 0.8
        if text_wrap_width_pixels < 10: text_wrap_width_pixels = 10

        self.canvas_text_id = self.canvas.create_text(final_text_x, final_text_y,
                                                     text=self.display_text,
                                                     font=font_style,
                                                     fill=self.text_color,
                                                     anchor=tk.CENTER,
                                                     width=text_wrap_width_pixels)

# --- Main Application Execution ---
if __name__ == "__main__":
    # NEW: Initialize pygame mixer here, before app instantiation
    try:
        # Mixer parameters: frequency, size, channels, buffer
        # Defaults are usually good. 44100 Hz, -16-bit signed, 2 channels (stereo), 4096 buffer
        pygame.mixer.init()
    except Exception as e:
        print(f"Warning: Could not initialize pygame mixer outside ZoidbergApp: {e}")
        # If mixer fails here, subsequent sound calls inside app might still fail,
        # but at least we tried to initialize it properly.

    root = tk.Tk()
    app = ZoidbergApp(root)
    root.mainloop()
    
    # NEW: Quit pygame mixer when the application closes
    if pygame.mixer.get_init(): # Only quit if it was successfully initialized
        pygame.mixer.quit()
