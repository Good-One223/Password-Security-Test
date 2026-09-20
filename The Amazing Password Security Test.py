from tkinter import *
white = "#FDF6E2"
# ------------------------------------------------------------------------------
# Character limit


def character_limit(P):
    limit = 30
    if len(P) <= limit:
        counter.config(text=f"{len(P)}/{limit}")
        password_length = len(P)
        number_of_characters.config(
            text=f"Number of characters: {password_length}")
        uppercase = 0
        lowercase = 0
        number = 0
        special = 0
        for c in P:
            if c.isupper():
                uppercase += 1
            elif c.islower():
                lowercase += 1
            elif c.isdigit():
                number += 1
            else:
                special += 1

        uppercase_text.config(text=f"Number of uppercase letters:{uppercase}")
        lowercase_text.config(text=f"Number of lowercase letters:{lowercase}")
        number_text.config(text=f"Number of numbers:{number}")
        special_text.config(text=f"Number of special characters:{special}")

        if password_length < 8:
            length_dif = 8 - int(password_length)
            feedback.config(text="Password is too short, you need " +
                            str(length_dif) + " more characters")
        elif password_length < 16:
            length_dif = 16 - int(password_length)
            feedback.config(text="Okay length, adding " +
                            str(length_dif) + " more characters would make it better.")
        elif password_length >= 16 and uppercase < 1:
            feedback.config(
                text="Great length, try adding some uppercase letters.")
        elif password_length >= 16 and number < 1 and uppercase >= 1:
            feedback.config(text="Good job, now add some numbers.")
        elif password_length >= 16 and number >= 1 and uppercase >= 1 and special < 1:
            feedback.config(
                text="This password is already amazing, but if you add special characters then it would be even better")
        elif password_length >= 16 and number >= 3 and uppercase >= 2 and special >= 2:
            feedback.config(text="This password is amazing!")
        else:
            feedback.config(
                text="Amazing! keep adding more Uppercase letters, numbers and special characters to increse it's security.")

        if password_length < 8:
            number_of_characters.config(fg="#FF0000")
        elif password_length < 16:
            number_of_characters.config(fg="#DB8B00")
        else:
            number_of_characters.config(fg="#03D100")

        if uppercase == 0:
            uppercase_text.config(fg="#FF0000")
        elif uppercase == 1:
            uppercase_text.config(fg="#DB8B00")
        else:
            uppercase_text.config(fg="#03D100")

        if lowercase <= 3:
            lowercase_text.config(fg="#FF0000")
        elif lowercase <= 5:
            lowercase_text.config(fg="#DB8B00")
        else:
            lowercase_text.config(fg="#03D100")

        if number == 0:
            number_text.config(fg="#FF0000")
        elif number <= 2:
            number_text.config(fg="#DB8B00")
        else:
            number_text.config(fg="#03D100")

        if special == 0:
            special_text.config(fg="#FF0000")
        elif special == 1:
            special_text.config(fg="#DB8B00")
        else:
            special_text.config(fg="#03D100")
        return True
    return False


# ------------------------------------------------------------------------------
# Window settings
window = Tk()
window.geometry("440x550")
window.resizable(False, False)
window.title("The Amazing Password Security Test")
window.config(background=white)
# ------------------------------------------------------------------------------
# Title
title = Text(window,
             height=2,
             width=20,
             font=("Courier", 25, "bold"),
             relief=FLAT,
             bg=window.cget('bg'))
title.tag_configure("center", justify='center')
title.insert(1.0, "The Amazing Password Security Test")
title.tag_add("center", "1.0", "end")
title.pack(pady=20, fill=X)
# ------------------------------------------------------------------------------
# Number of characters
number_of_characters = Label(window,
                             text="Number of characters: 0",
                             font=("Courier", 12),
                             bg=white,
                             fg="#FF0000")
number_of_characters.pack(pady=5)
# ------------------------------------------------------------------------------
# Uppercase
uppercase_text = Label(window,
                       text="Number of uppercase letters: 0",
                       font=("Courier", 12),
                       bg=white,
                       fg="#FF0000")
uppercase_text.pack(pady=5)
# ------------------------------------------------------------------------------
# Lowercase
lowercase_text = Label(window,
                       text="Number of lowercase letters: 0",
                       font=("Courier", 12),
                       bg=white,
                       fg="#FF0000")
lowercase_text.pack(pady=5)
# ------------------------------------------------------------------------------
# Numbers
number_text = Label(window,
                    text="Number of numbers: 0",
                    font=("Courier", 12),
                    bg=white,
                    fg="#FF0000")
number_text.pack(pady=5)
# ------------------------------------------------------------------------------
# Special
special_text = Label(window,
                     text="Number of special characters: 0",
                     font=("Courier", 12),
                     bg=white,
                     fg="#FF0000")
special_text.pack(pady=5)
# ------------------------------------------------------------------------------
# Password box
vcmd = (window.register(character_limit), '%P')
password_box = Entry(window,
                     width=55,
                     justify=CENTER,
                     validate="key",
                     validatecommand=vcmd)
password_box.pack(pady=10)
password_box.focus_set()
# ------------------------------------------------------------------------------
# Character limit label
counter = Label(window,
                text="0/30",
                font=("Courier", 10),
                bg=white,
                fg="#555555")
counter.pack()
# ------------------------------------------------------------------------------
# Password feedback
feedback = Label(window,
                 text="Please type a password.",
                 font=("Courier", 15),
                 wraplength=380,
                 bg=white)
feedback.pack(pady=10)
# ------------------------------------------------------------------------------
window.mainloop()
