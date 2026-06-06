import random

import pyttsx3


# Initialize pyttsx3 TTS engine

engine = pyttsx3.init()

engine.setProperty("rate", 150)

engine.setProperty("volume", 0.9)


def speak(text):

    """Speak the text provided to the TTS engine."""

    engine.say(text)

    engine.runAndWait()


def get_samples():

    """Return a list of custom phrases and jokes."""

    return [

        "Hello! I am your computer!",

        "Python is awesome!",

        "This is AI speaking!",

        "Welcome to the future!",

        "Why don't skeletons fight each other? They don't have the guts!"

    ]


def main():

    print("🤖 AI VOICE LAB")

    speak("Hello! Type something for me to say!")

   

    while True:

        text = input("\n🎤 You: ").strip().lower()

       

        # Exit Command

        if text == 'exit':

            speak("Goodbye!")

            break

       

        # Random Sample Command

        elif text == 'sample':

            phrase = random.choice(get_samples())

            print(f"🎲 {phrase}")

            speak(phrase)

       

        # Custom Commands for Speed and Volume

        elif text == 'speed up':

            current_rate = engine.getProperty('rate') + 50

            engine.setProperty('rate', current_rate)

            speak(f"Speed increased to {current_rate}")

       

        elif text == 'slow down':

            current_rate = engine.getProperty('rate') - 50

            engine.setProperty('rate', current_rate)

            speak(f"Speed decreased to {current_rate}")

       

        elif text == 'increase volume':

            current_volume = engine.getProperty('volume') + 0.1

            if current_volume > 1: current_volume = 1

            engine.setProperty('volume', current_volume)

            speak(f"Volume increased to {current_volume}")

       

        elif text == 'decrease volume':

            current_volume = engine.getProperty('volume') - 0.1

            if current_volume < 0: current_volume = 0

            engine.setProperty('volume', current_volume)

            speak(f"Volume decreased to {current_volume}")

       

        # Custom Command for Jokes

        elif text == 'tell a joke':

            jokes = [

                "Why don't skeletons fight each other? They don't have the guts!",

                "What do you get when you cross a snowman and a vampire? Frostbite!",

                "Why don’t scientists trust atoms? Because they make up everything!"

            ]

            joke = random.choice(jokes)

            print(f"😂 {joke}")

            speak(joke)

       

        # Unrecognized Command

        else:

            print("💡 Type 'sample' for ideas or 'exit' to quit.")

            speak("I didn't quite catch that. Try again!")


if __name__ == "__main__":

    main()



Additional Hints:
Customizing Speech:
 Use engine.setProperty("rate", value) to modify how fast or slow the speech is. Experiment with values like 120, 150, and 200 for different speeds.
Volume Control:
 The engine.setProperty("volume", value) allows for volume adjustments. Values range from 0.0 (mute) to 1.0 (full volume).
Title
🎙️ Voice Master+: Extend Your Talking AI


Objective
To reinforce core concepts of Text-to-Speech (TTS), user input handling, randomness, and command interpretation by upgrading the original AI Voice Lab into a more interactive and responsive application.


Goal
Students will build on the lesson project by:

Expanding random responses (using lists)
Adding custom commands for jokes and speech controls
Implementing error-handling for unknown inputs
Practicing dynamic interaction using loops

Getting Started
Open the code you built during class (ai_voice_lab.py)
Ensure pyttsx3 is installed:

pip install pyttsx3

Copy the full code below into a new file named voice_master_plus.py
Run the program and interact using voice commands!

Instruction
Add 5 or more fun new phrases to the get_samples() list.
Add speech rate and volume control:
speed up, slow down
increase volume, decrease volume
Add a custom command:
tell a joke → AI speaks a random joke.
Add error handling:
If command not understood, reply with: “I didn’t quite catch that. Try again!”
Keep the loop running until exit is typed.

Hint (Complete Code Solution)

import random

import pyttsx3


# Initialize pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 150)

engine.setProperty("volume", 0.9)


def speak(text):

    """Convert text to speech"""

    engine.say(text)

    engine.runAndWait()


def get_samples():

    return [

        "Hello! I am your computer!",

        "Python is awesome!",

        "This is AI speaking!",

        "Welcome to the future!",

        "Never give up on learning!",

        "AI can be fun and helpful!",

        "Speak your thoughts into code!"

    ]


def main():

    print("🤖 VOICE MASTER+")

    speak("Hello! Type something for me to say!")


    while True:

        user_input = input("\n🎤 You: ").strip().lower()


        if user_input == "exit":

            speak("Goodbye! See you next time.")

            break


        elif user_input == "sample":

            phrase = random.choice(get_samples())

            print(f"🎲 {phrase}")

            speak(phrase)


        elif user_input == "speed up":

            rate = engine.getProperty("rate") + 50

            engine.setProperty("rate", rate)

            speak(f"Speaking faster now at {rate} rate.")


        elif user_input == "slow down":

            rate = engine.getProperty("rate") - 50

            engine.setProperty("rate", rate)

            speak(f"Speaking slower now at {rate} rate.")


        elif user_input == "increase volume":

            vol = engine.getProperty("volume") + 0.1

            vol = min(1.0, vol)

            engine.setProperty("volume", vol)

            speak("Volume increased.")


        elif user_input == "decrease volume":

            vol = engine.getProperty("volume") - 0.1

            vol = max(0.0, vol)

            engine.setProperty("volume", vol)

            speak("Volume decreased.")


        elif user_input == "tell a joke":

            jokes = [

                "Why don't scientists trust atoms? Because they make up everything!",

                "What do you call fake spaghetti? An impasta!",

                "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep!'"

            ]

            joke = random.choice(jokes)

            print(f"😂 {joke}")

            speak(joke)


        elif user_input:

            speak(user_input)


        else:

            print("💡 Type 'sample', 'tell a joke', or 'exit'")

            speak("I didn’t quite catch that. Try again!")


if __name__ == "__main__":

    main()



