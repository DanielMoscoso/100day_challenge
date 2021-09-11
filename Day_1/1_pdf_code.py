import PyPDF2

# Reading from PDF:
f = open("Working_Business_Proposal.pdf", "rb")  # rb = Read binary

pdf_reader = PyPDF2.PdfFileReader(f)

pdf_reader.numPages

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()

page_one_text
f.close()

# Writing to a PDF:
# %%
f = open("Working_Business_Proposal.pdf", "rb")  # rb = Read binary

pdf_reader = PyPDF2.PdfFileReader(f)

last_page = pdf_reader.getPage(-1)  # This gets the entire page, not only the number.

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(last_page)  # It should be a pdf.PageObject, not a raw Python string.

# pdf_output = open("Working_Business_Proposal.pdf", "wb")  # Write binary (It will overwrite).
pdf_output = open("Working_Business_Proposal_2.pdf", "wb")  # Write binary (It will overwrite).
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()

# Multiple pages:
# %%
f = open("Working_Business_Proposal.pdf", "rb")  # rb = Read binary

pdf_text = []
pdf_raw = []

pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())  # Adding the writen part of the PDF into a list.
    pdf_raw.append(page)  # Adding the raw page of the PDF into a list.

pdf_text[1]
# f.close()  # Use this statement if you don't want to use the las piece of this part.

# You can also create a new PDF with the individual pages:
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_output = open("Working_Business_Proposal_2.pdf", "wb")
# pdf_writer.addPage(pdf_raw[3])
# pdf_writer.write(pdf_output)

# Or recreate the entire PDF:
pdf_writer = PyPDF2.PdfFileWriter()
for page in range(pdf_reader.numPages):
    individual_page = pdf_reader.getPage(page)

    pdf_writer.addPage(individual_page)

pdf_output = open("Working_Business_Proposal_2.pdf", "wb")  # "wb" will not overwrite the original PDF
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()
del pdf_writer  # You need to delete what is inside this variable, otherwise you
#                 will keep appending pages to your final output.
