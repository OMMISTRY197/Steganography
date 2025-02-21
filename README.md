# Secure Data Hiding in Image Using Steganography

## 📌 About the Project
This project implements a **secure image steganography system** using the **Least Significant Bit (LSB) technique** to hide **encrypted text** within images. It enhances security with **Fernet encryption**, ensuring data remains protected even if extracted. A **user-friendly GUI** allows easy encryption, embedding, extraction, and decryption, strengthening **covert communication and data privacy** in cybersecurity applications.

## 🚀 Features
- 🔒 **Dual Security:** LSB steganography + Fernet encryption for strong protection.  
- 🛡 **Password-Based Encryption:** Uses hash-derived keys for message security.  
- 🎨 **User-Friendly GUI:** Simple **Tkinter-based** interface for seamless operation.  
- 📈 **Scalability:** Can be extended to **other encryption methods and media types**.  
- ✅ **Robust Validation:** Ensures **error handling** and **key authentication** to prevent unauthorized access.  

## 🛠 Technologies Used
- **Programming Language:** Python
- **Libraries:** OpenCV, NumPy, Tkinter, Cryptography (Fernet), Hashlib, Base64
- **Techniques:** Least Significant Bit (LSB) Steganography, Symmetric Encryption
- **GUI Framework:** Tkinter
- **Supported Image Formats:** PNG, JPG, JPEG

## 🔧 Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed. Then, install the required dependencies:
```bash
pip install opencv-python numpy cryptography tkinter
```

### Running the Project
1. **Clone the repository**:
   ```bash
   git clone <your-github-repo-link>
   cd <repository-name>
   ```
2. **Run the script**:
   ```bash
   python Stego.py
   ```

## 🎯 How It Works
1. **Encryption & Hiding:**
   - Enter the text message & encryption key.
   - Select an image for hiding the message.
   - The encrypted text is embedded into the image using LSB steganography.
2. **Decryption & Extraction:**
   - Load the encoded image & enter the decryption key.
   - The hidden message is extracted and decrypted.

## 📌 Future Scope
- 🔐 **Advanced Encryption:** Integrate **AES or RSA encryption** for stronger security.
- 🎵 **Support for Other Media:** Extend steganography to **audio, video, and PDFs**.
- 🧠 **AI-Based Detection Prevention:** Implement **steganalysis-resistant** techniques.
- ☁ **Cloud Integration:** Enable **secure cloud-based encoding and decoding**.
- 📱 **Mobile & Web App Development:** Create **cross-platform applications**.

## 👥 End Users
- **Cybersecurity Professionals** – Secure data transmission.
- **Forensic Investigators** – Hide and retrieve sensitive case-related data.
- **Journalists & Activists** – Secure communication in restricted environments.
- **Government & Intelligence Agencies** – Confidential data exchange.
- **General Users** – Secure personal data within images.

## 📜 License
This project is licensed under the **MIT License**.

## 📩 Contact & Contribution
Feel free to **fork the repository**, **open issues**, and **submit pull requests**.

📧 Contact: ommistry1976@gmail.com  
🔗 GitHub Repository: [Your GitHub Link]
