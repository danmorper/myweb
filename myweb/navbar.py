import reflex as rx
navbar_height = "3em"
navbar_color = "#145DA0"
navbar_style = {
    "position": "fixed",
    "width": "100%",  # Ensure the navbar spans the full width
    "height": navbar_height,
    "padding": "0.5em 1em",
    "display": "flex",
    "justify-content": "space-between",  # This spreads out the items on the navbar
    "align-items": "center",
    "background-color": "#231579",
    "box-shadow": "0 0.2em 0.4em rgba(0,0,0,.1)",
    "font-size": "1.2em"
}


def navbar():
    return rx.box(
        rx.link(
            rx.text("El vertedero de un señor y un caballero"),
            href="https://vertedero-senor-caballero.reflex.run/"
            ),
        rx.link(
            "Sobre mí",
            href="https://danimoreno.reflex.run/",
        ),
        # If you have other navbar items, you can include them here
        style=navbar_style
    )
