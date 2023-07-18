from config import Config
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI as OpenAILLM
from langchain.prompts import *
from langchain.chains import LLMChain

chat = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)

"""Base class for all prompt templates, returning a prompt."""
# base_prompt = BasePromptTemplate()

"""String prompt should expose the format method, returning a prompt."""
# string_prompt = StringPromptTemplate()


prompt = PromptTemplate(
        input_variables=["sentence"],
        template="Translate the following in Greek {sentence}",
    )


""" CHAT PROMPTS """
# ai_prompt = AIMessagePromptTemplate()


if __name__ == '__main__':

    chain_chat = LLMChain(
        llm=chat,
        prompt=prompt
    )

    # chain_chat.run('hey')

    # An example prompt with one input variable
    one_input_prompt = PromptTemplate(input_variables=["subject"], template="tell me a joke about {subject}")
    one_input_prompt.format(subject="soccer")
    print(one_input_prompt)
    # -> "Tell me a funny joke."

    string_prompt = PromptTemplate.from_template("tell me a joke about {subject}")
    string_prompt_value = string_prompt.format_prompt(subject="soccer")
    print(string_prompt_value.to_string())
    print(string_prompt_value.to_messages())



