import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cryptography.fernet import Fernet
import base64
import hashlib

# Function to generate a secret key from a user-provided password
def generate_key_from_password(password):
    hashed_password = hashlib.sha256(password.encode()).digest()  # Create a 256-bit hash
    return base64.urlsafe_b64encode(hashed_password[:32])  # Use only 32 bytes for Fernet key

# Encrypt the message using the generated key
def encrypt_message(message, key):
    cipher = Fernet(key)  # Initialize cipher with the key
    return cipher.encrypt(message.encode()).decode()  # Encrypt message and return as string

# Decrypt the message using the provided key
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    try:
        return cipher.decrypt(encrypted_message.encode()).decode()  # Try decrypting
    except:
        return None  # Return None if the key is incorrect

# Function to encode (hide) text inside an image
def encode_text(image_path, secret_text, output_path, key):
    key = generate_key_from_password(key)  # Generate encryption key
    secret_text = encrypt_message(secret_text, key)  # Encrypt the message
    binary_text = ''.join(format(ord(char), '08b') for char in secret_text) + '1111111111111110'  # Convert to binary with delimiter

    img = cv2.imread(image_path)  # Load image
    if img is None:
        messagebox.showerror("Error", "Invalid image file.")
        return

    data_index = 0
    data_len = len(binary_text)
    rows, cols, channels = img.shape  # Get image dimensions

    # Modify image pixels to hide binary data
    for row in range(rows):
        for col in range(cols):
            for ch in range(channels):
                if data_index < data_len:
                    pixel_value = int(img[row, col, ch])
                    img[row, col, ch] = np.clip((pixel_value & ~1) | int(binary_text[data_index]), 0, 255)
                    data_index += 1

    cv2.imwrite(output_path, img)  # Save the new image with hidden text
    messagebox.showinfo("Success", "Data encoded successfully! Image saved.")

# Function to decode (extract) hidden text from an image
def decode_text(image_path, key):
    key = generate_key_from_password(key)  # Generate decryption key
    img = cv2.imread(image_path)  # Load image
    if img is None:
        messagebox.showerror("Error", "Invalid image file.")
        return ""

    binary_text = ""
    rows, cols, channels = img.shape  # Get image dimensions

    # Extract binary data from image
    for row in range(rows):
        for col in range(cols):
            for ch in range(channels):
                binary_text += str(img[row, col, ch] & 1)  # Get LSB
                if binary_text[-16:] == '1111111111111110':  # Check for delimiter
                    text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text)-16, 8))
                    decrypted_text = decrypt_message(text, key)  # Decrypt message

                    if decrypted_text is None:  # If incorrect key
                        messagebox.showerror("Error", "Invalid decryption key! Hidden text is present but cannot be decrypted.")
                        return ""
                    
                    return decrypted_text  # Return the decrypted message
    
    messagebox.showinfo("Info", "No hidden text found in the selected image.")  # If no message found
    return ""

# Function to open a file selection dialog for choosing an image
def select_image():
    return filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

# Function to open a file save dialog for saving the encoded image
def save_image():
    return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

# GUI - Encryption Interface
def show_encrypt_frame():
    for widget in frame.winfo_children():
        widget.destroy()  # Clear previous widgets
    
    tk.Label(frame, text="Enter Text:").pack()
    text_entry = tk.Entry(frame, width=50)
    text_entry.pack()

    tk.Label(frame, text="Enter Encryption Key:").pack()
    key_entry = tk.Entry(frame, width=50, show='*')  # Password field
    key_entry.pack()
    
    # Function to handle encryption
    def encrypt_action():
        image_path = select_image()  # Select image
        if not image_path:
            return
        output_path = save_image()  # Choose output path
        if not output_path:
            return
        secret_text = text_entry.get()
        key = key_entry.get()
        
        if not secret_text or not key:  # Check if inputs are valid
            messagebox.showerror("Error", "Please enter text and key to encode.")
            return
        
        encode_text(image_path, secret_text, output_path, key)  # Perform encoding
    
    tk.Button(frame, text="Encrypt & Hide", command=encrypt_action).pack()  # Encrypt button

# GUI - Decryption Interface
def show_decrypt_frame():
    for widget in frame.winfo_children():
        widget.destroy()  # Clear previous widgets

    tk.Label(frame, text="Enter Decryption Key:").pack()
    key_entry = tk.Entry(frame, width=50, show='*')  # Password field
    key_entry.pack()
    
    # Function to handle decryption
    def decrypt_action():
        image_path = select_image()  # Select encrypted image
        if not image_path:
            return
        key = key_entry.get()
        
        if not key:  # Check if key is entered
            messagebox.showerror("Error", "Please enter decryption key.")
            return
        
        decoded_text = decode_text(image_path, key)  # Perform decoding
        if decoded_text:
            messagebox.showinfo("Decrypted Text", decoded_text)  # Show decrypted text
    
    tk.Button(frame, text="Decrypt & Reveal", command=decrypt_action).pack()  # Decrypt button

# Main Function - Initializes GUI
def main():
    global frame
    
    root = tk.Tk()  # Create root window
    root.title("Image Steganography")
    root.geometry("500x300")  # Set window size
    
    tk.Label(root, text="Choose an option:").pack()
    tk.Button(root, text="Encrypt", command=show_encrypt_frame).pack()  # Button for encryption
    tk.Button(root, text="Decrypt", command=show_decrypt_frame).pack()  # Button for decryption
    
    frame = tk.Frame(root)
    frame.pack()  # Add frame for content
    
    root.mainloop()  # Start GUI loop

# Run the main function when script is executed
if __name__ == "__main__":
    main()