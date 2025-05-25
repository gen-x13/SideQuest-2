""" #genxcode - SIDEQUEST : Chatbot ! """

import customtkinter as ctk
import datetime

clock = datetime.datetime.now()

# Function for bot's answers

def chatbot_response(user_input):
    
    responses = {
        
        "hello":"Welcome, how can I help you today ?",
        "how are you ?":"Glad you ask. As a shiny cloud floating peacefully, and you ?",
        "i'm fine and you ?":"Always fine, what are you up to, my dear ?",
        "what time is it ?":f"It's already {clock.hour} H {clock.minute} min.",
        "any brilliant ideas ?":"You can search the first word that comes in your mind, on the internet. Inspiration will kicking soon.",
        "goodbye":"You leave already ? Okay. Take care of yourself and rest well.",
        "i need help":"I am always here to listen to everything you say. What happened ?",
        "see you later":"I will wait here, come back as soon as you can !"
        
        }
    
    return responses.get(user_input.lower(), "Sorry, I can't understand your request... May you try again ?")

def send_message(event=None):
    
    user_message = user_input.get()
    
    if user_message.strip()!= "": # remove leading and trailing spaces
        
        chat.configure(state="normal")
        chat.insert("end", f'You: {user_message}\n', "user")
        bot_response = chatbot_response(user_message)
        chat.insert("end", f'Chatbot: {bot_response}\n', "bot")
        
        chat.configure(state = "disabled")
        chat.see("end")
        
        user_input.delete(0, "end")
        

# Configuration of the GUI

screen = ctk.CTk()
screen.geometry("700x600")
screen.title("Your daily assistant")
screen.configure(fg_color="darkgrey")

# Display the menu

def optionmenu_callback(choice):
    
    print("optionmenu dropdown clicked:", choice)
    
    if choice == "Light":
        
        screen.configure(fg_color = "lightgrey")
        chat.configure(fg_color="white")
        chat.tag_config("user", foreground="black")
        chat.tag_config("bot", foreground="red")
        
        optionmenu.set("Menu")
    
    elif choice == "Dark":
        
        screen.configure(fg_color = "darkgrey")
        chat.configure(fg_color="black")
        chat.tag_config("user", foreground="purple")
        chat.tag_config("bot", foreground="grey")
        
       
    elif choice == "Quit":
        
        screen.destroy()


optionmenu = ctk.CTkOptionMenu(screen, 
                               values= ["Light", "Dark", "Quit"], 
                               command=optionmenu_callback, button_color="grey", 
                               button_hover_color="black", fg_color="black")

optionmenu.set("Menu")
optionmenu.pack(anchor="nw")


# Header

header = ctk.CTkLabel(screen, 
                      text="Good Morning, a pleasure to see you.",
                      font=("Helvetica", 20), text_color="black")

header.pack(pady=10)

# Display of the messages

chat = ctk.CTkTextbox(screen, height=400, state="disabled")
chat.configure(fg_color="black")
chat.tag_config("user", foreground="purple")
chat.tag_config("bot", foreground="grey")
chat.configure(font=("Helvetica", 20))
chat.pack(pady=10, padx=10, fill="both", expand=True) # filling height and width

# Input box for the user

user_input_frame = ctk.CTkFrame(screen)
user_input_frame.configure(fg_color="darkgrey")
user_input_frame.pack(pady=10, padx=10, fill="x")

user_input = ctk.CTkEntry(user_input_frame, 
                          placeholder_text="Text me...", width=550)
user_input.pack(side="left", padx=5)

send_b = ctk.CTkButton(user_input_frame, text="Send !", command=send_message)
send_b.pack(side="left")

screen.bind("<Return>", send_message)


screen.mainloop()