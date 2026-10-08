import streamlit as st
from groq import Groq
import yaml


# load config and prompt
def load_config():
    with open("../config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_prompt():
    with open("../prompts/system_prompt.txt", "r") as f:
        return f.read()


def get_available_models(client):
    try:
        models = client.models.list()
        chat_models = [
            m.id for m in models.data 
            if not m.id.startswith("whisper") and not "guard" in m.id
        ]
        return chat_models
    except Exception:
        return []


def analyze(client, model_name, argument):
    """send argument to groq and get steelman analysis back"""
    config = load_config()
    model_cfg = config["model"]
    prompt = load_prompt()
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Analyze this argument:\n\n{argument}"},
        ],
        temperature=model_cfg.get("temperature", 0.7),
        max_tokens=model_cfg.get("max_tokens", 4096),
        top_p=model_cfg.get("top_p", 0.95),
    )
    
    return response.choices[0].message.content


# --- page setup ---
st.set_page_config(page_title="Argument Steelman", page_icon="⚔️", layout="wide")

st.markdown("""
<style>
    .main-title { text-align: center; padding: 0.5rem 0; }
    .main-title h1 { color: #667eea; font-size: 2.5rem; }
    .main-title p { color: #888; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
    <h1>⚔️ Argument Steelman</h1>
    <p>Enter any argument and get the strongest possible counter-argument</p>
</div>
""", unsafe_allow_html=True)


# --- sidebar ---
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input(
        "Groq API Key",
        type="password",
        help="Get yours free at https://console.groq.com/keys"
    )
    
    selected_model = None
    if api_key:
        try:
            client = Groq(api_key=api_key)
            models = get_available_models(client)
            if models:
                st.success(f"Connected! {len(models)} models available")
                selected_model = st.selectbox("Select Model", models, index=0)
            else:
                st.warning("No chat models found for this key.")
        except Exception as e:
            st.error(f"Invalid API Key or connection error: {e}")
    
    st.divider()
    st.subheader("Try these examples")
    examples = [
        "Social media has made society more connected overall.",
        "AI will replace most human jobs within 10 years.",
        "College degrees are no longer worth the cost.",
        "Remote work is always more productive than office work.",
    ]
    for i, ex in enumerate(examples):
        if st.button(ex, key=f"ex_{i}"):
            st.session_state["user_arg"] = ex


# --- main area ---
argument = st.text_area(
    "Enter your argument:",
    value=st.session_state.get("user_arg", ""),
    height=150,
    max_chars=5000,
    placeholder="Type your argument or opinion here..."
)

if st.button("⚔️ Steelman This", use_container_width=True):
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    elif not argument or len(argument.strip()) < 20:
        st.warning("Please write a more detailed argument.")
    elif not selected_model:
        st.error("Please enter a valid API key to load available models.")
    else:
        try:
            client = Groq(api_key=api_key)
            with st.spinner(f"Analyzing argument with {selected_model}..."):
                result = analyze(client, selected_model, argument)
            
            st.divider()
            st.markdown("## Analysis Results")
            st.markdown(result)
            
        except Exception as e:
            st.error(f"Something went wrong: {e}")


st.markdown("---")
st.caption("Built with Streamlit & Groq")
