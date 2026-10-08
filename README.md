# Argument Steelman ⚔️

A tool that takes any argument or opinion and constructs the strongest possible counter-argument (steelman) against it. It also finds logical weaknesses, scores the argument, and suggests improvements.

## What is a Steelman?

A steelman is the opposite of a strawman. Instead of misrepresenting the opposing view to make it easier to attack, a steelman builds the **best and strongest version** of the counter-argument, forcing you to actually engage with the toughest criticism of your position.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Get a free Groq API key from https://console.groq.com/keys

3. Run the app:
```
cd src
streamlit run app.py
```

4. Enter your API key in the sidebar and start analyzing arguments.

## Project Structure

```
argument-steelman/
├── config.yaml              - model configuration  
├── prompts/
│   └── system_prompt.txt    - system prompt for the LLM
├── src/
│   └── app.py               - main application (streamlit)
├── requirements.txt
└── README.md
```

## Model Used

- **Model**: Llama 3.1 8B Instant (via Groq)
- **Context Window**: 128,000 tokens
- **Max Output**: 8,192 tokens
- **Type**: Text-to-Text
- **Why this model**: Ultra-fast inference on Groq LPUs, generous free limits (30 RPM, 14,400 RPD), reliable availability

## How It Works

1. User enters an argument in the text box
2. The argument gets sent to the LLM along with the system prompt
3. The model analyzes the argument structure, finds weaknesses, and builds a counter-argument
4. Results are displayed with scores and improvement suggestions

## Tech Stack

- Python
- Streamlit (frontend)
- Groq API with Llama 3.3 70B (LLM)
- PyYAML (config parsing)
