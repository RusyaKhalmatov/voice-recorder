import pyaudio
import wave


def define_device_index():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)['name'])


# def record_voice():
#     chunk = 1024  # Запись кусками по 1024 сэмпла
#     sample_format = pyaudio.paInt16  # 16 бит на выборку
#     channels = 2
#     rate = 44100  # Запись со скоростью 44100 выборок(samples) в секунду
#     seconds = 10
#     filename = "output_sound_new.wav"
#     p = pyaudio.PyAudio()  # Создать интерфейс для PortAudio
#
#     print('Recording...')
#
#     stream = p.open(format=sample_format,
#                     channels=channels,
#                     rate=rate,
#                     frames_per_buffer=chunk,
#                     input_device_index=1,  # индекс устройства с которого будет идти запись звука
#                     input=True)
#     frames = []  # Инициализировать массив для хранения кадров
#
#     # Хранить данные в блоках в течение 3 секунд
#     for i in range(0, int(rate / chunk * seconds)):
#         data = stream.read(chunk)
#     frames.append(data)
#
#     # Остановить и закрыть поток
#     stream.stop_stream()
#     stream.close()
#     # Завершить интерфейс PortAudio
#     p.terminate()
#
#     print('Finished recording!')
#
#     # Сохранить записанные данные в виде файла WAV
#     wf = wave.open(filename, 'wb')
#     wf.setnchannels(channels)
#     wf.setsampwidth(p.get_sample_size(sample_format))
#     wf.setframerate(rate)
#     wf.writeframes(b''.join(frames))
#     wf.close()

def record_voice(device_index, channels):
    chunk = 1024  # Запись кусками по 1024 сэмпла
    sample_format = pyaudio.paInt16  # 16 бит на выборку
    # channels = 2
    rate = 44100  # Запись со скоростью 44100 выборок(samples) в секунду
    seconds = 10
    filename = "output_sound_new.wav"
    p = pyaudio.PyAudio()  # Создать интерфейс для PortAudio

    print('Recording...')

    stream = p.open(format=sample_format,
                    channels=int(channels),
                    rate=rate,
                    frames_per_buffer=chunk,
                    input_device_index=int(device_index),  # индекс устройства с которого будет идти запись звука
                    input=True)
    frames = []  # Инициализировать массив для хранения кадров

    # Хранить данные в блоках в течение 3 секунд
    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
    frames.append(data)

    # Остановить и закрыть поток
    stream.stop_stream()
    stream.close()
    # Завершить интерфейс PortAudio
    p.terminate()

    print('Finished recording!')

    # Сохранить записанные данные в виде файла WAV
    wf = wave.open(filename, 'wb')
    wf.setnchannels(int(channels))
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    define_device_index()
    device_index = input("Enter device index: ")
    channels = input("Number of channels: ")
    record_voice(device_index, channels)
    # record_voice()

