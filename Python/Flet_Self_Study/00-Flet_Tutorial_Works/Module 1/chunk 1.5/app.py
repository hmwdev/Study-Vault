import flet as ft

def main(page: ft.Page):
    page.title = "Alignment Visualizer"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30

    math_content = r"""
    Here is the famous **Bernoulli's equation**:
    
    $$
    P + \frac{1}{2} \rho v^2 + \rho g h = \text{constant}
    $$
    
    And here is the quadratic formula:
    
    $$
    x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    $$
    """
    # ==========================================
    # HELPER FUNCTION: Creates small colored boxes
    # ==========================================
    def make_box(text, color):
        return ft.Container(
            content=ft.Text(text, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            bgcolor=color,
            width=60,
            height=60,
            # FIXED: Capital A and Capital CENTER
            alignment=ft.Alignment.CENTER, 
            border_radius=8
        )

    # ==========================================
    # EXAMPLE 1: THE ROW (Horizontal)
    # ==========================================
    page.add(
        ft.Markdown(
            value=math_content,
            selectable=True,
            # Optional: You can control the size of the equations
            latex_scale_factor=1.5, 
            # Optional: You can style the text of the math formulas
            latex_style=ft.TextStyle(color=ft.Colors.BLUE_400)
        ),
        ft.Text("1. Row Layout (Grey Background)", size=20, weight=ft.FontWeight.BOLD),
        ft.Text("Main Axis (Horizontal): SPACE_BETWEEN | Cross Axis (Vertical): CENTER"),
        ft.Container(
            bgcolor=ft.Colors.GREY_300,
            height=150, 
            padding=10,
            border_radius=8,
            content=ft.Row(
                controls=[
                    make_box("A", ft.Colors.RED_500),
                    make_box("B", ft.Colors.RED_600),
                    make_box("C", ft.Colors.RED_700),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
                vertical_alignment=ft.CrossAxisAlignment.CENTER, 
            )
        ),
        ft.Divider(height=40, color=ft.Colors.TRANSPARENT) 
    )

    # ==========================================
    # EXAMPLE 2: THE COLUMN (Vertical)
    # ==========================================
    page.add(
        ft.Text("2. Column Layout (Blue Background)", size=20, weight=ft.FontWeight.BOLD),
        ft.Text("Main Axis (Vertical): END | Cross Axis (Horizontal): CENTER"),
        ft.Container(
            bgcolor=ft.Colors.BLUE_100,
            width=300, 
            height=300,
            padding=10,
            border_radius=8,
            content=ft.Column(
                controls=[
                    make_box("1", ft.Colors.BLUE_500),
                    make_box("2", ft.Colors.BLUE_600),
                    make_box("3", ft.Colors.BLUE_700),
                ],
                alignment=ft.MainAxisAlignment.END, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            )
        ),
        ft.Divider(height=40, color=ft.Colors.TRANSPARENT)
    )

    # ==========================================
    # EXAMPLE 3: THE CONTAINER (2D Plane)
    # ==========================================
    page.add(
        ft.Text("3. Container Layout (Green Background)", size=20, weight=ft.FontWeight.BOLD),
        ft.Text("Alignment (2D Plane): BOTTOM_RIGHT"),
        ft.Container(
            bgcolor=ft.Colors.GREEN_100,
            width=300,
            height=200,
            border_radius=8,
            # FIXED: Capital A and Capital BOTTOM_RIGHT
            alignment=ft.Alignment.BOTTOM_RIGHT, 
            padding=10,
            content=make_box("Single", ft.Colors.GREEN_600)
        )
    )

ft.run(main)