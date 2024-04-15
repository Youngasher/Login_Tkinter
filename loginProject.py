import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Initialize login_screen to None at the global scope
login_screen = None

def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    main_screen.geometry("1200x800")
    main_screen.title("Account Login")

    # Create the login and registration section
    login_frame = tk.Frame(main_screen ,pady=200, bg="#98002E")
    login_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    Label(login_frame, text="Choose Login Or Register", bg="#98002E", width="30", height="2", font=("Aptos", 18), fg="#F9A01B").pack()
    Label(login_frame, text="" , bg="#98002E" ).pack()

    # Open the image file
    image = Image.open("qwe.png")

    # Convert the image to a format supported by tkinter
    photo_image = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(login_frame, image=photo_image, height="80", width="80", bg="#98002E")
    image_label.pack()
    Label(login_frame, text="",pady=10, bg="#98002E").pack() 

    Button(login_frame, text="Login", height="2", width="30", command=login, font=("Aptos", 12), bg="#F9A01B" , fg="#98002E").pack()
    Label(login_frame, text="",pady=5, bg="#98002E").pack() 

    Button(login_frame, text="Register", height="2", width="30", command=register, font=("Aptos", 12), bg="#F9A01B" ,fg="#98002E").pack()

    # Create the gif display section
    gif_frame = tk.Frame(main_screen)
    gif_frame.pack(side=LEFT, fill=BOTH, expand=True)
    gif_lb = tk.Label(gif_frame,  bg="#000000")
    gif_lb.pack(fill=BOTH, expand=True)
    ready_gif(gif_lb, login_frame)  

    main_screen.mainloop()

    
def ready_gif(label, login_frame):  
    print('Started')
    gif_file = Image.open('giphy1.gif')

    gif_frames = []
    for r in range(0, gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy())

    frame_delay = gif_file.info['duration']
    print('Completed')
    play_gif(label, gif_frames, frame_delay, login_frame)  

def play_gif(label, frames, delay, login_frame, count=-1):  
    if count >= len(frames) - 1:
        count = -1

    count += 1
    current_frame = ImageTk.PhotoImage(frames[count])
    label.config(image=current_frame)
    label.image = current_frame
    main_screen.after(delay, play_gif, label, frames, delay, login_frame, count)


# Rest of your code for login and registration...


def register():
    global register_screen
    register_screen = Toplevel(main_screen, pady=100 ,bg="#000000")
    register_screen.title("Register")
    register_screen.geometry("600x500")

    global username
    global password
    global username_entry
    global password_entry   

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", font=("Aptos", 18), bg="#000000" ,fg="#F9A01B").pack()
    Label(register_screen, text="" ,bg="#000000").pack()

    Label(register_screen, text="Username * ", font=("Aptos", 12), bg="#000000" ,fg="#F9A01B").pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    Label(register_screen, text="Password * " , font=("Aptos", 12), bg="#000000" ,fg="#F9A01B").pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    Label(register_screen, text="", bg="#000000").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#F9A01B", command=register_user).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open("credentials.txt", "a")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    # Print the contents of the file for debugging
    with open("credentials.txt", "r") as f:
        print("Contents of credentials.txt:")
        print(f.read())


def login():
    global login_screen
    login_screen = Toplevel(main_screen, pady=100 ,bg="#F9A01B")

    login_screen.title("Login")
    login_screen.geometry("600x500")

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Please enter details below to login", font=("Aptos", 18), bg="#F9A01B" ,fg="#000000").pack()
    Label(login_screen, text="", bg="#F9A01B").pack()

    Label(login_screen, text="Username * ", font=("Aptos", 12), bg="#F9A01B" ,fg="#000000").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="Password * ", font=("Aptos", 12), bg="#F9A01B" ,fg="#000000").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    Label(login_screen, text="", bg="#F9A01B").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()

def login_verification():
    username1 = username_verify.get()
    password1 = password_verify.get()

    # Open the credentials file
    with open("credentials.txt", "r") as file1:
        # Read all lines from the file
        verify = file1.read().splitlines()

    # Check if username exists in the list of usernames
    if username1 in verify:
        # Find the index of the username in the list
        index = verify.index(username1)
        # Check if the password matches the password stored in the next line
        if password1 == verify[index + 1]:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen, bg="#70ff70")
    login_success_screen.title("Success")
    login_success_screen.geometry("300x250")
    Label(login_success_screen, text="Login Success", bg="#70ff70").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def delete_login_success():
    login_success_screen.destroy()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen) 
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

if __name__ == "__main__":
    frame_count = -1
    main_account_screen()
