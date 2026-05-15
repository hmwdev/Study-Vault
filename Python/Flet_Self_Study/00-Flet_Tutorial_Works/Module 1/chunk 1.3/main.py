# Problem: Create an app that display a counter. Include a button to imcrement
# the counter and another to reset it. The current count should be clearly visible.

import flet as ft 

def main(page: ft.Page):
    page.title = "Counter app"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    counter = ft.Text("0", size=70, weight=ft.FontWeight.BOLD)

    def increment(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    def reset(e):
        counter.value = "0"
        page.update()

    page.add(
        ft.Column([
            counter,
            ft.Row([
                ft.ElevatedButton("Increment", on_click=increment),
                ft.ElevatedButton("Reset", on_click=reset),
            ], alignment = ft.MainAxisAlignment.CENTER, spacing = 20)
        ],
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        spacing=30)
    )



ft.app(target=main)