import streamlit as st
import streamlit.components.v1 as components
import base64

# Load your .mmd file content
def load_mmd_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Base64 encode the .mmd content
def encode_mmd_content(mmd_content):
    return base64.b64encode(mmd_content.encode()).decode()

# Define the HTML template with embedded JS to render Mermaid diagram
def create_mermaid_html(encoded_mmd):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mermaid Diagram Display</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
  <div class="mermaid" id="mermaid">
    <!-- The .mmd content will be loaded here -->
  </div>

  <script>
    // Decode the base64 .mmd content
    const encodedContent = "{encoded_mmd}";
    const decodedContent = atob(encodedContent);
  
    // Initialize Mermaid
    mermaid.initialize({{ startOnLoad: true }});

    // Add the .mmd content to the Mermaid div
    document.addEventListener('DOMContentLoaded', (event) => {{
      document.getElementById('mermaid').textContent = decodedContent;
      mermaid.init(undefined, '#mermaid');
    }});
  </script>
</body>
</html>
"""


# Main function to run the Streamlit app
def main():
    # Path to your .mmd file
    mmd_file_path = 'output.mmd'

    # Load and encode the content of the .mmd file
    mmd_content = load_mmd_content(mmd_file_path)
    encoded_mmd = encode_mmd_content(mmd_content)

    # Create the HTML content
    html_content = create_mermaid_html(encoded_mmd)

    # Display the HTML content with the Mermaid diagram in the Streamlit app
    components.html(html_content, height=600, scrolling=True)

# Run the main function
if __name__ == "__main__":
    main()
