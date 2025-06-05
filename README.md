# 🧠 NeuroMind AI – Smarter Job Search

Welcome to **NeuroMind AI – Smarter Job Search**! This AI-powered Streamlit app helps you find the best jobs, estimate salaries, and prepare for interviews—all in one place.

---

## 🚀 Features

- **Resume Analysis**: Upload your PDF or DOCX resume and get AI-suggested job titles based on your experience.
- **Job Search**: Instantly search for jobs using your resume or custom keywords.
- **Salary Insights**: Get salary information for any job title via Levels.fyi.
- **Interview Prep**: Access company-specific interview resources from Glassdoor.

---

## 🌐 Live Demo

Try the app live: [https://neuromindai.streamlit.app/](https://neuromindai.streamlit.app/)

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

---

## 📄 Example Usage

- Upload your resume or enter a job title.
- Click **Analyze & Search Jobs**.
- View suggested job titles, job listings, salary info, and interview prep links.

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