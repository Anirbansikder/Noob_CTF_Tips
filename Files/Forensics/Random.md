# Random 

1. We are given a zip file with name 60*50 and after extracting we get 3000 files. Upon looking closely it is clear we need to merge them to get a single image.
    ```python
    from PIL import Image
    new_image = Image.new('RGB',(600, 500), (250,250,250))
    for i in range(1,3001):
        image1 = Image.open('60x50/' + str(i) + '.jpg')
        # image1 = image1.resize((100,100))
        new_image.paste(image1,(((i-1)//50)*10,((i-1)%50)*10))
    new_image.show()
    ```
2. We are given a .pcapng . One of the data packets contain a password to zip and the other contain zip but in reversed order. To extract the zip ->
    ```python
    from scapy.all import *

    packets = rdpcap('network2.pcapng')

    temp = bytes("",'utf-8')

    lmao = packets[66][Raw].load[::-1]

    file = open("out.zip","wb")
    file.write(lmao)
    file.close()
    ```