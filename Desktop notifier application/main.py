import time
import requests
from plyer import notification
from PIL import Image, ImageDraw, ImageFont

# Function to fetch tasks from a remote API or predefined list
def fetch_tasks():
    """
    Fetch tasks from a remote API or return a predefined list.
    Returns:
        list: A list of tasks with 'task' and 'time' keys.
    """
    # Example API call (uncomment to use an actual API)
    # response = requests.get("https://example.com/api/tasks")
    # tasks = response.json()
    
    # For demonstration purposes, use a predefined list
    tasks = [
        {"task": "Submit project report", "time": "15:00"},
        {"task": "Team meeting", "time": "16:30"},
    ]
    return tasks

# Function to create a custom notification image
def create_notification_image(task):
    """
    Create an image for the notification.
    Args:
        task (str): The task description.
    Returns:
        str: Path to the generated image.
    """
    width, height = 300, 100
    img = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    draw.text((10, 10), "Task Reminder", font=font, fill=(0, 0, 0))
    draw.text((10, 40), task, font=font, fill=(0, 0, 0))
    
    image_path = "notification_image.png"
    img.save(image_path)
    return image_path

# Function to send a notification
def send_notification(task):
    """
    Display a desktop notification for a task.
    Args:
        task (str): The task description.
    """
    image_path = create_notification_image(task)
    notification.notify(
        title="Task Reminder",
        message=task,
        app_icon=None,  # Icons can be added if available
        timeout=5  # Notification duration in seconds
    )

# Main function
def main():
    """
    Main function to fetch tasks and send notifications.
    """
    tasks = fetch_tasks()
    
    while True:
        current_time = time.strftime("%H:%M")
        for task in tasks:
            if task["time"] == current_time:
                send_notification(task["task"])
                tasks.remove(task)  # Remove task after notification
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
