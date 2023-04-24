import openai
import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# OpenAI API credentials
openai.api_key = "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"

# GitHub credentials
github_repository_name = "mkkaoa"
github_username = "MKVde"
token = "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"

# Email credentials
my_email_address = "abdi.moa11021@outlook.com"
email_password = "Mka*&#BWhdsh1109119841098@#@"
received_email_address = "mo.crisaaq@gmail.com"

base_dir = "C:/Users/abdir/OneDrive/Desktop/Web Dev/Web Scraping Learn/Automated GitHub repository/This file to GitHub/Another Try"

# Specify the path to the web scraping script
#script_path = "C:/Users/abdir/OneDrive/Desktop/Web Dev/Web Scraping Learn/Automated GitHub repository/This file to GitHub/web_scraping_script.py"
script_path = f"{base_dir}/web_scraping_script.py"

# Read the script contents
with open(script_path, "r") as f:
    script_contents = f.read()
engine_model = "text-davinci-002"
# Generate the README using OpenAI's GPT-3 language model
response = openai.Completion.create(
    engine= engine_model,
    prompt=(
        "- Generate a README file for a web scraping project that reads the following script: \n - Use common template for a structure README file in GitHub.\n"
        f"{script_contents}"
    ),
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.7,
)

# Get the generated README text
readme_text = response.choices[0].text

# Step 2: Create the README file
#readme_path = "C:/Users/abdir/OneDrive/Desktop/Web Dev/Web Scraping Learn/Automated GitHub repository/This file to GitHub/README.md"
readme_path = f"{base_dir}/README.md"

with open(readme_path, "w") as f:
    f.write(readme_text)



# Change to the project directory
#os.chdir("C:/Users/abdir/OneDrive/Desktop/Web Dev/Web Scraping Learn/Automated GitHub repository/This file to GitHub")
os.chdir(base_dir)
# Initialize the git repository
subprocess.run(["git", "init"])

# Add all files to the git repository
subprocess.run(["git", "add", "."])

# Commit the changes
subprocess.run(["git", "commit", "-m", "Initial commit"])

# Set the remote origin to the GitHub repository
subprocess.run(
    [
        "git",
        "remote",
        "add",
        "origin",
        f"git@github.com:{github_username}/{github_repository_name}.git",
    ]
)

# Push the changes to the GitHub repository
subprocess.run(["git", "push", "-u", "origin", "master"])


# Create a multipart message
message = MIMEMultipart()

# Add the email subject and body
message["Subject"] = "GitHub repository upload complete"
message["From"] = my_email_address
message["To"] = received_email_address
body = "Your project has been successfully uploaded to GitHub! Here is the link to the repository:\n\n"
repository_url = f"https://github.com/{github_username}/{github_repository_name}"
body += repository_url
message.attach(MIMEText(body, "plain"))

# Add the README file as an attachment
with open(readme_path, "rb") as f:
    attachment = MIMEApplication(f.read(), _subtype="txt")
    attachment.add_header("Content-Disposition", "attachment", filename="README.md")
    message.attach(attachment)

# Send the email
with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(my_email_address, email_password)
        server.sendmail(my_email_address, received_email_address, message.as_string())
        print("Email sent successfully!")