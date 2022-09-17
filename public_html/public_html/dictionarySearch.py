def main():
   sampleString = " Hello there conglomeration "
   words=sampleString.split()
   myDictionary=[]
   wordsIn = open("words.txt","r")
   word = wordsIn.readline()
   print("creating dictionary array... ")
   while word != "": # copy file to array
       myDictionary.append(word.strip("\n"))
       word = wordsIn.readline()
   myDictionary.sort()
   print("dictionary array of",len(myDictionary),"words created")
   for word in words:
        if binary_search(myDictionary,word.lower()) or \
          binary_search(myDictionary,word):
            print("word",word,"found in dictionary")
        else:
            print("word",word,"spelled wrong - not found in dictionary")
def binary_search(arr, value):

   first = 0 #0 relative array

   last = len(arr) - 1

   found = False

   while not found and first <= last: #if first = last then notfound

       middle = (first + last) // 2 #find middle index - // as index integer 🙂

       if arr[middle] == value:    #check value for middle index as what you are looking for

           found = True

       elif arr[middle] > value: # else if value is in the lower half...

           last = middle - 1    # -1 since middle not it

       else:                    # else if value is in the upper half...

           first = middle + 1   # +1 since middle not it

   return found
main()
