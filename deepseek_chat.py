from transformers import AutoTokenizer, AutoModelForCausalLM
import os

modelo = "deepseek-ai/deepseek-llm-7b-chat"

if not os.path.exists("offload"):
    os.makedirs("offload")

print("🔄 Cargando tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(modelo)

print("🔄 Cargando modelo con offload...")
model = AutoModelForCausalLM.from_pretrained(
    modelo,
    device_map="auto",
    torch_dtype="auto",
    offload_folder="offload"
)

while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("👋 Hasta luego")
        break

    input_ids = tokenizer(entrada, return_tensors="pt").input_ids.to(model.device)
    output = model.generate(input_ids, max_new_tokens=100, temperature=0.7)
    respuesta = tokenizer.decode(output[0], skip_special_tokens=True)

    print("\n🤖 DeepSeek:", respuesta)











