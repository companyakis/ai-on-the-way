A Tool is a function given to the LLM. This function should fulfill a clear objective.

Here are some commonly used tools in AI agents:

<img width="679" height="280" alt="image" src="https://github.com/user-attachments/assets/926e383d-3ab8-40f4-8832-6ab7cdf70d47" />

Those are only examples, as you can in fact create a tool for any use case!

A good tool should be something that complements the power of an LLM.

For instance, if you need to perform arithmetic, giving a calculator tool to your LLM will provide better results than relying on the native capabilities of the model.

Furthermore, LLMs predict the completion of a prompt based on their training data, which means that their internal knowledge only includes events prior to their training. 
Therefore, if your agent needs up-to-date data you must provide it through some tool.

For instance, if you ask an LLM directly (without a search tool) for today’s weather, the LLM will potentially hallucinate random weather.

A Tool should contain:

A textual description of what the function does.

A Callable (something to perform an action).

Arguments with typings.

(Optional) Outputs with typings.
