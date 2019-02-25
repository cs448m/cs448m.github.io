# cs448m.github.io
course website for cs448m

**Guide to original Base Template:** https://mmistakes.github.io/skinny-bones-jekyll/getting-started/

#### Structure:
- Landing Page: index.md
- Craft Inspiration: craft_inspiration.md

### To test changes locally: 
`bundle exec jekyll serve`
`bundle exec jekyll build`

### craft_inspiration.md
1. This page is organized by *machine types* under the **machines** list.
2. Each machine type under the **machines** list has (1) a named **kind** label that denotes the machine type, (2) a list of example product images (**products**) and (3) a list of images of things that you can make with the machine (**crafts**).  
3. The examples under both the **products** and **crafts** list have the same structure:
	- `imageurl` : Url of the image to be shown. To avoid hotlinking, I've been saving images inside the *images/* directory.
	- `caption` : Caption describing the image.
	- `credit` : Image Credit/Source
	- `link` : Link to the page where you found the original image. 
4. To add a new machine type, simply add these a block under the top level **machines** list with **kind**, **products**, and **crafts** attributes. 
