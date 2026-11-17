import flet as ft


def main(page: ft.Page):
    # Keep the name here so both route views can read it.
    name = ""
    name_field = ft.TextField(label="Your name", autofocus=True)

    def show_route(route_event):
        page.views.clear()

        if page.route == "/greeting":
            page.views.append(
                ft.View(
                    route="/greeting",
                    controls=[
                        ft.Text(f"Hello, {name}!"),
                        ft.Button("Back", on_click=go_back),
                    ],
                )
            )
        else:
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Text("Welcome to the Greeting App", size=24),
                        name_field,
                        ft.Button("Continue", on_click=continue_to_greeting),
                    ],
                )
            )

        page.update()

    async def continue_to_greeting(event):
        nonlocal name
        entered_name = (name_field.value or "").strip()
        if not entered_name:
            page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Name required"),
                    content=ft.Text("Please enter your name before continuing."),
                )
            )
            return

        name = entered_name
        await page.push_route("/greeting")

    async def go_back(event):
        await page.push_route("/")

    page.on_route_change = show_route
    show_route(None)


ft.run(main)
