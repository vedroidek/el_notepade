from GUI.main_window import Notification


if __name__ == "__main__":
    app = Notification(winsize=(800, 400), 
                       title_='El Notepade, Amigo v0.1.0')    
    app.mainloop()