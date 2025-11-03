from typing import Dict
from certificates.base_markdown_string import base_markdown_string
import yaml

with open('certificates/certificates.yaml', 'r') as file:
    cert_data = yaml.safe_load(file)

def generate_certificate_link(cert: Dict[str, str]) -> str:
    course_name = cert.get('course_name')
    course_link = cert.get('course_link')
    return f"[{course_name}]({course_link})"

markdown_string = ""
for cert in cert_data:
    markdown_string += f"   - {cert}"
    if type(cert_data[cert]) is list:
        for course in cert_data[cert]:
            markdown_string += f"\n     - {generate_certificate_link(course)}"
        markdown_string += "\n"
    
    elif type(cert_data[cert]) is dict:
        for sub_cert in cert_data[cert]:
            markdown_string += f"\n     - {sub_cert}"
            for course in cert_data[cert][sub_cert]:
                markdown_string += f"\n         - {generate_certificate_link(course)}"
            markdown_string += "\n"

final_markdown = base_markdown_string + markdown_string
with open('README.md', 'w', encoding='utf-8') as md_file:
    md_file.write(final_markdown)