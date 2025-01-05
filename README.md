# Research Paper Summarizer

This project is a web-based application that allows users to upload research papers in PDF format, which are then summarized using Natural Language Processing (NLP) techniques. The summarized content can be downloaded by the user in either DOCX or PDF format.

## Features

- Upload a PDF research paper.
- Automatically generate a summary of the paper.
- Download the summarized paper in either DOCX or PDF format.
- Easy-to-use interface with modern design.

## Technologies Used

- **Flask**: Python web framework used for building the web application.
- **python-docx**: Python library to handle DOCX files.
- **pdfkit**: Library to convert HTML to PDF.
- **NLTK**: Natural Language Toolkit, used for text processing and summarization.
- **HTML/CSS**: For front-end user interface.

## Project Structure

```
project-directory/
│
├── app.py                # Flask app code (main backend logic)
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates for pages
│   ├── upload.html       # Upload form for the paper
│   └── summary.html      # Display summarized paper
├── static/               # Static files (CSS, images)
│   ├── css/
│   │   └── styles.css    # Custom CSS for styling the pages
│   └── images/           # Images (e.g., logos, icons)
└── venv/                 # Virtual environment folder (if created)
```

### Files to Note:

1. **app.py**: Main Python file running the Flask application, handling routing, file uploads, summarization, and file downloads.
2. **requirements.txt**: Contains all the required Python libraries and dependencies for the project.
3. **templates/upload.html**: HTML file for uploading a research paper.
4. **templates/summary.html**: HTML file displaying the summarized content with download options.
5. **static/css/styles.css**: Custom CSS file used to style the pages and make the UI more professional.
6. **static/images/**: Folder to store any images (e.g., logos, icons) used in the user interface.

## Setup Instructions

Follow these steps to run the project locally:

### Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd project-directory
```

### Step 2: Create and Activate a Virtual Environment (Optional but Recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Run the following command to install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask App

Now that the dependencies are installed, you can start the Flask application:

```bash
python app.py
```

By default, the app will run on `http://127.0.0.1:5000/`. Open this URL in your web browser to access the Research Paper Summarizer app.

### Step 5: Upload and Summarize Papers

- Navigate to the upload page (`/upload`) and upload your research paper.
- After the file is uploaded, the app will process it and provide a summarized version of the paper.
- You can then download the summary in either **DOCX** or **PDF** format.

### Step 6: Exit or Upload Another File

You can upload another file, or simply exit the application after receiving the summary.

## Folder Structure Details

- **static/images**: Store any images (like logos, icons) used in the UI here.
- **static/css/styles.css**: Custom CSS file for designing and styling the front-end pages.
- **templates**: Contains the HTML files for the user interface (`upload.html` for file upload and `summary.html` for displaying the summary).

## Example Usage

1. **Uploading a Paper**: On the home page, users can select a file from their local system and click "Summarize Paper."
2. **Viewing the Summary**: After the summary is generated, it will be displayed on the next page, where users can download the summary in DOCX or PDF format.
3. **Exiting or Uploading Another Paper**: The user can either exit the app or upload another paper for summarization.

## Known Issues

- The summarization process may take a few seconds depending on the length of the document.
- Ensure that the file uploaded is in PDF format for best results.

## Future Improvements

- Add support for additional document formats (e.g., DOCX).
- Improve the summary generation algorithm by integrating advanced NLP models.
- Provide options for customizing the summary (e.g., length of the summary).
