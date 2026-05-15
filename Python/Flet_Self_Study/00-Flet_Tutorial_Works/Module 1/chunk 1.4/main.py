# Problem: create a beautiful login-style card with a tiltle, two input fields, and a button.abs
import flet as ft 

def main(page: ft.Page):
    page.title = "Login Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    login_card = ft.Container(
        content=ft.Column([
            ft.Text("Welcome Back", size=30, weight=ft.FontWeight.BOLD),
            ft.TextField(label="Email", width=300),
            ft.TextField(label="password", password=True, width=300),
            ft.ElevatedButton("Login", width=300),
        ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=ft.Colors.BLUE_GREY_900,
        border_radius=20,
        padding=20,
        width=400,
        shadow=ft.BoxShadow(blur_radius=25, color=ft.Colors.BLACK_26)
    )

    page.add(login_card)

ft.app(target=main)