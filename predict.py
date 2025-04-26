import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

def load_model():
    base_model = "meta-llama/Llama-2-7b-hf"
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        device_map="auto",
        load_in_4bit=True,
        quantization_config=BitsAndBytesConfig(load_in_4bit=True)
    )
    model = PeftModel.from_pretrained(model, "model/")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

def predict(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
    return tokenizer.decode(output[0], skip_special_tokens=True)
