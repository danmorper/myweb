from rxconfig import config
import reflex as rx

# Blue website
aboutme_color = "white"
background_color = "#0C2D48"
sidebar_color = "#2E8BC0"
shadow_color = "#B1D4E0"
color_card = "white"
border_card = "1px solid #B1D4E0"
cv_border = "2px solid #3E4A68"

# Black and white website
# aboutme_color = "black"
# background_color = "white" 
# shadow_color = "gray"
# background_color_card = "white"
# color_card = "black"
# border_card = "1px solid black"
# cv_border = "2px solid #000000"
# cv_shadow = "0 0.2em 0.4em #000000"

class Styles():
    aboutme = {
        "color": aboutme_color,
        "font-size": "1.2em",
        "line-height": "1.5em",
        "width": "100vw",
        "height": "100vh",
    }
    aboutme_main_content_width = "100vw"
    aboutme_main_content = {
        "background-color": background_color,
        "width": aboutme_main_content_width,
        "height": "400vh",
        "display": "flex",
        "flex-direction": "column",
        "align-items": "center",
        "padding-top": "0.5em"
    }

    cards = {
        "width": "35em", 
        "height": "auto", 
        "margin": "1em auto", 
        "border-radius": "1em", 
        "padding": "2em", 
        "box-shadow": "0 0.2em 0.4em" + shadow_color,
        "color": color_card,
        "border": border_card,
        }

    CV_image = {
        "width": "10em",  # Adjust this value as needed to make the image smaller
        "height": "15em",
        "display": "block",
        "margin": "0.5em 2em 1em 2em",  # Add top margin to give space and center horizontally,
        "border": cv_border,
        "shadow": "0 0.2em 0.4em" + shadow_color
    }

class State(rx.State):
    """The app state."""

    pass


def main_content():
    return rx.span(
        rx.heading("Daniel Moreno", style={"text-align": "center", "width": "100%"}),
        rx.hstack(
            rx.link(
                rx.image(src='linkedin.png', style={"width": "2em", "height": "2em"}),
                href="https://www.linkedin.com/in/daniel-moreno-006869241/",
                style={"color": "white", "font-size": "1.5em", "margin": "0.5em"}
            ),
            rx.link(
                rx.image(src='github-mark/github-mark.png', style={"width": "2em", "height": "2em", "background_color": "white"}),  # Change the source to the light version of the GitHub mark
                href="https://github.com/danmorper",
                style={"color": "white", "font-size": "1.5em", "margin": "0.5em"}
            ),
        ),
        #rx.heading("Who am I?", style={"margin": "3em", "text-align": "center", "width": "100%"}),
        rx.image(src="/CV.jpg", style=Styles.CV_image),
        rx.box(  # Changed from rx.card to rx.box for custom styling
            rx.heading("Introducción", style={"text-align": "center", "width": "100%"}),
            rx.text("Data enthusiast with a strong background in mathematics and statistics."),
            style= Styles.cards
        ),
        rx.box(  # This box should act as the card for the education section
            rx.heading("Education", style={"text-align": "center", "width": "100%"}),
            rx.unordered_list(
                rx.list_item("Bachelor of Science in Mathematics from the University of Sevilla. 2018-2024"),
                rx.list_item("Bachelor of Science in Statistics from the University of Sevilla. 2018-2024"),
                rx.list_item("Erasmus Exchange Program at the Technical University of Munich, focusing on Data Science and Machine Learning. 2021-2022"),
            ),
            style=Styles.cards  # Make sure this style is applied to the education box
        ),
        rx.box(
            rx.heading("Projects", style={"text-align": "center", "width": "100%"}),
            rx.unordered_list(
                rx.list_item("Data Science and Machine Learning projects:")
            ),
            style=Styles.cards
        ),
        rx.box(
            rx.heading("Languages", style={"text-align": "center", "width": "100%", "font-size": "1.4em", "font-weight": "bold"}),
            rx.unordered_list(
                rx.list_item("Spanish - Native"),
                rx.list_item("English - Professional Proficiency (C1)"),
                rx.list_item("German - Intermediate (B1)"),
                style={"padding-left": "1em", "text-align": "left", "line-height": "1.6em"}
            ),
            style=Styles.cards
        ),

        rx.box(  # This box should act as the card for the experience section
            rx.heading("Experience", style={"text-align": "center", "width": "100%"}),
            rx.text("Content Writer at Simpleclub (Aug2022-Nov2022)", 
                style={"text-align": "center", "font-size": "1.2em", "font-weight": "bold", "font-style": "italic"}
                ),
            rx.unordered_list(
                rx.list_item("Adapt mathematics content to the needs of the Spanish educational system"),
                rx.list_item("Team up with other content writers and designers to create a complete and coherent course")
            ),            
            style=Styles.cards  # Apply the updated card style
        ),
        rx.box(
            rx.heading("Skills", style={"text-align": "center", "width": "100%", "font-size": "1.4em", "font-weight": "bold"}),
            rx.unordered_list(
                rx.list_item("Advanced Mathematics and Statistical Analysis"),
                rx.list_item("Data Science and Machine Learning"),
                rx.list_item("Programming Languages: Python, R"),
                rx.list_item("Databases: SQL, MongoDB"),
                rx.list_item("Web Development: HTML, CSS, JavaScript, PHP, Reflex (Python)"),
                rx.list_item("Version Control: Git/Github"),
                rx.list_item("Software: MS Word, MS Excel"),
                style={"padding-left": "1em", "text-align": "left", "line-height": "1.6em"}
            ),
            style=Styles.cards
        ),
        rx.box(
            rx.heading("Hobbies and Interests", style={"text-align": "center", "width": "100%", "font-size": "1.4em", "font-weight": "bold"}),
            rx.text("I am deeply passionate about aquatic sports and enjoy both competitive and recreational swimming. I have a strong interest in linguistics and am actively improving my German. In my spare time, I also delve into web development and experiment with AI through OpenAI's API, exploring the intersection between technology and creativity."),
            style=Styles.cards
        ),


        style=Styles.aboutme_main_content
    )
def index():
    return rx.vstack(
        rx.box(
            # sidebar(),
            main_content(),
        ),
        style=Styles.aboutme
    )



# Add state and page to the app.
app = rx.App()
app.add_page(index)
