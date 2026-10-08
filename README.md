# NLP Project - Argument Steelman

## Student Information
- **Name**: Lakshya Gupta
- **Registration Number**: 23FE10CDS00519
- **Branch**: Computer Science & Engineering (Data Science)
- **Batch**: Batch F
- **Project Title**: Argument Steelman - NLP-Powered Counter-Argumentation & Debate Analysis
- **GitHub Username**: 14k5hy4
- **Training Program**: NLP & LLM Training Program

---

## Overview

A web tool that takes any argument or opinion and performs a **steelman analysis** on it. A steelman is the opposite of a strawman — instead of attacking a weak version of an argument, it constructs the **strongest possible counter-argument**, identifies logical fallacies/biases, scores the reasoning (1-10), and suggests specific ways to strengthen the original claim.

## Repository Structure

```
MUJ-DS-23FE10CDS00519/
├── README.md               # Student info and project documentation
├── code/                   # Project source code
│   ├── app.py              # Main Streamlit application
│   ├── config.yaml         # Model & inference parameters
│   ├── prompts/
│   │   └── system_prompt.txt # System prompt for argument analysis
│   └── requirements.txt    # Python dependencies
├── assignments/            # Course assignments
├── notebooks/              # Jupyter notebooks
├── resources/              # Project references & docs
├── presentations/          # Presentation slides & docs
└── capstone/               # Capstone project files
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/14k5hy4/MUJ-DS-23FE10CDS00519.git
   cd MUJ-DS-23FE10CDS00519
   ```

2. Install dependencies:
   ```bash
   pip install -r code/requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   cd code
   streamlit run app.py
   ```

4. Enter your Groq API key in the sidebar and click **Steelman This**.

## Model Details
- **Provider**: Groq API
- **Model**: Auto-detected from active models on account (e.g. `llama-3.1-8b-instant`, `llama3-70b-8192`, `gemma2-9b-it`)
- **Type**: Text-to-Text
- **Temperature**: 0.7
- **Max Output**: 4,096 tokens
