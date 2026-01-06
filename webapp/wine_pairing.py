# LLM을 통한 요리 정보 설명
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.runnables import RunnableLambda

from dotenv import load_dotenv
import os

load_dotenv(override=True, dotenv_path="../.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 와인과 페어링되는 음식
def describe_dish_prompt(input_type):

    prompt = ChatPromptTemplate([
        (
            "system", """
                You are a world-class gourmet and food connoisseur who has tasted cuisines from every culture and era.
                You have an exceptional ability to identify dishes from visual cues alone and to describe flavors with vivid, sensory language.

                Given an image of a dish, do the following:

                1. Identify the most likely name of the dish.
                - If the exact name is uncertain, suggest the closest well-known dish or culinary category.
                2. Briefly describe the origin or culinary style (e.g., Chinese banquet cuisine, Italian rustic cooking, modern fusion).
                3. Describe the flavor profile in rich, evocative detail, including:
                - Dominant tastes (umami, sweetness, saltiness, acidity, bitterness)
                - Aromas and sauces
                - Texture and mouthfeel
                - Balance and depth of flavor
                4. Write as if you have personally eaten this dish many times.

                Tone and style guidelines:
                - Sophisticated, vivid, and expressive
                - Sensory-focused (taste, aroma, texture)
                - Confident but not speculative
                - Avoid mentioning the image itself; speak as a gourmet describing the dish directly

                Output format:

                Dish Name:
                Culinary Style / Origin:
                Flavor Description:

            """),
        HumanMessagePromptTemplate.from_template([
            {"text": """아래의 이미지의 요리에 대한 요리명과 요리의 풍미를 설명해 주세요.
             출력형태 :
             요리명 : 
             풍미 설명 :
             """},
            {"image_url": "{image_url}"} # image_url는 정해져 있음.
        ])
    ])

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1,
        api_key=GEMINI_API_KEY
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    return chain

# 함수 실행
def wine_pairing_main(img_url):

    # 함수를 전달인자로 넣기
    runnable_1 = RunnableLambda(describe_dish_prompt)

    # RunnableLambda를 통한 함수 실행
    input_data = {
        "image_url": img_url
        }
    
    response = runnable_1.invoke(input_data)
    return response

# 모듈 테스트용 코드
if __name__ == "__main__":
    img = "https://postfiles.pstatic.net/MjAyNDAyMTRfMTYx/MDAxNzA3OTEzODI5NDYx.LBvJwuKNKG2Sg6z61m0GwwXClLZ2AtRggm1oq_aGLFkg.tpalMG_Xm2GxJx7JbTfdN_PZ4xXBZky7Y-2lnbokHCcg.JPEG.alswl0224/%EC%A0%84%EA%B0%80%EB%B3%B5_(2).jpg?type=w966"
    result = wine_pairing_main(img)
    print(result)