import os
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    print("Hello!")
    load_dotenv(find_dotenv(), override=True)

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

information = """
George Washington (February 22, 1732 – December 14, 1799) was an American Founding Father, military officer, and politician who served as the first president of the United States from 1789 to 1797. Appointed by the Second Continental Congress as commander of the Continental Army in 1775, Washington led Patriot forces to victory in the American Revolutionary War and then served as president of the Constitutional Convention in 1787, which drafted the current Constitution of the United States. Washington has thus become commonly known as the "Father of his Country".

Washington's first public office, from 1749 to 1750, was as surveyor of Culpeper County in the Colony of Virginia. In 1752, he received military training and was granted the rank of major in the Virginia Regiment. During the French and Indian War, Washington was promoted to lieutenant colonel in 1754 and subsequently became head of the Virginia Regiment in 1755. He was later elected to the Virginia House of Burgesses and was named a delegate to the Continental Congress in Philadelphia, which appointed him commander-in-chief of the Continental Army. Washington led American forces to a decisive victory over the British in the Revolutionary War, leading the British to sign the Treaty of Paris, which acknowledged the sovereignty and independence of the United States. He resigned his commission in 1783 after the conclusion of the Revolutionary War.

Washington played an indispensable role in adopting and ratifying the Constitution, which replaced the Articles of Confederation in 1789. He was then twice elected president unanimously by the Electoral College in 1788 and 1792. As the first U.S. president, Washington implemented a strong, well-financed national government while remaining impartial in a fierce rivalry that emerged between cabinet members Thomas Jefferson and Alexander Hamilton. During the French Revolution, he proclaimed a policy of neutrality while additionally sanctioning the Jay Treaty. He set enduring precedents for the office of president, including republicanism, a peaceful transfer of power, the use of the title "Mr. President", and the two-term tradition. His 1796 farewell address became a preeminent statement on republicanism in which he wrote about the importance of national unity and the dangers that regionalism, partisanship, and foreign influence pose to it.

Washington's image is an icon of American culture. He has been memorialized by monuments, a federal holiday, various media depictions, geographical locations including the national capital, the State of Washington, stamps, and currency. In 1976, Washington was posthumously promoted to the rank of general of the Armies, the highest rank in the U.S. Army. Washington consistently ranks in both popular and scholarly polls as one of the greatest presidents in American history.
"""

# The old method/way of creating chains

summary_template = """
Given the information: {information} about a person, I want you to create: 
1. a short summary 
2. two interesting facts about them
"""

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain = LLMChain(llm=llm, prompt=summary_prompt_template, verbose=True)

output = chain.invoke({"information": information})

print(output)

# The new method/way of creating chains

summary_template_new = """
Given the information: {information} about a person, I want you to create: 
1. a short summary 
2. two interesting facts about them
"""

summary_prompt_template_new = PromptTemplate(
    input_variables=["information"], template=summary_template_new
)

llm_new = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

chain_2 = summary_prompt_template_new | llm_new

print(chain_2.invoke(input={"information": information}))
