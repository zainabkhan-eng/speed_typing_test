from random import randint
import time
sentence=["The quick brown fox jumps over the lazy dog",
          "To be or not to be , that is the question",
          "Honesty is the best policy",
          "Train your own mindset for the success",
          "create your own kind of happy"]

def calculate_wpm(time,words):
    minutes=time/60
    wpm=words/minutes
    return wpm


print("Get ready to type this sentence : ")
sentence= sentence[randint(0,4)]
print(sentence)

time.sleep(1)
print("in 3 ,",end="  ")
time.sleep(1)
print("2,",end="  ")
time.sleep(1)
print("1 go !")


start_time=time.time()
user_input=input()
end_time=time.time()

if user_input==sentence:
    #calculate the wpm
    words=len(sentence.split())
    wpm=calculate_wpm(end_time-start_time,words)
    print("Your typing speed is", wpm)
else:
    print("The input does not match the sentence, Try again !")
    