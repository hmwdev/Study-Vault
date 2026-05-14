# Imports
import flet as ft

# Flet App Structure and setup

def main(page: ft.Page):
    page.title = "Temperature Converter"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 750
    page.window_resize = True
    page.padding = 20
    # Add Window Icon
    # Point to the file inside the assets folder
    page.window.icon = "icon.ico"
   
    

    # Input Fields for C, F, K
    celcius_input = ft.TextField(
        label="Celcius °C : ",
        hint_text="Enter temperature in Celcius",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE_70,
        border_color=ft.Colors.WHITE,
        on_change= lambda e: convert_from_celcius(e.control.value)

    )

    fahrenheit_input = ft.TextField(
        label="Fahrenheit °F : ",
        hint_text="Enter temperature in Fahrenheit",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE_70,
        border_color=ft.Colors.WHITE,
        on_change = lambda e: convert_from_fahrenheit(e.control.value)
    )

    kelvin_input = ft.TextField(
        label="Kelvin K : ",
        hint_text="Enter temperature in Kelvin",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.WHITE_70,
        border_color=ft.Colors.WHITE,
        on_change = lambda e: convert_from_kelvin(e.control.value)
    )

    # Add functionality to the APP
    def convert_from_celcius(value):
        if value and value.strip():
            try:
                celcius = float(value)
                fahrenheit = (celcius * 9/5) + 32
                kelvin = celcius + 273.15

                fahrenheit_input.value = f"{fahrenheit:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()

            except ValueError:
                celcius_input.value= "Error!"

    def convert_from_fahrenheit(value):
        if value and value.strip():
            try:
                fahrenheit = float(value)
                celcius = (fahrenheit - 32) * 5/9
                kelvin = celcius + 273.15

                celcius_input.value = f"{celcius:.2f}"
                kelvin_input.value = f"{kelvin:.2f}"
                page.update()

            except ValueError:
                fahrenheit_input.value= "Error!"
             
    def convert_from_kelvin(value):
        if value and value.strip():
            try:
                kelvin = float(value)
                celcius = kelvin - 273.15
                fahrenheit = (celcius * 9/5) + 32

                celcius_input.value = f"{celcius:.2f}"
                fahrenheit_input.value = f"{fahrenheit:.2f}"
                page.update()

            except ValueError:
                kelvin_input.value= "Error!"

    def clear_all(e):
        celcius_input.value = ""
        fahrenheit_input.value = ""
        kelvin_input.value = ""
        page.update()
        
             



    # Create the main UI -> Containers
    page.add(
        ft.Column([
            ft.Text(
                "Temperature Converter",
                size=28,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.BLUE_700
                ),
            ft.Divider(height=20),

            celcius_input,
            ft.Divider(height=10),

            fahrenheit_input,
            ft.Divider(height=10),

            kelvin_input,
            ft.Divider(height=10),

            ft.ElevatedButton(
                " Clear All",
                on_click=clear_all,
                icon=ft.Icons.CLEAR,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.RED_400,
                    color=ft.Colors.WHITE
                )

            ),
            ft.Divider(height=20),

            ft.Container(
                content=ft.Column([
                    ft.Text("Conversion Formulas: ", weight=ft.FontWeight.BOLD),
                    ft.Text(" Celsius to Fahrenheit: F = (C x 9/5) + 32"),
                    ft.Text(" Fahrenheit to Celsius: C = (F -32) x 5/9"),
                    ft.Text(" Celcius to Kelvin: K = C + 273.15"),
                ], spacing=5),
                padding=15,
                bgcolor="#2A2A2A",
                border_radius=10
            )

        ])
    )


# Run a flet app
if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
