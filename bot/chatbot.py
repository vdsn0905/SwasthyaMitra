import requests

def get_covid_stats(country: str = "India") -> str:
    """Fetch live COVID-19 stats (no API key required)"""
    try:
        url = f"https://disease.sh/v3/covid-19/countries/{country}"
        response = requests.get(url).json()
        cases = response.get("cases", "N/A")
        deaths = response.get("deaths", "N/A")
        recovered = response.get("recovered", "N/A")
        today_cases = response.get("todayCases", "N/A")
        return (
            f"🦠 COVID-19 in {country}:\n"
            f"Cases: {cases:,}\n"
            f"Deaths: {deaths:,}\n"
            f"Recovered: {recovered:,}\n"
            f"New cases today: {today_cases:,}"
        )
    except:
        return "⚠️ Unable to fetch COVID-19 stats right now."

def get_global_covid_stats() -> str:
    """Fetch global COVID-19 stats (no API key required)"""
    try:
        url = "https://disease.sh/v3/covid-19/all"
        response = requests.get(url).json()
        cases = response.get("cases", "N/A")
        deaths = response.get("deaths", "N/A")
        recovered = response.get("recovered", "N/A")
        return (
            f"🌍 Global COVID-19 Stats:\n"
            f"Cases: {cases:,}\n"
            f"Deaths: {deaths:,}\n"
            f"Recovered: {recovered:,}"
        )
    except:
        return "⚠️ Unable to fetch global COVID-19 stats."

def get_disease_stats(disease: str = "dengue") -> str:
    """Fetch outbreak data for specific diseases (from disease.sh, no key)"""
    try:
        url = "https://disease.sh/v3/covid-19/historical/all?lastdays=1"
        response = requests.get(url).json()
        # disease.sh mainly has COVID historical data,
        # but we simulate for other diseases (static message or link).
        if disease.lower() == "monkeypox":
            return "🐒 Monkeypox cases are being tracked by WHO. Common symptoms: fever, rash, swollen lymph nodes."
        elif disease.lower() == "dengue":
            return "🦟 Dengue outbreaks are common in tropical regions. Symptoms: high fever, headache, joint pain. Prevent with mosquito nets & repellents."
        elif disease.lower() == "ebola":
            return "🧬 Ebola outbreaks: rare but deadly. Symptoms: fever, bleeding, weakness. Immediate isolation & medical care needed."
        else:
            return f"⚠️ Sorry, I don’t have live stats for {disease}. Try asking about COVID, dengue, or monkeypox."
    except:
        return "⚠️ Unable to fetch outbreak data right now."

# ---------- MAIN CHATBOT ----------

def health_chatbot(user_message: str) -> str:
    """Health chatbot with static + live outbreak data"""
    user_message = user_message.lower()

    # Greetings
    if "hello" in user_message or "hi" in user_message:
        return "Hello 👋 I am your Health Bot. You can ask me about symptoms, prevention, COVID stats, or outbreaks like dengue/monkeypox."

    # Live data
    elif "covid cases" in user_message or "covid stats" in user_message:
        return get_covid_stats("India")
    elif "global covid" in user_message or "world covid" in user_message:
        return get_global_covid_stats()
    elif "dengue" in user_message:
        return get_disease_stats("dengue")
    elif "monkeypox" in user_message:
        return get_disease_stats("monkeypox")
    elif "ebola" in user_message:
        return get_disease_stats("ebola")

    # Symptoms & diseases
    elif "fever" in user_message:
        return "🌡️ Fever may be caused by infection or dehydration. Rest, drink fluids, and monitor. If it lasts >3 days, see a doctor."
    elif "headache" in user_message:
        return "🤕 Headache may be due to stress, dehydration, or eye strain. Drink water, rest, and avoid screen time."
    elif "cough" in user_message:
        return "😷 Cough can result from cold, flu, or allergies. Drink warm fluids, avoid dust, and use steam inhalation. Persistent cough? Get checked."
    elif "diabetes" in user_message:
        return "🍬 Diabetes management: balanced diet, exercise, regular sugar checks. Avoid excess sugar & processed foods."
    elif "heart" in user_message:
        return "❤️ Heart health tip: exercise daily, eat fruits/veggies, avoid smoking & excess alcohol."

    # Prevention & lifestyle
    elif "vaccine" in user_message:
        return "💉 Vaccines protect against severe diseases. Stay updated with COVID, Flu, and other vaccines. Visit your nearest health center."
    elif "diet" in user_message:
        return "🥗 Eat fruits, vegetables, whole grains, lean proteins. Limit fried foods & sugary drinks."
    elif "exercise" in user_message:
        return "🏃‍♂️ 30 mins of daily activity (walking, yoga, cycling) keeps your body and mind healthy."

    # Default
    else:
        return "❓ Sorry, I didn't understand. Try asking about fever, COVID stats, dengue, monkeypox, vaccines, or heart health."
