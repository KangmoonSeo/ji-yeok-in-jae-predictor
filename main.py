import random


시행_횟수 = 10000
뽑는_인원 = 13
살아남은_2등_인원 = 10
로그_활성화 = False
추가_점수공개_인원 = [
    # "부산 B",
    # "부산 C",
    # "제주",
]


def main() -> None:

    print(f"총 인원: {len(추가_점수공개_인원)+15}명 ")
    print(f"1차 합격 인원: {뽑는_인원}명")
    print(f"시행 횟수: {시행_횟수}")

    for 인원 in range(살아남은_2등_인원 + 1):

        run_game(살아남은_2등_인원=인원)

    return


def run_game(살아남은_2등_인원: int):

    유효_감지 = 0
    text_log = ""

    for _ in range(시행_횟수):
        result, lg = play_once(살아남은_2등_인원=살아남은_2등_인원)

        if result is True:
            text_log = lg
            유효_감지 += 1

    if 로그_활성화 and len(text_log) > 1:
        print(text_log)

    확률 = round(유효_감지 / 시행_횟수 * 100)

    print(
        f"살아남은 2등 인원: {뽑는_인원}명 중 {살아남은_2등_인원}명, 유효 감지: {유효_감지} ({확률}%)"
    )


def play_once(살아남은_2등_인원: int):

    ballots = [
        "경기의 외로운 사자",
        "경기의 맹렬한 호랑이",
        "강원의 눈 덮인 늑대",
        "강원의 용맹한 백두산 호랑이",
        "강원의 신비로운 백두산 요정",
        "충남의 불굴의 백호",
        "충북의 씩씩한 맹호",
        "충북의 늠름한 금강산 용",
        "광주의 빛나는 불새",
        "전북의 거친 백두산 사자",
        "대구의 미친 개",
        "경북의 거대한 태산",
        "부산의 푸른 바다 용",
        "경남의 지혜로운 거북",
    ]

    ballots.extend(추가_점수공개_인원)
    sampled_ballots = ["인천"]
    b = random.sample(ballots, len(ballots))

    sampled_ballots.extend(b)

    m = {}
    cnt = 0
    i = 0
    text = "======\n"
    for ballot in sampled_ballots:

        i += 1
        text += f"{i}위: {ballot}"

        ballot = ballot[:2]
        if ballot in m:
            m[ballot] += 1
            text += f" {m[ballot]}등"
        else:
            m[ballot] = 1

        text += "\t"
        if i % 5 == 0:
            text += "\n"

        if i <= 뽑는_인원 and m[ballot] > 1:
            cnt += 1

    if cnt == 살아남은_2등_인원:
        return True, text

    return False, text


if __name__ == "__main__":

    main()
