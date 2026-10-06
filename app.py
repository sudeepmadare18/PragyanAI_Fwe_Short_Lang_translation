import streamlit as st
from groq import Groq
import os

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="English → Kannada Translator",
    page_icon="🌐",
    layout="centered"
)

# ==========================================
# GROQ CLIENT
# ==========================================

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY2")
)

# ==========================================
# FEW-SHOT EXAMPLES
# ==========================================

examples = """
Example 1:
English: Good morning.
Kannada: ಶುಭೋದಯ.

Example 2:
English: How are you?
Kannada: ನೀವು ಹೇಗಿದ್ದೀರಿ?

Example 3:
English: I am going to school.
Kannada: ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತಿದ್ದೇನೆ.

Example 4:
English: I love learning new things.
Kannada: ನನಗೆ ಹೊಸ ವಿಷಯಗಳನ್ನು ಕಲಿಯುವುದು ಇಷ್ಟ.

Example 5:
English: What is your name?
Kannada: ನಿಮ್ಮ ಹೆಸರೇನು?
"""

# ==========================================
# TRANSLATION FUNCTION
# ==========================================

def translate_to_kannada(english_text):

    prompt = f"""
You are an expert English to Kannada translator.

Translate the English sentence into natural,
clear and grammatically correct Kannada.

Use the following examples as guidance:

{examples}

Now translate this sentence:

English: {english_text}

Kannada:
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# ==========================================
# STREAMLIT UI
# ==========================================

st.title("🌐 English → Kannada Translator")

st.write(
    "Few-Shot Prompt Engineering using Groq LLM"
)

english_text = st.text_area(
    "Enter English Text",
    placeholder="Enter an English sentence here..."
)

if st.button("Translate to Kannada"):

    if english_text.strip():

        with st.spinner("Translating..."):

            try:
                result = translate_to_kannada(
                    english_text
                )

                st.subheader("Kannada Translation")

                st.success(result)

            except Exception as e:

                st.error(
                    f"Error occurred: {e}"
                )

    else:

        st.warning(
            "Please enter an English sentence."
        )
