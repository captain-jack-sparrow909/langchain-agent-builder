from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI



load_dotenv()



def main():
    information = """
        Muhammad ibn Musa al-Khwarizmi,[note 1] or simply al-Khwarizmi (c. 780 – c. 850) was a mathematician active during the Islamic Golden Age, who produced Arabic-language works in mathematics, astronomy, and geography. Around 820, he worked at the House of Wisdom in Baghdad, the contemporary capital city of the Abbasid Caliphate. One of the most prominent scholars of the period, his works were widely influential on later authors, both in the Islamic world and Europe.
        Few biographical details are known about al-Khwarizmi's life. His popularizing treatise on algebra, compiled between 813 and 833 as Al-Jabr (The Compendious Book on Calculation by Completion and Balancing),[7]: 171  presented the first systematic solution of linear and quadratic equations. One of his achievements in algebra was his demonstration of how to solve quadratic equations by completing the square, for which he provided geometric justifications.[8]: 14  Because al-Khwarizmi was the first person to treat algebra as an independent discipline and introduced the methods of "reduction" and "balancing" (the transposition of subtracted terms to the other side of an equation, that is, the cancellation of like terms on opposite sides of the equation),[9] he has been described as the father[10][11][12] or founder[13][14] of algebra. The English term algebra comes from the short-hand title of his aforementioned treatise (الجبر Al-Jabr, transl. "completion" or "rejoining").[15] His name gave rise to the English terms algorism and algorithm; the Spanish, Italian, and Portuguese terms algoritmo; and the Spanish term guarismo[16] and Portuguese term algarismo, all meaning 'digit'.
    """

    summary_template = """
    Given the following information about {information}, I want you to create:
    1. A short summary of the information
    2. 2 interesting facts about the information
    """

    prompt = PromptTemplate(input_variables=["information"], template=summary_template);
    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    chain = prompt | llm
    response = chain.invoke({"information": information})
    print("Hello from langchain!", response)


if __name__ == "__main__":
    main()
