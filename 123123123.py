from pydub import AudioSegment

# Загрузка аудио файла
audio_file = AudioSegment.from_file("www.wav")

# Задание коэффициента изменения скорости
speed = 1.5 # Ускорение в 1.5 раза
#speed = 2.0 # Замедление в 2 раза

# Изменение скорости аудио файла
changed_speed = audio_file._spawn(audio_file.raw_data, overrides={'frame_rate': int(audio_file.frame_rate * speed)})
changed_speed.export("changed_speed.wav", format="wav") # Сохранение измененного файла в формате wav