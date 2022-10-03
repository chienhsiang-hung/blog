---
title: "Add Page Break in HTML print / for PDFKit (plus Avoid Page Break Inside)"
date: 2022-08-23
lastmod: 2022-08-23
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "A HTML report that is going to be printable, and it has “sections” that should start in a new page.\nIs there any way to put something in…"
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Page Break", "CSS", "HTML", "Print", "Pdfkit"]
toc:
  enable: false
zhtw: false
---
![](https://miro.medium.com/max/1400/0*yfgGaIVglDR0FT--)

Photo by  [Hello I'm Nik](https://unsplash.com/@helloimnik?utm_source=medium&utm_medium=referral)  on  [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

A HTML report that is going to be printable, and it has “sections” that should start in a new page.  
Is there any way to put something in the HTML/CSS that will signal to the browser that it needs to force a page break (start a new page) at that point? Especially for creating a PDF with HTML and transfored by PDFKit.

Answers:

1.  For print ([Chris Doggett](https://stackoverflow.com/users/64203/chris-doggett))

[Can I force a page break in HTML printing? — Stack Overflow](https://stackoverflow.com/questions/1664049/can-i-force-a-page-break-in-html-printing)

Add a CSS class called “pagebreak” (or “pb”), like so:
```css
@media print {  
    .pagebreak { page-break-before: always; } /* page-break-after works, as well */  
}
```
Then add an empty DIV tag ([or any block element that generates a box](https://developer.mozilla.org/en-US/docs/Web/CSS/page-break-after)) where you want the page break.
```html
<div class="pagebreak"> </div>
```
It won’t show up on the page, but will break up the page when printing.

P.S. Perhaps this only applies when using  `-after`  (and also what else you might be doing with other  `<div>`s on the page), but I found that I had to augment the CSS class as follows:
```css
@media print {  
    .pagebreak {  
        clear: both;  
        page-break-after: always;  
    }  
}
```
2. For PDFKit ([Andrew](https://stackoverflow.com/users/5508175/andrew))

[Add a page break in html for PDFKit in Swift — Stack Overflow](https://stackoverflow.com/questions/66222073/add-a-page-break-in-html-for-pdfkit-in-swift)

By changing it to  `page-break-before`  instead of  `page-break-after`  it seems to work. This is what I changed your contextString to, I used a multiline string as it is easier to read and gave it some clearer content.
```javascript
let contextString = """  
<p>Content in page 1</p>  
<p style=\"page-break-before: always;\"></p>  
<p>Content in page 2</p>  
"""
```
Here is a very simple example that you could drop into Xcode.
```javascript
class ViewController: UIViewController { let button = UIButton()  
    override func viewDidLoad() {  
        super.viewDidLoad()  
        // Do any additional setup after loading the view.  
        view.addSubview(button)  
        button.translatesAutoresizingMaskIntoConstraints = false button.setTitle("Print", for: .normal)  
        button.setTitleColor(.systemBlue, for: .normal)  
        button.addTarget(self, action: #selector(tapped), for: .touchUpInside) NSLayoutConstraint.activate([  
            button.centerXAnchor.constraint(equalTo: view.centerXAnchor),  
            button.centerYAnchor.constraint(equalTo: view.centerYAnchor),  
            button.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),  
        ])  
        view.backgroundColor = .systemBackground  
    } @objc func tapped() { let contextString = """  
        <p>Content in page 1</p>  
        <p style=\"page-break-before: always;\"></p>  
        <p>Content in page 2</p>  
        """ let print = UIMarkupTextPrintFormatter(markupText: contextString) let render = UIPrintPageRenderer()  
        render.addPrintFormatter(print, startingAtPageAt: 0) let page = CGRect(x: 0, y: 0, width: 595.2, height: 841.8) // A4, 72 dpi  
        render.setValue(page, forKey: "paperRect")  
        render.setValue(page, forKey: "printableRect") let pdfData = NSMutableData()  
        UIGraphicsBeginPDFContextToData(pdfData, .zero, nil) for i in 0..<render.numberOfPages {  
        UIGraphicsBeginPDFPage();  
            render.drawPage(at: i, in: UIGraphicsGetPDFContextBounds())  
        }  
        UIGraphicsEndPDFContext(); let av = UIActivityViewController(activityItems: [pdfData], applicationActivities: nil) self.present(av, animated: true, completion: nil)  
    }  
}
```
Here is a gif of it showing the two pages with the text:

![](https://miro.medium.com/max/648/0*NFlgUUM_n5tEEUp9.gif)

# Bonus:

use  `page-break-inside: avoid;`  to avoid page break inside

Contact me:  [Hung, Chien-Hsiang (chienhsiang-hung.github.io)](https://chienhsiang-hung.github.io/)