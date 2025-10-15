import os
import random

# folder name replace 
BASE_PATH = "gpt_cyber_ai"

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"📁 Created new folder: {folder_path}")

def create_default_answer(folder_path):
    # Default text to insert
    default_text = "This is a new topic. Add more answers later!"
    file_path = os.path.join(folder_path, "default.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(default_text)
    print(f"📝 Default answer created in: {file_path}")

def chatbot(user_input):
    user_input = user_input.lower().strip()
    folder_path = os.path.join(BASE_PATH, user_input)

    # 🔧 Step 1: Ensure folder exists (if not, create)
    if not os.path.isdir(folder_path):
        ensure_folder_exists(folder_path)
        create_default_answer(folder_path)
        return f"🆕 New topic created: '{user_input}'. Please add more .txt files."

    # 🔧 Step 2: Load answers
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    if not files:
        return "⚠️ Folder exists but no answer files found."

    chosen = random.choice(files)
    with open(os.path.join(folder_path, chosen), 'r', encoding='utf-8') as f:
        return f.read()

# 🔁 Main Chat Loop
print("🤖 ARIS ")
print("Type any topic (folder) name. Type 'exit' to quit.\n")

while True:
    user = input("🧑 You: ")
    if user.lower() == "exit":
        print("🤖 Chatbot: Goodbye!")
        break
    print("🤖", chatbot(user))
