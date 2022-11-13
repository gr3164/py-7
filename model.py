from view import *
import os

def ViewContacts():
    contact = LabelFrame(text="Контакты", width=400,height=50,padx=50)
    
    with open('text.txt', 'r', encoding='utf-8') as f:
        if os.stat("text.txt").st_size == 0:
            cont = ttk.Label(contact, text="Пусто", padding=10,width=400)
            
        else:
            cont = ttk.Label(contact, text=f"{f.read()}", padding=10,width=400, anchor=W)
    cont.pack(fill=Y)
    contact.pack()
    
def export():
    with open('text.txt', 'r', encoding='utf-8') as f:
        s = f.readlines()
        with open('text.html', 'w', encoding='utf-8') as h:
            h.write("<!DOCTYPE html>\n")
            h.write("<html lang=\"en\">\n")
            h.write("<head>\n")
            h.write("<meta charset=\"UTF-8\">\n")
            h.write("<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
            h.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
            h.write("<title>Контакты</title>\n")
            h.write("</head>\n")
            h.write("<body>\n")
            h.write("<h1>Контакты</h1>")
            for i in s:
                h.write(f'<p>{i}</p>')
            h.write("</body>\n")
            h.write("</html>\n")
      
def exportXml():
    
    with open('text.txt', 'r', encoding='utf-8') as f:
        s = f.readlines()
        with open('text.xml', 'w', encoding='utf-8') as h:
            h.writelines("<Contacts>")
            count = 1
            for i in s:
                if i != '\n':
                    h.writelines(f'<contact{count}>{i}</contact{count}>')
                    count +=1
            h.write("</Contacts>")
    
 
        
            
        
        