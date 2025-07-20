from pdf_utils import extract_text_from_pdf
from ai_assistant import summarize_text, chat_with_ai
from audio_converter import text_to_speech

def main():
    print("=== SmartPDF Assistant ===")
    pdf_path = input("Enter the path to the PDF file: ")

    text = extract_text_from_pdf(pdf_path)
    print("\n--- PDF Extracted ---\n")

    while True:
        print("\nChoose an option:")
        print("1. Summarize PDF")
        print("2. Chat with AI")
        print("3. Convert PDF to Audio")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            summary = summarize_text(text)
            print("\n--- Summary ---\n", summary)

        elif choice == "2":
            user_input = input("Ask AI: ")
            response = chat_with_ai(user_input)
            print("\nAI:", response)

        elif choice == "3":
            audio_file = "pdf_audio.mp3"
            text_to_speech(text, audio_file)
            print(f"Audio saved as {audio_file}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
