
import hashlib

pdf1 = r'C:\Users\MI-Store\Desktop\beginner projects python\check-if-2-files-are-indentical\comaprepdf1.pdf'
pdf2 = r"C:\Users\MI-Store\Desktop\beginner projects python\check-if-2-files-are-indentical\comparepdf2.pdf"


def compare(file1, file2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(file1,"rb") as file:
        chunk = ""
        while chunk != b"":
            chunk = file.read(1024)
            h1.update(chunk)

    with open(file2,"rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()


first_file , second_file = compare(pdf1,pdf2)

if first_file != second_file:
    print("These files are not identical")
else:
    print("These files are identical")
