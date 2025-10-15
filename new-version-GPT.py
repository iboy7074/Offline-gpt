import os
import random

BASE_PATH = "gpt_cyber_ai"

def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"📁 Created new folder: {folder_path}")

def create_default_answer(folder_path):
    default_text = "This is a new topic. Add more answers later!"
    file_path = os.path.join(folder_path, "default.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(default_text)
    print(f"📝 Default answer created in: {file_path}")

def create_custom_txt(folder, filename, message):
    folder_path = os.path.join(BASE_PATH, folder)
    ensure_folder_exists(folder_path)
    file_path = os.path.join(folder_path, f"{filename}.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(message)
    return f"✅ File '{filename}.txt' created inside '{folder}' with your message."

def list_folders():
    if not os.path.exists(BASE_PATH):
        return "📂 No folders found."
    folders = [f for f in os.listdir(BASE_PATH) if os.path.isdir(os.path.join(BASE_PATH, f))]
    return "\n".join(f"📁 {f}" for f in folders) if folders else "📂 No folders found."

def list_files_in(folder):
    folder_path = os.path.join(BASE_PATH, folder)
    if not os.path.exists(folder_path):
        return "❌ Folder not found."
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    return "\n".join(f"📄 {f}" for f in files) if files else "📂 No .txt files in folder."

def delete_file(folder, filename):
    file_path = os.path.join(BASE_PATH, folder, f"{filename}.txt")
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"🗑️ File '{filename}.txt' deleted from '{folder}'."
    return "❌ File not found."

def chatbot(user_input):
    user_input = user_input.strip()

    # 🔧 Handle commands
    if user_input.startswith("/create folder "):
        folder = user_input.replace("/create folder ", "").strip()
        folder_path = os.path.join(BASE_PATH, folder)
        ensure_folder_exists(folder_path)
        create_default_answer(folder_path)
        return f"📁 Folder '{folder}' created."

    elif user_input.startswith("/add txt file "):
        try:
            parts = user_input.replace("/add txt file ", "").split("|")
            folder = parts[0].strip()
            filename = parts[1].strip()
            message = parts[2].strip()
            return create_custom_txt(folder, filename, message)
        except:
            return "⚠️ Invalid format! Use: /add txt file folder | filename | message"

    elif user_input == "/list folders":
        return list_folders()

    elif user_input.startswith("/list files in "):
        folder = user_input.replace("/list files in ", "").strip()
        return list_files_in(folder)

    elif user_input.startswith("/delete file "):
        try:
            parts = user_input.replace("/delete file ", "").split("|")
            folder = parts[0].strip()
            filename = parts[1].strip()
            return delete_file(folder, filename)
        except:
            return "⚠️ Invalid format! Use: /delete file folder | filename"

    # 🔎 Normal folder mode (get random .txt)
    folder_path = os.path.join(BASE_PATH, user_input.lower())
    if not os.path.isdir(folder_path):
        ensure_folder_exists(folder_path)
        create_default_answer(folder_path)
        return f"🆕 New topic created: '{user_input}'. Please add .txt files."

    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    if not files:
        return "⚠️ Folder exists but no .txt files found."

    chosen = random.choice(files)
    file_path = os.path.join(folder_path, chosen)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    return (
        f"🔗 **Link from '{user_input}' folder:**\n"
        f"👉 {content}\n\n"
        "📌 Copy this link and use it only once per day!\n"
        "📝 Paste in Telegram/Browser to access."
    )

# 🔁 Main Loop
print("🤖 GPT CYBER AI – Full Chatbot Shell")
print("Type 'exit' to quit.\n")
print("Available commands:")
print(" - /create folder <folder_name>")
print(" - /add txt file <folder> | <filename> | <message>")
print(" - /list folders")
print(" - /list files in <folder>")
print(" - /delete file <folder> | <filename>")
print(" - Or type any topic name (folder)\n")

while True:
    user = input("🧑 You: ")
    if user.lower() == "exit":
        print("🤖 Chatbot: Goodbye!")
        break
    print("🤖", chatbot(user))
