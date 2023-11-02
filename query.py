import openai
import time

# Set API key
api_key = $APIKEY
openai.api_key = api_key

with open('abandon.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
    words = [line.strip() for line in lines]

# Split the words list into chunks of 50 (to stay within token limits)
chunks = [words[i:i + 50] for i in range(0, len(words), 50)]

# Iterate over each chunk
for chunk in chunks:
    query_content = "Ensure that the format for each line goes 'word, emoji' for these words: " + ", ".join(chunk)
    
    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query_content}
        ],
        temperature=0.8,
        max_tokens=1000  # Lowered to stay within token limits
    )
    
    # Extract and format the response content
    response_content = response['choices'][0]['message']['content'].strip()
    response_lines = response_content.split(", ")
    formatted_lines = [f"{word}, {emoji}" for word, emoji in zip(chunk, response_lines)]
    
    # Print each formatted line
    for line in formatted_lines:
        print(line)
    
    time.sleep(2)
