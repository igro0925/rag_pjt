from fastapi import FastAPI
from wine_pairing import wine_pairing_main # 파일에 있는것을 메모리에 올리기 

# FastAPI 객체 생성
app = FastAPI()

# 홈
# https://postfiles.pstatic.net/MjAyNDAyMTRfMTYx/MDAxNzA3OTEzODI5NDYx.LBvJwuKNKG2Sg6z61m0GwwXClLZ2AtRggm1oq_aGLFkg.tpalMG_Xm2GxJx7JbTfdN_PZ4xXBZky7Y-2lnbokHCcg.JPEG.alswl0224/%EC%A0%84%EA%B0%80%EB%B3%B5_(2).jpg?type=w966
@app.get("/")
async def home(image_url: str):
    # 사용자 image_url 입력 받기
    print(image_url)

    # 이미지의 요리명, 요리의 풍미 설명(llm) -> wine top-5 검색 -> 요리에 어울리는 와인 추천
    # llm을 통해 추천 받은 것을 사용자에게 반환
    # result = wine_pairing_main(image_url)
    # print(result)

    result = """
    요리명: 팔보채 (Palbochae)

    풍미 설명:
    이 요리는 중국식 연회 요리의 정수 중 하나로, 풍성한 해산물과 다채로운 채소가 어우러져 시각과 미각을 동시에 만족시키는 걸작입니다. 한 입 맛보는 순간, 혀끝을 감싸는 진하고 농후한 감칠맛이 가장 먼저 다가옵니다. 간장과 굴 소스, 그리고 깊은 육수가 완
    벽하게 어우러진 소스는 윤기 흐르는 벨벳 같은 질감으로 모든 재료를 부드럽게 감싸 안습니다.

    주요 해산물에서는 각기 다른 매력이 폭발합니다. 탱글탱글하게 씹히는 새우는 바다의 신선한 단맛을 선사하고, 오징어는 부드럽고 쫄깃한 식감 사이로 은은한 바다향을 뿜어냅니다. 특히 관자는 입안에서 사르르 녹아내리며 응축된 감칠맛을 남기고, 농어 또는 전복 같은 귀한 재료
    들은 탄력 있는 살점과 깊은 풍미로 요리의 품격을 더합니다.

    여기에 더해진 채소들은 단순히 거드는 역할이 아닙니다. 두툼하게 썰린 표고버섯은 고기처럼 쫄깃한 식감과 흙내음 가득한 깊은 향을 더하고, 연근은 아삭한 식감으로 전체적인 조화에 상쾌한 대비를 제공합니다. 큼직한 파와 아삭한 죽순은 향긋한 풍미를 더하며, 선명한 초록색의
    완두콩은 색감뿐 아니라 톡 터지는 식감으로 즐거움을 줍니다.

    전반적으로 이 팔보채는 짭짤하고 고소한 감칠맛이 지배적이지만, 재료 본연의 단맛과 채소의 신선함이 섬세하게 균형을 이룹니다. 매콤함은 거의 느껴지지 않으며, 재료 각각의 맛과 향을 살리면서도 걸쭉한 소스가 이를 하나로 묶어주는 조화로운 깊이가 인상적입니다. 입안 가득 
    다채로운 식감과 풍부한 맛의 향연이 펼쳐지는, 진정으로 잊을 수 없는 미식 경험을 선사하는 요리입니다.
    """

    return {"message": result}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000, reload=True)