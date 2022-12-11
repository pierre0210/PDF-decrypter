from PyPDF2 import PasswordType, PdfReader, PdfWriter
import os
import argparse

def get_parser():
	parser = argparse.ArgumentParser(description="Decrypt pdf files.")
	parser.add_argument("-f", "--file", dest="file", help="paths to the pdf files", nargs="*")
	parser.add_argument("-d", "--directory", dest="directory", help="pdf files directory", default=os.getcwd())
	parser.add_argument("-a", "--all", dest="all", help="process all pdf files", action="store_true")
	parser.add_argument("-p", "--password", dest="password", help="pdf passwords", nargs="+", required=True)
	parser.add_argument("--delete", dest="delete", help="delete original files after decrytion.", action="store_true")
	return parser

def decrypt_pdf(file_path: str, password_list: list[str], delete: bool):
	reader = PdfReader(file_path)
	writer = PdfWriter()
	if reader.is_encrypted:
		state: PasswordType
		for password in password_list:
			state = reader.decrypt(password)
			if state == PasswordType.OWNER_PASSWORD or state == PasswordType.USER_PASSWORD: 
				break
		if state == PasswordType.OWNER_PASSWORD or state == PasswordType.USER_PASSWORD:
			for page in reader.pages:
				writer.add_page(page)
			with open(file_path[:-4]+"-decrypt.pdf", "wb") as f:
				writer.write(f)
				print("PDF file decrypted {}".format(file_path[:-4]+"-decrypt.pdf"))
				if delete:
					os.remove(file_path)
					print("Original file deleted {}".format(file_path))
		elif state == PasswordType.NOT_DECRYPTED:
			print("Wrong password")

def main(args: argparse.Namespace):
	#print(args)
	if args.all:
		for item in os.listdir(args.directory):
			if os.path.isfile(os.path.join(args.directory, item)) and item.endswith(".pdf"):
				decrypt_pdf(os.path.join(args.directory, item), args.password, args.delete)
	elif args.all != True and args.file != None:
		for file in args.file:
			if os.path.exists(file) and str(file).endswith(".pdf"):
				decrypt_pdf(file, args.password, args.delete)
	else:
		print("Wrong format")


if __name__ == "__main__":
	parser = get_parser()
	args = parser.parse_args()
	main(args)