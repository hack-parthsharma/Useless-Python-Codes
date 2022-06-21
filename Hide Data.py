#Title: Hide data in image using Python.
#Author: @CodeProgrammer on Telegram.

from stegano import lsb

#Choose an image with path.
image= "/content/Python.png"

#Select the name of the new image that contains the data.
new_img="Python1.png"

#Choose the text of the message that you want to hide in the new image.
msg= "Hi, This is a test text from @CodeProgrammer"

#To Hide message.
lsb.hide(image, message=msg).save(new_img)

#To reveal hidden message.
message = lsb.reveal(new_img)

#Check the secret text.
print("Hideden message: ", message)