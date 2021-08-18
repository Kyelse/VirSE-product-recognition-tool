# required module for text to speech conversion
from gtts import gTTS
  
# required module to play the converted audio
from playsound import playsound

def process_text(unprocessedText):
    processedText = ""
    textList = unprocessedText.split(',')
    for element in textList:
        element = element.replace("'", "")
        if element.replace(" ", "").isalpha():
            processedText += " " + element
    return processedText

### Unprocessed: [([[168, 74], [194, 74], [194, 98], [168, 98]], 'Gtàr', 0.02099325694143772), ([[191, 107], [323, 107], [323, 173], [191, 173]], '[gys', 0.32288601994514465), ([[184, 197], [319, 197], [319, 262], [184, 262]], 'Wavy', 0.6142613887786865), ([[157, 255], [345, 255], [345, 275], [157, 275]], 'Vi Bò Bít Tết Manhattan', 0.8644237803209461), ([[173, 279], [327, 279], [327, 291], [173, 291]], 'Manhattan Rib Eve Steak Flavor', 0.746261442720589), ([[118, 422], [182, 422], [182, 430], [118, 430]], 'Snoce Khoui Tas', 0.09766823939409566), ([[125.04217371477885, 87.71265211443365], [151.8376105968386, 81.45373221945307], [153.95782628522116, 91.28734788556635], [127.16238940316138, 97.54626778054693]], '(Snock', 0.19611234472050082), ([[135.01941932430907, 94.80388386486182], [167.88821764315594, 87.54057708112623], [169.98058067569093, 97.19611613513818], [137.11178235684406, 103.45942291887377]], '38 ] Ing', 0.4016182652697378)]
### Processed: Gtàr  Wavy  Vi Bò Bít Tết Manhattan  Manhattan Rib Eve Steak Flavor  Snoce Khoui Tas
processedText = process_text("[([[168, 74], [194, 74], [194, 98], [168, 98]], 'Gtàr', 0.02099325694143772), ([[191, 107], [323, 107], [323, 173], [191, 173]], '[gys', 0.32288601994514465), ([[184, 197], [319, 197], [319, 262], [184, 262]], 'Wavy', 0.6142613887786865), ([[157, 255], [345, 255], [345, 275], [157, 275]], 'Vi Bò Bít Tết Manhattan', 0.8644237803209461), ([[173, 279], [327, 279], [327, 291], [173, 291]], 'Manhattan Rib Eve Steak Flavor', 0.746261442720589), ([[118, 422], [182, 422], [182, 430], [118, 430]], 'Snoce Khoui Tas', 0.09766823939409566), ([[125.04217371477885, 87.71265211443365], [151.8376105968386, 81.45373221945307], [153.95782628522116, 91.28734788556635], [127.16238940316138, 97.54626778054693]], '(Snock', 0.19611234472050082), ([[135.01941932430907, 94.80388386486182], [167.88821764315594, 87.54057708112623], [169.98058067569093, 97.19611613513818], [137.11178235684406, 103.45942291887377]], '38 ] Ing', 0.4016182652697378)]")
print(processedText)
  
# Passing the text and language to the engine,
# lang='en' to set language to English,
# slow=False to converted text to a high speed audio
audioObj = gTTS(text=processedText, lang='en', slow=False)
  
# Save the converted audio in a mp3 file
audioObj.save("output.mp3")
  
# Play the converted file
playsound("output.mp3")