from pydub import AudioSegment
import argparse
import os
import os
import sys
folder = 'try_test'
for filename in os.listdir(folder):
    infilename = os.path.join(folder, filename)
    if not os.path.isfile(infilename):
        continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.tmp', '.m4a')
    output = os.rename(infilename, newname)


# Convert m4a extension files to wav extension files


# for (dirpath, dirnames, filenames) in os.walk("try_test"):
#        print(dirpath, dirnames, filenames)

def m4a_wav(folder_name="try_test", if_remove=True):
    formats_to_convert = ['.m4a']

    for (dirpath, dirnames, filenames) in os.walk(folder_name):
        for filename in filenames:
            if filename.endswith(tuple(formats_to_convert)):
                filepath = f'{dirpath}/{filename}'
                (path, file_extension) = os.path.splitext(filepath)
                file_extension_final = file_extension.replace('.', '')
                try:
                    track = AudioSegment.from_file(filepath,
                                                   file_extension_final)
                    wav_filename = filename.replace(
                        file_extension_final, 'wav')
                    wav_path = f'{dirpath}/{wav_filename}'
                    print(f'CONVERTING: {str(filepath)}')
                    file_handle = track.export(wav_path, format='wav')
                    if if_remove:
                        os.remove(filepath)
                except:
                    print(f"ERROR CONVERTING {str(filepath)}")


m4a_wav(folder_name="try_test", if_remove=False)
