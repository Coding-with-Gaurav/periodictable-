import tkinter as tk
from tkinter import ttk
import periodictable

def display_element_info():
    try:
        atomic_number = int(atomic_number_entry.get())
        element = periodictable.elements[atomic_number]

        # Create a frame for element information
        element_frame = ttk.Frame(info_frame, relief="solid", borderwidth=2, padding=(10, 5))
        element_frame.grid(row=info_frame.grid_size()[1], column=0, padx=10, pady=5, sticky="ew")

        # Display element information in the frame with different colors
        info = (f"Atomic Number: {element.number}\n"
                f"Symbol: {element.symbol}\n"
                f"Name: {element.name}\n"
                f"Atomic Mass: {element.mass}\n"
                f"Density: {element.density}")

        text_widget = tk.Text(element_frame, wrap="word", width=40, height=5, font=('Arial', 12), bg='#ecf0f1', fg='#2c3e50')
        text_widget.insert(tk.END, info)

        # Add tags and configure colors
        text_widget.tag_configure('atomic_number', foreground='#e74c3c')
        text_widget.tag_configure('symbol', foreground='#3498db')
        text_widget.tag_configure('name', foreground='#2ecc71')
        text_widget.tag_configure('mass', foreground='#e67e22')
        text_widget.tag_configure('density', foreground='#9b59b6')

        # Apply tags to specific parts of the text
        text_widget.tag_add('atomic_number', '1.0', '1.15')
        text_widget.tag_add('symbol', '2.0', '2.8')
        text_widget.tag_add('name', '3.0', '3.6')
        text_widget.tag_add('mass', '4.0', '4.13')
        text_widget.tag_add('density', '5.0', '5.8')

        text_widget.configure(state='disabled')  # Make the text widget read-only
        text_widget.grid(row=0, column=0, sticky="w")

    except ValueError:
        error_label.config(text="Please enter a valid atomic number.")
        error_label.grid(row=info_frame.grid_size()[1], column=0, padx=10, pady=5, sticky="ew")

# Create the main window
root = tk.Tk()
root.title("Periodic Table Information")

# Configure window size and style
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg='#3498db')

# Create and place widgets with styling
label = ttk.Label(root, text="Enter Element Atomic Number:", font=('Arial', 12), background='#3498db', foreground='white')
label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

atomic_number_entry = ttk.Entry(root, font=('Arial', 12))
atomic_number_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = ttk.Button(root, text="Search", command=display_element_info, style='TButton')
search_button.grid(row=0, column=2, padx=10, pady=10, sticky='w')

# Create a frame to hold the dynamic element information
info_frame = ttk.Frame(root, relief="solid", borderwidth=2)
info_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Label for error messages
error_label = ttk.Label(info_frame, text="", font=('Arial', 12), foreground='red')
error_label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# Style the button
style = ttk.Style()
style.configure('TButton', font=('Arial', 12), foreground='white', background='#2980b9', padding=5)

# Binding the Enter key to trigger the search
root.bind('<Return>', lambda event=None: search_button.invoke())

# Set row and column weights to make the info_frame expandable
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the main loop
root.mainloop()
