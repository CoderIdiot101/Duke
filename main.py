from PIL import Image
import streamlit as st
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Dukepaw Studios', page_icon=':heart:', layout='wide')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile('coding.json')
lottie_sending = load_lottiefile('send.json')
lottie_first = load_lottiefile('welcome.json')

img_contact_form = Image.open("images/Image.PNG")
Duke = Image.open("images/duke.PNG")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():
    left, right = st.columns(2)
    with left:
        st.image(Duke)
    with right:
        st_lottie(lottie_first, height=500, key="welcome")
    st.title('A Show For My GameDev Journey')
    st.write('Im Passionate About Ways To find Your Likings And Dreams To come true in GAMES!')
    st.write("[Support Me >](https://coderidiot.itch.io/)")
    st.write("[Support My Father >](https://www.mas4d.co.za/)")

with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.header("What Do I Do?")
        st.write('##')
        st.write(
            """
            On My Itch Page I Upload All My Games I Make And I Am:
            - Looking For Ways To Better gaming Community
            - Trying To Build My Self A Future
            - Doing It Because I LOVE It!
            """
        )

        st.write('[My Itch Page >](https://coderidiot.itch.io/)')

    with right:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Best Work!")
    st.write("##")
    image, text = st.columns((1, 2))
    with image:
        st.image(img_contact_form)
    with text:
        st.subheader("This Is Some OF My Best Work Ever Created")
        st.write(
            """
            Let Me Tell You That Farm Topia TOOK Two and a half Weeks To create because of me losing some work!
            Now yes thats very good and all but I never Gave Up!
            So Im Telling You To Never Ever GIVE UP!
            """
            )
        st.markdown("[Check FarmTopia Out...](https://coderidiot.itch.io/farmtopia-demo)")


with st.container():
    st.write("---")
    st.write("Get In Touch About Any Ideas?")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/C0D3R1D10T@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left, right = st.columns(2)
    with left:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right:
        st_lottie(lottie_sending, height=300, key="Send")
