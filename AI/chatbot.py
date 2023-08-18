import requests
import json

def get_answer(question):
  """
  This function gets an answer from Google Search for the given question.

  Args:
    question: The question to ask Google Search.

  Returns:
    The answer from Google Search.
  """

  # Make a request to Google Search.
  response = requests.get("https://www.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_SEARCH_ENGINE_ID&q=" + question)

  # Check if the request was successful.
  if response.status_code == 200:
    # Parse the JSON response.
    result = json.loads(response.content)

    # Get the first result.
    result_0 = result["items"][0]

    # Return the title and snippet of the first result.
    return result_0["title"], result_0["snippet"]
  else:
    # The request was not successful.
    return None, None

def main():
  # Get the user's question.
  question = input("What is your question? ")

  # Get the answer from Google Search.
  answer, snippet = get_answer(question)

  # Print the answer.
  print("Answer:", answer)
  print("Snippet:", snippet)

if __name__ == "__main__":
  main()
