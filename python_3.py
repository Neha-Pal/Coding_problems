# There are 7 events planned by an organization in a week. If Sunday then they will organize an event of
# laughing and similarly on Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday there are some
# events respectively book reading, storytelling, tree plantation, painting, dancing, and photo shoot.
# ➢ Make a function that will take the day as a parameter and return the related event to that
# day (Do not use If, elif, or else).

def get_events(day):
    events = {
        "Sunday": "Laughing",
        "Monday": "Book Reading",
        "Tuesday": "Story Telling",
        "Wednesday": "Tree Plantation",
        "Thursday": "Painting",
        "Friday": "Dancing",
        "Saturday": "Photo Shoot"
    }
    return events.get(day, "Invalid Day")
day = "Friday"
print(get_events(day))