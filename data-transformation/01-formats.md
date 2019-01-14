# Data 1: Formats

## Types of Formats

Skim through this article: https://fileinfo.com/help/binary_vs_text_files

- Text
	- Text formats can be opened in any text editor (like Notepad, Sublime, TextEdit, etc.)
	- Text formats are easy to version control as git can clearly see what changed between two versions of a file.
- Binary
	- Binary formats cannot be opened in a text editor and often require a custom program (Acrobat Reader for pdf, Microsoft Excel for xlsx, Photoshop for psd, etc.)
	- Binary formats are a bit more difficult to version control. The reason Git is so efficient is that it does not need to store a copy of every single version of a file but instead it can store **just the changes** (the lines of text that have changed) between two versions of a file. When working with binary files, git cannot do this.

## Common Formats

### CSV (Comma Separated Values)

A simple format that can be viewed in excel. Really easy to see in text editor, contains only one table.

This is what a csv looks like. The first line is the headers and each line there after is a row where the columns are separated by a comma.

```
date,close
22-Jan-17,46
22-Jan-17,45
23-Jan-17,45
24-Jan-17,42.1
24-Jan-17,46
24-Jan-17,57
25-Jan-17,42.3
25-Jan-17,36
26-Jan-17,42.6
```

When you open this in excel, the table will end up looking like this:

| date      | close |
| --------- | ----- |
| 22-Jan-17 |  46.0 |
| 22-Jan-17 |  45.0 |
| 23-Jan-17 |  45.0 |
| 24-Jan-17 |  42.1 |
| 24-Jan-17 |  46.0 |
| 24-Jan-17 |  57.0 |
| 25-Jan-17 |  42.3 |
| 25-Jan-17 |  36.0 |
| 26-Jan-17 |  42.6 |

### TSV (Tab Separated Values)

Same as CSV, but separates values with tabs rather than commas, can also be opened in excel.

This is what a TSV looks like. Note how the commas are replaced with the tab character.

```
date	close
22-Jan-17	46
22-Jan-17	45
23-Jan-17	45
24-Jan-17	42.1
24-Jan-17	46
24-Jan-17	57
25-Jan-17	42.3
25-Jan-17	36
26-Jan-17	42.6
```

The table will render in the same way as the CSV in excel.

### JSON (JavaScript Object Notation)

![](https://www.evernote.com/shard/s150/sh/90cf283d-4adc-4f6f-aeaf-c8f2660d13c7/793cabb9f194996b/res/62dd9784-077a-45ee-8b47-c23054e2cc59/skitch.png?resizeSmall&width=832)
Source: http://stackoverflow.com/questions/4310315/what-exactly-is-json

We'll dig more into this later.

### XML (eXtensible Markup Language)

XML is an older data format that started in the late 1990's. It uses the idea of a "tree" to represent data. If you're familar with HTML (hypertext markup language), XML is a superset of HTML. Instead of having a defined set of "tags" such as `body`, `head` `title`, etc. XML allows one to define their own arbitrary tags.

For example, in the snippet below, we have a tag defined as `note`. Each `note` contains `to`, `from`, `heading`, and `body`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

If we wanted to represent a "list", we just put the same tag multiple times. For example, if we wanted the above note to be for multiple people, we could add an additional `to` tag within the `note`.

These days, JSON is much more popular than XML. However, you may still run into XML data in the wild since it reigned supreme for decades.

Here is an example of the House of Representatives providing data via XML: https://xml.house.gov/

### PDF (Portable Document Format)

PDF data is hard to extract. If you have PDFs containing tables, you may be able to copy and paste the tables into a text file or into excel.

I have had success extracting data from PDFs with off the shelf tools when either (1) the PDF contains tables or (2) you have many PDFs that are exactly the same in structure with different data (for example many copies of a form). In these two cases, I'd consider trying
  - http://tabula.technology/
  - https://pdftables.com/

On macOS, install Tabula by running `brew cask install tabula`.

### HTML (Hypertext Markup Language)

- Copy/Paste - try this first, sometimes you can just copy an HTML table and paste directly into excel then save as CSV
- import.io (and other [similar tools](https://gist.github.com/cassidoo/9b1791a47411dd1253af2e5e8ef7c72a)) is especially good with extracting tables from websites, but can also extract data from other parts of a website using CSS selectors.

### XLS & XLSX

- Binary format
- Demo: Unzip roster.xlsx with Unarchiver

https://github.com/unitedstates/congress-legislators
