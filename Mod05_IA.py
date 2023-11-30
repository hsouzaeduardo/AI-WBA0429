import os
import azure.cognitiveservices.speech as speechsdk

speech_key, service_region = "[Chave do Serviço]", "[LocalDoServiço]"
# Cria uma configuração com a chave e a região
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    
def speech_to_text():
    
    #criar uma instancia para o microfone padrão
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config
                                                   , language="pt-BR"
                                                   , audio_config=audio_config)
    print("Diz algo ai...")
    while True:
        result = speech_recognizer.recognize_once()
        print(result.text)
        if result.text == "sair":
            break

def read_audio_file():
    audio_input = speechsdk.audio.AudioConfig(filename="1.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config
                                                   , language="en-US"
                                                   , audio_config=audio_input)
    result = speech_recognizer.recognize_once()
    print("Reconhecido: {}".format(result.text))

def read_audio_transalate():
    #criar uma instancia para o microfone padrão
    translation_config = speechsdk.translation.SpeechTranslationConfig(
        subscription=speech_key
        , region=service_region
        , speech_recognition_language="en-US"
        , target_languages=("pt-BR", "es", "fr"))
    audio_config = speechsdk.audio.AudioConfig(filename="1.wav")
    recognizer = speechsdk.translation.TranslationRecognizer(
        translation_config=translation_config
        , audio_config=audio_config)
    
    result = recognizer.recognize_once()
    print("Reconhecido: {}".format(result.text))
    print("Tradução PT: {}".format(result.translations["pt"]))
    print("Tradução ES: {}".format(result.translations["es"]))
    print("Tradução FR: {}".format(result.translations["fr"]))
    
    
if __name__ == "__main__":
    #speech_to_text()
    #read_audio_file()
    read_audio_transalate()