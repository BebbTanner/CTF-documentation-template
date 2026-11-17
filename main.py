'''
    File "c:\Users\tbebb\Documents\CTF-documentation-template\main.py", line 66, in <module>
    customtkinter.set_default_color_theme(THEMES[theme_name])
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\tbebb\Documents\CTF-documentation-template\.venv\Lib\site-packages\customtkinter\__init__.py", line 70, in set_default_color_theme
    ThemeManager.load_theme(color_string)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    File "C:\Users\tbebb\Documents\CTF-documentation-template\.venv\Lib\site-packages\customtkinter\windows\widgets\theme\theme_manager.py", line 23, in load_theme
    with open(theme_name_or_path, "r") as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'c:\\Users\\tbebb\\Documents\\CTF-documentation-template\\assets\\violet.json'

    I think I need some extra files for this.
    It appears in that first comment that this has json files, but I did not see any attached when I was on the documentation site.
'''

import os
import customtkinter

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

# a built-in theme is loaded by its name, an own theme by the path to its .json file
THEMES = {
    "Violet (own theme)": os.path.join(ASSETS, "violet.json"),
    "Blue": "blue",
    "Dark blue": "dark-blue",
    "Green": "green",
    "Gold": "gold",
}


class App(customtkinter.CTk):
    def __init__(self, theme_name):
        super().__init__()

        self.title("Colors and themes")
        self.geometry("440x330")
        self.grid_columnconfigure((0, 1), weight=1)
        self.next_theme = None

        self.theme_label = customtkinter.CTkLabel(self, text="Theme")
        self.theme_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.theme_menu = customtkinter.CTkOptionMenu(self, values=list(THEMES), command=self.change_theme)
        self.theme_menu.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")
        self.theme_menu.set(theme_name)

        # these widgets get all their colors from the theme
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.button = customtkinter.CTkButton(self, text="CTkButton")
        self.button.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.checkbox = customtkinter.CTkCheckBox(self, text="CTkCheckBox")
        self.checkbox.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.checkbox.select()
        self.switch = customtkinter.CTkSwitch(self, text="CTkSwitch")
        self.switch.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        self.switch.select()
        self.slider = customtkinter.CTkSlider(self)
        self.slider.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.segmented_button = customtkinter.CTkSegmentedButton(self, values=["Day", "Week", "Month"])
        self.segmented_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.segmented_button.set("Week")

        # own colors for single widgets: a tuple has a color for light and one for dark mode
        self.delete_button = customtkinter.CTkButton(self, text="Delete",
                                                     fg_color=("#DC2626", "#B91C1C"),
                                                     hover_color=("#B91C1C", "#7F1D1D"))
        self.delete_button.grid(row=5, column=0, padx=20, pady=(10, 20), sticky="ew")
        self.cancel_button = customtkinter.CTkButton(self, text="Cancel", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "gray90"))
        self.cancel_button.grid(row=5, column=1, padx=20, pady=(10, 20), sticky="ew")

    def change_theme(self, theme_name):
        # widgets get their colors from the theme when they are created,
        # so the window is closed and opened again with the new theme
        self.next_theme = theme_name
        self.destroy()


theme_name = "Violet (own theme)"
while theme_name is not None:
    customtkinter.set_default_color_theme(THEMES[theme_name])
    app = App(theme_name)
    app.mainloop()
    theme_name = app.next_theme