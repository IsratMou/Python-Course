print(
      """Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!"""
)

#print er moddhe triple '''/ """ die multiline print kora hoy. just like multilne comment


#   ---- question 3
# Import the required module for text 
# to speech conversion
import pyttsx3

# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()

# say method on the engine that passing input text to be spoken
engine.say('Hello sir, how may I help you, sir.')

# run and wait method, it processes the voice commands. 
engine.runAndWait()


engine = pyttsx3.init()
engine.say('Hello Mou. Mou loves cat')
engine.runAndWait()