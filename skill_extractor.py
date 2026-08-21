SKILLS = [

    # Programming
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",

    # Data Science
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",

    # Python libraries
    "numpy",
    "pandas",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "matplotlib",
    "seaborn",

    # Database
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "oracle",

    # AI
    "langchain",
    "langgraph",
    "llm",
    "generative ai",
    "nlp",
    "computer vision",

    # Cloud
    "aws",
    "azure",
    "google cloud",

    # Tools
    "git",
    "github",
    "docker",
    "kubernetes",

    # Web
    "html",
    "css",
    "react",
    "flask",
    "django",
    "fastapi",

    # Other
    "excel",
    "power bi",
    "tableau"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_skill_match(resume_skills, job_skills):

    if len(job_skills) == 0:
        return 0

    matching = set(resume_skills).intersection(
        set(job_skills)
    )

    score = (
        len(matching) /
        len(set(job_skills))
    ) * 100

    return round(score, 2)