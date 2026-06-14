import streamlit as st

st.title("Откриване дали сте народ")
st.text("маркирайте верния отговор")

score_map = {
    "Напълно съгласен": 4,
    "Частично съгласен": 3,
    "Частично несъгласен": 2,
    "Напълно несъгласен": 1,
}

# Инициализираме паметта за текущия въпрос
if "page" not in st.session_state:
    st.session_state.page = 1


class Questions:

    def __init__(self):
        self.score = 0

    def Question(self, num):
        n = num
        match n:
            case 1:
                st.radio("Човек се ражда индивид, но се превръща в част от народ чрез съзнателен избор.", list(score_map), key="q1")
            case 2:
                st.radio("Познаването на родовата история е задължително условие за силно самосъзнание.", list(score_map), key="q2")
            case 3:
                st.radio("Един народ съществува само докато пази живи своите традиции и обичаи.", list(score_map), key="q3")
            case 4:
                st.radio("Споделената болка от исторически несправедливости обединява хората повече от успеха.", list(score_map), key="q4")
            case 5:
                st.radio("Без обща ценностна система една група хора е просто население, а не народ.", list(score_map), key="q5")
            case 6:
                st.radio("Националното самосъзнание е пречка пред развитието на модерния, globalен човек.", list(score_map), key="q6")
            case 7:
                st.radio("Чувствам се лично отговорен за бъдещето на моя народ.", list(score_map), key="q7")
            case 8:
                st.radio("Общата визия за бъдещето е по-важна за един народ от общото му минало.", list(score_map), key="q8")
            case 9:
                st.radio("Чувствам се по-близък с хора, които споделят моите интереси, отколкото с тези от моята националност.", list(score_map), key="q9")
            case 10:
                st.radio("Процесът на „ставане на народ“ изисква всекидневно усилие, а не е еднократен исторически акт.", list(score_map), key="q10")

    def get_current_score(self):
        # Автоматично събира точките от всички отговорени до момента въпроси
        total = 0
        for i in range(1, 11):
            key = f"q{i}"
            if key in st.session_state:
                user_choice = st.session_state[key]
                total += score_map[user_choice]
        return total


q = Questions()

# Показваме текущия въпрос
st.write(f"### Въпрос {st.session_state.page} от 10")
q.Question(st.session_state.page)

# Навигация с бутони
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

# СИСТЕМА ЗА ОЦЕНЯВАНЕ И РЕЗУЛТАТИ
st.divider()
total_points = q.get_current_score()

if st.session_state.page == 10:
    st.subheader(f"Вашият краен резултат: {total_points} точки")
    
    # Проверка на скалата и извеждане на съответния коментар и съвет
    if 10 <= total_points <= 19:
        st.error("**Резултат:** Далеч от идеята за истинска общност.")
        st.info("**Съвет:** Започни да слушаш, уважаваш и помагаш на другите.")
        
    elif 20 <= total_points <= 24:
        st.warning("**Резултат:** Показва първи стъпки към общностните ценности.")
        st.info("**Съвет:** Участвай по-често в общи дейности и инициативи.")
        
    elif 25 <= total_points <= 29:
        st.info("**Резултат:** Разбира значението на единството и взаимопомощта.")
        st.info("**Съвет:** Развивай чувство за отговорност към общността.")
        
    elif 30 <= total_points <= 35:
        st.success("**Резултат:** Близо до ценностите на сплотения народ.")
        st.info("**Съвет:** Бъди пример за единство, уважение и солидарност.")
        
    elif 36 <= total_points <= 40:
        st.success("**Резултат:** Отличен пример за гражданска отговорност и единство.")
        st.info("**Съвет:** Продължавай да обединяваш хората и да вдъхновяваш.")
else:
    st.caption(f"Текущ временен резултат: {total_points} т.")
