from tkinter import Button, Canvas, Entry, END, HIDDEN, IntVar
from tkinter import Label, NORMAL, Radiobutton, Text, Tk, W
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from pet import StatesOfPet


class Game:
    pet = StatesOfPet()

    @staticmethod
    def show():
        information = str("""Welcome to the tamagochi! Here you can create your own pet.
        At the beginning you should choose your pet's color and name and click save.
        Congratulations, your pet is created! It has four states: health, fun, satiety and energy.
        To increase first three of them you should click on buttons heal, play and feed respectively.
        To increase energy put your pet to sleep.
        Attention! If one of the states will be 0, your pet will die, you will be able to restart game.
        Good luck!""")
        showinfo("Guide", information)

    def open_game(self):
        rt = Tk()
        self.show()
        rt.destroy()
        self.choose_settings()

    def choose_settings(self):

        def ok():
            showinfo("Information", "saved successfully")
            if value_of_button.get() == 1:
                self.pet.color = "tomato"
            if value_of_button.get() == 2:
                self.pet.color = "gold"
            if value_of_button.get() == 3:
                self.pet.color = "sky blue"
            if value_of_button.get() == 4:
                self.pet.color = "SeaGreen1"
            if value_of_button.get() == 5:
                self.pet.color = "magenta"
            settings_window.destroy()
            self.launch_game()
        settings_window = Tk()
        settings_window.title("settings")
        value_of_button = IntVar()
        choose_of_pet_color = Label(text="Choose your pet's color")
        red_button = Radiobutton(text="red", variable=value_of_button, value=1)
        red_button.grid(row=1, column=0, sticky=W)
        red_button.select()
        yellow_button = Radiobutton(text="yellow", variable=value_of_button, value=2)
        yellow_button.grid(row=2, column=0, sticky=W)
        blue_button = Radiobutton(text="light blue", variable=value_of_button, value=3)
        blue_button.grid(row=3, column=0, sticky=W)
        green_button = Radiobutton(text="green", variable=value_of_button, value=4)
        green_button.grid(row=4, column=0, sticky=W)
        purple_button = Radiobutton(text="purple", variable=value_of_button, value=5)
        purple_button.grid(row=5, column=0, sticky=W)

        pet_name = Label(text="Enter your pet's name")
        pet_name.grid(row=6, column=0)
        text_from_pet_name = Entry()
        self.pet.name = text_from_pet_name.get()
        text_from_pet_name.grid(row=6, column=1)
        save_button = Button(text="save", font=("Ubuntu", 10), command=ok)
        save_button.grid(row=7, columnspan=2)
        settings_window.mainloop()

    def launch_game(self):

        def restart_game():
            showinfo("Information", "Your pet is dead")
            answer = askquestion("Restart", "Do you want to try again?")
            if answer == "yes":
                root.destroy()
                self.pet.fun = 101
                self.pet.satiety = 101
                self.pet.health = 101
                self.pet.energy = 101
                self.open_game()
            else:
                root.destroy()

        def show_happy(event):
            if (20 <= event.x <= 350) and (20 <= event.y <= 100):
                self.pet.fun = min(100, self.pet.fun + 5)
                st = str(self.pet.fun)
                state_of_fun.delete(1.0, END)
                state_of_fun.insert(1.0, st)
                canvas.itemconfigure(cheek_left, state=NORMAL)
                canvas.itemconfigure(cheek_right, state=NORMAL)
                canvas.itemconfigure(mouth_normal, state=HIDDEN)
                canvas.itemconfigure(mouth_happy, state=NORMAL)
            else:
                canvas.itemconfigure(cheek_left, state=HIDDEN)
                canvas.itemconfigure(cheek_right, state=HIDDEN)
                canvas.itemconfigure(mouth_normal, state=NORMAL)
                canvas.itemconfigure(mouth_happy, state=HIDDEN)

        def sleep():
            self.pet.energy = 100
            new_state_of_energy = str(self.pet.energy)
            state_of_energy.delete(1.0, END)
            state_of_energy.insert(1.0, new_state_of_energy)
            new_color = canvas.body_color
            canvas.itemconfigure(pupil_left, fill=new_color, outline=new_color)
            canvas.itemconfigure(pupil_right, fill=new_color, outline=new_color)
            canvas.itemconfigure(eye_left, fill=new_color)
            canvas.itemconfigure(eye_right, fill=new_color)

        def wake_up():
            new_color = 'white'
            canvas.itemconfigure(pupil_left, fill="black", outline="black")
            canvas.itemconfigure(pupil_right, fill="black", outline="black")
            canvas.itemconfigure(eye_left, fill=new_color)
            canvas.itemconfigure(eye_right, fill=new_color)

        def pet_decline_in_satiety():
            self.pet.decline_in_satiety()
            if self.pet.satiety <= 0:
                restart_game()
            new_state_of_satiety = str(self.pet.satiety)
            state_of_satiety.delete(1.0, END)
            state_of_satiety.insert(1.0, new_state_of_satiety)
            root.after(4000, pet_decline_in_satiety)

        def pet_decline_in_fun():
            self.pet.decline_in_fun()
            if self.pet.fun <= 0:
                restart_game()
            new_state_of_fun = str(self.pet.fun)
            state_of_fun.delete(1.0, END)
            state_of_fun.insert(1.0, new_state_of_fun)
            root.after(3000, pet_decline_in_fun)

        def pet_decline_in_health():
            self.pet.decline_in_health()
            if self.pet.health <= 0:
                restart_game()
            new_state_of_health = str(self.pet.health)
            state_of_health.delete(1.0, END)
            state_of_health.insert(1.0, new_state_of_health)
            root.after(5000, pet_decline_in_health)

        def pet_decline_in_energy():
            self.pet.decline_in_energy()
            if self.pet.energy <= 0:
                restart_game()
            new_state_of_fun = str(self.pet.fun)
            state_of_fun.delete(1.0, END)
            state_of_fun.insert(1.0, new_state_of_fun)

            new_state_of_energy = str(self.pet.energy)
            state_of_energy.delete(1.0, END)
            state_of_energy.insert(1.0, new_state_of_energy)
            root.after(10000, pet_decline_in_energy)

        def pet_increase_health():
            self.pet.increase_health()
            new_state_of_health = str(self.pet.health)
            state_of_health.delete(1.0, END)
            state_of_health.insert(1.0, new_state_of_health)

        def pet_increase_fun():
            if self.pet.energy * self.pet.satiety * self.pet.health <= 0:
                restart_game()
            self.pet.increase_fun()

            new_state_of_energy = str(self.pet.energy)
            state_of_energy.delete(1.0, END)
            state_of_energy.insert(1.0, new_state_of_energy)

            new_state_of_health = str(self.pet.health)
            state_of_health.delete(1.0, END)
            state_of_health.insert(1.0, new_state_of_health)

            new_state_of_satiety = str(self.pet.satiety)
            state_of_satiety.delete(1.0, END)
            state_of_satiety.insert(1.0, new_state_of_satiety)

            new_state_of_fun = str(self.pet.fun)
            state_of_fun.delete(1.0, END)
            state_of_fun.insert(1.0, new_state_of_fun)

        def pet_increase_satiety():
            self.pet.increase_satiety()
            new_state_of_energy = str(self.pet.energy)
            state_of_energy.delete(1.0, END)
            state_of_energy.insert(1.0, new_state_of_energy)

            new_state_of_satiety = str(self.pet.satiety)
            state_of_satiety.delete(1.0, END)
            state_of_satiety.insert(1.0, new_state_of_satiety)

        root = Tk()
        root.title(self.pet.name)
        canvas = Canvas(root, width=400, height=400)

        # creating pet
        canvas.body_color = self.pet.color
        body = canvas.create_oval(35, 20, 365, 350, fill=canvas.body_color)
        ear_left = canvas.create_polygon(75, 80, 75, 10, 165, 70, fill=canvas.body_color)
        ear_right = canvas.create_polygon(255, 45, 325, 10, 325, 77, fill=canvas.body_color)
        mouth_normal = canvas.create_line(170, 250, 200, 272, 230, 250, width=2, smooth=1)
        foot_left = canvas.create_oval(65, 320, 145, 360, fill=canvas.body_color)
        foot_right = canvas.create_oval(250, 320, 330, 360, fill=canvas.body_color)
        eye_left = canvas.create_oval(130, 110, 160, 170, fill="white")
        eye_right = canvas.create_oval(230, 110, 260, 170, fill="white")
        pupil_left = canvas.create_oval(140, 130, 150, 155, fill="black")
        pupil_right = canvas.create_oval(240, 130, 250, 155, fill="black")
        cheek_left = canvas.create_oval(70, 180, 120, 230, fill='pink', state=HIDDEN)
        cheek_right = canvas.create_oval(280, 180, 330, 230, fill='pink', state=HIDDEN)
        mouth_happy = canvas.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)

        canvas.grid(rowspan=17, columnspan=4)

        canvas.bind('<Motion>', show_happy)

        # create states of pet in text format

        feed = Button(text="FEED", width=10, height=2, command=pet_increase_satiety)
        feed.grid(row=9, column=5, sticky=W)

        play = Button(text="PLAY", width=10, height=2, command=pet_increase_fun)
        play.grid(row=11, column=5, sticky=W)

        heal = Button(text="HEAL", width=10, height=2, command=pet_increase_health)
        heal.grid(row=13, column=5, sticky=W)

        put = Button(text="PUT TO SLEEP", width=10, height=2, command=sleep)
        put.grid(row=15, column=5, sticky=W)

        wake = Button(text="WAKE UP", width=10, height=2, command=wake_up)
        wake.grid(row=17, column=5, sticky=W)

        text_in_button_satiety = "SATIETY"
        satiety = Text(width=8, height=1)
        satiety.insert(1.0, text_in_button_satiety)
        satiety.grid(row=0, column=5)

        text_in_button_fun = "FUN"
        fun = Text(width=8, height=1)
        fun.insert(1.0, text_in_button_fun)
        fun.grid(row=2, column=5)

        text_in_button_health = "HEALTH"
        health = Text(width=8, height=1)
        health.insert(1.0, text_in_button_health)
        health.grid(row=4, column=5)

        text_in_button_energy = "ENERGY"
        energy = Text(width=8, height=1)
        energy.insert(1.0, text_in_button_energy)
        energy.grid(row=6, column=5)

        # create states of pet which will change

        text_in_window_with_state_of_satiety = str(self.pet.satiety)
        state_of_satiety = Text(width=3, height=1)
        state_of_satiety.insert(1.0, text_in_window_with_state_of_satiety)
        state_of_satiety.grid(row=0, column=6)

        text_in_window_with_state_of_fun = str(self.pet.fun)
        state_of_fun = Text(width=3, height=1)
        state_of_fun.insert(1.0, text_in_window_with_state_of_fun)
        state_of_fun.grid(row=2, column=6)

        text_in_window_with_state_of_health = str(self.pet.health)
        state_of_health = Text(width=3, height=1)
        state_of_health.insert(1.0, text_in_window_with_state_of_health)
        state_of_health.grid(row=4, column=6)

        text_in_window_with_state_of_energy = str(self.pet.energy)
        state_of_energy = Text(width=3, height=1)
        state_of_energy.insert(1.0, text_in_window_with_state_of_energy)
        state_of_energy.grid(row=6, column=6)

        pet_decline_in_satiety()
        pet_decline_in_energy()
        pet_decline_in_health()
        pet_decline_in_fun()

        root.mainloop()