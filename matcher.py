from resume_parser import extract_text
from skill_extractor import extract_skills, calculate_skill_match
from ner_extractor import extract_entities, get_person_name
from similarity import calculate_similarity

def analyze_resume(resume_path, job_description_path):

    # Extract text from resume and job description
    resume_text=extract_text(resume_path)
    

    # Extract entities from resume text
    entities=extract_entities(resume_text)

    # Extract person name from entities
    person_name=get_person_name(resume_text)

    # Extract resume skills
    resume_skills=extract_skills(resume_text)

    # Extract job skills 
    job_skills=extract_skills(job_description)

    # Calculate skill match score
    matching_skills=