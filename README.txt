spaCy Text Classifier - Full Setup Guide and Lesson Plan

1️⃣ Install Python 3.10.11:
https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

2️⃣ Open the Project in VS Code:
File > Open Folder > Choose the extracted project folder.

3️⃣ Set Python Interpreter in VS Code:
Ctrl+Shift+P > "Python: Select Interpreter" > Choose Python 3.10

4️⃣ Set PowerShell Script Permissions (Windows Only):
Run this in PowerShell:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

(Mac users do NOT need this step)

5️⃣ Create a Virtual Environment:
python -m venv venv

6️⃣ Activate the Virtual Environment:
PowerShell: .\venv\Scripts\Activate.ps1
CMD: venv\Scripts\activate.bat
Mac/Linux: source venv/bin/activate

7️⃣ Install Dependencies:
pip install -r requirements.txt

8️⃣ Download Language Model:
python -m spacy download en_core_web_sm

9️⃣ Train the Model:
python train_model.py

🔟 Test the Model with CLI:
python classify_input.py

🔢 Evaluate Accuracy:
python evaluate_model.py

Happy coding!
