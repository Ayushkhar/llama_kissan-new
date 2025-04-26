# Hey Kissan - LLaMA 7B Agri Assistant 🇮🇳🌾

This model is a fine-tuned version of LLaMA 7B, built using QLoRA for agriculture-based Q&A for Indian farmers.

## 🚜 Example Prompts

- "How to grow paddy in Punjab?"
- "What is the best fertilizer for wheat in Haryana?"
- "How to irrigate sugarcane?"

## 📦 Model Details

- Base: LLaMA 7B (QLoRA, 4-bit)
- Finetuned with 10,000 custom agriculture examples
- Tokenizer + Adapter included

## 🔁 Usage

```python
import replicate

output = replicate.run(
  "your-username/hey-kissan-agri-assistant",
  input={"prompt": "How to grow paddy in Punjab?"}
)
print(output)
