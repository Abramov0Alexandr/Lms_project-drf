def course_upload_path(model, file) -> str:
    return f"course/{model.title}/{file}"


def lesson_upload_path(model, file) -> str:
    return f"lesson/{model.title}/{file}"
