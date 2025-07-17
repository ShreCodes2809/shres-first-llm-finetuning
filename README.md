# 🧠 Palantir Foundry Assistant — Fine-Tuned LLaMA 3.2 with QLoRA

A lightweight, locally-deployable AI assistant designed to help new employees onboard more efficiently by answering questions about Palantir Foundry. This project fine-tunes the **LLaMA 3.2 1B** model using the **QLoRA** technique on Palantir’s technical documentation. The final assistant is capable of answering contextual queries based on internal docs through a streamlined inference setup with **Langflow** and **Ollama**.

---

## 🔍 Project Overview

- **Goal**: Help new Palantir employees understand the Foundry platform through a personalized LLM-powered assistant.
- **Approach**: Fine-tune LLaMA 3.2 locally using QLoRA, powered by instruction-tuned QA pairs generated from documentation.
- **Deployment**: Uses Ollama for local model serving and Langflow for interactive iterative prompting.

---

## 🧱 Key Components

| Component                | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| `palantir_foundry_tech_doc.pdf` | Source document for technical content                   |
| `preprocessing.py`       | Cleans and chunks the PDF content                            |
| `syntheticdatageneration.py` | Uses `Qwen-2.5-14B` locally to generate QA pairs        |
| `generated_prompt.py`    | Formats prompts using LLaMA 3.2’s chat template              |
| `dataquality.py`         | Evaluates answer quality and filters noisy samples           |
| `main.py`                | Orchestrates the QLoRA fine-tuning pipeline                  |
| `Modelfile`              | Ollama configuration to serve the fine-tuned model           |
| `qualityresults.json`    | Stores QA evaluations from the filtering step                |

---

## ⚙️ Workflow

1. **Data Preprocessing**  
   Palantir Foundry docs are chunked into semantically meaningful segments (`preprocessing.py`).

2. **Synthetic QA Generation**  
   QA pairs are generated from each chunk using the local **Qwen-2.5-14B** model (`syntheticdatageneration.py`).

3. **Prompt Formatting**  
   QA pairs are structured into an instruction format compatible with **LLaMA 3.2**’s expected template (`generated_prompt.py`).

4. **Data Quality Filtering**  
   Poorly structured or irrelevant QAs are filtered using rule-based evaluation (`dataquality.py`), and results are logged in `qualityresults.json`.

5. **Fine-Tuning with QLoRA**  
   The cleaned data is used to fine-tune LLaMA 3.2 locally using **QLoRA** in `main.py`.

6. **Deployment**  
   The fine-tuned model is served via **Ollama**, and queried interactively through **Langflow** for real-time feedback and usability testing.

---

## 🧪 Model & Training

- **Base Model**: `LLaMA 3.2-1B`
- **Fine-Tuning Technique**: QLoRA (efficient low-rank adapters for small model tuning)
- **QA Generator**: Qwen-2.5-14B run locally
- **Evaluation**: Rule-based quality scoring and filtering

---

## 💡 Why This Project Matters

New employees often struggle with internal documentation overload. This assistant provides:
- Instant access to high-context, technical answers
- A personalized way to learn Palantir Foundry
- An example of LLM fine-tuning and RAG-ready preprocessing from scratch

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python main.py
ollama run pftech-100:latest
```

Use Langflow or a local CLI for interaction.

---

## 🛠 Tech Stack

| Component         | Tools                                                                 |
|------------------|-----------------------------------------------------------------------|
| **Language**      | Python                                                                |
| **IDE**           | PyCharm                                                               |
| **Libraries**     | `transformers`, `langchain`, `pandas`, `numpy`, `matplotlib`|
| **Models**        | `llama3.2-1b`, `Qwen-2.5-14B`                                          |
| **Prompting**     | Custom chat template for LLaMA 3.2                                    |
| **Fine-Tuning**   | QLoRA                                                                 |
| **Evaluation**    | Rule-based scoring, JSON logging                                      |
| **Deployment**    | Ollama, Langflow                                                      |


---

## 📁 Folder Structure

```bash
├── main.py
├── preprocessing.py
├── syntheticdatageneration.py
├── dataquality.py
├── generated_prompt.py
├── Modelfile
├── qualityresults.json
└── palantir_foundry_tech_doc.pdf
```

---

## 🧠 Future Improvements

- Support for multi-turn conversational memory and chat history.
- Integration with Foundry APIs for real-time, context-aware assistance.
- Extended fine-tuning with additional internal documentation and use-case scenarios.
- GPU-accelerated backend with async I/O and optimized token streaming.
- Web-based UI using Gradio or Langchain Chat components.

---

## 📚 References & Learning Resources

This project was developed with insights and guidance from the following resources:

1. [How to Fine Tune your own LLM using LoRA (on a CUSTOM dataset!)](https://youtu.be/D3pXSkGceY0?si=5PAzWecclTuzRwYx)
2. [Hugging Face PEFT Library (QLoRA support)](https://github.com/huggingface/peft)
3. [Langflow: Visual Framework for Building LLM Apps](https://github.com/logspace-ai/langflow)
4. [Ollama Docs: Running LLMs Locally](https://ollama.com/)
5. [Hugging Face Transformers: Custom Prompt Templates](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationConfig)
6. [QLoRA: Efficient Fine-Tuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)

> These resources guided the development of the pipeline — from prompt engineering and QA generation to local model serving, Langflow integration, and efficient fine-tuning with QLoRA.
