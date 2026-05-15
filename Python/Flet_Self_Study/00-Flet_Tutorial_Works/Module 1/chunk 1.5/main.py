import flet as ft 

def main(page: ft.Page):
    page.title = "Event Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_name = ft.TextField(label="Enter your name", width=300)
    greeting = ft.Text(size=30)

    def greet(e):
        if txt_name.value:
            greeting.value = f"Hello, {txt_name.value}!"
        else:
            greeing.value ="Please enter a name!"
        page.update()
    box = ft.Container()

    page.add(
        ft.Column([
            txt_name,
            ft.ElevatedButton("Greet Me", on_click=greet),
            greeting
        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        alignment = ft.MainAxisAlignment.START)
    )

ft.app(target=main)