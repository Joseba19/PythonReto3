FILENAME = "chat_hiystory.txt"
palabrotas = ("tonto")

print("Welcome to the chat! Type 'q' to exit.")

while True:
    message = input("You: ")
    
    if message == "q":
        break
    
    if palabrotas in message:
        print("Mensaje no guardado por contener palabrotas")
    else:
        with open(FILENAME, "a") as f:
            f.write(f"{message}\n")
        print(f"[Saved] {message}")