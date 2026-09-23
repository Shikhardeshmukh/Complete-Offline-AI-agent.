import ollama
import os
from datetime import datetime

MODEL = "qwen3:4b"
NOTES_FILE = "data/notes.txt"


def setup():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8") as file:
            file.write("")


def ask_ai(prompt):
    try:
        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful offline AI assistant. "
                        "Give clear, practical and concise answers."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


def save_note(note):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {note}\n")

    print("\nAssistant: Note saved successfully!")


def show_notes():
    if not os.path.exists(NOTES_FILE):
        print("\nAssistant: No notes found.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.read().strip()

    if not notes:
        print("\nAssistant: No notes found.")
    else:
        print("\n========== YOUR NOTES ==========")
        print(notes)
        print("================================")


def summarize_file(file_path):
    if not os.path.exists(file_path):
        print("\nAssistant: File not found.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            print("\nAssistant: The file is empty.")
            return

        prompt = f"""
Summarize the following text.

Give:
1. Main idea
2. Important points
3. Short conclusion

TEXT:
{content}
"""

        print("\nAssistant: Analyzing file...\n")
        result = ask_ai(prompt)

        print(result)

    except Exception as e:
        print(f"\nAssistant: Could not read the file. {e}")


def print_help():
    print("""
========== OFFLINE AI ASSISTANT ==========

Commands:

/help
    Show available commands.

/note <text>
    Save a personal note.

/notes
    Show saved notes.

/summarize <file>
    Summarize a local text file.

/clear
    Clear the terminal.

/exit
    Exit the assistant.

Anything else:
    Ask the AI normally.

==========================================
""")


def main():
    setup()

    print("\n==========================================")
    print("       OFFLINE AI ASSISTANT")
    print("==========================================")
    print(f"Model: {MODEL}")
    print("Running locally using Ollama")
    print("Internet is NOT required.")
    print("Type /help to see commands.")
    print("==========================================\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "/exit":
                print("\nAssistant: Goodbye! 👋")
                break

            elif user_input.lower() == "/help":
                print_help()

            elif user_input.lower() == "/notes":
                show_notes()

            elif user_input.lower() == "/clear":
                os.system("cls" if os.name == "nt" else "clear")

            elif user_input.lower().startswith("/note "):
                note = user_input[6:].strip()

                if note:
                    save_note(note)
                else:
                    print("\nAssistant: Please enter a note.")

            elif user_input.lower().startswith("/summarize "):
                file_path = user_input[11:].strip()
                summarize_file(file_path)

            else:
                print("\nAssistant: Thinking...\n")

                response = ask_ai(user_input)

                print(f"Assistant: {response}\n")

        except KeyboardInterrupt:
            print("\n\nAssistant: Goodbye! 👋")
            break

        except Exception as e:
            print(f"\nUnexpected error: {e}\n")


if __name__ == "__main__":
    main()