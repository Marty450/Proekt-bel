import streamlit as st

st.title("Откриване дали сте народ")
st.text("маркирайте верния отговор")

score_map = {
    "Напълно съгласен": 4,
    "Частично съгласен": 3,
    "Частично несъгласен": 2,
    "Напълно несъгласен": 1,
}

# 1. Инициализираме състоянието на сесията
if "page" not in st.session_state:
    st.session_state.page = 1

if "answers" not in st.session_state:
    # Задаваме начален отговор "Напълно съгласен" за всички 10 въпроса в паметта
    st.session_state.answers = {i: "Напълно съгласен" for i in range(1, 11)}


class Questions:

    def __init__(self):
        self.score = 0

    def save_choice(self, page_num):
        """Функция, която веднага записва избора в дългосрочната памет"""
        key = f"q{page_num}"
        if key in st.session_state:
            st.session_state.answers[page_num] = st.session_state[key]

    def Question(self, num):
        n = num
        options = list(score_map)
        # Взимаме записания отговор от паметта, за да знаем кой индекс да маркираме
        current_saved = st.session_state.answers[n]
        default_idx = options.index(current_saved)

        # Използваме 'on_change', за да извикаме записването веднага при клик
        match n:
            case 1:
                st.radio("Човек се ражда индивид, но се превръща в част от народ чрез съзнателен избор.", options, index=default_idx, key="q1", on_change=self.save_choice, args=(1,))
            case 2:
                st.radio("Познаването на родовата история е задължително условие за силно самосъзнание.", options, index=default_idx, key="q2", on_change=self.save_choice, args=(2,))
            case 3:
                st.radio("Един народ съществува само докато пази живи своите традиции и обичаи.", options, index=default_idx, key="q3", on_change=self.save_choice, args=(3,))
            case 4:
                st.radio("Споделената болка от исторически несправедливости обединява хората повече от успеха.", options, index=default_idx, key="q4", on_change=self.save_choice, args=(4,))
            case 5:
                st.radio("Без обща ценностна система една група хора е просто население, а не народ.", options, index=default_idx, key="q5", on_change=self.save_choice, args=(5,))
            case 6:
                st.radio("Националното самосъзнание е пречка перед развитието на модерния, глобален човек.", options, index=default_idx, key="q6", on_change=self.save_choice, args=(6,))
            case 7:
                st.radio("Чувствам се лично отговорен за бъдещето на моя народ.", options, index=default_idx, key="q7", on_change=self.save_choice, args=(7,))
            case 8:
                st.radio("Общата визия за бъдещето е по-важна за един народ от общото му минало.", options, index=default_idx, key="q8", on_change=self.save_choice, args=(8,))
            case 9:
                st.radio("Чувствам се по-близък с хора, които споделят моите интереси, отколкото с тези от моята националност.", options, index=default_idx, key="q9", on_change=self.save_choice, args=(9,))
            case 10:
                st.radio("Процесът на „ставане на народ“ изисква всекидневно усилие, а не е еднократен исторически акт.", options, index=default_idx, key="q10", on_change=self.save_choice, args=(10,))

    def get_current_score(self):
        # Пресмятаме резултата директно от сигурната дългосрочна памет
        total = 0
        for i in range(1, 11):
            ans = st.session_state.answers[i]
            total += score_map[ans]
        return total


q = Questions()

# Извеждаме текущия въпрос
st.write(f"### Въпрос {st.session_state.page} от 10")
q.Question(st.session_state.page)

# Сигурен междинен запис преди смяна на страницата
q.save_choice(st.session_state.page)

# Бутони за навигация
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

# СИСТЕМА ЗА ОЦЕНЯВАНЕ
st.divider()
total_points = q.get_current_score()

if st.session_state.page == 10:
    st.subheader(f"Вашият краен резултат: {total_points} точки")
    
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
