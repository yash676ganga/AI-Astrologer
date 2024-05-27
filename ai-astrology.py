
from kerykeion import Report, AstrologicalSubject

import google.generativeai as genai

genai.configure(api_key="Enter your API Key")

# Define the astrological subject
def get_user_input():
    name = input("Enter name: ")
    year = int(input("Enter birth year: "))
    month = int(input("Enter birth month: "))
    day = int(input("Enter birth day: "))
    hour = int(input("Enter birth hour: "))
    minute = int(input("Enter birth minute: "))
    city = input("Enter city: ")
    nation = input("Enter nation: ")
    return name, year, month, day, hour, minute, city, nation

name, year, month, day, hour, minute, city, nation = get_user_input()

Ram = AstrologicalSubject(name, year, month, day, hour, minute, city, nation)


def retrograde_planets_message(subject):
    planets = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
    
    retrograde_planets = [planet for planet in planets if getattr(subject, planet).get('retrograde', False)]
    non_retrograde_planets = [planet for planet in planets if planet not in retrograde_planets]
    
    retrograde_message = f"Retrograde planets: {retrograde_planets}"
    
    if non_retrograde_planets:
        retrograde_message += f"\nremaining planets are non-retrograde."
    else:
        retrograde_message += "\nAll planets are in retrograde."
    
    return retrograde_message

# Get astrological report
report = Report(Ram)


# Extract Sun data from Ram.sun

# ... (previous code)

sun_data = Ram.sun
sun_info = f"Sun in {sun_data['sign']} sign, positioned {sun_data['position']:.1f}° in {sun_data['house']}."

moon_data = Ram.moon
moon_info = f"Moon in {moon_data['sign']} sign, positioned {moon_data['position']:.1f}° in {moon_data['house']}."

mercury_data = Ram.mercury
mercury_info = f"Mercury in {mercury_data['sign']} sign, positioned {mercury_data['position']:.1f}° in {mercury_data['house']}."

venus_data = Ram.venus
venus_info = f"Venus in {venus_data['sign']} sign, positioned {venus_data['position']:.1f}° in {venus_data['house']}."

mars_data = Ram.mars
mars_info = f"Mars in {mars_data['sign']} sign, positioned {mars_data['position']:.1f}° in {mars_data['house']}."

jupiter_data = Ram.jupiter
jupiter_info = f"Jupiter in {jupiter_data['sign']} sign, positioned {jupiter_data['position']:.1f}° in {jupiter_data['house']}."

saturn_data = Ram.saturn
saturn_info = f"Saturn in {saturn_data['sign']} sign, positioned {saturn_data['position']:.1f}° in {saturn_data['house']}."

uranus_data = Ram.uranus
uranus_info = f"Uranus in {uranus_data['sign']} sign, positioned {uranus_data['position']:.1f}° in {uranus_data['house']}."

neptune_data = Ram.neptune
neptune_info = f"Neptune in {neptune_data['sign']} sign, positioned {neptune_data['position']:.1f}° in {neptune_data['house']}."

pluto_data = Ram.pluto
pluto_info = f"Pluto in {pluto_data['sign']} sign, positioned {pluto_data['position']:.1f}° in {pluto_data['house']}."

mean_node_data = Ram.mean_node
mean_node_info = f"Mean Node in {mean_node_data['sign']} sign, positioned {mean_node_data['position']:.1f}° in {mean_node_data['house']}."

true_node_data = Ram.true_node
true_node_info = f"True Node in {true_node_data['sign']} sign, positioned {true_node_data['position']:.1f}° in {true_node_data['house']}."

chiron_data = Ram.chiron
chiron_info = f"Chiron in {chiron_data['sign']} sign, positioned {chiron_data['position']:.1f}° in {chiron_data['house']}."

first_house_data = Ram.first_house
first_house_info = f"First House in {first_house_data['sign']} sign, positioned {first_house_data['position']:.1f}°."

second_house_data = Ram.second_house
second_house_info = f"Second House in {second_house_data['sign']} sign, positioned {second_house_data['position']:.1f}°."

third_house_data = Ram.third_house
third_house_info = f"Third House in {third_house_data['sign']} sign, positioned {third_house_data['position']:.1f}°."

fourth_house_data = Ram.fourth_house
fourth_house_info = f"Fourth House in {fourth_house_data['sign']} sign, positioned {fourth_house_data['position']:.1f}°."

fifth_house_data = Ram.fifth_house
fifth_house_info = f"Fifth House in {fifth_house_data['sign']} sign, positioned {fifth_house_data['position']:.1f}°."

