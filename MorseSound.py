import sounddevice as sd
import numpy as np
import time

# Define Morse code dictionary
morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                   '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                   '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                   '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                   '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
                   '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                   '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

# Variables for Morse code decoding
dot_duration = 0.2  # Adjust this based on the actual Morse code signal duration
sound_threshold = 0.05
recording_duration = 1.5

def record_audio():
    print("Recording...")
    audio_data = sd.rec(int(recording_duration * 44100), samplerate=44100, channels=1, dtype=np.float32)
    sd.wait()
    print("Recording complete.")
    return audio_data.flatten()

def decode_morse_code(signal):
    morse_code = ""
    threshold_crossed = False
    for amplitude in signal:
        if amplitude > sound_threshold:
            threshold_crossed = True
            morse_code += "-"
        else:
            if threshold_crossed:
                morse_code += "."
                threshold_crossed = False
    return morse_code

def translate_morse_code(morse_code):
    words = morse_code.split("   ")  # Morse code uses three spaces to separate words
    decoded_message = ""
    for word in words:
        characters = word.split(" ")
        for char in characters:
            if char in morse_code_dict:
                decoded_message += morse_code_dict[char]
        decoded_message += " "
    return decoded_message.strip()

def main():
    while True:
        input("Press Enter to start recording...")
        audio_signal = record_audio()
        morse_code = decode_morse_code(audio_signal)
        decoded_message = translate_morse_code(morse_code)
        print("Decoded Morse Code:", morse_code)
        print("Decoded Message:", decoded_message)
        print()

if __name__ == "__main__":
    main()
