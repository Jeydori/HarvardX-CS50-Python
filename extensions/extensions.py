def main():
    file_name = str(input("File name: ")).strip().lower()
    file_type = file_name.split(".")
    extension = file_type[-1]
    extract(extension)

def extract(extension):
    match extension:
        case "jpg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
