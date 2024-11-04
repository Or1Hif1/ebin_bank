import tkinter as tk
import bank_functions as bf

# Initialize the main window
root = tk.Tk()
root.title("Ebin Bank")

# Set the window size to 1280x720
root.geometry("1280x720")

# Set the background color to black
root.configure(bg="green")

# Variables to store the input text
input_text1 = tk.StringVar()
input_text2 = tk.StringVar()
input_text3 = tk.StringVar()
input_text4 = tk.StringVar()
input_text5 = tk.StringVar()


# Function to handle the Enter key press
def save_text(event=None):
    global saved_text1, saved_text2, saved_text3, saved_text4, saved_text5
    saved_text1 = input_text1.get()
    saved_text2 = input_text2.get()
    saved_text3 = input_text3.get()
    saved_text4 = input_text4.get()
    saved_text5 = input_text5.get()
    bf.create_user(saved_text1, saved_text2, saved_text3, saved_text4, saved_text5)

    # Print the saved text to the console for confirmation
    print("Text 1 saved:", saved_text1)
    print("Text 2 saved:", saved_text2)
    print("Text 3 saved:", saved_text3)
    print("Text 4 saved:", saved_text4)
    print("Text 5 saved:", saved_text5)


# Label and Entry for first input
spaces_ = tk.Label(root, text="", fg="white", bg="green", font=("Arial", 14))
spaces_.pack(pady=60)
label1 = tk.Label(root, text="Enter User Name:", fg="white", bg="green", font=("Arial", 14))
label1.pack(pady=5)
text_input1 = tk.Entry(root, textvariable=input_text1, font=("Arial", 14), width=50)
text_input1.pack(pady=5)

# Label and Entry for second input
label2 = tk.Label(root, text="Enter Password:", fg="white", bg="green", font=("Arial", 14))
label2.pack(pady=5)
text_input2 = tk.Entry(root, textvariable=input_text2, font=("Arial", 14), width=50)
text_input2.pack(pady=5)

# Label and Entry for third input
label3 = tk.Label(root, text="Enter Card Number:", fg="white", bg="green", font=("Arial", 14))
label3.pack(pady=5)
text_input3 = tk.Entry(root, textvariable=input_text3, font=("Arial", 14), width=50)
text_input3.pack(pady=5)

# Label and Entry for fourth input
label4 = tk.Label(root, text="Enter CVV:", fg="white", bg="green", font=("Arial", 14))
label4.pack(pady=5)
text_input4 = tk.Entry(root, textvariable=input_text4, font=("Arial", 14), width=50)
text_input4.pack(pady=5)

# Label and Entry for fifth input
label5 = tk.Label(root, text="Enter Card Date:", fg="white", bg="green", font=("Arial", 14))
label5.pack(pady=5)
text_input5 = tk.Entry(root, textvariable=input_text5, font=("Arial", 14), width=50)
text_input5.pack(pady=5)

# Bind the Enter key to save_text function on the last input field
text_input5.bind("<Return>", save_text)

# Run the main loop
root.mainloop()
