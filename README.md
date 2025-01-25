Research Paper Text Summarization Tool
A Python-based GUI tool that simplifies the summarization of research papers or any large text files using machine learning. The tool provides an intuitive user interface with options for loading text files, generating summaries, saving the output, and much more.

Features
Summarization with AI: Powered by Hugging Face's transformers library.
User-Friendly Interface: Built with Tkinter, featuring colorful designs and smooth transitions.
File Management: Load text files and save summaries with ease.
Customizable Summary: Adjust the length of summaries as needed.
Real-Time Processing: Instantly processes input text into concise summaries.
Scrollable Instructions: Clear and detailed steps for usage.
Dynamic Animations: Enhanced UI with transitions and visual effects.
Demo

(Add a screenshot or GIF showing your tool in action.)

Installation
Prerequisites
Python Version: Ensure Python 3.8 - 3.11 is installed on your system.
Dependencies: Install the required libraries.
Steps to Install
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/research-paper-summarization-tool.git
cd research-paper-summarization-tool
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download necessary machine learning models: The Hugging Face transformers library will automatically download the required pre-trained models during the first run.

Libraries Used
tkinter: For creating the graphical user interface.
transformers: For text summarization using pre-trained models.
torch: Required for running Hugging Face models.
ttkbootstrap: For advanced UI theming.
Pillow: For image handling in the GUI.
Install these dependencies using:

bash
Copy
Edit
pip install transformers torch ttkbootstrap pillow
Usage
Run the tool:

bash
Copy
Edit
python main.py
Load your research paper or any text file:

Click on the Load File button to browse and load a .txt file.
Summarize the text:

Click the Summarize button to generate a concise summary of the loaded text.
Save the summary:

Use the Save Summary button to save the generated text into a .txt file.
Optional:

Scroll through the instructions for help and tips on usage.
Adjust the time delay for scheduled summarization.
How to Get Sender Password for Email Functionality
If you're using the email functionality of the tool:

Enable 2-Step Verification for your Google account:

Go to your Google Account Settings → Security → Turn On 2-Step Verification.
Generate an App Password:

Go to App Passwords → Select the app (Mail) and the device → Generate.
Use the generated app password as the sender_password in the tool.

Contributions
Feel free to contribute to this project by submitting issues or pull requests. Contributions to improve the UI, add features, or enhance performance are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

