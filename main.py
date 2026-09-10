# main.py

# 기본 프롬프트 데이터 (이전 미션에서 작성한 프롬프트 3개 이상)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝은 배경과 선명한 색감으로 표현해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 기술 용어를 쉽게 풀어 설명해주세요.",
        "category": "페르소나",
        "favorite": False
    },
]

# 카테고리 목록 (미션 요구사항의 6가지)
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def input_not_empty(message):
    """빈 값이면 다시 입력받는 함수"""
    while True:
        value = input(message).strip()
        if value:              # 값이 있으면
            return value
        print("⚠️ 빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


def add_prompt():
    """새 프롬프트를 추가하는 함수"""
    print("\n=== 프롬프트 추가 ===")

def show_list():
    """저장된 모든 프롬프트를 목록으로 출력하는 함수"""

def show_by_category():
    """카테고리를 선택하면 해당 카테고리의 프롬프트만 출력하는 함수"""
    print("\n=== 카테고리별 조회 ===")

    # 카테고리 목록 정의 (add_prompt와 동일하게)
    categories = ["텍스트 생성", "이미지 생성", "영상 생성",
                  "페르소나", "자동화", "기타"]

    # 카테고리 번호와 함께 출력
    for i, name in enumerate(categories, start=1):
        print(f"{i}) {name}")

    choice = input("선택: ")

    # 입력값 검증: 1~6 사이 숫자인지 확인
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(categories):
        print("⚠️ 잘못된 번호입니다.")
        return

    # 선택한 카테고리 이름 구하기
    selected = categories[int(choice) - 1]

    # 해당 카테고리의 프롬프트만 골라내기
    filtered = [p for p in prompts if p["category"] == selected]

    # 결과 출력
    print(f"\n[{selected}] 카테고리 프롬프트:")

    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, p in enumerate(filtered, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")

    print(f"총 {len(filtered)}개의 프롬프트")




    print("\n=== 프롬프트 목록 ===")

    # 프롬프트가 하나도 없으면 안내
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 번호와 함께 하나씩 출력
    for i, p in enumerate(prompts, start=1):
        star = " ⭐" if p["favorite"] else ""   # 즐겨찾기면 별 표시
        print(f"{i}. [{p['category']}] {p['title']}{star}")

    print(f"총 {len(prompts)}개의 프롬프트")




    # 1. 제목, 내용 입력 (비어있으면 다시)
    title = input_not_empty("제목: ")
    content = input_not_empty("내용: ")

    # 2. 카테고리 선택
    print("카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}) {cat}")

    while True:
        choice = input("선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = CATEGORIES[int(choice) - 1]
            break
        print("⚠️ 잘못된 번호입니다. 다시 선택해주세요.")

    # 3. 딕셔너리로 만들어 리스트에 추가
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False        # 즐겨찾기 기본값 False
    }
    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다! ✅")

def show_menu():
    """메뉴를 화면에 출력하는 함수"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    """프로그램의 메인 실행 흐름"""
    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        elif choice == "1":
            add_prompt()          # ← "(준비 중)" 대신 실제 함수 호출!
        elif choice == "2":
            show_list()          # ← "(준비 중)" 대신 실제 함수 호출!
        elif choice == "3":
            show_by_category()   # ← 실제 함수 호출!
        elif choice == "4":
            print("→ (준비 중) 프롬프트 검색")
        elif choice == "5":
            print("→ (준비 중) 상세 보기")
        elif choice == "6":
            print("→ (준비 중) 즐겨찾기 관리")
        elif choice == "7":
            print("→ (준비 중) 즐겨찾기 목록")
        else:
            print("⚠️ 잘못된 번호입니다. 다시 선택해주세요.")


# 프로그램 시작점
if __name__ == "__main__":
    main()