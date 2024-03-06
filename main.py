import random


시행_횟수 = 1000
살아남은_2등_인원 = 3
로그_활성화 = True
추가_점수공개_인원 = [
    # "부산 B",
    # "제주",
]


def run_game() -> None:

    ballots = [
        "경기 A",
        "경기 B",
        "강원 A",
        "강원 B",
        "강원 C",
        "충남",
        "충북 A",
        "충북 B",
        "광주",
        "전북",
        "대구",
        "경북",
        "부산",
        "경남",
    ]
    ballots.extend(추가_점수공개_인원)

    유효_감지 = 0
    for _ in range(시행_횟수):
        result = play_once(
            로그_활성화=로그_활성화,
            살아남은_2등_인원=살아남은_2등_인원,
            ballots=ballots,
        )

        if result is True:
            유효_감지 += 1

    print(f"총 인원: {len(ballots)+1}명 ")
    print("1차 합격 인원: 13명")
    print(f"살아남은 2등 인원: 13명 중 {살아남은_2등_인원}명")
    print(f"시행 횟수: {시행_횟수}")
    print(f"유효 감지: {유효_감지}")

    return


def play_once(로그_활성화: bool, 살아남은_2등_인원: int, ballots: list):

    sampled_ballots = ["인천"]
    b = random.sample(ballots, len(ballots))

    sampled_ballots.extend(b)

    m = {}
    cnt = 0
    i = 0
    text = ""
    for ballot in sampled_ballots:

        ballot = ballot[:2]
        if ballot in m:
            m[ballot] += 1
        else:
            m[ballot] = 1

        i += 1
        text += f"{i}위: {ballot}"

        if m[ballot] > 1:
            text += f" {m[ballot]}등"
        text += "\t"
        if i % 3 == 0:
            text += "\n"

        if i <= 13 and m[ballot] > 1:
            cnt += 1

    text += "\n======\n"

    if cnt == 살아남은_2등_인원:

        if 로그_활성화:
            print(text)

        return True

    return False


if __name__ == "__main__":
    run_game()