sixth_house_data = Ram.sixth_house
sixth_house_info = f"Sixth House in {sixth_house_data['sign']} sign, positioned {sixth_house_data['position']:.1f}°."

seventh_house_data = Ram.seventh_house
seventh_house_info = f"Seventh House in {seventh_house_data['sign']} sign, positioned {seventh_house_data['position']:.1f}°."

eighth_house_data = Ram.eighth_house
eighth_house_info = f"Eighth House in {eighth_house_data['sign']} sign, positioned {eighth_house_data['position']:.1f}°."

ninth_house_data = Ram.ninth_house
ninth_house_info = f"Ninth House in {ninth_house_data['sign']} sign, positioned {ninth_house_data['position']:.1f}°."

tenth_house_data = Ram.tenth_house
tenth_house_info = f"Tenth House in {tenth_house_data['sign']} sign, positioned {tenth_house_data['position']:.1f}°."

eleventh_house_data = Ram.eleventh_house
eleventh_house_info = f"Eleventh House in {eleventh_house_data['sign']} sign, positioned {eleventh_house_data['position']:.1f}°."

retrograde_message = retrograde_planets_message(Ram)


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                             generation_config=generation_config,
                             safety_settings=safety_settings)

convo = model.start_chat(history=[
    {
    "role": "user",
    "parts": [
        f"You are a personalized astrocoach of {Ram.name} providing predictions based on his/her astrological data. "
        f"Astrological Information: {sun_info}, "
        f"{moon_info}, {mercury_info}, {venus_info}, {mars_info}, "
        f"{jupiter_info}, {saturn_info}, {uranus_info}, {neptune_info}, "
        f"{pluto_info}, {mean_node_info}, {true_node_info}, {chiron_info}, "
        f"{first_house_info}, {second_house_info}, {third_house_info}, "
        f"{fourth_house_info}, {fifth_house_info}, {sixth_house_info}, "
        f"{seventh_house_info}, {eighth_house_info}, {ninth_house_info}, "
        f"{tenth_house_info}, {eleventh_house_info}"
        f"{retrograde_message}"
    ]
    },
    
    {
        "role": "model",
        "parts": ["**Dear,**\n\n**Astrological Overview:**\n\nYour astrological chart indicates a vibrant personality with a strong sense of self. Leo and Sagittarius energies are prominent, suggesting you possess a natural charisma, a thirst for adventure, and a philosophical outlook. The Moon in Taurus brings balance and stability, while Mercury in Leo amplifies your intellectual curiosity and communication abilities.\n\n**Current Cosmic Influences:**\n\nThe current planetary alignment highlights the areas of relationships, finances, and emotional well-being. With Venus in the seventh house, you may experience opportunities for deeper connections and harmonizing existing partnerships. Jupiter in the seventh house emphasizes the importance of collaboration and shared goals.\n\nMars in the twelfth house suggests a need for introspection and a focus on your inner healing. This could be a time of spiritual growth and emotional release. The presence of Neptune and Uranus in the first house indicates a period of self-discovery and the potential for unexpected personal transformations.\n\n**Areas of Focus:**\n\n* **Relationships:** Pay attention to the needs of those around you and strive for harmony in your connections.\n* **Finances:** Be cautious with spending and consider long-term financial strategies.\n* **Emotional well-being:** Nurture your inner self through self-care, mindfulness, and seeking support when needed.\n\n**Opportunities and Challenges:**\n\n* **Opportunities:** Embracing your natural charisma and intellectual curiosity can lead to new adventures and growth.\n* **Challenges:** Introspection and emotional healing may require confronting inner shadows and releasing old patterns.\n\n**Recommendations:**\n\n* Spend time reflecting on your relationships and seek ways to deepen them.\n* Seek advice from trusted individuals regarding financial matters.\n* Explore spiritual or therapeutic practices to support your emotional well-being.\n* Be open to unexpected personal transformations and embrace the process of self-discovery.\n\nRemember, these astrological predictions are not set in stone but rather a roadmap to guide your journey. Embrace the opportunities and challenges presented by the cosmos and use them as a catalyst for personal growth and transformation.\n\n**With cosmic blessings,**\n**Your Astrocoach**"]
  },
])

while True:
    # Get user input
    user_input = input("You: ")
    
    # Send user input to the model
    convo.send_message(user_input)
    
    # Print the last response from the conversation
    print("Model:", convo.last.text)
