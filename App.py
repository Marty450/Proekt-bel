import streamlit as st

st.title("Откриване дали сте народ")
st.text("маркирайте верния отговор")

score_map = {
    "Напълно съгласен": 4,
    "Частично съгласен": 3,
    "Частично несъгласен": 2,
    "Напълно несъгласен": 1
}

if "page" not in st.session_state:
    st.session_state.page = 1
class Questions:

    def __init__(self):
        self.score = 0

    def Question(self, num):
        n = num

        match n:

            case 1:
                answer = st.radio("Човек се ражда индивид, но се превръща в част от народ чрез съзнателен избор.",list(score_map),key=1)
                self.score += score_map[answer]
            case 2:
                answer = st.radio("Познаването на родовата история е задължително условие за силно самосъзнание.",list(score_map),key=2)
                self.score += score_map[answer]
            case 3:
                answer = st.radio("Един народ съществува само докато пази живи своите традиции и обичаи.",list(score_map),key=3)
                self.score += score_map[answer]
            case 4:
                answer = st.radio("Споделената болка от исторически несправедливости обединява хората повече от успеха.",list(score_map),key=4)
                self.score += score_map[answer]
            case 5:
                answer = st.radio("Без обща ценностна система една група хора е просто население, а не народ.",list(score_map),key=5)
                self.score += score_map[answer]
            case 6:
                answer = st.radio("Националното самосъзнание е пречка пред развитието на модерния, глобален човек.",list(score_map),key=6)
                self.score += score_map[answer]
            case 7:
                answer = st.radio("Чувствам се лично отговорен за бъдещето на моя народ.",list(score_map),key=7)
                self.score += score_map[answer]
            case 8:
                answer = st.radio("Общата визия за бъдещето е по-важна за един народ от общото му минало.",list(score_map),key=8)
                self.score += score_map[answer]
            case 9:
                answer = st.radio("Чувствам се по-близък с хора, които споделят моите интереси, отколкото с тези от моята националност.",list(score_map),key=9)
                self.score += score_map[answer]
            case 10:
                answer = st.radio("Процесът на „ставане на народ“ изисква всекидневно усилие, а не е еднократен исторически акт.",list(score_map),key=10)
                self.score += score_map[answer]

q = Questions()
st.write(f"Въпрос {st.session_state.page} от 10")
q.Question(st.session_state.page)

col1, col2 = st.columns(2)
with col1:
    if st.session_state.page > 1:
        if st.button("Предишен въпрос"):
            st.session_state.page -= 1
            st.rerun()
with col2:
    if st.session_state.page < 10:
        if st.button("Следващ въпрос"):
            st.session_state.page += 1
            st.rerun()

st.write("Общ резултат:", q.score)
