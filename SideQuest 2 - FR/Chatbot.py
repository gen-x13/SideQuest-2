""" #genxcode - SIDEQUEST : Chatbot ! """

import customtkinter as ctk
import datetime

clock = datetime.datetime.now()

# Fonction pour les réponses du bot

def chatbot_response(user_input):
    
    responses = {
        
        "bonjour":"Bienvenue, comment puis-je vous aider aujourd'hui ?",
        "comment vas-tu ?":"Je suis heureux que vous posiez la question. Comme un nuage brillant flottant paisiblement, et vous ?",
        "je vais bien et toi ?":"Toujours bien, que faites-vous, ma chère ?",
        "quelle heure est-il ?":f"Il est déjà {clock.hour} H {clock.minute} min.",
        "as-tu des idées brillantes ?":"Vous pouvez chercher le premier mot qui vous vient à l'esprit sur l'internet. L'inspiration ne tardera pas à venir.",
        "au revoir":"Vous partez déjà ? D'accord. Prenez soin de vous et reposez-vous bien.",
        "j'ai besoin d'aide":"Je suis toujours là pour écouter tout ce que tu dis. Que s'est-il passé ?",
        "à plus tard":"J'attendrai ici, revenez dès que possible !"
        
        }
    
    return responses.get(user_input.lower(), "Désolé, je ne comprends pas votre demande... Pouvez-vous réessayer ?")

def send_message(event=None):
    
    user_message = user_input.get()
    
    if user_message.strip()!= "": # supprimer les espaces de début et de fin
        
        chat.configure(state="normal")
        chat.insert("end", f'Toi: {user_message}\n', "user")
        bot_response = chatbot_response(user_message)
        chat.insert("end", f'Chatbot: {bot_response}\n', "bot")
        
        chat.configure(state = "disabled")
        chat.see("end")
        
        user_input.delete(0, "end")
        

# Configuration du GUI

screen = ctk.CTk()
screen.geometry("700x600")
screen.title("Ton assistant quotidien")
screen.configure(fg_color="darkgrey")

# Affichage du menu

def optionmenu_callback(choice):
    
    print("optionmenu dropdown clicked:", choice)
    
    if choice == "Clair":
        
        screen.configure(fg_color = "lightgrey")
        chat.configure(fg_color="white")
        chat.tag_config("user", foreground="black")
        chat.tag_config("bot", foreground="red")
        
        optionmenu.set("Menu")

    elif choice == "Sombre":
        
        screen.configure(fg_color = "darkgrey")
        chat.configure(fg_color="black")
        chat.tag_config("user", foreground="purple")
        chat.tag_config("bot", foreground="grey")
        
       
    elif choice == "Quitter":
        
        screen.destroy()


optionmenu = ctk.CTkOptionMenu(screen, 
                               values= ["Clair", "Sombre", "Quitter"], 
                               command=optionmenu_callback, button_color="grey", 
                               button_hover_color="black", fg_color="black")

optionmenu.set("Menu")
optionmenu.pack(anchor="nw")


# Header

header = ctk.CTkLabel(screen, 
                      text="Bonjour, c'est un plaisir de vous voir.",
                      font=("Helvetica", 20), text_color="black")

header.pack(pady=10)

# Affichage des messages

chat = ctk.CTkTextbox(screen, height=400, state="disabled")
chat.configure(fg_color="black")
chat.tag_config("user", foreground="purple")
chat.tag_config("bot", foreground="grey")
chat.configure(font=("Helvetica", 20))
chat.pack(pady=10, padx=10, fill="both", expand=True) # Remplissage de la hauteur et de la largeur

# Zone de saisie pour l'utilisateur

user_input_frame = ctk.CTkFrame(screen)
user_input_frame.configure(fg_color="darkgrey")
user_input_frame.pack(pady=10, padx=10, fill="x")

user_input = ctk.CTkEntry(user_input_frame, 
                          placeholder_text="Parle moi...", width=550)
user_input.pack(side="left", padx=5)

send_b = ctk.CTkButton(user_input_frame, text="Envoyé !", command=send_message)
send_b.pack(side="left")

screen.bind("<Return>", send_message)


screen.mainloop()