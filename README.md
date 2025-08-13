---

 🚀 Running the Application Locally

Follow these steps to set up and run the application on your local machine:

1️⃣ Clone the Repository

```bash
git clone <your_repository_url>
cd <repository_folder>
```
2️⃣ Open the Project

Open the project folder in your preferred code editor (VS Code, PyCharm, etc.).

3️⃣ Verify Project Files

Ensure the following files exist in the same folder:
`app.py`
`requirements.txt`

 4️⃣ Create a Virtual Environment

```bash
python -m venv venv
```
 5️⃣ Activate the Virtual Environment
Windows (PowerShell / CMD):

  ```bash
  venv\Scripts\activate
  ```

 6️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
 7️⃣ Run the Application

```bash
streamlit run app.py
```
---

✅ Tip:
If you encounter dependency issues, delete the `venv` folder and repeat steps 4–6.
