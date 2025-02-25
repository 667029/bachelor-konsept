import os
import re

class RegexExFileModule:
    def extract_emails(text: str) -> list:
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        return re.findall(email_pattern, text)
    
    def extract_dates(text: str) -> list:
        date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
        return re.findall(date_pattern, text)