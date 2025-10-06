
import random
import tkinter as tk
from tkinter import scrolledtext

# -------- Knowledge Base --------
responses_simple = {
    "courses": ["NRIIT offers B.Tech and M.Tech programs."],
    "admission": ["Admissions are based on EAPCET and management quota."],
    "default": ["Please ask about courses or admission."]
}

responses_enhanced = {
    "courses": [
        "NRIIT offers B.Tech in CSE, ECE, EEE, Mechanical, Civil, AI&DS, and IoT.",
        "We also provide M.Tech and MBA programs approved by AICTE."
    ],
    "admission": [
        "Admissions at NRIIT are based on EAPCET ranks and management quota.",
        "You can apply online or visit the campus directly."
    ],
    "fees": [
        "B.Tech fee is around ₹75,000 per year.",
        "M.Tech and MBA fees vary; contact admission office."
    ],
    "location": [
        "NRIIT is located in Agiripalli, near Vijayawada, Andhra Pradesh.",
        "The campus is well-connected by road and near the city center."
    ],
    "facilities": [
        "We have hostels, labs, library, Wi-Fi campus, transport, and canteen."
    ],
    "placements": [
        "Companies like Infosys, TCS, Wipro visit NRIIT for placements.",
        "Placement training, aptitude, and soft skills sessions are provided."
    ],
    "contact": [
        "Email: info@nriit.edu.in | Phone: +91-866-1234567",
        "Website: www.nriit.edu.in"
    ],
    "default": [
        "I'm sorry, I didn't understand that. Please ask about courses, admission, fees, facilities, or placements."
    ]
}

# -------- Chatbot Logic --------
def get_response(user_input, version="enhanced"):
    if version == "simple":
        data = responses_simple
    else:
        data = responses_enhanced
    user_input = user_input.lower()
    if any(word in user_input for word in ["course", "branch", "program"]):
        return random.choice(data.get("courses", data["default"]))
    elif any(word in user_input for word in ["admission", "apply", "join"]):
        return random.choice(data.get("admission", data["default"]))
    elif any(word in user_input for word in ["fee", "fees", "payment"]):
        return random.choice(data.get("fees", data["default"]))
    elif any(word in user_input for word in ["location", "where", "place"]):
        return random.choice(data.get("location", data["default"]))
    elif any(word in user_input for word in ["facility", "hostel", "library", "transport"]):
        return random.choice(data.get("facilities", data["default"]))
    elif any(word in user_input for word in ["placement", "job", "career"]):
        return random.choice(data.get("placements", data["default"]))
    elif any(word in user_input for word in ["contact", "email", "phone", "website"]):
        return random.choice(data.get("contact", data["default"]))
    else:
        return random.choice(data.get("default"))

# -------- GUI Version --------
def start_gui():
    def send_message():
        user_input = entry.get()
        if user_input.strip() != "":
            chat_window.config(state='normal')
            chat_window.insert(tk.END, "You: " + user_input + "\n")
            bot_reply = get_response(user_input)
            chat_window.insert(tk.END, "Bot: " + bot_reply + "\n\n")
            chat_window.config(state='disabled')
            chat_window.yview(tk.END)
            entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("🤖 NRIIT AI Chatbot - GUI")
    root.geometry("500x500")

    chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
    chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, width=60)
    entry.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.X, expand=True)

    send_button = tk.Button(root, text="Send", command=send_message, width=8)
    send_button.pack(padx=5, pady=10, side=tk.RIGHT)

    root.mainloop()

# -------- Console Version --------
def start_console(version="enhanced"):
    print(f"🤖 Welcome to NRIIT Chatbot ({version} version)!")
    print("Ask me anything about NRIIT. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Thank you! Have a great day 😊")
            break
        print("Bot:", get_response(user_input, version=version))

# -------- Main Menu --------
def main_menu():
    print("=== NRIIT AI Chatbot ===")
    print("Select version to run:")
    print("1 - Simple Console Chatbot")
    print("2 - Enhanced Console Chatbot")
    print("3 - GUI Chatbot (Tkinter)")
    choice = input("Enter choice (1/2/3): ")
    if choice == "1":
        start_console(version="simple")
    elif choice == "2":
        start_console(version="enhanced")
    elif choice == "3":
        start_gui()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main_menu()
