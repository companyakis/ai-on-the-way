LLMs are amazing models, but they can only generate text.

However, if you ask a well-known chat application like HuggingChat or ChatGPT to generate an image, they can! How is that possible?

The answer is that the developers of HuggingChat, ChatGPT and similar apps implemented additional functionality (called Tools), that the LLM can use to create images.

What type of tasks can an Agent do?

An Agent can perform any task we implement via Tools to complete Actions.

For example, if I write an Agent to act as my personal assistant (like Siri) on my computer, and I ask it to “send an email to my Manager asking to delay today’s meeting”, I can give it some code to send emails. 

This will be a new Tool the Agent can use whenever it needs to send an email. We can write it in Python:

<img width="969" height="127" alt="image" src="https://github.com/user-attachments/assets/188b751b-1bab-4dd0-855e-41ef22a68d15" />

The design of the Tools is very important and has a great impact on the quality of your Agent. 

Some tasks will require very specific Tools to be crafted, while others may be solved with general purpose tools like “web_search”.

Note that Actions are not the same as Tools. An Action, for instance, can involve the use of multiple Tools to complete.

