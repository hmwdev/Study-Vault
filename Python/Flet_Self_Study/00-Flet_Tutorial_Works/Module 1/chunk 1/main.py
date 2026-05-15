""" 
problem: create a Flet app that displays a greeting and has a button
that adds a new message when clicked.

"""
import flet as ft 

def main(page: ft.Page):
    page.title = "Hello Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def greet(e):
        page.add(ft.Text(f"Hello, {name.value}!", size=30))
        page.update()

    name = ft.TextField(label="Your name", width=300)

    page.add(
        ft.Row([
            name,
            ft.ElevatedButton("Greet", on_click=greet)
        ], alignment= ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)