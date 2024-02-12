

while True:

  user_input = input("You: ").lower()

  if user_input == "hi":
    print(f"Hi! How are you doing?")
  elif user_input == "good":
    print(f"That's great to hear! ")
  elif user_input == "bad":
    print(f"Oh no, sorry to hear that.  Is there anything I can do to help?")
  elif user_input in ["what's your name", "who are you"]:
    print(f"I'm Bard, your friendly chatbot! ")
  elif user_input == "bye":
    print(f"It was nice talking to you!  Until next time.")
  else:
    print(f"Sorry, I'm not sure what you mean.  How can I help you today?")

