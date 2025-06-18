# 🧠 NeuroMind AI – Smarter Job Search

Welcome to **NeuroMind AI – Smarter Job Search**! This AI-powered Streamlit app helps you find the best jobs, estimate salaries, and prepare for interviews—all in one place.

---

## 🚀 Features

- **Resume Analysis:** Upload your PDF or DOCX resume and get AI-suggested job titles based on your experience.
- **Job Search:** Instantly search for jobs using your resume or custom keywords.
- **Salary Insights:** Get salary information for any job title via Levels.fyi.
- **Interview Prep:** Access company-specific interview resources from Glassdoor.

---

## 🌐 Live Demo

✨ Try the app live: [https://neuromindai.streamlit.app/](https://neuromindai.streamlit.app/)

---

## 🧩 Sections & Files Used in This Project

- `app.py` or `streamlit_app.py`: Main Streamlit application file. Run this to launch the app.
- `requirements.txt`: Lists all Python dependencies. Install with `pip install -r requirements.txt`.
- `.env`: Store your API keys here (see setup instructions below).
- `README.md`: Project documentation and instructions.
- `job_env/`: (Optional) Local Python environment folder (if present).

---

## 🖥️ How to Run

1. **Clone the repository**
   ```powershell
   git clone <your-repo-url>
   cd NeuroMind-AI-Smarter-Job-Search-
   ```
2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Set up API keys**
   - Create a `.env` file in the project root with:
     ```env
     SERPAPI_API_KEY="<your-serpapi-key>"
     HUGGINGFACE_API_KEY="<your-huggingface-key>"
     ```
4. **Run the app**
   ```powershell
   streamlit run app.py
   ```
   or
   ```powershell
   streamlit run streamlit_app.py
   ```

---

## 📄 Example Usage

1. Upload your resume or enter a job title.
2. Click **Analyze & Search Jobs**.
3. View suggested job titles, job listings, salary info, and interview prep links.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Inference API
- SerpAPI (Google Jobs)
- python-docx, PyPDF2

---

## 📬 Feedback & Contributions

Pull requests and issues are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License.