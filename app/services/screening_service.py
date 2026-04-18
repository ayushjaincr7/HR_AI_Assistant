from app.chains.screening_chain import chain


def screen_resume(resume_text: str, job_desc:  str):
    response = chain.invoke({
        'resume_text': resume_text,
        'job_description': job_desc
    }
    )
    return response


