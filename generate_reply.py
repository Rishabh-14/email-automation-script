def recommend_action(email_content):
    if "meeting" in email_content:
        return fetch_available_slots_from_calendar()
    elif "document about" in email_content:
        topic = extract_topic_from_email(email_content)
        return fetch_relevant_document_link(topic)
    # ... add more contextual actions

# Usage
email_content = "Can we have a meeting tomorrow about the project?"
recommended_action = recommend_action(email_content)
print(recommended_action)  # Output: "Available slots: 10 AM, 2 PM"
