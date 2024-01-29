from rxconfig import config
import reflex as rx

from combine import combine_dicts
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
        "height": "620vh",
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
        "border": border_card
        }

    CV_image = {
        "width": "10em",  # Adjust this value as needed to make the image smaller
        "height": "15em",
        "display": "block",
        "margin": "0.5em 2em 1em 2em",  # Add top margin to give space and center horizontally,
        "border": cv_border,
        "shadow": "0 0.2em 0.4em" + shadow_color
    }

    heading_cards = {
        "text-align": "center", 
        "width": "100%",
          "margin": "0 0 0.5em 0"
    }

class State(rx.State):
    """The app state."""

    pass

def education():
    return rx.box(
        rx.heading("Education", style=Styles.heading_cards),
        rx.box(
            rx.box("2018-2024", style={"grid-area": "date1", "font-weight": "bold"}),
            rx.box("Bachelor of Science in Mathematics from the University of Sevilla.", style={"grid-area": "degree1"}),
            rx.box("2018-2024", style={"grid-area": "date2", "font-weight": "bold"}),
            rx.box("Bachelor of Science in Statistics from the University of Sevilla.", style={"grid-area": "degree2"}),
            rx.box("2021-2022", style={"grid-area": "date3", "font-weight": "bold"}),
            rx.box("Erasmus Exchange Program at the Technical University of Munich, focusing on Data Science and Machine Learning.", style={"grid-area": "degree3"}),
            style={
                "display": "grid",
                "grid-template-areas": "'date1 degree1' 'date2 degree2' 'date3 degree3'",
                "grid-gap": "1em",
                "align-items": "start"
            }
        ),
        rx.text("Both the Bachelor of Science in Mathematics and the Bachelor of Science in Statistics are part of a double degree program, together summing 342 ECTS.", style={"font-size": "0.7em", "text-align": "center"}),
        style=Styles.cards
    )



class Projects():

    def header():
        return rx.box(
            rx.heading("Projects", style=Styles.heading_cards),
        )

    def swimming_app():
        return rx.box(
            rx.text("Swimming Data Analysis and Management with Streamlit", style={"display":"block","text-align": "center", "width": "100%", "font-size": "1.3em", "font-weight": "bold"}),
            rx.markdown("Developed an interactive web application using **Streamlit** that facilitates the analysis and management of swimming data. Integrated **Pandas** for data manipulation and utilized **OpenAI's API** within a Python environment to enhance analytics capabilities.", style={"text-align": "center"}),
            rx.link(
                rx.hstack(
                    rx.image(src='github-mark/github-mark-white.png', style={"width": "2em", "height": "2em", "background_color": "black"}),  # Change the source to the light version of the GitHub mark
                    rx.text("View on GitHub")
                ),
                href="https://github.com/danmorper/swimming-app",
                style={"align-self": "center", "margin": "1em 0 0 0"}
            ),
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "flex-start",
                "padding": "1em",
                "margin": "1em",
                "border": "2px solid #3498DB",  # Blue border for visibility
                "border-radius": "0.5em"
            }
        )
    def webscrapping():
        return rx.box(
            rx.text("Webscrapping: Swimming Competition Data", style={"display":"block","text-align": "center", "width": "100%", "font-size": "1.3em", "font-weight": "bold"}),
            rx.markdown("Created an automated system for extracting swimming competition results using **Selenium**. Implemented processes to convert PDF data into CSV format, organizing and merging datasets effectively while leveraging headless browsing techniques for efficiency.", style={"text-align": "center"}),
            rx.link( 
                rx.hstack(
                    rx.image(src='github-mark/github-mark-white.png', style={"width": "2em", "height": "2em", "background_color": "black"}), 
                    rx.text("View on GitHub"), 
                ),
            href="https://github.com/danmorper/automatization-swimming-data",
            style={"align-self": "center", "margin": "1em 0 0 0"}
            ),
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "flex-start",
                "padding": "1em",
                "margin": "1em",
                "border": "2px solid #3498DB",  # Blue border for visibility
                "border-radius": "0.5em"
            }
        )
    
    def reflex_chatbot():
        return rx.box(
            rx.text("Reflex Chatbot", style={"display":"block","text-align": "center", "width": "100%", "font-size": "1.3em", "font-weight": "bold"}),
            rx.markdown("Developed a Reflex-based chatbot proficient in understanding and processing human language, utilizing OpenAI's API within a Python environment to enable responsive and intelligent user interactions.", style={"text-align": "center"}),
            rx.link(
                rx.hstack(
                    rx.image(src='github-mark/github-mark-white.png', style={"width": "2em", "height": "2em", "background_color": "black"}),  # Change the source to the light version of the GitHub mark
                    rx.text("View on GitHub"),                
            ),
            href="https://github.com/danmorper/reflex-tutorial",
            style={"align-self": "center", "margin": "1em 0 0 0"}
            ),
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "flex-start",
                "padding": "1em",
                "margin": "1em",
                "border": "2px solid #3498DB",  # Blue border for visibility
                "border-radius": "0.5em"
            }
        )
    def web_development_databases():
        return rx.box(
            rx.text("Web Development and Databases", style={"display":"block","text-align": "center", "width": "100%", "font-size": "1.3em", "font-weight": "bold"}),
            rx.markdown("Developed a full-stack web application integrating **HTML**, CSS, **JavaScript**, and **PHP** with a **SQL** and **MongoDB** backend to manage complex datasets.", style={"text-align": "center"}),
            rx.link(
                rx.hstack(
                    rx.image(src='github-mark/github-mark-white.png', style={"width": "2em", "height": "2em", "background_color": "black"}),  # Change the source to the light version of the GitHub mark
                    rx.text("View on GitHub"), 
                ),
                href="https://github.com/danmorper/trabajo-base-datos",
                style={"align-self": "center", "margin": "1em 0 0 0"}
            ),
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "flex-start",
                "padding": "1em",
                "margin": "1em",
                "border": "2px solid #3498DB",  # Blue border for visibility
                "border-radius": "0.5em"
            }
        )
    def rincon():
        return rx.box(
            rx.text("Personal Blog with Reflex", style={"display":"block","text-align": "center", "width": "100%", "font-size": "1.3em", "font-weight": "bold"}),
            rx.markdown("Constructed a personal blog platform using **Reflex**, a **Python**-based framework, to publish content and share insights. Designed to be a reflective space for personal and professional growth, with a focus on simplicity and minimalism.", style={"text-align": "center"}),
            rx.link(
                rx.hstack(
                    rx.image(src='github-mark/github-mark-white.png', style={"width": "2em", "height": "2em", "background_color": "black"}),  # Change the source to the light version of the GitHub mark
                    rx.text("View on GitHub"), 
                ),
                href="https://github.com/danmorper/el-rincon-del-caballero",
                style={"align-self": "center", "margin": "1em 0 0 0"}
            ),
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "flex-start",
                "padding": "1em",
                "margin": "1em",
                "border": "2px solid #3498DB",  # Blue border for visibility
                "border-radius": "0.5em"
            }
        )
    def this_website():
        return rx.box(
            rx.text("This website", style={"display":"block","text-align": "center", "width": "100%", "font-size": "1.3em", "font-weight": "bold"}),
            rx.markdown("Crafted this professional portfolio website to showcase my projects and skills. Built with **Reflex** and **Python**", style={"text-align": "center"}),
            rx.link(
                rx.hstack(
                    rx.image(src='github-mark/github-mark-white.png', style={"width": "2em", "height": "2em", "background_color": "black"}),  # Change the source to the light version of the GitHub mark
                    rx.text("View on GitHub"), 
                ),
                href="https://github.com/danmorper/myweb",
                style={"align-self": "center", "margin": "1em 0 0 0"}
            ),
            style={
                "display": "flex",
                "flex-direction": "column",
                "align-items": "flex-start",
                "padding": "1em",
                "margin": "1em",
                "border": "2px solid #3498DB",  # Blue border for visibility
                "border-radius": "0.5em"
            }
        )


