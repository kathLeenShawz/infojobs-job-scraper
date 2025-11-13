thonimport json

def parse_job_listing(job_data):
    parsed_data = {
        "title": job_data['title'],
        "description": job_data['description'],
        "company": job_data['company'],
        "location": job_data['location'],
        "contract_type": job_data['contractType'],
        "teleworking": job_data['teleworking'],
        "published_at": job_data['publishedAt'],
        "url": job_data['link']
    }
    return parsed_data

def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)