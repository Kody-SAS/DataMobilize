import os
import requests
import sqlite3

# Replace with your bot token and group chat ID
bot_token = "BOT_TOKEN"
chat_id = "CHAT_ID"

# Function to check for required fields in the issue body
def check_required_fields(issue_body):
  required_fields = ["age", "gender", "city", "telegram_handle"]

  # Check if all required fields are present
  for field in required_fields:
    if field not in issue_body.lower():
      return False

  return True

# Function to add user to Telegram group
def add_user_to_group(telegram_handle):
  url = f"https://api.telegram.org/bot{bot_token}/addChatMember"
  data = {
    "chat_id": chat_id,
    "username": telegram_handle,
  }

  try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return True
  except requests.exceptions.RequestException as e:
    print(f"Error adding user to group: {e}")
    return False

# Function to store user information in a SQLite database
def store_user_info(age, gender, city):
  # Connect to the database (create it if it doesn't exist)
  conn = sqlite3.connect("hackathon_participants.db")
  c = conn.cursor()

  # Create the table if it doesn't exist
  c.execute('''CREATE TABLE IF NOT EXISTS participants (
                age INTEGER,
                gender TEXT,
                city TEXT
              )''')

  # Insert data into the table
  c.execute("INSERT INTO participants VALUES (?, ?, ?)", (age, gender, city))
  conn.commit()
  conn.close()

# Main execution
def main():
  # Get the issue number from the context
  issue_number = os.getenv("GITHUB_ISSUE_NUMBER")

  # Get the issue details from the GitHub API
  url = f"https://api.github.com/repos/{os.getenv('GITHUB_REPOSITORY')}/issues/{issue_number}"
  headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
  # Raise an exception for non-200 status codes
    issue_data = response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving issue data: {e}")
    return

  # Extract the issue body and user's Telegram handle
  issue_body = issue_data["body"]
  telegram_handle = None

  # Check if required fields are present
  if check_required_fields(issue_body):
    # Extract user information from the body (you may need to modify this based on your template)
    for line in issue_body.splitlines():
      if line.lower().startswith("telegram_handle:"):
        telegram_handle = line.split(":")[1].strip()
        break

    # Add user to Telegram group and store information if valid
    if telegram_handle:
      if add_user_to_group(telegram_handle):
        # Extract and store user information (modify based on your template)
        age = None
        gender = None
        city = None
        for line in issue_body.splitlines():
          if line.lower().startswith("age:"):
            age = int(line.split(":")[1].strip())
          elif line.lower().startswith("gender:"):
            gender = line.split(":")[1].strip()
          elif line.lower().startswith("city:"):
            city = line.split(":")[1].strip()

        if age and gender and city:
          store_user_info(age, gender, city)
          print(f"User with Telegram handle {telegram_handle} added to group and information stored.")
        else:
          print(f"Error: Could not extract all user information for {telegram_handle}.")
      else:
        print(f"Error adding user {telegram_handle} to group.")
  else:
    print("Issue is missing required fields. Leaving a comment...")
    # Add a comment to the issue mentioning missing fields (modify as needed
