# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass

def get_button(button_text , img_src,href_url):
    return pc.link(
                pc.hstack(
                    pc.image(
                                src=img_src,
                                width="30px" 
                            ),
                            
                    pc.text(button_text, 
                        font_size="20px", 
                        font_weight= "500",
                        font_family="DM Sans",
                        text_align= "center",
                        color='#57618A',
                        width="calc(100% - 80px)"
                        
                    ),

                    padding="9px 7px",
                    width="95vw", 
                    max_width= "700px", 
                    border="1px solid rgb(128, 160, 201)",
                    border_radius="5px",
                    bg='white',


                    box_shadow = "rgb(128 160 201) 8px 8px 0px 0px",

                    _hover={
                        "cursor": "pointer",
                        "translate": "4px 4px",
                        "box_shadow":"rgb(128 160 201) 4px 4px 0px 0px"
                    },
        
                ),

                href=href_url,
                _hover={}
        )

def get_social_media_button(image_path, href_url):
    return pc.link(
                pc.image(
                        src=image_path,
                        width='60px',
                        _hover={
                                    "cursor": "pointer",
                                    "transform": "scale(1.1)",
                                },
                    ),
                    href=href_url
            )



def index() -> pc.Component:
    return  pc.box(
                pc.center(
                    pc.vstack(
                    pc.vstack(
                        pc.image(
                                src="profile_pic.png", 
                                width="168px", 
                                height="168px",
                                border_radius="50%",
                                margin_bottom="8px",
                                ),
                        pc.text("Minnie lda", 
                                font_weight="700",
                                font_size="36px", 
                                line_height='1.5em',
                                font_family="DM Sans",
                                text_align= "center",
                                width="100%",
                                color = "rgb(255, 255, 255)",
                                padding_bottom='3px'
                            ),

                        pc.text("Community focused artist, with a taste for everything local", 
                                font_weight="500",
                                font_size="18px", 
                                font_family="DM Sans",
                                text_align= "center",
                                width="100%",
                                color = "rgb(255, 255, 255)",
                                padding_bottom='30px'
                            ),
                            spacing="0",
                        ),
                        pc.vstack(
                            get_button('Tour dates',
                                       'calendar.png',
                                       "https://google.com"
                                       ),

                            get_button('Our Discord',
                                       'discord.png',
                                       "https://google.com"),

                            get_button('Website',
                                       'link.png',
                                       "https://google.com"),

                            get_button('Email',
                                       'email.png',
                                       "https://google.com"),

                            pc.hstack(
                                get_social_media_button('twitter_logo_white.png',
                                                        'https://twitter.com/'
                                                        ),

                                get_social_media_button('instagram_logo_white.png',
                                                        'https://instagram.com/'
                                                        ),

                                get_social_media_button('facebook_logo_white.png',
                                                        'https://facebook.com/'
                                                        ),

                                   spacing="0.2em",  

                            ),

                            spacing="0.9em",

                            )
                        
                        
                    

                    ),
                    
                    padding_top="36px",
                    width="100vw"
                ),


                bg="linear-gradient(160deg, rgba(103,151,193,255) , rgba(225,156,162,255))",
                width="100vw",
                height="100vh",
                
            )



# Add state and page to the app.
app = pc.App(state=State,
             stylesheets =[
                "https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;500;600;700&display=swap"
             ]
             
             )
app.add_page(index)
app.compile()