def languages():
    return rx.box(
            rx.heading("Languages", style=Styles.heading_cards),
            rx.span(
                rx.markdown("**Spanish** - Native"),
                rx.markdown("**English** - Professional Proficiency (C1)"),
                rx.markdown("**German** - Intermediate (B1)"),
            ),
            style=combine_dicts(Styles.cards, {"text-align": "center",})
        )
def skills():
    return rx.box(
            rx.heading("Skills", style=Styles.heading_cards),
            rx.span(
                rx.markdown("Advanced Mathematics and Statistical Analysis"),
                rx.markdown("**Data Science** and **Machine Learning**"),
                rx.markdown("Programming Languages: **Python**, **R**"),
                rx.markdown("Databases: **SQL**MongoDB"),
                rx.markdown("Web Development: HTML, CSS, JavaScript, PHP, Reflex (Python)"),
                rx.markdown("Version Control: Git/Github"),
                rx.markdown("Software: MS Word, MS Excel"),
                style={"text-align": "center"}
            ),
            style=Styles.cards
        )
def hobbies():
    return rx.box(
            rx.heading("Hobbies and Interests", style=Styles.heading_cards),
            rx.markdown("I am deeply passionate about aquatic sports and enjoy both competitive and recreational **swimming**. I have a strong interest in languages and I am actively improving my **German**. In my spare time, I also delve into web development and experiment with **LLM** through **OpenAI's API**, exploring the intersection between technology and creativity.", style={"text-align": "center"}),
            style=Styles.cards
        )
def experience():
    return rx.box(  # This box should act as the card for the experience section
            rx.heading("Experience", style=Styles.heading_cards),
            rx.text("Content Writer at Simpleclub (Aug2022-Nov2022)", 
                style={"text-align": "center", "font-size": "1.2em", "font-weight": "bold", "font-style": "italic", "border-bottom": "1px solid #B1D4E0"}
                ),
            rx.span(
                rx.markdown("Adapted mathematics content to the needs of the Spanish educational system"),
                rx.markdown("Team up with other content writers and designers to create a complete and coherent course"),
                rx.link(rx.markdown("*Click to read Reference Letter*"), href="https://drive.google.com/file/d/1TUs9L_YbaJVAJLx4B-6RlNFB6XftrOsS/view?usp=drive_link", style={"text-align": "center"}),
                style={"text-align": "center"}
            ),            
            style=Styles.cards  # Apply the updated card style
        )
def connect():
    return rx.hstack(
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
        )
def main_content():
    return rx.span(
        rx.heading("Daniel Moreno", style=Styles.heading_cards),
        connect(),
        #rx.heading("Who am I?", style={"margin": "3em", "text-align": "center", "width": "100%"}),
        rx.image(src="/CV.jpg", style=Styles.CV_image),
        rx.box(  # Changed from rx.card to rx.box for custom styling
            rx.heading("Introduction", style=Styles.heading_cards),
            rx.text("Data enthusiast, Mathematician, and Statistician, currently working on my bachelor's thesis on deep neural network models for detection and classification in medical imaging.", style={"text-align": "center"}),
            style= Styles.cards
        ),
        education(),
        rx.box(
            Projects.header(),
            Projects.swimming_app(),
            Projects.webscrapping(),
            Projects.reflex_chatbot(),
            Projects.web_development_databases(),
            Projects.rincon(),
            Projects.this_website(),
            style=Styles.cards
        ),
        languages(),
        experience(),
        skills(),
        hobbies(),
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
